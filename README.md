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

#### 🚂 روش ۱: Railway (توصیه می‌شه — رایگان و بدون سرور)

**Railway** یه پلتفرم ابری هست که پنل رو با یه کلیک deploy می‌کنه. نیازی به سرور، Docker، یا تنظیمات پیچیده نداری.

**✅ مزایا:**
- 🆓 پلن رایگان ($5 credit ماهانه)
- ⚡ Deploy خودکار از GitHub
- 🔄 Redeploy خودکار با هر push
- 🌐 دامنه‌ی HTTPS خودکار
- 💾 Volume برای ذخیره‌ی داده‌ها

---

##### 🎯 گام ۱: Fork کردن ریپو

برو به [github.com/omidiran-gaming/omidiran](https://github.com/omidiran-gaming/omidiran) و روی دکمه‌ی **Fork** (بالا-راست) کلیک کن.

##### 🎯 گام ۲: ساخت حساب Railway

برو به [railway.app](https://railway.app) و با حساب **GitHub** وارد شو.

##### 🎯 گام ۳: ساخت پروژه‌ی جدید

۱. روی **New Project** کلیک کن
۲. گزینه‌ی **Deploy from GitHub repo** رو انتخاب کن
۳. اگه اولین باره، به Railway اجازه بده به GitHub دسترسی داشته باشه
۴. ریپوی fork شده (`omidiran`) رو انتخاب کن
۵. روی **Deploy Now** کلیک کن

> 🎉 صبر کن تا build تموم بشه (حدود ۲-۴ دقیقه). Railway خودکار Dockerfile رو پیدا و اجرا می‌کنه.

##### 🎯 گام ۴: تنظیم متغیرهای محیطی (خیلی مهم!)

برو به **Settings → Variables** و این‌ها رو اضافه کن:

| Variable | Value | توضیح |
|----------|-------|-------|
| `ADMIN_USERNAME` | `omid` (یا هرچی می‌خوای) | نام کاربری پنل |
| `ADMIN_PASSWORD` | `رمز-قوی-خودت` | رمز عبور پنل |
| `SECRET_KEY` | یه رشته‌ی تصادفی طولانی | کلید Session |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | لینک پشتیبانی (اختیاری) |
| `TELEGRAM_BOT_TOKEN` | (خالی بذار یا توکن) | ربات تلگرام (اختیاری) |
| `TELEGRAM_ADMIN_IDS` | (خالی بذار یا IDها) | Admin IDها (اختیاری) |

برای ساخت `SECRET_KEY` تصادفی:

```bash
# Linux/macOS
openssl rand -hex 32

# Windows PowerShell
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 64 | % {[char]$_})
```

> ⚠️ **مهم:** Railway خودکار `PORT` رو ست می‌کنه — نیازی نیست خودت اضافه کنی.

##### 🎯 گام ۵: اضافه کردن Volume (برای ذخیره‌ی داده‌ها)

بدون Volume، با هر redeploy همه‌ی کانفیگ‌ها از دست می‌رن.

۱. توی پروژه‌ی Railway، روی سرویس کلیک کن
۲. برو به تب **Volumes** → **Add Volume**
۳. تنظیم کن:
   - **Mount Path:** `/data`
   - **Size:** `1 GB` (رایگان)
۴. روی **Add** کلیک کن

حالا Railway خودکار redeploy می‌کنه و داده‌ها موندگار می‌شن.

##### 🎯 گام ۶: دریافت دامنه

۱. برو به تب **Settings** → **Networking**
۲. روی **Generate Domain** کلیک کن
۳. یه دامنه‌ی HTTPS می‌گیری مثل:
   ```
   https://omidiran-production.up.railway.app
   ```
۴. همون‌جا می‌تونی **Custom Domain** هم اضافه کنی (اگه دامنه داری)

##### 🎯 گام ۷: ورود به پنل

۱. دامنه‌ی HTTPS رو توی مرورگر باز کن
۲. با `ADMIN_USERNAME` و `ADMIN_PASSWORD` که ست کردی وارد شو
۳. **همین! 🎉** پنل آماده‌ست

---

##### 🔧 تنظیمات پیشرفته

**اگه می‌خوای redeploy خودکار بشه با هر push به main:**

به‌صورت پیش‌فرض فعاله. هر `git push` به branch `main` → Railway خودکار redeploy می‌کنه.

**اگه می‌خوای از image آماده‌ی GHCR استفاده کنی (بدون build):**

۱. توی Railway → **New Project** → **Empty Project**
۲. روی **+ Create** → **Docker Image** کلیک کن
۳. توی فیلد image بنویس:
   ```
   ghcr.io/omidiran-gaming/omidiran:latest
   ```
۴. باقی مراحل مشابه بالاست

> 💡 **مزیت:** build سریع‌تر، حجم کمتر، بدون نیاز به Dockerfile

**تنظیم resources:**

توی **Settings → Resources** می‌تونی:
- حافظه رو افزایش بدی (اگه کم آوردی)
- تعداد replicaها رو مشخص کنی
- منطقه‌ی جغرافیایی رو تغییر بدی

---

##### 🐛 عیب‌یابی

| مشکل | راه‌حل |
|------|--------|
| Build fail | لاگ‌ها رو توی تب **Deployments** چک کن |
| پنل باز نمی‌شه | مطمئن شو دامنه توی **Networking** ساخته شده |
| داده‌ها بعد از redeploy می‌پرن | Volume رو توی `/data` ست کن |
| خطای `502 Bad Gateway` | چند دقیقه صبر کن — هنوز در حال اجراست |
| `SECRET_KEY` بعد از restart تغییر می‌کنه | `SECRET_KEY` رو دستی توی Variables ست کن |

---

#### 🐳 روش ۲: Docker (توصیه می‌شه برای VPS)

```bash
docker run -d \
  --name omidiran-panel \
  -p 8000:8000 \
  -v omidiran-data:/data \
  -e ADMIN_USERNAME=omid \
  -e ADMIN_PASSWORD=changeme \
  ghcr.io/omidiran-gaming/omidiran:latest
```

#### 🐳 روش ۳: Docker Compose

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

#### 🐍 روش ۴: اجرای مستقیم (Python)

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
| `PORT` | `8000` | پورت سرور (Railway خودکار روی `8080` ست می‌کنه) |
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
├── railway.json
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

#### 🚂 Method 1: Railway (Recommended — Free, No Server Needed)

**Railway** is a cloud platform that deploys the panel in one click. No server, Docker, or complex setup required.

**✅ Benefits:**
- 🆓 Free plan ($5 monthly credit)
- ⚡ Auto-deploy from GitHub
- 🔄 Auto-redeploy on every push
- 🌐 Automatic HTTPS domain
- 💾 Volume for persistent data

---

##### 🎯 Step 1: Fork the repo

Go to [github.com/omidiran-gaming/omidiran](https://github.com/omidiran-gaming/omidiran) and click the **Fork** button (top-right).

##### 🎯 Step 2: Create Railway account

Go to [railway.app](https://railway.app) and sign in with **GitHub**.

##### 🎯 Step 3: Create new project

1. Click **New Project**
2. Choose **Deploy from GitHub repo**
3. Authorize Railway to access GitHub (first time only)
4. Select your forked repo (`omidiran`)
5. Click **Deploy Now**

> 🎉 Wait ~2-4 minutes for the build. Railway auto-detects and uses the Dockerfile.

##### 🎯 Step 4: Set environment variables (VERY IMPORTANT!)

Go to **Settings → Variables** and add:

| Variable | Value | Notes |
|----------|-------|-------|
| `ADMIN_USERNAME` | `omid` (or your choice) | Panel username |
| `ADMIN_PASSWORD` | `your-strong-password` | Panel password |
| `SECRET_KEY` | A long random string | Session key |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | Support link (optional) |
| `TELEGRAM_BOT_TOKEN` | (empty or token) | Telegram bot (optional) |
| `TELEGRAM_ADMIN_IDS` | (empty or IDs) | Admin IDs (optional) |

Generate a random `SECRET_KEY`:

```bash
# Linux/macOS
openssl rand -hex 32

# Windows PowerShell
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 64 | % {[char]$_})
```

> ⚠️ Railway auto-sets `PORT` — no need to add it.

##### 🎯 Step 5: Add a Volume (for persistent data)

Without a volume, all configs are lost on every redeploy.

1. In your Railway project, click the service
2. Go to **Volumes** tab → **Add Volume**
3. Configure:
   - **Mount Path:** `/data`
   - **Size:** `1 GB` (free)
4. Click **Add**

Railway will auto-redeploy, and data will persist.

##### 🎯 Step 6: Get a domain

1. Go to **Settings** → **Networking**
2. Click **Generate Domain**
3. You'll get an HTTPS domain like:
   ```
   https://omidiran-production.up.railway.app
   ```
4. You can add a **Custom Domain** here too (if you have one)

##### 🎯 Step 7: Log in

1. Open your HTTPS domain in a browser
2. Log in with `ADMIN_USERNAME` and `ADMIN_PASSWORD`
3. **Done! 🎉** Panel is ready.

---

##### 🔧 Advanced

**Auto-redeploy on push:**

Enabled by default. Any `git push` to `main` → Railway auto-redeploys.

**Using pre-built GHCR image (no build):**

1. Railway → **New Project** → **Empty Project**
2. Click **+ Create** → **Docker Image**
3. Enter image:
   ```
   ghcr.io/omidiran-gaming/omidiran:latest
   ```
4. Rest of steps are identical

> 💡 **Benefit:** Faster builds, smaller size, no Dockerfile needed

---

##### 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails | Check logs in **Deployments** tab |
| Panel not loading | Make sure domain is generated in **Networking** |
| Data lost after redeploy | Set Volume mount path to `/data` |
| `502 Bad Gateway` | Wait a minute — still starting |
| `SECRET_KEY` changes on restart | Set `SECRET_KEY` manually in Variables |

---

#### 🐳 Method 2: Docker (Recommended for VPS)

```bash
docker run -d \
  --name omidiran-panel \
  -p 8000:8000 \
  -v omidiran-data:/data \
  -e ADMIN_USERNAME=omid \
  -e ADMIN_PASSWORD=changeme \
  ghcr.io/omidiran-gaming/omidiran:latest
```

Open `http://localhost:8000` in your browser.

#### 🐳 Method 3: Docker Compose

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

```bash
docker compose up -d
```

#### 🐍 Method 4: Python (dev)

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
| `PORT` | `8000` | Server port (Railway auto-sets to `8080`) |
| `ADMIN_USERNAME` | `omid` | Panel username |
| `ADMIN_PASSWORD` | `omid` | Panel password |
| `SECRET_KEY` | auto | Session key (auto-persisted) |
| `DATA_DIR` | `/data` | State storage directory |
| `RAILWAY_PUBLIC_DOMAIN` | `localhost` | Public domain |
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
