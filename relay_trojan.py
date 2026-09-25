# relay_trojan.py
# ══════════════════════════════════════════════════════════════════════════════
# Trojan WebSocket Relay — production-oriented implementation
#
# Features
#   • Trojan password authentication via SHA-224 + constant-time comparison
#   • TCP CONNECT
#   • UDP ASSOCIATE
#   • IPv4 / Domain / IPv6 targets
#   • Handles a header split across multiple WebSocket frames
#   • Preserves payload appended to the initial Trojan request
#   • Shared quota/check_and_use support
#   • Shared throttle support
#   • IP-limit / link-state / expiry validation
#   • Connection statistics + main.connections integration when available
#   • Graceful bidirectional shutdown and resource cleanup
#   • Compatibility handler: handle_trojan_ws(...)
#
# The module does not require main.py at import time. The integrated
# websocket_tunnel_trojan() wrapper uses the same project helpers as the
# VMess relay when they are available.
# ══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import asyncio
import hashlib
import hmac
import ipaddress
import logging
import socket
import struct
import time
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Optional, Tuple

from fastapi import WebSocket, WebSocketDisconnect

try:
    import main  # type: ignore
except Exception:  # pragma: no cover - allows standalone import/tests
    main = None  # type: ignore


logger = logging.getLogger("OMIDIRAN_PANEL.TROJAN")

RELAY_BUF = 256 * 1024
TCP_CONNECT_TIMEOUT = 10.0
FIRST_FRAME_TIMEOUT = 15.0
UDP_IDLE_TIMEOUT = 120.0
MAX_FIRST_BUFFER = 64 * 1024
MAX_DOMAIN_LENGTH = 255
MAX_WS_UDP_BUFFER = 4 * 1024 * 1024
UDP_MAX_PAYLOAD = 65507


class _NeedMoreData(Exception):
    """Internal parser signal."""


@dataclass(slots=True)
class TrojanRequest:
    password_hash: str
    cmd: int
    address_type: int
    target_host: str
    target_port: int
    payload_offset: int


def _sha224_hex(password: str) -> str:
    return hashlib.sha224(password.encode("utf-8")).hexdigest()


def _client_ip(websocket: WebSocket) -> str:
    if main is not None:
        try:
            return main.client_ip(websocket)
        except Exception:
            pass

    client = websocket.client
    return client.host if client else "0.0.0.0"


def _safe_stat_inc(name: str, amount: int = 1) -> None:
    if main is None:
        return
    try:
        stats = getattr(main, "stats", None)
        if isinstance(stats, dict):
            stats[name] = stats.get(name, 0) + amount
    except Exception:
        pass


def _register_connection(conn_id: str, real_uid: str, ip: str) -> None:
    if main is None:
        return
    try:
        connections = getattr(main, "connections", None)
        if isinstance(connections, dict):
            connections[conn_id] = {
                "uuid": real_uid,
                "ip": ip,
                "bytes": 0,
                "connected_at": main.now_ir().isoformat(),
                "transport": "trojan-ws",
            }
    except Exception:
        pass


def _add_connection_bytes(conn_id: str, amount: int) -> None:
    if main is None:
        return
    try:
        connections = getattr(main, "connections", None)
        if isinstance(connections, dict) and conn_id in connections:
            connections[conn_id]["bytes"] += amount
    except Exception:
        pass


def _remove_connection(conn_id: str) -> None:
    if main is None:
        return
    try:
        connections = getattr(main, "connections", None)
        if isinstance(connections, dict):
            connections.pop(conn_id, None)
    except Exception:
        pass


def _record_error(exc: Exception, conn_id: str) -> None:
    if main is None:
        return
    try:
        main.stats["total_errors"] += 1
    except Exception:
        pass

    try:
        main.error_logs.append(
            {
                "error": str(exc),
                "type": "trojan_ws_tunnel",
                "time": main.now_ir().isoformat(),
                "connection": conn_id,
            }
        )
    except Exception:
        pass


async def _quota_check(uid: str, amount: int) -> bool:
    """
    Uses the project's shared quota checker when available.
    This is intentionally lazy so the relay can still be imported/tested alone.
    """
    if amount <= 0:
        return True

    try:
        from relay_vless import check_and_use  # type: ignore

        return bool(await check_and_use(uid, amount))
    except ImportError:
        return True
    except Exception as exc:
        logger.error("Trojan quota check failed for %s: %s", uid, exc)
        return False


async def _throttle(uid: str, amount: int) -> None:
    if amount <= 0:
        return

    try:
        from speed_limit import throttle  # type: ignore

        await throttle(uid, amount)
    except ImportError:
        return
    except Exception as exc:
        logger.warning("Trojan throttle error for %s: %s", uid, exc)


def _link_is_active(link: dict[str, Any]) -> bool:
    try:
        if main is not None and hasattr(main, "is_link_allowed"):
            return bool(main.is_link_allowed(link))
    except Exception:
        return False

    if not link.get("is_active", True):
        return False

    exp_time = link.get("expire_time", 0) or 0
    if exp_time > 0 and time.time() > float(exp_time):
        return False

    max_bytes = link.get("max_bytes", 0) or 0
    if max_bytes > 0:
        used = (
            int(link.get("download_bytes", 0) or 0)
            + int(link.get("upload_bytes", 0) or 0)
        )
        if used >= max_bytes:
            return False

    return True


def _ip_allowed(link: dict[str, Any], real_uid: str, client_ip: str) -> bool:
    if main is not None and hasattr(main, "is_ip_allowed"):
        try:
            return bool(main.is_ip_allowed(link, real_uid, client_ip))
        except TypeError:
            # Compatibility with the older injected/helper signature:
            # is_ip_allowed(client_ip, link)
            try:
                return bool(main.is_ip_allowed(client_ip, link))
            except Exception:
                return False
        except Exception:
            return False

    return True


async def _close_ws(
    websocket: WebSocket,
    code: int = 1000,
    reason: str | None = None,
) -> None:
    try:
        await websocket.close(code=code, reason=reason)
    except Exception:
        pass


async def _receive_binary(
    websocket: WebSocket,
    timeout: float | None = None,
) -> bytes | None:
    async def _recv() -> bytes | None:
        msg = await websocket.receive()

        if msg["type"] == "websocket.disconnect":
            return None

        if msg["type"] != "websocket.receive":
            return None

        data = msg.get("bytes")
        if data is not None:
            return bytes(data)

        # Trojan-over-WS is binary. We deliberately do not reinterpret
        # arbitrary text as protocol bytes because that can corrupt payloads.
        if msg.get("text") is not None:
            raise ValueError("Trojan WebSocket requires binary frames")

        return b""

    if timeout is None:
        return await _recv()

    return await asyncio.wait_for(_recv(), timeout=timeout)


def _parse_request_header(data: bytes) -> TrojanRequest:
    """
    Parses:
        56-byte SHA224 hex
        CRLF
        CMD
        ATYP
        DST.ADDR
        DST.PORT
        CRLF

    Raises _NeedMoreData when the buffer is valid so far but incomplete.
    """
    if len(data) < 58:
        raise _NeedMoreData

    try:
        password_hash = data[:56].decode("ascii").lower()
    except UnicodeDecodeError:
        raise ValueError("invalid password hash encoding") from None

    if (
        len(password_hash) != 56
        or any(ch not in "0123456789abcdef" for ch in password_hash)
    ):
        raise ValueError("invalid SHA224 password hash")

    if data[56:58] != b"\r\n":
        raise ValueError("missing CRLF after password hash")

    idx = 58

    if len(data) < idx + 2:
        raise _NeedMoreData

    cmd = data[idx]
    address_type = data[idx + 1]
    idx += 2

    if cmd not in (1, 3):
        raise ValueError(f"unsupported Trojan command: {cmd}")

    if address_type == 1:  # IPv4
        if len(data) < idx + 4:
            raise _NeedMoreData

        target_host = socket.inet_ntoa(data[idx : idx + 4])
        idx += 4

    elif address_type == 3:  # Domain
        if len(data) < idx + 1:
            raise _NeedMoreData

        domain_len = data[idx]
        idx += 1

        if domain_len == 0 or domain_len > MAX_DOMAIN_LENGTH:
            raise ValueError("invalid domain length")

        if len(data) < idx + domain_len:
            raise _NeedMoreData

        try:
            target_host = data[idx : idx + domain_len].decode("idna")
        except UnicodeError:
            try:
                target_host = data[idx : idx + domain_len].decode("utf-8")
            except UnicodeDecodeError:
                raise ValueError("invalid domain encoding") from None

        target_host = target_host.strip()
        if not target_host:
            raise ValueError("empty domain")

        idx += domain_len

    elif address_type == 4:  # IPv6
        if len(data) < idx + 16:
            raise _NeedMoreData

        target_host = socket.inet_ntop(socket.AF_INET6, data[idx : idx + 16])
        idx += 16

    else:
        raise ValueError(f"unsupported address type: {address_type}")

    if len(data) < idx + 4:
        raise _NeedMoreData

    target_port = struct.unpack("!H", data[idx : idx + 2])[0]
    idx += 2

    if target_port == 0:
        raise ValueError("destination port cannot be zero")

    if data[idx : idx + 2] != b"\r\n":
        # We already know two bytes exist due to len(idx + 4).
        raise ValueError("missing CRLF after Trojan request")

    idx += 2

    return TrojanRequest(
        password_hash=password_hash,
        cmd=cmd,
        address_type=address_type,
        target_host=target_host,
        target_port=target_port,
        payload_offset=idx,
    )


def parse_trojan_header(
    data: bytes,
) -> Optional[Tuple[str, int, str, int, int]]:
    """
    Backward-compatible parser.

    Returns:
        (hex_hash, cmd, target_host, target_port, payload_offset)

    Returns None for malformed/incomplete input.
    """
    try:
        req = _parse_request_header(data)
    except (ValueError, _NeedMoreData):
        return None

    return (
        req.password_hash,
        req.cmd,
        req.target_host,
        req.target_port,
        req.payload_offset,
    )


async def _read_trojan_request(
    websocket: WebSocket,
) -> tuple[TrojanRequest, bytes]:
    """
    Receives enough binary WS frames to parse the Trojan request header.

    Returns:
        request, payload_already_appended_to_the_header
    """
    buffer = bytearray()

    while True:
        data = await _receive_binary(
            websocket,
            timeout=FIRST_FRAME_TIMEOUT,
        )

        if data is None:
            raise WebSocketDisconnect()

        if not data:
            continue

        buffer.extend(data)

        if len(buffer) > MAX_FIRST_BUFFER:
            raise ValueError("Trojan request header exceeds safety buffer")

        try:
            request = _parse_request_header(bytes(buffer))
        except _NeedMoreData:
            continue

        payload = bytes(buffer[request.payload_offset :])
        return request, payload


async def _authenticate(
    key: str,
    request: TrojanRequest,
    find_link_func: Callable[[str], tuple[str | None, dict | None]],
    is_ip_allowed_func: Callable[..., bool],
    links_lock: asyncio.Lock,
    client_ip: str,
) -> tuple[str, dict]:
    async with links_lock:
        real_uid, link = find_link_func(key)

        if not link:
            raise PermissionError("link not found")

        if not _link_is_active(link):
            raise PermissionError("link inactive or expired")

        link_password = (
            link.get("password")
            or link.get("uuid")
            or link.get("id")
            or ""
        )
        if not isinstance(link_password, str) or not link_password:
            raise PermissionError("link has no Trojan password")

        expected_hash = _sha224_hex(link_password)

        if not hmac.compare_digest(request.password_hash, expected_hash):
            raise PermissionError("authentication failed")

        # Prefer the injected helper in compatibility mode.
        try:
            ip_ok = bool(is_ip_allowed_func(client_ip, link))
        except TypeError:
            ip_ok = _ip_allowed(link, real_uid or "", client_ip)

        if not ip_ok:
            raise PermissionError("IP limit exceeded")

        return real_uid or "", link


async def _connect_tcp(
    host: str,
    port: int,
) -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    # Keep this compatible with Python/asyncio versions that do not expose
    # the newer ``happy_eyeballs`` argument on create_connection().
    try:
        return await asyncio.wait_for(
            asyncio.open_connection(
                host,
                port,
                family=socket.AF_UNSPEC,
            ),
            timeout=TCP_CONNECT_TIMEOUT,
        )
    except TypeError as exc:
        # Extremely old asyncio builds may reject the family keyword too.
        if "family" not in str(exc):
            raise
        return await asyncio.wait_for(
            asyncio.open_connection(
                host,
                port,
            ),
            timeout=TCP_CONNECT_TIMEOUT,
        )


class _UDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, queue: asyncio.Queue[tuple[bytes, tuple[Any, ...]]]):
        self.queue = queue
        self.transport: asyncio.DatagramTransport | None = None

    def connection_made(self, transport: asyncio.BaseTransport) -> None:
        self.transport = transport  # type: ignore[assignment]

    def datagram_received(self, data: bytes, addr: tuple[Any, ...]) -> None:
        try:
            self.queue.put_nowait((bytes(data), addr))
        except asyncio.QueueFull:
            # Drop the oldest-style overflow rather than blocking the event
            # loop inside datagram_received().
            pass

    def error_received(self, exc: Exception) -> None:
        logger.debug("Trojan UDP socket error: %s", exc)

    def connection_lost(self, exc: Exception | None) -> None:
        if exc:
            logger.debug("Trojan UDP socket closed with error: %s", exc)


@dataclass(slots=True)
class _UDPTransportPair:
    ipv4: asyncio.DatagramTransport | None
    ipv6: asyncio.DatagramTransport | None


async def _create_udp_transports(
    loop: asyncio.AbstractEventLoop,
    queue: asyncio.Queue[tuple[bytes, tuple[Any, ...]]],
) -> _UDPTransportPair:
    ipv4: asyncio.DatagramTransport | None = None
    ipv6: asyncio.DatagramTransport | None = None

    try:
        transport, _ = await loop.create_datagram_endpoint(
            lambda: _UDPProtocol(queue),
            local_addr=("0.0.0.0", 0),
            family=socket.AF_INET,
            allow_broadcast=False,
        )
        ipv4 = transport
    except OSError as exc:
        logger.warning("Unable to create Trojan IPv4 UDP socket: %s", exc)

    try:
        transport, _ = await loop.create_datagram_endpoint(
            lambda: _UDPProtocol(queue),
            local_addr=("::", 0),
            family=socket.AF_INET6,
            allow_broadcast=False,
        )
        ipv6 = transport
    except OSError as exc:
        logger.warning("Unable to create Trojan IPv6 UDP socket: %s", exc)

    if ipv4 is None and ipv6 is None:
        raise OSError("Unable to create any UDP socket")

    return _UDPTransportPair(ipv4=ipv4, ipv6=ipv6)


def _close_udp_transports(transports: _UDPTransportPair) -> None:
    if transports.ipv4 is not None:
        transports.ipv4.close()
    if transports.ipv6 is not None:
        transports.ipv6.close()


async def _resolve_udp_target(
    host: str,
    port: int,
) -> list[tuple[int, tuple[Any, ...]]]:
    """
    Resolve one Trojan UDP destination to usable IPv4/IPv6 socket addresses.
    IP literals avoid a DNS lookup.
    """
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None

    if ip is not None:
        family = socket.AF_INET if ip.version == 4 else socket.AF_INET6
        return [
            (
                family,
                (str(ip), port)
                if family == socket.AF_INET
                else (str(ip), port, 0, 0),
            )
        ]

    infos = await asyncio.get_running_loop().getaddrinfo(
        host,
        port,
        family=socket.AF_UNSPEC,
        type=socket.SOCK_DGRAM,
    )

    result: list[tuple[int, tuple[Any, ...]]] = []
    seen: set[tuple[int, tuple[Any, ...]]] = set()

    for family, socktype, proto, canonname, sockaddr in infos:
        if family not in (socket.AF_INET, socket.AF_INET6):
            continue
        item = (family, tuple(sockaddr))
        if item in seen:
            continue
        seen.add(item)
        result.append(item)

    if not result:
        raise OSError(f"Unable to resolve UDP target: {host}:{port}")

    return result


def _udp_record(
    source: tuple[Any, ...],
    payload: bytes,
) -> bytes:
    """
    Trojan UDP response packet:
        ATYP + SRC.ADDR + SRC.PORT + LENGTH + CRLF + PAYLOAD
    """
    if len(payload) > UDP_MAX_PAYLOAD:
        raise ValueError("UDP payload too large")

    host = source[0]
    port = int(source[1])

    try:
        ip = ipaddress.ip_address(host)
    except ValueError as exc:
        raise ValueError("UDP source is not an IP address") from exc

    if ip.version == 4:
        header = bytes([1]) + ip.packed
    else:
        header = bytes([4]) + ip.packed

    return header + struct.pack("!HH", port, len(payload)) + b"\r\n" + payload


def _parse_udp_records(
    buffer: bytes,
) -> tuple[list[tuple[str, int, bytes]], bytes]:
    """
    Parses zero or more Trojan UDP records.

    Returns:
        (complete_records, incomplete_tail)
    """
    records: list[tuple[str, int, bytes]] = []
    idx = 0
    total = len(buffer)

    while idx < total:
        start = idx

        if total - idx < 1:
            break

        atype = buffer[idx]
        idx += 1

        if atype == 1:
            if total - idx < 4:
                idx = start
                break
            host = socket.inet_ntoa(buffer[idx : idx + 4])
            idx += 4

        elif atype == 3:
            if total - idx < 1:
                idx = start
                break

            domain_len = buffer[idx]
            idx += 1

            if domain_len == 0 or domain_len > MAX_DOMAIN_LENGTH:
                raise ValueError("invalid UDP domain length")

            if total - idx < domain_len:
                idx = start
                break

            try:
                host = buffer[idx : idx + domain_len].decode("idna")
            except UnicodeError:
                host = buffer[idx : idx + domain_len].decode(
                    "utf-8",
                    errors="strict",
                )

            idx += domain_len

        elif atype == 4:
            if total - idx < 16:
                idx = start
                break
            host = socket.inet_ntop(socket.AF_INET6, buffer[idx : idx + 16])
            idx += 16

        else:
            raise ValueError(f"invalid UDP ATYP: {atype}")

        if total - idx < 6:
            idx = start
            break

        port, length = struct.unpack("!HH", buffer[idx : idx + 4])
        idx += 4

        if buffer[idx : idx + 2] != b"\r\n":
            raise ValueError("invalid UDP CRLF")

        idx += 2

        if port == 0:
            raise ValueError("UDP destination port cannot be zero")

        if length > UDP_MAX_PAYLOAD:
            raise ValueError("UDP payload exceeds maximum size")

        if total - idx < length:
            idx = start
            break

        payload = bytes(buffer[idx : idx + length])
        idx += length
        records.append((host, port, payload))

    return records, bytes(buffer[idx:])


async def _trojan_tcp_relay(
    websocket: WebSocket,
    reader: asyncio.StreamReader,
    writer: asyncio.StreamWriter,
    conn_id: str,
    uid: str,
    initial_payload: bytes,
) -> None:
    if initial_payload:
        if not await _quota_check(uid, len(initial_payload)):
            raise PermissionError("quota exceeded")

        await _throttle(uid, len(initial_payload))
        writer.write(initial_payload)
        await writer.drain()
        _safe_stat_inc("total_requests")
        _add_connection_bytes(conn_id, len(initial_payload))

    async def ws_to_tcp() -> None:
        try:
            while True:
                data = await _receive_binary(websocket)
                if data is None or not data:
                    break

                if not await _quota_check(uid, len(data)):
                    await _close_ws(websocket, 1008, "quota/disabled/unknown")
                    return

                await _throttle(uid, len(data))
                writer.write(data)

                if writer.transport and (
                    writer.transport.get_write_buffer_size() > RELAY_BUF
                ):
                    await writer.drain()

                _safe_stat_inc("total_requests")
                _add_connection_bytes(conn_id, len(data))

            try:
                if writer.can_write_eof():
                    writer.write_eof()
            except Exception:
                pass

        except (WebSocketDisconnect, asyncio.CancelledError):
            raise
        except Exception as exc:
            logger.debug("Trojan WS->TCP closed [%s]: %s", conn_id, exc)

    async def tcp_to_ws() -> None:
        try:
            while True:
                data = await reader.read(RELAY_BUF)
                if not data:
                    break

                if not await _quota_check(uid, len(data)):
                    await _close_ws(websocket, 1008, "quota/disabled/unknown")
                    return

                await _throttle(uid, len(data))
                await websocket.send_bytes(data)
                _add_connection_bytes(conn_id, len(data))

        except asyncio.CancelledError:
            raise
        except Exception as exc:
            logger.debug("Trojan TCP->WS closed [%s]: %s", conn_id, exc)

    tasks = {
        asyncio.create_task(ws_to_tcp()),
        asyncio.create_task(tcp_to_ws()),
    }

    try:
        done, pending = await asyncio.wait(
            tasks,
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()

        await asyncio.gather(*done, *pending, return_exceptions=True)
    finally:
        await _close_ws(websocket)


async def _trojan_udp_relay(
    websocket: WebSocket,
    conn_id: str,
    uid: str,
    initial_payload: bytes,
) -> None:
    loop = asyncio.get_running_loop()
    incoming: asyncio.Queue[tuple[bytes, tuple[Any, ...]]] = asyncio.Queue(
        maxsize=256
    )
    transports = await _create_udp_transports(loop, incoming)

    outbound_buffer = bytearray(initial_payload)
    dns_cache: dict[
        tuple[str, int],
        list[tuple[int, tuple[Any, ...]]],
    ] = {}

    async def send_udp_record(
        host: str,
        port: int,
        payload: bytes,
    ) -> None:
        if not payload:
            return

        cache_key = (host, port)
        targets = dns_cache.get(cache_key)

        if targets is None:
            targets = await _resolve_udp_target(host, port)
            dns_cache[cache_key] = targets

        last_exc: Exception | None = None

        for family, sockaddr in targets:
            transport = (
                transports.ipv4
                if family == socket.AF_INET
                else transports.ipv6
            )

            if transport is None:
                continue

            try:
                transport.sendto(payload, sockaddr)
                return
            except Exception as exc:
                last_exc = exc

        if last_exc:
            raise last_exc

        raise OSError(f"No UDP transport available for {host}:{port}")

    async def process_client_udp(buffer: bytearray) -> None:
        records, tail = _parse_udp_records(bytes(buffer))
        buffer.clear()
        buffer.extend(tail)

        for host, port, payload in records:
            if not await _quota_check(uid, len(payload)):
                await _close_ws(websocket, 1008, "quota/disabled/unknown")
                raise PermissionError("quota exceeded")

            await _throttle(uid, len(payload))
            await send_udp_record(host, port, payload)

            _safe_stat_inc("total_requests")
            _add_connection_bytes(conn_id, len(payload))

    async def ws_to_udp() -> None:
        nonlocal outbound_buffer

        # The first request payload, if any, is already part of the UDP stream.
        if outbound_buffer:
            await process_client_udp(outbound_buffer)

        while True:
            data = await _receive_binary(websocket)
            if data is None:
                break

            if not data:
                continue

            if len(outbound_buffer) + len(data) > MAX_WS_UDP_BUFFER:
                raise ValueError("UDP WebSocket buffer exceeded safety limit")

            outbound_buffer.extend(data)
            await process_client_udp(outbound_buffer)

    async def udp_to_ws() -> None:
        while True:
            try:
                data, addr = await asyncio.wait_for(
                    incoming.get(),
                    timeout=UDP_IDLE_TIMEOUT,
                )
            except asyncio.TimeoutError:
                return

            if len(data) > UDP_MAX_PAYLOAD:
                continue

            packet = _udp_record(addr, data)

            if not await _quota_check(uid, len(packet)):
                await _close_ws(websocket, 1008, "quota/disabled/unknown")
                return

            await _throttle(uid, len(packet))
            await websocket.send_bytes(packet)
            _add_connection_bytes(conn_id, len(packet))

    tasks = {
        asyncio.create_task(ws_to_udp()),
        asyncio.create_task(udp_to_ws()),
    }

    try:
        done, pending = await asyncio.wait(
            tasks,
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()

        await asyncio.gather(*done, *pending, return_exceptions=True)

    finally:
        _close_udp_transports(transports)
        await _close_ws(websocket)


async def _run_trojan(
    websocket: WebSocket,
    key: str,
    find_link_func: Callable[[str], tuple[str | None, dict | None]],
    is_ip_allowed_func: Callable[..., bool],
    links_lock: asyncio.Lock,
) -> None:
    await websocket.accept()

    conn_id = f"trojan-{id(websocket)}"
    client_ip = _client_ip(websocket)

    real_uid = ""
    target_writer: asyncio.StreamWriter | None = None

    try:
        # ── Frame 1+: Trojan authentication + request ───────────────────────
        request, initial_payload = await _read_trojan_request(websocket)

        real_uid, link = await _authenticate(
            key=key,
            request=request,
            find_link_func=find_link_func,
            is_ip_allowed_func=is_ip_allowed_func,
            links_lock=links_lock,
            client_ip=client_ip,
        )

        # Register only after authentication succeeds.
        _register_connection(conn_id, real_uid, client_ip)
        logger.info(
            "✅ Trojan [%s] uid=%s ip=%s cmd=%s target=%s:%s",
            conn_id,
            real_uid[:8] if real_uid else "?",
            client_ip,
            request.cmd,
            request.target_host,
            request.target_port,
        )

        # The request header itself counts toward traffic quota in the same
        # spirit as the VMess relay's initial frame accounting.
        # We cannot recover its exact frame boundaries here, so account only
        # the parsed request header bytes plus any initial payload handled below.
        header_bytes = request.payload_offset
        if not await _quota_check(real_uid, header_bytes):
            await _close_ws(websocket, 1008, "quota/disabled/unknown")
            return
        await _throttle(real_uid, header_bytes)
        _safe_stat_inc("total_requests")
        _add_connection_bytes(conn_id, header_bytes)

        if request.cmd == 1:
            # ── TCP CONNECT ─────────────────────────────────────────────────
            try:
                reader, writer = await _connect_tcp(
                    request.target_host,
                    request.target_port,
                )
                target_writer = writer
            except Exception as exc:
                logger.warning(
                    "Trojan connect failed [%s] %s:%s -> %s",
                    conn_id,
                    request.target_host,
                    request.target_port,
                    exc,
                )
                await _close_ws(
                    websocket,
                    1011,
                    "Failed to connect to target",
                )
                return

            sock = writer.transport.get_extra_info("socket")
            if sock is not None:
                try:
                    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                except OSError:
                    pass

            await _trojan_tcp_relay(
                websocket=websocket,
                reader=reader,
                writer=writer,
                conn_id=conn_id,
                uid=real_uid,
                initial_payload=initial_payload,
            )
            return

        # ── UDP ASSOCIATE ────────────────────────────────────────────────────
        await _trojan_udp_relay(
            websocket=websocket,
            conn_id=conn_id,
            uid=real_uid,
            initial_payload=initial_payload,
        )

    except PermissionError as exc:
        logger.warning(
            "🚫 Trojan rejected [%s] ip=%s: %s",
            conn_id,
            client_ip,
            exc,
        )
        await _close_ws(websocket, 1008, str(exc))

    except (WebSocketDisconnect, asyncio.CancelledError):
        pass

    except (ValueError, _NeedMoreData) as exc:
        logger.warning(
            "⚠️ Trojan header/request error [%s] ip=%s: %s",
            conn_id,
            client_ip,
            exc,
        )
        await _close_ws(websocket, 1002, "Invalid Trojan request")

    except Exception as exc:
        _record_error(exc, conn_id)
        logger.exception("Trojan tunnel error [%s]: %s", conn_id, exc)
        await _close_ws(websocket, 1011, "Trojan relay error")

    finally:
        if target_writer is not None:
            try:
                target_writer.close()
                await target_writer.wait_closed()
            except Exception:
                pass

        _remove_connection(conn_id)

        try:
            if main is not None and hasattr(main, "save_state"):
                asyncio.create_task(main.save_state())
        except Exception:
            pass

        await _close_ws(websocket)

        logger.info(
            "🔌 Trojan closed [%s] ip=%s",
            conn_id,
            client_ip,
        )


async def handle_trojan_ws(
    websocket: WebSocket,
    key: str,
    find_link_func,
    is_ip_allowed_func,
    links_lock: asyncio.Lock,
):
    """
    Backward-compatible public handler.

    Existing route code can keep calling:
        await handle_trojan_ws(ws, key, find_link_by_key,
                               is_ip_allowed, LINKS_LOCK)
    """
    await _run_trojan(
        websocket=websocket,
        key=key,
        find_link_func=find_link_func,
        is_ip_allowed_func=is_ip_allowed_func,
        links_lock=links_lock,
    )


async def websocket_tunnel_trojan(
    websocket: WebSocket,
    key: str,
):
    """
    Integrated wrapper for the same main.py architecture used by the
    VMess relay.

    Expected main.py helpers:
        LINKS_LOCK
        find_link_by_key(key)
        is_ip_allowed(link, uid, ip)
    """
    if main is None:
        raise RuntimeError("main.py is not available")

    links_lock = getattr(main, "LINKS_LOCK", None)
    find_link_by_key = getattr(main, "find_link_by_key", None)
    is_ip_allowed = getattr(main, "is_ip_allowed", None)

    if links_lock is None or find_link_by_key is None or is_ip_allowed is None:
        raise RuntimeError(
            "main.py is missing LINKS_LOCK/find_link_by_key/is_ip_allowed"
        )

    await _run_trojan(
        websocket=websocket,
        key=key,
        find_link_func=find_link_by_key,
        is_ip_allowed_func=is_ip_allowed,
        links_lock=links_lock,
    )


__all__ = [
    "TrojanRequest",
    "parse_trojan_header",
    "handle_trojan_ws",
    "websocket_tunnel_trojan",
]
