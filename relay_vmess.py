# relay_vmess.py
# ══════════════════════════════════════════════════════════════════════════════
# VMess AEAD Relay — Xray-compatible request/response headers + body AEAD
#
# Based on the current VMess AEAD wire format used by Xray/v2ray:
#   • CmdKey = MD5(UUID bytes + fixed VMess command-key suffix)
#   • AuthID = AES-128-ECB(KDF(CmdKey, "AES Auth ID Encryption"))
#                over [timestamp(8) | random(4) | CRC32(4)]
#   • Nested-HMAC VMess KDF (not an HMAC digest cascade)
#   • Request header contains: AuthID | encrypted_length | connection_nonce |
#     encrypted_payload
#   • AEAD AAD for request header = AuthID
#   • Response header is encrypted using SHA256(request_body_key/iv)
#   • VMess body uses 2-byte chunk length + AEAD ciphertext/tag
#   • AES-128-GCM and ChaCha20-Poly1305 body security are supported
#   • Security type 0/5 (none) is passed through as raw body
#
# Existing project hooks preserved:
#   main.find_link_by_key / is_link_allowed / is_ip_allowed / client_ip
#   main.connections / main.stats / main.error_logs / save_state / now_ir
#   relay_vless.check_and_use
#   speed_limit.throttle
# ══════════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import asyncio
import hashlib
import hmac
import logging
import secrets
import socket
import struct
import time
import zlib
from collections import OrderedDict
from typing import Optional, Tuple
from uuid import UUID

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from fastapi import WebSocket, WebSocketDisconnect

import main
from relay_vless import check_and_use
from speed_limit import throttle

logger = logging.getLogger("OMIDIRAN_PANEL.VMESS")

RELAY_BUF = 256 * 1024
TCP_CONNECT_TIMEOUT = 10.0
FIRST_FRAME_TIMEOUT = 15.0
BODY_CHUNK_SIZE = 16 * 1024
MAX_HEADER_SIZE = 64 * 1024
AUTH_ID_WINDOW = 120
AUTH_ID_CACHE_MAX = 8192

# Xray / v2ray VMess constants.
KDF_SALT = b"VMess AEAD KDF"
AUTH_ID_ENCRYPTION_KEY = "AES Auth ID Encryption"
SALT_REQ_LEN_KEY = "VMess Header AEAD Key_Length"
SALT_REQ_LEN_NONCE = "VMess Header AEAD Nonce_Length"
SALT_REQ_PAY_KEY = "VMess Header AEAD Key"
SALT_REQ_PAY_NONCE = "VMess Header AEAD Nonce"
SALT_RESP_LEN_KEY = "AEAD Resp Header Len Key"
SALT_RESP_LEN_IV = "AEAD Resp Header Len IV"
SALT_RESP_PAY_KEY = "AEAD Resp Header Key"
SALT_RESP_PAY_IV = "AEAD Resp Header IV"
VMESS_CMD_KEY_SUFFIX = b"c48619fe-8f02-49e0-b9e9-edf763e17e21"

# VMess security types used by Xray's current client encoder.
SEC_AES_GCM = 3
SEC_CHACHA20_POLY1305 = 4
SEC_NONE = 5
SEC_ZERO = 6

# VMess request option flags.
OPT_CHUNK_STREAM = 1
OPT_CONNECTION_REUSE = 2
OPT_CHUNK_MASKING = 4
OPT_GLOBAL_PADDING = 8
OPT_AUTHENTICATED_LENGTH = 16


# ══════════════════════════════════════════════════════════════════════════════
# KDF
# ══════════════════════════════════════════════════════════════════════════════

class _NestedHash:
    """Hash adapter used to reproduce Xray's nested-HMAC KDF exactly."""

    digest_size = hashlib.sha256().digest_size
    block_size = hashlib.sha256().block_size
    name = "sha256"

    __slots__ = ("_fn", "_buf")

    def __init__(self, fn):
        self._fn = fn
        self._buf = bytearray()

    def update(self, data: bytes) -> None:
        self._buf.extend(data)

    def digest(self) -> bytes:
        return self._fn(bytes(self._buf))

    def hexdigest(self) -> str:
        return self.digest().hex()

    def copy(self):
        other = _NestedHash(self._fn)
        other._buf.extend(self._buf)
        return other


def _kdf(key: bytes, *paths: bytes) -> bytes:
    """Exact Xray/v2ray VMess AEAD nested-HMAC construction."""
    fn = lambda msg: hmac.new(KDF_SALT, msg, hashlib.sha256).digest()

    for path in paths:
        parent = fn
        fn = lambda msg, path=path, parent=parent: hmac.new(
            path,
            msg,
            digestmod=lambda: _NestedHash(parent),
        ).digest()

    return fn(key)


def _kdf16(key: bytes, *paths: bytes) -> bytes:
    return _kdf(key, *paths)[:16]


# ══════════════════════════════════════════════════════════════════════════════
# VMess UUID / AuthID
# ══════════════════════════════════════════════════════════════════════════════

def _cmd_key_from_uuid(u_bytes: bytes) -> bytes:
    return hashlib.md5(u_bytes + VMESS_CMD_KEY_SUFFIX).digest()


def _aes_ecb_block(key: bytes, data: bytes, decrypt: bool) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    ctx = cipher.decryptor() if decrypt else cipher.encryptor()
    return ctx.update(data) + ctx.finalize()


def _decode_auth_id(auth_id: bytes, cmd_key: bytes) -> Tuple[Optional[int], Optional[str]]:
    if len(auth_id) != 16:
        return None, "Auth ID length invalid"

    aes_key = _kdf16(cmd_key, AUTH_ID_ENCRYPTION_KEY.encode())

    try:
        plain = _aes_ecb_block(aes_key, auth_id, decrypt=True)
    except Exception as exc:
        return None, f"Auth ID decrypt failed: {exc}"

    if len(plain) != 16:
        return None, "Auth ID plaintext length invalid"

    timestamp = struct.unpack(">Q", plain[:8])[0]
    expected_crc = struct.unpack(">I", plain[12:16])[0]
    actual_crc = zlib.crc32(plain[:12]) & 0xFFFFFFFF

    if expected_crc != actual_crc:
        return None, "Auth ID CRC32 mismatch"

    now = int(time.time())
    if abs(now - int(timestamp)) > AUTH_ID_WINDOW:
        return None, "Auth ID timestamp outside allowed window"

    return int(timestamp), None


_AUTH_ID_CACHE: "OrderedDict[bytes, float]" = OrderedDict()
_AUTH_ID_CACHE_LOCK = asyncio.Lock()


async def _check_replay(auth_id: bytes) -> bool:
    """Return True when auth_id is new; False when already seen."""
    now = time.monotonic()
    async with _AUTH_ID_CACHE_LOCK:
        # Drop stale entries first.
        stale = []
        for key, ts in _AUTH_ID_CACHE.items():
            if now - ts > AUTH_ID_WINDOW:
                stale.append(key)
            else:
                break
        for key in stale:
            _AUTH_ID_CACHE.pop(key, None)

        if auth_id in _AUTH_ID_CACHE:
            return False

        _AUTH_ID_CACHE[auth_id] = now
        while len(_AUTH_ID_CACHE) > AUTH_ID_CACHE_MAX:
            _AUTH_ID_CACHE.popitem(last=False)
        return True


# ══════════════════════════════════════════════════════════════════════════════
# Request header
# ══════════════════════════════════════════════════════════════════════════════

def _decrypt_gcm(key: bytes, nonce: bytes, ciphertext: bytes, aad: bytes | None) -> bytes:
    return AESGCM(key).decrypt(nonce, ciphertext, aad)


def _parse_address(payload: bytes, idx: int, addr_type: int) -> Tuple[str, int]:
    if addr_type == 1:  # IPv4
        if len(payload) < idx + 4:
            raise ValueError("truncated IPv4 address")
        return socket.inet_ntoa(payload[idx:idx + 4]), idx + 4

    if addr_type == 2:  # Domain
        if len(payload) < idx + 1:
            raise ValueError("truncated domain length")
        dlen = payload[idx]
        idx += 1
        if len(payload) < idx + dlen:
            raise ValueError("truncated domain address")
        return payload[idx:idx + dlen].decode("utf-8", errors="ignore"), idx + dlen

    if addr_type == 3:  # IPv6
        if len(payload) < idx + 16:
            raise ValueError("truncated IPv6 address")
        return socket.inet_ntop(socket.AF_INET6, payload[idx:idx + 16]), idx + 16

    raise ValueError(f"unknown address type: {addr_type}")


def _decode_request_header(data: bytes, user_uuid: str):
    """Decode a complete VMess AEAD request from one contiguous byte string.

    Returns:
        (info, error)
    """
    try:
        u_bytes = UUID(user_uuid).bytes
    except (ValueError, AttributeError, TypeError):
        return None, "فرمت UUID نامعتبر است"

    if len(data) < 16 + 18 + 8:
        return None, "داده‌ی هدر VMess کافی نیست"

    auth_id = data[:16]
    cmd_key = _cmd_key_from_uuid(u_bytes)

    _, auth_err = _decode_auth_id(auth_id, cmd_key)
    if auth_err:
        return None, f"اعتبارسنجی Auth ID ناموفق بود: {auth_err}"

    # VMess AEAD uses an anti-replay AuthID.
    # Replay check is performed before expensive header decryption.
    # (Caller will await the async cache check.)

    encrypted_len = data[16:34]
    connection_nonce = data[34:42]

    length_key = _kdf16(
        cmd_key,
        SALT_REQ_LEN_KEY.encode(),
        auth_id,
        connection_nonce,
    )
    length_nonce = _kdf(
        cmd_key,
        SALT_REQ_LEN_NONCE.encode(),
        auth_id,
        connection_nonce,
    )[:12]

    try:
        dec_len = _decrypt_gcm(length_key, length_nonce, encrypted_len, auth_id)
        if len(dec_len) != 2:
            return None, "طول هدر VMess نامعتبر است"
        header_len = struct.unpack(">H", dec_len)[0]
    except Exception as exc:
        return None, f"خطا در رمزگشایی طول هدر: {exc}"

    if header_len < 41 or header_len > MAX_HEADER_SIZE:
        return None, f"طول هدر خارج از محدوده است: {header_len}"

    total_header_end = 42 + header_len + 16
    if len(data) < total_header_end:
        return None, "بدنه‌ی هدر VMess ناقص است"

    payload_ct = data[42:total_header_end]
    payload_key = _kdf16(
        cmd_key,
        SALT_REQ_PAY_KEY.encode(),
        auth_id,
        connection_nonce,
    )
    payload_nonce = _kdf(
        cmd_key,
        SALT_REQ_PAY_NONCE.encode(),
        auth_id,
        connection_nonce,
    )[:12]

    try:
        payload = _decrypt_gcm(payload_key, payload_nonce, payload_ct, auth_id)
    except Exception as exc:
        return None, f"خطا در رمزگشایی بدنه‌ی هدر: {exc}"

    if len(payload) < 45:
        return None, "ساختار هدر VMess کوتاه است"

    # Fixed portion from Xray's EncodeRequestHeader:
    # version(1) | IV(16) | key(16) | responseHeader(1) | option(1) |
    # security(1) | reserved(1) | command(1) | address...
    ver = payload[0]
    req_iv = payload[1:17]
    req_key = payload[17:33]
    res_header = payload[33]
    option = payload[34]
    security = payload[35] & 0x0F
    reserved = payload[36]
    cmd = payload[37]

    port = struct.unpack(">H", payload[38:40])[0]
    addr_type = payload[40]
    try:
        host, idx = _parse_address(payload, 41, addr_type)
    except ValueError as exc:
        return None, str(exc)

    # Security field high nibble is the global-padding length.
    padding_len = (payload[35] >> 4) & 0x0F

    # The VMess request header ends with padding + FNV1a32 checksum.
    # Verify checksum whenever the payload has the expected trailer.
    if len(payload) < idx + padding_len + 4:
        return None, "هدر VMess برای padding/checksum ناقص است"

    checksum_offset = len(payload) - 4
    checksum = struct.unpack(">I", payload[checksum_offset:])[0]
    body_for_hash = payload[:checksum_offset]

    # FNV-1a 32, matching the Xray request encoder.
    fnv = 2166136261
    for b in body_for_hash:
        fnv ^= b
        fnv = (fnv * 16777619) & 0xFFFFFFFF
    if fnv != checksum:
        return None, "FNV1a header checksum mismatch"

    # Mux is not routed as a normal host/port target in this relay.
    if cmd != 1:  # TCP
        return None, f"فرمان VMess پشتیبانی نمی‌شود: {cmd}"

    return {
        "u_bytes": u_bytes,
        "cmd_key": cmd_key,
        "auth_id": auth_id,
        "connection_nonce": connection_nonce,
        "ver": ver,
        "req_iv": req_iv,
        "req_key": req_key,
        "res_header": res_header,
        "option": option,
        "sec_type": security,
        "reserved": reserved,
        "cmd": cmd,
        "host": host,
        "port": port,
        "padding_len": padding_len,
        "header_payload": payload,
        "header_end": total_header_end,
        "body_init": data[total_header_end:],
    }, None


# ══════════════════════════════════════════════════════════════════════════════
# Response header
# ══════════════════════════════════════════════════════════════════════════════

def _build_response_header(info: dict) -> bytes:
    """Build Xray-compatible AEAD response header."""
    req_key = info["req_key"]
    req_iv = info["req_iv"]

    # Xray derives response body key/IV from request body key/IV via SHA-256.
    resp_key = hashlib.sha256(req_key).digest()[:16]
    resp_iv = hashlib.sha256(req_iv).digest()[:16]

    info["resp_body_key"] = resp_key
    info["resp_body_iv"] = resp_iv

    # Response header starts with 4 bytes in the decrypted plaintext:
    # response-header-id, option, command, command-data-length.
    plaintext = bytes([
        info["res_header"],
        0x00,
        0x00,
        0x00,
    ])

    length_key = _kdf16(resp_key, SALT_RESP_LEN_KEY.encode())
    length_nonce = _kdf(resp_iv, SALT_RESP_LEN_IV.encode())[:12]
    enc_len = AESGCM(length_key).encrypt(
        length_nonce,
        struct.pack(">H", len(plaintext)),
        None,
    )

    payload_key = _kdf16(resp_key, SALT_RESP_PAY_KEY.encode())
    payload_nonce = _kdf(resp_iv, SALT_RESP_PAY_IV.encode())[:12]
    enc_payload = AESGCM(payload_key).encrypt(
        payload_nonce,
        plaintext,
        None,
    )

    return enc_len + enc_payload


# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# VMess body framing / AEAD
# ══════════════════════════════════════════════════════════════════════════════

class _ShakeReader:
    """SHAKE-128 reader matching Xray's streaming size-mask generator."""

    __slots__ = ("_shake", "_offset")

    def __init__(self, nonce: bytes):
        self._shake = hashlib.shake_128(nonce)
        self._offset = 0

    def read(self, n: int) -> bytes:
        if n <= 0:
            return b""
        end = self._offset + n
        digest = self._shake.digest(end)
        out = digest[self._offset:end]
        self._offset = end
        return out

    def read_u16(self) -> int:
        return struct.unpack(">H", self.read(2))[0]

    def snapshot(self) -> int:
        return self._offset

    def restore(self, offset: int) -> None:
        self._offset = offset


class _VMessBodyFramer:
    """
    Xray-compatible VMess body framing:
      - chunk-stream framing
      - SHAKE-128 chunk masking
      - global padding (0..63 bytes)
      - authenticated length
      - AES-128-GCM / ChaCha20-Poly1305
      - NONE/ZERO raw or chunked bodies
    """

    __slots__ = (
        "security", "key", "iv", "option", "chunk_stream",
        "chunk_masking", "global_padding", "authenticated_length",
        "shake", "payload_aead", "length_aead", "length_key", "length_iv",
        "payload_counter", "length_counter", "buffer", "max_chunk",
    )

    def __init__(self, security: int, key: bytes, iv: bytes, option: int,
                 *, max_chunk: int = 16 * 1024,
                 length_key: bytes | None = None,
                 length_iv: bytes | None = None):
        self.security = security
        self.key = key
        self.iv = iv[:16]
        self.option = option
        self.chunk_stream = bool(option & OPT_CHUNK_STREAM)
        self.chunk_masking = bool(option & OPT_CHUNK_MASKING)
        self.global_padding = bool(option & OPT_GLOBAL_PADDING)
        self.authenticated_length = bool(option & OPT_AUTHENTICATED_LENGTH)
        self.shake = _ShakeReader(self.iv) if (
            self.chunk_masking or self.global_padding
        ) else None
        self.payload_aead = None
        self.length_aead = None
        # Xray uses requestBodyKey/requestBodyIV for authenticated chunk
        # length in BOTH directions, while payload AEAD uses the directional
        # body key/IV.
        self.length_key = length_key if length_key is not None else key
        self.length_iv = (length_iv if length_iv is not None else iv)[:16]
        self.payload_counter = 0
        self.length_counter = 0
        self.buffer = bytearray()
        self.max_chunk = max(1024, min(int(max_chunk), 32768))

        if self.global_padding and not self.chunk_masking:
            raise ValueError("VMess global padding requires chunk masking")

        if security == SEC_AES_GCM:
            self.payload_aead = AESGCM(key)
        elif security == SEC_CHACHA20_POLY1305:
            self.payload_aead = ChaCha20Poly1305(_chacha_key(key))
        elif security not in (SEC_NONE, SEC_ZERO):
            raise ValueError(f"unsupported VMess security: {security}")

        if self.authenticated_length:
            if security == SEC_AES_GCM:
                self.length_aead = AESGCM(_kdf16(self.length_key, b"auth_len"))
            elif security == SEC_CHACHA20_POLY1305:
                self.length_aead = ChaCha20Poly1305(
                    _chacha_key(_kdf16(self.length_key, b"auth_len"))
                )
            else:
                raise ValueError("authenticated length requires AEAD security")

    @property
    def overhead(self) -> int:
        return 16 if self.security in (SEC_AES_GCM, SEC_CHACHA20_POLY1305) else 0

    def _nonce(self, counter: int) -> bytes:
        nonce = bytearray(self.iv[:12])
        struct.pack_into(">H", nonce, 0, counter & 0xFFFF)
        return bytes(nonce)

    def _length_nonce(self, counter: int) -> bytes:
        nonce = bytearray(self.length_iv[:12])
        struct.pack_into(">H", nonce, 0, counter & 0xFFFF)
        return bytes(nonce)

    def _next_padding_len(self) -> int:
        if not self.global_padding:
            return 0
        return self.shake.read_u16() % 64

    def _next_size_mask(self) -> int:
        return self.shake.read_u16() if self.chunk_masking else 0

    def _seal_payload(self, plain: bytes) -> bytes:
        if self.security in (SEC_NONE, SEC_ZERO):
            return plain
        try:
            encrypted = self.payload_aead.encrypt(
                self._nonce(self.payload_counter), plain, None
            )
        except Exception as exc:
            raise ValueError(f"VMess body encryption failed: {exc}") from exc
        self.payload_counter = (self.payload_counter + 1) & 0xFFFF
        return encrypted

    def _open_payload(self, encrypted: bytes) -> bytes:
        if self.security in (SEC_NONE, SEC_ZERO):
            return encrypted
        try:
            plain = self.payload_aead.decrypt(
                self._nonce(self.payload_counter), encrypted, None
            )
        except Exception as exc:
            raise ValueError(f"VMess body decryption failed: {exc}") from exc
        self.payload_counter = (self.payload_counter + 1) & 0xFFFF
        return plain

    def _encode_size(self, payload_and_padding: int) -> bytes:
        if payload_and_padding < self.overhead:
            raise ValueError("invalid VMess encoded chunk size")

        if self.authenticated_length:
            plain = struct.pack(
                ">H", (payload_and_padding - self.overhead) & 0xFFFF
            )
            encrypted = self.length_aead.encrypt(
                self._length_nonce(self.length_counter), plain, None
            )
            self.length_counter = (self.length_counter + 1) & 0xFFFF
            return encrypted

        value = payload_and_padding
        if self.chunk_masking:
            value ^= self._next_size_mask()
        return struct.pack(">H", value)

    def _decode_size(self, encoded: bytes) -> int:
        if self.authenticated_length:
            if len(encoded) != 18:
                raise ValueError("invalid authenticated VMess size field")
            try:
                plain = self.length_aead.decrypt(
                    self._length_nonce(self.length_counter), encoded, None
                )
            except Exception as exc:
                raise ValueError(
                    f"VMess authenticated length decrypt failed: {exc}"
                ) from exc
            self.length_counter = (self.length_counter + 1) & 0xFFFF
            if len(plain) != 2:
                raise ValueError("invalid authenticated VMess length")
            return struct.unpack(">H", plain)[0] + self.overhead

        if len(encoded) != 2:
            raise ValueError("invalid VMess size field")
        value = struct.unpack(">H", encoded)[0]
        if self.chunk_masking:
            value ^= self._next_size_mask()
        return value

    def encode(self, data: bytes) -> list[bytes]:
        if not data:
            return []
        if not self.chunk_stream:
            return [self._seal_payload(data)]

        result = []
        pos = 0
        while pos < len(data):
            part = data[pos:pos + self.max_chunk]
            pos += len(part)
            padding_len = self._next_padding_len()
            encrypted = self._seal_payload(part)
            total_len = len(encrypted) + padding_len
            if total_len > 0xFFFF:
                raise ValueError("VMess chunk exceeds uint16 length")
            size = self._encode_size(total_len)
            padding = secrets.token_bytes(padding_len) if padding_len else b""
            result.append(size + encrypted + padding)
        return result

    def feed(self, data: bytes) -> list[bytes]:
        if not data:
            return []
        if not self.chunk_stream:
            return [self._open_payload(data)]

        self.buffer.extend(data)
        result = []
        size_len = 18 if self.authenticated_length else 2

        while True:
            if len(self.buffer) < size_len:
                break

            shake_offset = self.shake.snapshot() if self.shake else 0
            payload_counter = self.payload_counter
            length_counter = self.length_counter

            padding_len = self._next_padding_len()
            encoded_size = bytes(self.buffer[:size_len])
            size = self._decode_size(encoded_size)

            if size < self.overhead + padding_len:
                raise ValueError("VMess chunk size smaller than padding/overhead")

            total = size_len + size
            if len(self.buffer) < total:
                if self.shake:
                    self.shake.restore(shake_offset)
                self.payload_counter = payload_counter
                self.length_counter = length_counter
                break

            del self.buffer[:size_len]
            framed = bytes(self.buffer[:size])
            del self.buffer[:size]

            encrypted = framed[:-padding_len] if padding_len else framed
            if len(encrypted) == self.overhead:
                continue

            plain = self._open_payload(encrypted)
            if plain:
                result.append(plain)

        return result

    def finish(self) -> None:
        if self.chunk_stream and self.buffer:
            raise ValueError("incomplete VMess body chunk")


class _BodyDecoder:
    __slots__ = ("framer",)
    def __init__(self, framer: _VMessBodyFramer):
        self.framer = framer
    def feed(self, data: bytes) -> list[bytes]:
        return self.framer.feed(data)
    def finish(self) -> None:
        self.framer.finish()


class _BodyEncoder:
    __slots__ = ("framer",)
    def __init__(self, framer: _VMessBodyFramer):
        self.framer = framer
    def encode(self, data: bytes) -> list[bytes]:
        return self.framer.encode(data)


def _chacha_key(key16: bytes) -> bytes:
    first = hashlib.md5(key16).digest()
    second = hashlib.md5(first).digest()
    return first + second


# Socket tuning
# ══════════════════════════════════════════════════════════════════════════════

def _tune_socket(writer: asyncio.StreamWriter):
    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except OSError:
        pass


# ══════════════════════════════════════════════════════════════════════════════
# Data transfer: WebSocket → TCP
# ══════════════════════════════════════════════════════════════════════════════

async def _vmess_ws_to_tcp(
    ws: WebSocket,
    writer: asyncio.StreamWriter,
    conn_id: str,
    uid: str,
    decoder: _BodyDecoder,
):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break

            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue

            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break

            await throttle(uid, len(data))
            main.stats["total_requests"] += 1
            if conn_id in main.connections:
                main.connections[conn_id]["bytes"] += len(data)

            for plaintext in decoder.feed(data):
                writer.write(plaintext)
                if writer.transport.get_write_buffer_size() > RELAY_BUF:
                    await writer.drain()

    except WebSocketDisconnect:
        pass
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        logger.warning(f"⚠️ VMess uplink error [{conn_id}]: {exc}")
    finally:
        try:
            decoder.finish()
        except Exception:
            pass
        try:
            if writer.can_write_eof():
                writer.write_eof()
        except Exception:
            pass


# ══════════════════════════════════════════════════════════════════════════════
# Data transfer: TCP → WebSocket
# ══════════════════════════════════════════════════════════════════════════════

async def _vmess_tcp_to_ws(
    ws: WebSocket,
    reader: asyncio.StreamReader,
    conn_id: str,
    uid: str,
    encoder: _BodyEncoder,
):
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break

            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break

            await throttle(uid, len(data))
            if conn_id in main.connections:
                main.connections[conn_id]["bytes"] += len(data)

            for chunk in encoder.encode(data):
                await ws.send_bytes(chunk)

    except asyncio.CancelledError:
        raise
    except Exception as exc:
        logger.warning(f"⚠️ VMess downlink error [{conn_id}]: {exc}")


# ══════════════════════════════════════════════════════════════════════════════
# Main VMess tunnel
# ══════════════════════════════════════════════════════════════════════════════

async def websocket_tunnel_vmess(websocket: WebSocket, uuid: str):
    await websocket.accept()
    conn_id = f"vmess-{id(websocket)}"
    ip = main.client_ip(websocket)

    async with main.LINKS_LOCK:
        real_uid, link = main.find_link_by_key(uuid)

    if not link or not main.is_link_allowed(link):
        logger.warning(f"🚫 VMess rejected uuid={uuid[:8]}… (not allowed)")
        await websocket.close(code=4000, reason="لینک غیرفعال یا منقضی شده است")
        return

    if not main.is_ip_allowed(link, real_uid, ip):
        logger.warning(f"🚫 VMess rejected uuid={uuid[:8]}… ip={ip} (ip limit)")
        await websocket.close(code=4001, reason="محدودیت تعداد آی‌پِی هم‌زمان")
        return

    main.connections[conn_id] = {
        "uuid": real_uid,
        "ip": ip,
        "bytes": 0,
        "connected_at": main.now_ir().isoformat(),
        "transport": "vmess-ws",
    }
    logger.info(
        f"✅ VMess [{conn_id}] uuid={real_uid[:8]}… ip={ip} "
        f"total={len(main.connections)}"
    )

    target_writer: Optional[asyncio.StreamWriter] = None
    tasks: set[asyncio.Task] = set()

    try:
        # ── Frame 1: must contain the complete AEAD VMess header ──
        try:
            first_frame = await asyncio.wait_for(
                websocket.receive_bytes(),
                timeout=FIRST_FRAME_TIMEOUT,
            )
        except asyncio.TimeoutError:
            logger.warning(f"⏱️ VMess first-frame timeout [{ip}]")
            return

        if not first_frame:
            return

        header_info, err = _decode_request_header(first_frame, real_uid)
        if err or not header_info:
            logger.warning(f"⚠️ VMess header parse error [{ip}]: {err}")
            await websocket.close(code=4002, reason="خطا در خواندن هدر VMess")
            return

        if not await _check_replay(header_info["auth_id"]):
            logger.warning(f"🚫 VMess replayed AuthID [{ip}]")
            await websocket.close(code=4002, reason="AuthID تکراری است")
            return

        sec_type = header_info["sec_type"]
        if sec_type not in (SEC_AES_GCM, SEC_CHACHA20_POLY1305, SEC_NONE, SEC_ZERO):
            logger.warning(f"⚠️ VMess unsupported security [{ip}]: {sec_type}")
            await websocket.close(code=4002, reason="نوع رمز VMess پشتیبانی نمی‌شود")
            return

        # ── Quota: original websocket frame bytes ──
        if not await check_and_use(real_uid, len(first_frame)):
            await websocket.close(code=1008, reason="quota/disabled/unknown")
            return
        main.stats["total_requests"] += 1
        if conn_id in main.connections:
            main.connections[conn_id]["bytes"] += len(first_frame)

        host = header_info["host"]
        port = header_info["port"]

        # ── Connect to target ──
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=TCP_CONNECT_TIMEOUT,
            )
            target_writer = writer
            _tune_socket(writer)
        except Exception as exc:
            logger.error(f"VMess connect failed {host}:{port} -> {exc}")
            await websocket.close(code=4003, reason="امکان اتصال به مقصد نیست")
            return

        logger.info(
            f"➡️ VMess [{conn_id}] → {host}:{port} "
            f"sec_type={sec_type}"
        )

        # ── Body framing / codecs ──
        request_framer = _VMessBodyFramer(
            sec_type,
            header_info["req_key"],
            header_info["req_iv"],
            header_info["option"],
        )
        response_key = hashlib.sha256(header_info["req_key"]).digest()[:16]
        response_iv = hashlib.sha256(header_info["req_iv"]).digest()[:16]
        response_framer = _VMessBodyFramer(
            sec_type,
            response_key,
            response_iv,
            header_info["option"],
            length_key=header_info["req_key"],
            length_iv=header_info["req_iv"],
        )

        request_decoder = _BodyDecoder(request_framer)
        response_encoder = _BodyEncoder(response_framer)

        # ── Send any body records carried after the request header ──
        body_init = header_info["body_init"]
        if body_init:
            for plaintext in request_decoder.feed(body_init):
                writer.write(plaintext)
            await writer.drain()

        # ── Send AEAD-encrypted response header ──
        resp_header = _build_response_header(header_info)
        await websocket.send_bytes(resp_header)

        # ── Bidirectional relay ──
        tasks = {
            asyncio.create_task(
                _vmess_ws_to_tcp(
                    websocket,
                    writer,
                    conn_id,
                    real_uid,
                    request_decoder,
                )
            ),
            asyncio.create_task(
                _vmess_tcp_to_ws(
                    websocket,
                    reader,
                    conn_id,
                    real_uid,
                    response_encoder,
                )
            ),
        }

        done, pending = await asyncio.wait(
            tasks,
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in done:
            try:
                task.result()
            except asyncio.CancelledError:
                pass
            except Exception as exc:
                logger.warning(f"⚠️ VMess relay task failed [{conn_id}]: {exc}")

        for task in pending:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            except Exception:
                pass

        asyncio.create_task(main.save_state())

    except WebSocketDisconnect:
        pass
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        main.stats["total_errors"] += 1
        main.error_logs.append({
            "error": str(exc),
            "type": "vmess_ws_tunnel",
            "time": main.now_ir().isoformat(),
        })
        logger.error(f"VMess tunnel error [{conn_id}]: {exc}")
    finally:
        for task in tasks:
            if not task.done():
                task.cancel()

        main.connections.pop(conn_id, None)

        if target_writer:
            try:
                target_writer.close()
                await target_writer.wait_closed()
            except Exception:
                pass

        try:
            await websocket.close()
        except Exception:
            pass

        logger.info(
            f"🔌 VMess closed [{conn_id}] total={len(main.connections)}"
        )
