# ══════════════════════════════════════════════════════════════════════════
# OMID-IRAN PANEL v2.0.0 — Production Dockerfile
# ══════════════════════════════════════════════════════════════════════════
#   • Base: python:3.11-slim (سبک، امن، با پشتیبانی طولانی)
#   • Non-root user برای امنیت
#   • Volume mount point روی /data برای persist state
#   • Healthcheck روی /health
#   • Multi-arch ready (amd64 + arm64)
# ══════════════════════════════════════════════════════════════════════════

FROM python:3.11-slim

# ── System dependencies ───────────────────────────────────────────────────
# ca-certificates → برای TLS (httpx به HTTPS وصل می‌شه)
# tzdata          → برای ZoneInfo("Asia/Tehran")
# curl            → اختیاری، برای healthcheck/diagnostics
# بدون gcc/pybuild-essential چون همه‌ی پکیج‌ها wheel آماده دارن
RUN apt-get update && apt-get install -y --no-install-recommends \
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

# ── Python dependencies (cache layer) ─────────────────────────────────────
# این لایه کش می‌شه مادامی که requirements.txt تغییر نکنه
COPY requirements.txt ./

RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

# ── Application code ──────────────────────────────────────────────────────
COPY . .

# ── Non-root user (امنیت) ─────────────────────────────────────────────────
RUN groupadd --system --gid 1000 omid \
 && useradd  --system --uid 1000 --gid omid --create-home omid \
 && mkdir -p /data \
 && chown -R omid:omid /app /data

USER omid

# ── Volume (state persistence) ────────────────────────────────────────────
# روی سرور باید mount بشه:  -v /host/path:/data
VOLUME ["/data"]

# ── Port ──────────────────────────────────────────────────────────────────
EXPOSE 8000

# ── Healthcheck ───────────────────────────────────────────────────────────
# از پایتون استفاده می‌کنیم چون curl توی slim image پیش‌فرض نیست
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request, sys; \
        sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3).status == 200 else 1)"

# ── Start command ─────────────────────────────────────────────────────────
CMD ["python", "main.py"]