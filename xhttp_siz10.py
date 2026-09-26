# xhttp_siz10.py
# ══════════════════════════════════════════════════════════════════════════════
# Siz10a · XHTTP Ultra Transport — two modes: packet-up / stream-up
# Built from the known multi-protocol working XHTTP core.
# Only VLESS mobile compatibility and Trojan-UDP remainder handling are changed.
#  (stream-one حذف شد. منطق relay_vless دست‌نخورده.
#   stream-up بازنویسی شده با موتور تطبیقی: _AdaptiveFlow (AIMD روی high-water)
#   + _QuotaGate تطبیقی (batch بر اساس نرخ واقعی هر سشن) + سوکت تیون‌شده)
# ══════════════════════════════════════════════════════════════════════════════

import asyncio
import hmac
import secrets
import socket
import time
from datetime import datetime

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse

from main import (
    LINKS,
    LINKS_LOCK,
    stats,
    hourly_traffic,
    connections,
    error_logs,
    logger,
    is_link_allowed,
    is_ip_allowed,
    save_state,
)
from relay_vless import parse_vless_header, check_and_use
from relay_vmess import (
    _decode_request_header,
    _check_replay,
    _build_response_header,
    _VMessBodyFramer,
    _BodyDecoder,
    _BodyEncoder,
    SEC_AES_GCM, SEC_CHACHA20_POLY1305, SEC_NONE, SEC_ZERO,
)
from relay_trojan import (
    _parse_request_header,
    _NeedMoreData,
    _sha224_hex,
    _create_udp_transports,
    _resolve_udp_target,
    _udp_record,
    _parse_udp_records,
)
from main import normalize_protocol, split_protocol
from speed_limit import throttle

router = APIRouter()

XHTTP_BUF = 512 * 1024
DOWNLINK_QUEUE_MAX = 512
SESSION_IDLE_TIMEOUT = 30
REAPER_INTERVAL = 10
TCP_CONNECT_TIMEOUT = 10.0

# ── تنظیمات موتور تطبیقی ──────────────────────────────────────────────────────
SOCK_BUF_SIZE = 2 * 1024 * 1024     # SO_SNDBUF / SO_RCVBUF

# _AdaptiveFlow: بازه‌ی مجاز برای high-water تطبیقی (AIMD)
FLOW_MIN_HW = 256 * 1024
FLOW_MAX_HW = 16 * 1024 * 1024
FLOW_START_HW = 2 * 1024 * 1024
FLOW_FAST_DRAIN_MS = 2.0    # زیر این یعنی downstream خیلی سریعه → بافر مجاز رو زیاد کن
FLOW_SLOW_DRAIN_MS = 25.0   # بالای این یعنی backpressure واقعی → فوری نصفش کن

# _QuotaGate: بازه‌ی مجاز برای batch تطبیقی چک کوتا
QUOTA_MIN_BATCH = 32 * 1024
QUOTA_MAX_BATCH = 1 * 1024 * 1024
QUOTA_START_BATCH = 64 * 1024
QUOTA_CHECK_INTERVAL = 0.2  # سقف زمانی؛ حتی اگر batch پر نشده، بعد این مدت چک کن

PACKET_UP_HIGH_WATER = 2 * 1024 * 1024  # packet-up همون منطق ساده‌ی قبلی رو داره (تمرکز این راند فقط stream-up بود)
MAX_BUFFERED_POSTS = 30

xhttp_sessions: dict = {}
XHTTP_LOCK = asyncio.Lock()

FINGERPRINTS = {
    # XHTTP downlink is an HTTP streaming response; Xray uses SSE-style
    # headers for the default disguise. The proxy payload itself remains raw.
    "chrome": {
        "content-type": "text/event-stream; charset=utf-8",
        "cache-control": "no-store",
        "x-accel-buffering": "no",
        "access-control-allow-origin": "*",
        "access-control-allow-methods": "GET, POST",
    },
    "plain": {
        "content-type": "application/octet-stream",
        "cache-control": "no-store",
        "x-accel-buffering": "no",
        "access-control-allow-origin": "*",
        "access-control-allow-methods": "GET, POST",
    },
}
DEFAULT_FINGERPRINT = "chrome"


def _resp_headers(fp: str) -> dict:
    return dict(FINGERPRINTS.get(fp, FINGERPRINTS[DEFAULT_FINGERPRINT]))



def _tune_socket(writer: asyncio.StreamWriter):
    """TCP_NODELAY + بافرهای بزرگ‌تر سوکت برای کاهش سربار سیستم‌عامل روی ترافیک بالا."""
    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCK_BUF_SIZE)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, SOCK_BUF_SIZE)
    except OSError:
        pass


class _QuotaGate:
    """
    نسخه‌ی تطبیقی: به‌جای await check_and_use() به‌ازای هر چانک، و به‌جای یک آستانه‌ی
    ثابت، نرخ واقعی ترافیک هر سشن رو با EWMA اندازه می‌گیره و اندازه‌ی batch رو زنده
    عوض می‌کنه:
      - سشن پرسرعت (دانلود حجیم) → batch بزرگ می‌شه → await های سنگین کمتر.
      - سشن کم‌ترافیک/تعاملی → batch کوچیک می‌مونه → کوتا دقیق‌تر و قطع سریع‌تر
        اگه کاربر تموم کرده باشه.
    داده هیچ‌وقت نگه داشته نمی‌شه، فقط لحظه‌ی چک‌کردنِ کوتا adaptive هست.
    """
    __slots__ = ("uuid", "pending", "last_check", "ok", "batch_bytes", "rate_ewma")

    def __init__(self, uuid: str):
        self.uuid = uuid
        self.pending = 0
        self.last_check = time.monotonic()
        self.ok = True
        self.batch_bytes = QUOTA_START_BATCH
        self.rate_ewma = 0.0

    async def add(self, nbytes: int) -> bool:
        if not self.ok:
            return False
        self.pending += nbytes
        now = time.monotonic()
        elapsed = now - self.last_check
        if self.pending >= self.batch_bytes or elapsed >= QUOTA_CHECK_INTERVAL:
            flush, self.pending = self.pending, 0
            if elapsed > 0:
                inst_rate = flush / elapsed
                self.rate_ewma = inst_rate if self.rate_ewma == 0 else (0.7 * self.rate_ewma + 0.3 * inst_rate)
                target = int(self.rate_ewma * QUOTA_CHECK_INTERVAL)
                self.batch_bytes = max(QUOTA_MIN_BATCH, min(QUOTA_MAX_BATCH, target or QUOTA_MIN_BATCH))
            self.last_check = now
            self.ok = await check_and_use(self.uuid, flush)
            return self.ok
        return True

    async def flush(self) -> bool:
        if self.pending:
            flush, self.pending = self.pending, 0
            self.ok = self.ok and await check_and_use(self.uuid, flush)
        return self.ok


class _AdaptiveFlow:
    """
    high-water تطبیقی برای drain(), رفتار شبیه AIMD در TCP congestion control:
      - هر بار drain() صدا زده می‌شه، مدت زمانش اندازه‌گیری می‌شه.
      - اگه سریع تموم بشه (لینک پایین‌دستی داره جواب می‌ده) → سقف بافر مجاز رو
        additive increase می‌کنیم؛ یعنی دفعه‌ی بعد دیرتر drain صدا زده می‌شه،
        پس syscall/context-switch کمتر می‌شه و throughput واقعی بالا می‌ره.
      - اگه drain کند بشه (backpressure واقعیه، صف داره جمع می‌شه) → سقف رو فوری
        نصف می‌کنیم (multiplicative decrease) تا بافربلوت/لتنسی رشد نکنه.
    هر سشن یک نمونه‌ی جدا از این داره، پس مسیرهای کند و سریع تداخلی با هم ندارن.
    """
    __slots__ = ("high_water", "last_drain_ms")

    def __init__(self):
        self.high_water = FLOW_START_HW
        self.last_drain_ms = 0.0

    def should_drain(self, buf_size: int) -> bool:
        return buf_size > self.high_water

    async def drain(self, writer: asyncio.StreamWriter):
        t0 = time.monotonic()
        await writer.drain()
        elapsed_ms = (time.monotonic() - t0) * 1000
        self.last_drain_ms = elapsed_ms
        if elapsed_ms < FLOW_FAST_DRAIN_MS:
            self.high_water = min(FLOW_MAX_HW, int(self.high_water * 1.5) + 65536)
        elif elapsed_ms > FLOW_SLOW_DRAIN_MS:
            self.high_water = max(FLOW_MIN_HW, self.high_water // 2)


def _req_client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"




MAX_HANDSHAKE_BUFFER = 64 * 1024


def _family_for_link(link: dict) -> tuple[str, str]:
    return split_protocol(normalize_protocol(link.get("protocol")))


def _is_incomplete_vless_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return any(k in msg for k in (
        "chunk too small", "index out of range", "out of range",
        "truncated", "not enough", "invalid",
    ))


def _vmess_header_incomplete(error: str) -> bool:
    msg = (error or "").lower()
    return any(k in msg for k in ("کافی نیست", "ناقص", "truncated", "incomplete"))


async def _check_link(uuid: str):
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    if not is_link_allowed(link):
        raise HTTPException(status_code=403, detail="not authorized")
    return link


async def _get_or_create_session(uuid: str, mode: str, session_id: str, ip: str = "نامشخص") -> dict:
    """Create an XHTTP session and lock its inner proxy protocol to the link."""
    async with XHTTP_LOCK:
        sess = xhttp_sessions.get(session_id)
        if sess is not None:
            if sess.get("uuid") != uuid or sess.get("mode") != mode:
                raise HTTPException(status_code=409, detail="session id already belongs to another connection")
            sess["last_seen"] = time.time()
            return sess

        async with LINKS_LOCK:
            link = LINKS.get(uuid)
        if not is_link_allowed(link):
            raise HTTPException(status_code=403, detail="not authorized")
        if not is_ip_allowed(link, uuid, ip):
            logger.warning(f"🚫 XHTTP[{mode}] rejected uuid={uuid[:8]} ip={ip} (ip limit reached)")
            raise HTTPException(status_code=403, detail="ip limit reached")

        family, transport = _family_for_link(link)
        expected_mode = transport if family != "vless" or transport != "ws" else None
        if expected_mode not in ("packet-up", "stream-up"):
            raise HTTPException(status_code=404, detail="link is not an XHTTP configuration")
        if expected_mode != mode:
            raise HTTPException(status_code=404, detail="XHTTP mode mismatch")

        conn_id = secrets.token_urlsafe(6)
        connections[conn_id] = {
            "uuid": uuid,
            "ip": ip,
            "connected_at": datetime.now().isoformat(),
            "bytes": 0,
            "transport": f"xhttp-{family}-{mode}",
        }
        sess = {
            "uuid": uuid, "mode": mode, "family": family,
            "session_id": session_id,
            "writer": None,
            "reader": None,
            "downlink_task": None,
            "uplink_task": None,
            "udp_task": None,
            "down_q": asyncio.Queue(maxsize=DOWNLINK_QUEUE_MAX),
            "last_seen": time.time(),
            "conn_id": conn_id, "tcp_open": False, "udp_open": False,
            "transport_open": False, "closed": False,
            "seq_buf": {}, "next_seq": 0,
            "gate": None,
            "flow": None,
            "handshake_buffer": bytearray(),
            "protocol_info": None,
            "vmess_decoder": None,
            "vmess_encoder": None,
            "udp_incoming": None,
            "udp_transports": None,
            "udp_dns_cache": {},
            "udp_buffer": bytearray(),
            "vmess_udp_transport": None,
            "vmess_udp_queue": None,
        }
        xhttp_sessions[session_id] = sess
        logger.info(f"new XHTTP[{family}/{mode}] session [{session_id[:8]}] uuid={uuid[:8]} ip={ip}")
        return sess


async def _teardown(session_id: str):
    async with XHTTP_LOCK:
        sess = xhttp_sessions.pop(session_id, None)
    if not sess:
        return
    sess["closed"] = True
    for t in ("uplink_task", "downlink_task", "udp_task"):
        task = sess.get(t)
        if task and task is not asyncio.current_task():
            task.cancel()
            try:
                await task
            except (asyncio.CancelledError, Exception):
                pass
    writer = sess.get("writer")
    if writer:
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass
    vmess_udp_transport = sess.get("vmess_udp_transport")
    if vmess_udp_transport:
        try:
            vmess_udp_transport.close()
        except Exception:
            pass

    pair = sess.get("udp_transports")
    if pair:
        for tr in (getattr(pair, "ipv4", None), getattr(pair, "ipv6", None)):
            if tr:
                try:
                    tr.close()
                except Exception:
                    pass
    connections.pop(sess.get("conn_id"), None)
    dq = sess.get("down_q")
    if dq:
        try:
            dq.put_nowait(None)
        except Exception:
            pass
    logger.info(f"closed XHTTP[{sess.get('family')}/{sess.get('mode')}] [{session_id[:8]}] total={len(xhttp_sessions)}")


async def _reaper():
    while True:
        await asyncio.sleep(REAPER_INTERVAL)
        now = time.time()
        async with XHTTP_LOCK:
            stale = [
                sid for sid, s in xhttp_sessions.items()
                if now - s["last_seen"] > SESSION_IDLE_TIMEOUT and not s.get("transport_open")
            ]
        for sid in stale:
            await _teardown(sid)


_reaper_started = False


def ensure_reaper():
    global _reaper_started
    if not _reaper_started:
        asyncio.create_task(_reaper())
        _reaper_started = True


async def _connect_target(host: str, port: int):
    reader, writer = await asyncio.wait_for(
        asyncio.open_connection(host, port), timeout=TCP_CONNECT_TIMEOUT
    )
    _tune_socket(writer)
    return reader, writer


class _XHTTPVMessUDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, queue: asyncio.Queue):
        self.queue = queue
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        if data:
            try:
                self.queue.put_nowait((data, addr))
            except asyncio.QueueFull:
                logger.warning("XHTTP VMess UDP receive queue full; dropping datagram from %s", addr)

    def error_received(self, exc):
        logger.warning("XHTTP VMess UDP socket error: %s", exc)

    def connection_lost(self, exc):
        try:
            self.queue.put_nowait((None, None))
        except asyncio.QueueFull:
            pass


async def _open_xhttp_vmess_udp(host: str, port: int):
    loop = asyncio.get_running_loop()
    queue = asyncio.Queue(maxsize=256)
    transport, protocol = await asyncio.wait_for(
        loop.create_datagram_endpoint(
            lambda: _XHTTPVMessUDPProtocol(queue),
            remote_addr=(host, port),
        ),
        timeout=TCP_CONNECT_TIMEOUT,
    )
    return transport, protocol, queue


async def _write_vmess_udp(sess: dict, data: bytes):
    if not data:
        return
    decoder = sess.get("vmess_decoder")
    transport = sess.get("vmess_udp_transport")
    if decoder is None or transport is None:
        raise ConnectionError("VMess UDP transport is not available")
    for datagram in decoder.feed(data):
        if datagram:
            transport.sendto(datagram)


async def _pump_vmess_udp_to_queue(sess: dict, queue: asyncio.Queue):
    gate = _QuotaGate(sess["uuid"])
    delivered = 0
    try:
        while True:
            data, _addr = await queue.get()
            if data is None:
                break
            if not await gate.add(len(data)):
                break
            await throttle(sess["uuid"], len(data))
            c = connections.get(sess["conn_id"])
            if c:
                c["bytes"] += len(data)
            delivered += len(data)
            encoder = sess.get("vmess_encoder")
            if encoder:
                for chunk in encoder.encode(data):
                    await sess["down_q"].put(chunk)
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        logger.debug("XHTTP VMess UDP downlink closed: %s", exc)
    finally:
        await gate.flush()
        logger.info(
            "downlink closed XHTTP[vmess/%s] [%s] udp-bytes=%d",
            sess.get("mode"), sess.get("session_id", "?")[:8], delivered
        )
        await _teardown(sess["session_id"])


async def _authenticate_and_parse_trojan(sess: dict, buffer: bytes):
    try:
        req = _parse_request_header(buffer)
    except _NeedMoreData:
        return None

    link = LINKS.get(sess["uuid"])
    password = (link or {}).get("password") or sess["uuid"]
    expected = _sha224_hex(password) if password else ""
    if not expected or not hmac.compare_digest(req.password_hash, expected):
        raise ValueError("Trojan authentication failed")
    return req


async def _try_initialize(sess: dict):
    """Try to consume the protocol handshake from handshake_buffer.
    Returns (ready, remainder)."""
    family = sess["family"]
    uuid = sess["uuid"]
    buf = bytes(sess["handshake_buffer"])
    if not buf:
        return False, b""

    if len(buf) > MAX_HANDSHAKE_BUFFER:
        raise ValueError("XHTTP protocol header exceeds safety buffer")

    if family == "vless":
        try:
            command, address, port, payload = await parse_vless_header(buf)
        except Exception as exc:
            if len(buf) < 64 * 1024 and _is_incomplete_vless_error(exc):
                return False, b""
            raise
        # Mobile-compatibility: keep the legacy relay behavior and let the
        # TCP target connection follow the parsed VLESS request.
        reader, writer = await _connect_target(address, port)
        sess["reader"], sess["writer"] = reader, writer
        sess["tcp_open"] = True
        sess["transport_open"] = True
        logger.info(f"connect XHTTP[vless/{sess['mode']}] [{sess['uuid'][:8]}] -> {address}:{port}")
        sess["downlink_task"] = asyncio.create_task(_pump_tcp_to_queue(sess, reader))
        return True, payload

    if family == "vmess":
        info, err = _decode_request_header(buf, uuid)
        if err or not info:
            if _vmess_header_incomplete(err or ""):
                return False, b""
            raise ValueError(err or "invalid VMess header")
        if not await _check_replay(info["auth_id"]):
            raise ValueError("VMess AuthID replay detected")
        if info["sec_type"] not in (SEC_AES_GCM, SEC_CHACHA20_POLY1305, SEC_NONE, SEC_ZERO):
            raise ValueError(f"unsupported VMess security type: {info['sec_type']}")

        sess["protocol_info"] = info
        request_framer = _VMessBodyFramer(
            info["sec_type"], info["req_key"], info["req_iv"], info["option"]
        )
        response_key = info.get("resp_body_key") or __import__("hashlib").sha256(info["req_key"]).digest()[:16]
        response_iv = info.get("resp_body_iv") or __import__("hashlib").sha256(info["req_iv"]).digest()[:16]
        sess["vmess_decoder"] = _BodyDecoder(request_framer)
        sess["vmess_encoder"] = _BodyEncoder(
            _VMessBodyFramer(
                info["sec_type"], response_key, response_iv, info["option"],
                length_key=info["req_key"], length_iv=info["req_iv"],
            )
        )

        if info["cmd"] == 2:
            udp_transport, _protocol, udp_queue = await _open_xhttp_vmess_udp(info["host"], info["port"])
            sess["vmess_udp_transport"] = udp_transport
            sess["vmess_udp_queue"] = udp_queue
            sess["udp_open"] = True
            sess["transport_open"] = True
            await sess["down_q"].put(_build_response_header(info))
            sess["downlink_task"] = asyncio.create_task(
                _pump_vmess_udp_to_queue(sess, udp_queue)
            )
            logger.info(
                f"connect XHTTP[vmess/{sess['mode']}/udp] [{sess['uuid'][:8]}] -> {info['host']}:{info['port']}"
            )
            body_init = info.get("body_init") or b""
            if body_init:
                await _write_vmess_udp(sess, body_init)
            return True, b""

        reader, writer = await _connect_target(info["host"], info["port"])
        sess["reader"], sess["writer"] = reader, writer
        sess["tcp_open"] = True
        sess["transport_open"] = True
        await sess["down_q"].put(_build_response_header(info))
        logger.info(f"connect XHTTP[vmess/{sess['mode']}] [{sess['uuid'][:8]}] -> {info['host']}:{info['port']}")
        sess["downlink_task"] = asyncio.create_task(_pump_tcp_to_queue(sess, reader))
        body_init = info.get("body_init") or b""
        if body_init:
            plaintext_parts = sess["vmess_decoder"].feed(body_init)
            for plaintext in plaintext_parts:
                writer.write(plaintext)
            if plaintext_parts:
                await writer.drain()
        return True, b""

    if family == "trojan":
        req = await _authenticate_and_parse_trojan(sess, buf)
        if req is None:
            return False, b""
        sess["protocol_info"] = req
        if req.cmd == 1:
            reader, writer = await _connect_target(req.target_host, req.target_port)
            sess["reader"], sess["writer"] = reader, writer
            sess["tcp_open"] = True
            sess["transport_open"] = True
            logger.info(f"connect XHTTP[trojan/{sess['mode']}] [{sess['uuid'][:8]}] -> {req.target_host}:{req.target_port}")
            sess["downlink_task"] = asyncio.create_task(_pump_tcp_to_queue(sess, reader))
            return True, buf[req.payload_offset:]
        if req.cmd == 3:
            loop = asyncio.get_running_loop()
            incoming: asyncio.Queue = asyncio.Queue(maxsize=256)
            pair = await _create_udp_transports(loop, incoming)
            if not pair.ipv4 and not pair.ipv6:
                raise OSError("no UDP transport available")
            sess["udp_incoming"] = incoming
            sess["udp_transports"] = pair
            sess["udp_open"] = True
            sess["transport_open"] = True
            sess["udp_task"] = asyncio.create_task(_pump_udp_to_queue(sess, incoming))
            logger.info(f"open XHTTP[trojan/{sess['mode']}] UDP [{sess['uuid'][:8]}]")
            return True, buf[req.payload_offset:]
        raise ValueError("unsupported Trojan command")

    raise ValueError(f"unsupported XHTTP protocol family: {family}")


async def _write_tcp(sess: dict, data: bytes, flow: _AdaptiveFlow | None = None):
    if not data:
        return
    if sess["family"] == "vmess":
        decoder = sess.get("vmess_decoder")
        plaintexts = decoder.feed(data) if decoder else []
    else:
        plaintexts = [data]
    writer = sess.get("writer")
    if not writer:
        raise ConnectionError("target writer is not available")
    for plaintext in plaintexts:
        if not plaintext:
            continue
        writer.write(plaintext)
        if flow is not None and flow.should_drain(writer.transport.get_write_buffer_size()):
            await flow.drain(writer)
        elif flow is None and writer.transport.get_write_buffer_size() > PACKET_UP_HIGH_WATER:
            await writer.drain()


async def _process_upload_data(sess: dict, data: bytes, flow: _AdaptiveFlow | None = None):
    if not data:
        return
    sess["last_seen"] = time.time()
    if not sess.get("transport_open"):
        sess["handshake_buffer"].extend(data)
        ready, remainder = await _try_initialize(sess)
        if not ready:
            return
        if remainder:
            if sess.get("tcp_open"):
                await _write_tcp(sess, remainder, flow)
            elif sess.get("udp_open"):
                # Trojan UDP sessions do not have a TCP writer. Route the
                # remainder back through the UDP parser instead of _write_tcp.
                sess["handshake_buffer"].clear()
                await _process_upload_data(sess, remainder, flow)
                return
        sess["handshake_buffer"].clear()
        return

    if sess.get("tcp_open"):
        await _write_tcp(sess, data, flow)
        return

    if sess.get("udp_open") and sess.get("family") == "vmess":
        await _write_vmess_udp(sess, data)
        return

    # Trojan UDP transport.
    if sess.get("udp_open"):
        sess["udp_buffer"].extend(data)
        records, tail = _parse_udp_records(bytes(sess["udp_buffer"]))
        sess["udp_buffer"] = bytearray(tail)
        pair = sess.get("udp_transports")
        for host, port, payload in records:
            if not payload:
                continue
            key = (host, port)
            targets = sess["udp_dns_cache"].get(key)
            if targets is None:
                targets = await _resolve_udp_target(host, port)
                sess["udp_dns_cache"][key] = targets
            delivered = False
            for family, sockaddr in targets:
                tr = pair.ipv4 if family == socket.AF_INET else pair.ipv6
                if not tr:
                    continue
                tr.sendto(payload, sockaddr)
                delivered = True
                break
            if not delivered:
                raise OSError(f"unable to send UDP target {host}:{port}")
        return

    raise ConnectionError("XHTTP session has no active transport")


async def _pump_tcp_to_queue(sess: dict, reader: asyncio.StreamReader):
    # Keep the HTTP layer and the proxy-protocol layer separate: the HTTP
    # response advertises SSE via Content-Type, while the actual proxy bytes
    # are forwarded unchanged. VLESS gets its two-byte response header once.
    first_vless = True
    gate = _QuotaGate(sess["uuid"])
    delivered = 0
    try:
        while True:
            data = await reader.read(XHTTP_BUF)
            if not data:
                break
            if not await gate.add(len(data)):
                break
            await throttle(sess["uuid"], len(data))
            c = connections.get(sess["conn_id"])
            if c:
                c["bytes"] += len(data)
            delivered += len(data)
            sess["last_seen"] = time.time()

            if sess["family"] == "vmess":
                encoder = sess.get("vmess_encoder")
                chunks = encoder.encode(data) if encoder else []
                for chunk in chunks:
                    await sess["down_q"].put(chunk)
            else:
                if sess["family"] == "vless" and first_vless:
                    await sess["down_q"].put(b"\x00\x00")
                    first_vless = False
                await sess["down_q"].put(data)
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        logger.debug("XHTTP TCP downlink closed: %s", exc)
    finally:
        await gate.flush()
        logger.info(
            "downlink closed XHTTP[%s/%s] [%s] bytes=%d",
            sess.get("family"), sess.get("mode"),
            sess.get("session_id", "?")[:8], delivered,
        )
        await _teardown(sess["session_id"])


async def _pump_udp_to_queue(sess: dict, incoming: asyncio.Queue):
    gate = _QuotaGate(sess["uuid"])
    try:
        while True:
            data, source = await incoming.get()
            if not data:
                continue
            if not await gate.add(len(data)):
                break
            await throttle(sess["uuid"], len(data))
            c = connections.get(sess["conn_id"])
            if c:
                c["bytes"] += len(data)
            await sess["down_q"].put(_udp_record(source, data))
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        logger.debug("XHTTP UDP downlink closed: %s", exc)
    finally:
        await gate.flush()
        await _teardown(sess["session_id"])


def _downstream_gen(sess: dict):
    async def gen():
        try:
            while True:
                chunk = await sess["down_q"].get()
                if chunk is None:
                    break
                sess["last_seen"] = time.time()
                yield chunk
        finally:
            pass
    return gen()


@router.get("/xhttp-siz10/{mode}/{uuid}/{session_id}")
async def xhttp_downlink(mode: str, uuid: str, session_id: str, request: Request):
    ensure_reaper()
    if mode not in ("packet-up", "stream-up"):
        raise HTTPException(status_code=404, detail="unknown mode")
    await _check_link(uuid)
    fp = request.query_params.get("fp", DEFAULT_FINGERPRINT)
    sess = await _get_or_create_session(uuid, mode, session_id, _req_client_ip(request))
    sess["session_id"] = session_id
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")
    headers = _resp_headers(fp)
    return StreamingResponse(_downstream_gen(sess), headers=headers, media_type=headers["content-type"])


@router.post("/xhttp-siz10/packet-up/{uuid}/{session_id}/{seq}")
async def packet_up_upload(uuid: str, session_id: str, seq: int, request: Request):
    ensure_reaper()
    sess = await _get_or_create_session(uuid, "packet-up", session_id, _req_client_ip(request))
    sess["session_id"] = session_id
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    sess["last_seen"] = time.time()
    body = await request.body()
    if not body:
        return {"ok": True}

    if not await check_and_use(uuid, len(body)):
        await _teardown(session_id)
        raise HTTPException(status_code=403, detail="quota/disabled/unknown")
    await throttle(uuid, len(body))
    stats["total_requests"] += 1
    connections[sess["conn_id"]]["bytes"] += len(body)

    try:
        if seq < sess["next_seq"]:
            return {"ok": True, "duplicate": True, "connected": bool(sess.get("transport_open"))}
        if seq != sess["next_seq"] and len(sess["seq_buf"]) >= MAX_BUFFERED_POSTS:
            await _teardown(session_id)
            raise HTTPException(status_code=409, detail="too many buffered XHTTP posts")
        sess["seq_buf"][seq] = body
        while sess["next_seq"] in sess["seq_buf"]:
            pending = sess["seq_buf"].pop(sess["next_seq"])
            await _process_upload_data(sess, pending)
            sess["next_seq"] += 1
        if sess.get("writer") and sess["writer"].transport.get_write_buffer_size() > PACKET_UP_HIGH_WATER:
            await sess["writer"].drain()
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail=f"{sess.get('family', 'xhttp')} write failed")

    return {"ok": True, "connected": bool(sess.get("transport_open"))}


@router.post("/xhttp-siz10/stream-up/{uuid}/{session_id}")
async def stream_up_upload(uuid: str, session_id: str, request: Request):
    ensure_reaper()
    sess = await _get_or_create_session(uuid, "stream-up", session_id, _req_client_ip(request))
    sess["session_id"] = session_id
    if sess.get("closed"):
        raise HTTPException(status_code=404, detail="session closed")

    gate = sess.get("gate")
    if gate is None:
        gate = _QuotaGate(uuid)
        sess["gate"] = gate
    flow = sess.get("flow")
    if flow is None:
        flow = _AdaptiveFlow()
        sess["flow"] = flow
    conn = connections[sess["conn_id"]]

    try:
        async for chunk in request.stream():
            if not chunk:
                continue
            sess["last_seen"] = time.time()
            if not await gate.add(len(chunk)):
                raise HTTPException(status_code=403, detail="quota/disabled/unknown")
            await throttle(uuid, len(chunk))
            stats["total_requests"] += 1
            conn["bytes"] += len(chunk)
            await _process_upload_data(sess, chunk, flow)
    except HTTPException:
        await gate.flush()
        await _teardown(session_id)
        raise
    except Exception as exc:
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        await gate.flush()
        await _teardown(session_id)
        raise HTTPException(status_code=502, detail=f"{sess.get('family', 'xhttp')} stream error")

    await gate.flush()
    return {"ok": True}
