# ══════════════════════════════════════════════════════════════════════════
# OMID-IRAN PANEL v2.0.0 — Production Dockerfile
# ══════════════════════════════════════════════════════════════════════════
# • Base: Python 3.11 Slim
# • Railway Volume compatible
# • Persistent data directory: /data
# • No VOLUME declaration
# • No non-root USER
# • Healthcheck on /health
# • Multi-arch compatible
# ══════════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# ── System dependencies ───────────────────────────────────────────────────
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# ── Environment ───────────────────────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    TZ=Asia/Tehran \
    DATA_DIR=/data \
    PORT=8000

# ── Working directory ─────────────────────────────────────────────────────
WORKDIR /app

# ── Python dependencies ───────────────────────────────────────────────────
# Copy requirements separately to maximize Docker layer caching.
COPY requirements.txt ./

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# ── Application code ──────────────────────────────────────────────────────
COPY . .

# ── Persistent data directory ─────────────────────────────────────────────
# Railway Volume will be mounted here at runtime.
RUN mkdir -p /data \
    && chmod 755 /data

# ── Port ──────────────────────────────────────────────────────────────────
EXPOSE 8000

# ── Healthcheck ────────────────────────────────────────────────────────────
HEALTHCHECK --interval=30s \
    --timeout=5s \
    --start-period=15s \
    --retries=3 \
    CMD python -c "import urllib.request, sys; \
        response = urllib.request.urlopen( \
            'http://127.0.0.1:8000/health', timeout=3 \
        ); \
        sys.exit(0 if response.status == 200 else 1)"

# ── Start command ──────────────────────────────────────────────────────────
CMD ["python", "main.py"]
