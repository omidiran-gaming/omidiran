<div align="center">

<img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/Docs/logo.png" width="120" alt="OMID-IRAN PANEL">

# 🚀 OMID-IRAN PANEL

**پنل مدیریت کانفیگ VLESS/WS + XHTTP Ultra**
**Modern VLESS/WS + XHTTP Ultra Management Panel**

[![Docker](https://img.shields.io/badge/Docker-ghcr.io-blue?logo=docker)](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@omid__gamingORG-26A5E4?logo=telegram&logoColor=white)](https://t.me/omid_gamingORG)

[🇮🇷 فارسی](#-فارسی) · [🇬🇧 English](#-english) · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Support](https://t.me/omid_gamingORG)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-mobile.png" width="30%" alt="Mobile">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-configs.png" width="30%" alt="Configs">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-stats.png" width="30%" alt="Stats">
</p>

---

<div dir="rtl">

## 🇮🇷 فارسی

### ✨ درباره‌ی پروژه

**OMID-IRAN PANEL** یه پنل مدیریت کانفیگ مدرن، سریع و امن برای پروتکل‌های **VLESS/WebSocket** و **XHTTP Ultra (Siz10a)** هست. طراحی تمیز، رابط دوزبانه، و معماری مبتنی بر FastAPI باعث می‌شه هم برای استفاده‌ی شخصی و هم برای تیم‌های کوچک مناسب باشه.

### 🎯 ویژگی‌های کلیدی

#### 🔐 هسته‌ی اتصال
- **VLESS over WebSocket** — ترابرد پایدار و سازگار با CDN
- **XHTTP Ultra (Siz10a)** — سه مود کامل: `packet-up`, `stream-up`, `stream-one`
- **UUID Auth سخت‌گیرانه** — فقط UUIDهای ثبت‌شده اجازه‌ی اتصال دارند
- **uTLS Fingerprint** — chrome, firefox, safari, ios, android, edge, 360, qq, random, randomized
- **ALPN سفارشی** — قابل تنظیم برای هر کانفیگ (h2, http/1.1, ...)

#### 🎛️ مدیریت کانفیگ
- سهمیه‌ی ترافیک (GB / MB / KB)
- تاریخ انقضا (روز از الان یا نامحدود)
- محدودیت IP (کاربر هم‌زمان)
- محدودیت سرعت (Mbps / KB/s / MB/s)
- **Sub Token سفارشی** — به‌جای UUID طولانی
- گروه‌بندی و Sub Groups
- ریست مصرف · فعال/غیرفعال‌سازی · ویرایش کامل
- QR Code استایل‌دار + لینک VLESS

#### 👥 اشتراک‌گذاری
- **Sub Group** — گروه‌بندی کانفیگ‌ها با URL یکتا
- **Public Page** — صفحه‌ی پابلیک زیبا برای هر گروه
- **رمز عبور اختیاری** برای صفحه‌ی پابلیک
- لینک ساب همه‌کاره (`/sub-all`)
- **Auto-import** به: v2rayNG, NekoBox, Sing-Box, Streisand, Shadowrocket, Clash, Hiddify, FoXray, v2rayN

#### 🎨 رابط کاربری
- **دو تم کامل:**
  - 🌙 **OMID Glass Premium** (Dark) — purple/pink glassmorphism
  - ☀️ **Arctic Premium** (Light) — frosted blue/lavender
- **دوزبانه:** فارسی (RTL) و انگلیسی (LTR) — تغییر لحظه‌ای بدون reload
- **App-like UI** با bottom nav روی موبایل
- **Sidebar داینامیک** — بر اساس زبان
- **Responsive کامل** — موبایل، تبلت، دسکتاپ
- PWA-friendly

#### 🤖 ربات تلگرام (اختیاری)
- مدیریت ربات از داخل پنل
- ساخت/حذف کانفیگ از تلگرام
- مشاهده‌ی آمار و اتصالات
- اعتبارسنجی توکن از BotFather

#### 📊 مانیتورینگ
- نمودار ترافیک ساعتی (Chart.js)
- اتصالات زنده با IP و مدت زمان
- لاگ فعالیت‌ها (Activity Log)
- لاگ خطاها (Error Log)
- WebSocket Test داخلی

#### 🔒 امنیت
- Session Cookie با `HttpOnly` + `SameSite=Lax`
- **SHA-256 + Salt** برای رمز عبور
- **SECRET_KEY پایدار روی دیسک** — بدون reset بعد از restart
- CORS قابل تنظیم
- اعتبارسنجی کامل ورودی‌ها

---

### 📦 نصب سریع

#### 🐳 روش ۱: Docker (توصیه می‌شه)

```bash
docker run -d \
  --name omidiran-panel \
  -p 8000:8000 \
  -v omidiran-data:/data \
  -e ADMIN_USERNAME=omid \
  -e ADMIN_PASSWORD=changeme \
  ghcr.io/omidiran-gaming/omidiran:latest
```

#### 🐳 روش ۲: Docker Compose

```yaml
# docker-compose.yml
version: "3.9"

services:
  omidiran:
    image: ghcr.io/omidiran-gaming/omidiran:latest
    container_name: omidiran-panel
    ports:
      - "8000:8000"
    volumes:
      - ./data:/data
    environment:
      - ADMIN_USERNAME=omid
      - ADMIN_PASSWORD=changeme
      - SECRET_KEY=your-strong-secret-here
      - TELEGRAM_BOT_TOKEN=
      - TELEGRAM_ADMIN_IDS=
      - SUPPORT_URL=https://t.me/omid_gamingORG
    restart: unless-stopped
```

سپس:

```bash
docker compose up -d
```

#### 🐍 روش ۳: اجرای مستقیم (Python)

```bash
# ۱. Clone
git clone https://github.com/omidiran-gaming/omidiran.git
cd omidiran

# ۲. محیط مجازی
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate       # Windows

# ۳. نصب پکیج‌ها
pip install -r requirements.txt

# ۴. اجرا
python main.py
```

پنل روی `http://localhost:8000` در دسترسه.

---

### ⚙️ متغیرهای محیطی

| متغیر | پیش‌فرض | توضیح |
|-------|---------|-------|
| `PORT` | `8000` | پورت سرور |
| `ADMIN_USERNAME` | `omid` | نام کاربری پنل |
| `ADMIN_PASSWORD` | `omid` | رمز عبور پنل |
| `SECRET_KEY` | auto | کلید Session (خودکار ذخیره می‌شه) |
| `DATA_DIR` | `/data` | مسیر ذخیره‌سازی State |
| `RAILWAY_PUBLIC_DOMAIN` | `localhost` | دامنه‌ی عمومی |
| `TELEGRAM_BOT_TOKEN` | — | توکن ربات تلگرام (اختیاری) |
| `TELEGRAM_ADMIN_IDS` | — | Admin IDها (با کاما) |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | لینک پشتیبانی |

> ⚠️ **مهم:** برای production حتماً `ADMIN_PASSWORD` و `SECRET_KEY` رو تغییر بده.

---

### 🌐 آدرس‌های مهم

| مسیر | توضیح |
|------|-------|
| `/` | Login Panel |
| `/dashboard` | پنل ادمین |
| `/sub/{uuid}` | ساب تکی (با Sub Token یا UUID) |
| `/sub-all` | ساب همه‌ی کانفیگ‌های فعال |
| `/sub-group/{key}` | ساب گروه |
| `/p/{key}` | صفحه‌ی پابلیک گروه |
| `/ws/{uuid}` | WebSocket Tunnel (VLESS/WS) |
| `/xhttp-siz10/{mode}/{uuid}` | XHTTP Ultra (3 modes) |
| `/health` | Health Check |
| `/stats` | Stats API |
| `/api/links` | مدیریت کانفیگ‌ها |

---

### 📁 ساختار پروژه

```
omidiran/
├── main.py                # FastAPI app + routes
├── pages.py               # LOGIN_HTML, DASHBOARD_HTML, i18n
├── public_page.py         # Public subscription pages
├── relay_vless.py         # VLESS/WS tunnel
├── xhttp_siz10.py         # XHTTP Ultra transport
├── telegram_bot.py        # Telegram bot integration
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/
    └── workflows/
        └── build-and-push.yml
```

---

### 🛠️ توسعه

```bash
# نصب وابستگی‌های توسعه
pip install -r requirements.txt

# اجرا با auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### ⚠️ نکات production

- حتماً **HTTPS/TLS** جلوی سرور (Nginx/Caddy/Traefik) قرار بده
- از **رمز عبور قوی** برای ادمین استفاده کن
- `SECRET_KEY` رو در env تنظیم کن
- Backup از پوشه‌ی `/data` بگیر
- لاگ‌ها رو مانیتور کن

---

### 💬 پشتیبانی

- 📢 **کانال تلگرام:** [@omid_gamingORG](https://t.me/omid_gamingORG)
- 💬 **پشتیبانی:** [@iran5090](https://t.me/iran5090)
- 🐛 **گزارش باگ:** [GitHub Issues](https://github.com/omidiran-gaming/omidiran/issues)

---

</div>

## 🇬🇧 English

### ✨ About

**OMID-IRAN PANEL** is a modern, fast, and secure management panel for **VLESS/WebSocket** and **XHTTP Ultra (Siz10a)** protocols. Clean design, bilingual UI, and FastAPI-based architecture make it suitable for both personal and small-team use.

### 🎯 Key Features

- 🔐 **VLESS/WebSocket** — stable, CDN-compatible transport
- ⚡ **XHTTP Ultra** — 3 modes: `packet-up`, `stream-up`, `stream-one`
- 🛡️ **Strict UUID Auth** — only registered UUIDs can connect
- 🎭 **uTLS Fingerprint** — chrome, firefox, safari, ios, android, ...
- 🎛️ **Full config management** — quota, expiry, IP/speed limits, sub tokens
- 👥 **Sub Groups + Public Pages** — with optional password
- 🎨 **Dual theme** — Dark (OMID Glass) + Light (Arctic Premium)
- 🌐 **Bilingual** — FA/EN with instant switching
- 🤖 **Telegram Bot** — optional remote management
- 📊 **Monitoring** — live traffic, connections, logs
- 🔒 **Security** — HttpOnly sessions, SHA-256, persistent SECRET_KEY

### 📦 Quick Start

```bash
# Docker (recommended)
docker run -d \
  --name omidiran-panel \
  -p 8000:8000 \
  -v omidiran-data:/data \
  -e ADMIN_USERNAME=omid \
  -e ADMIN_PASSWORD=changeme \
  ghcr.io/omidiran-gaming/omidiran:latest
```

Open `http://localhost:8000` in your browser.

### 🐍 Python (dev)

```bash
git clone https://github.com/omidiran-gaming/omidiran.git
cd omidiran
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8000` | Server port |
| `ADMIN_USERNAME` | `omid` | Panel username |
| `ADMIN_PASSWORD` | `omid` | Panel password |
| `SECRET_KEY` | auto | Session key (auto-persisted) |
| `DATA_DIR` | `/data` | State storage directory |
| `TELEGRAM_BOT_TOKEN` | — | Bot token (optional) |
| `TELEGRAM_ADMIN_IDS` | — | Admin IDs (comma-separated) |
| `SUPPORT_URL` | — | Support link |

### 🌐 Endpoints

| Path | Description |
|------|-------------|
| `/` | Login |
| `/dashboard` | Admin panel |
| `/sub/{uuid}` | Single subscription |
| `/sub-all` | All active configs |
| `/sub-group/{key}` | Group subscription |
| `/p/{key}` | Public group page |
| `/ws/{uuid}` | VLESS/WS tunnel |
| `/xhttp-siz10/{mode}/{uuid}` | XHTTP Ultra |
| `/health` | Health check |

### 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

**Made with ❤️ by OMID Network**

⭐ اگه برات مفید بود، یه ستاره بده! · Star this repo if it helps you!

[🐙 GitHub](https://github.com/omidiran-gaming/omidiran) · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Telegram](https://t.me/omid_gamingORG)

</div>
