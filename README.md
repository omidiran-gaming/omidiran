<div align="center">

<img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/Docs/logo.png" width="120" alt="OMID-IRAN PANEL">

# 🚀 OMID-IRAN PANEL

**پنل مدیریت کانفیگ VLESS / VMess / Trojan + WebSocket / XHTTP Ultra**

[![Railway](https://img.shields.io/badge/Deploy-Railway-7B61FF?logo=railway&logoColor=white)](https://railway.app/)
[![Docker](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=white)](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@omid__gamingORG-26A5E4?logo=telegram&logoColor=white)](https://t.me/omid_gamingORG)

**فقط Railway • دو روش نصب: Fork از GitHub یا Deploy مستقیم Container**

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-mobile.png" width="30%" alt="Mobile">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-configs.png" width="30%" alt="Configs">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-stats.png" width="30%" alt="Stats">
</p>

---

<div dir="rtl">

## 🇮🇷 فارسی

### ✨ معرفی

**OMID-IRAN PANEL** یک پنل مدیریت مدرن برای ساخت، مدیریت و اشتراک‌گذاری کانفیگ‌های **VLESS، VMess و Trojan** است که از **WebSocket** و **XHTTP Ultra (Siz10a)** پشتیبانی می‌کند.

هسته‌ی پروژه با **FastAPI** ساخته شده و بخش‌های پنل مدیریتی، Public Page و ربات تلگرام برای استفاده‌ی فارسی و انگلیسی طراحی شده‌اند. زبان اصلی رابط کاربری **English** است و ترجمه‌ی فارسی از روی همان متن‌های مرجع انجام می‌شود تا جابه‌جایی زبان باعث به‌هم‌ریختگی یا ترجمه‌ی چندباره نشود.

---

## 🔐 پروتکل‌ها و ترنسپورت‌ها

این نسخه از **۹ ترکیب** زیر پشتیبانی می‌کند:

| پروتکل | WebSocket | XHTTP packet-up | XHTTP stream-up |
|---|:---:|:---:|:---:|
| **VLESS** | ✅ | ✅ | ✅ |
| **VMess** | ✅ | ✅ | ✅ |
| **Trojan** | ✅ | ✅ | ✅ |

### VLESS
- WebSocket
- XHTTP `packet-up`
- XHTTP `stream-up`

### VMess
- WebSocket
- XHTTP `packet-up`
- XHTTP `stream-up`
- ساخت لینک VMess با فرمت سازگار با کلاینت‌های رایج و ایمپورترهای XHTTP

### Trojan
- WebSocket
- XHTTP `packet-up`
- XHTTP `stream-up`
- احراز هویت بر پایه‌ی پسورد
- پشتیبانی Relay برای TCP و UDP

### گزینه‌های اتصال
- **uTLS Fingerprint:** `chrome`, `firefox`, `safari`, `ios`, `android`, `edge`, `360`, `qq`, `random`, `randomized`
- **ALPN:** `http/1.1`، `h2` و `h2,http/1.1`
- پورت قابل تنظیم
- احراز هویت با UUID برای کانفیگ‌های مبتنی بر UUID

---

## 🎛️ مدیریت کانفیگ

برای هر کانفیگ می‌توان موارد زیر را تنظیم کرد:

- نام و توضیحات
- پروتکل و ترنسپورت
- سهمیه‌ی ترافیک
- تاریخ انقضا یا بدون انقضا
- محدودیت تعداد IP هم‌زمان
- محدودیت سرعت
- Fingerprint
- ALPN
- پورت
- Sub Token سفارشی
- فعال / غیرفعال کردن
- ریست مصرف
- حذف و ویرایش کامل

همچنین لینک اشتراک مناسب همان پروتکل به‌صورت خودکار ساخته می‌شود.

---

## 👥 Sub Group و اشتراک‌گذاری

- ساخت **Sub Group**
- اضافه کردن چند کانفیگ به یک گروه
- لینک Public Page اختصاصی
- لینک Subscription اختصاصی
- امکان تعیین رمز برای گروه
- Sub Token برای لینک‌های کوتاه‌تر
- خروجی مناسب برای کلاینت‌های مختلف
- تولید QR Code استایل‌دار برای لینک‌ها

کلاینت‌های پشتیبانی‌شده در رابط ایمپورت:

`v2rayNG` · `NekoBox` · `Sing-Box` · `Streisand` · `Shadowrocket` · `Clash` · `Hiddify` · `FoXray` · `v2rayN`

---

## 🎨 رابط کاربری

### پنل مدیریت
- فارسی و انگلیسی
- زبان پایه‌ی English
- تغییر زبان بدون reload
- پشتیبانی کامل از RTL و LTR
- طراحی Responsive برای موبایل، تبلت و دسکتاپ
- Sidebar و Navigation سازگار با زبان
- رابط مدرن و App-like

### تم‌ها
- 🌙 **OMID Glass Premium** برای حالت تاریک
- ☀️ **Arctic Premium** برای حالت روشن

### Public Page
- صفحه‌ی اشتراک مدرن و سبک
- مشاهده‌ی وضعیت و مصرف کانفیگ‌ها
- QR Code
- Import به کلاینت
- تنظیم زبان
- تنظیم تم

---

## 🤖 ربات تلگرام

ربات تلگرام به‌صورت اختیاری قابل فعال‌سازی است و امکانات زیر را ارائه می‌دهد:

- ساخت کانفیگ
- حذف کانفیگ
- ویرایش کانفیگ
- فعال / غیرفعال کردن
- مشاهده‌ی جزئیات
- مشاهده‌ی آمار و اتصالات
- مدیریت Sub Group
- Search و Filter
- Backup و Restore
- Export با فرمت JSON / CSV / TXT
- نمودار مصرف
- Notification
- مدیریت Admin
- QR Code استایل‌دار
- Inline Mode

### 🌐 زبان ربات

ربات به‌صورت کامل دو زبانه است:

- 🇬🇧 English
- 🇮🇷 فارسی

در اولین اجرای `/start`، کاربر زبان را انتخاب می‌کند و انتخاب او ذخیره می‌شود. بعد از آن، گزینه‌ی **🌐 Language** داخل منوی اصلی برای تغییر زبان در هر زمان در دسترس است.

---

## 📊 مانیتورینگ

- ترافیک کل
- مصرف ساعتی
- تعداد کانفیگ‌ها
- کانفیگ‌های فعال و منقضی
- اتصالات زنده
- IPهای متصل
- تعداد Sessionها
- Activity Log
- Error Log
- Uptime
- تست WebSocket

---

## 🔒 امنیت و نگهداری اطلاعات

- Session Cookie با `HttpOnly`
- `SameSite=Lax`
- احراز هویت پنل
- Password Hash بر پایه‌ی SHA-256 و Secret پایدار
- نگهداری Secret در صورت نیاز روی Storage
- محدودیت IP برای هر کانفیگ
- بررسی Active / Expiry / Quota قبل از اجازه‌ی اتصال
- ذخیره‌ی State در `gateway_state.json`

برای استقرار Railway، مسیر `/data` را به‌صورت Volume متصل کنید تا State و Secret بعد از Restart یا Redeploy از بین نروند.

---

# 🚀 نصب روی Railway

برای این پروژه فقط دو روش نصب پیشنهاد می‌شود:

1. **Fork از GitHub و Deploy از Repository**
2. **Deploy مستقیم Container از GitHub Container Registry**

Railway هر دو روش را به‌صورت رسمی پشتیبانی می‌کند؛ در روش Repository، سرویس از GitHub ساخته و با تغییرات Branch مجدداً Deploy می‌شود و در روش Container می‌توان مستقیماً یک Image عمومی از GHCR را Deploy کرد. urlراهنمای رسمی Deploy از GitHub و Docker Image در Railwayhttps://docs.railway.com/quick-start

---

## 1️⃣ نصب با Fork از GitHub

### مرحله ۱ — Fork

ابتدا Repository پروژه را در GitHub باز کنید:

```text
https://github.com/omidiran-gaming/omidiran
```

سپس روی **Fork** بزنید و پروژه را داخل اکانت GitHub خودتان کپی کنید.

### مرحله ۲ — ساخت پروژه در Railway

وارد Railway شوید:

```text
https://railway.com/
```

سپس:

```text
New Project
→ Deploy from GitHub Repo
→ Connect GitHub
→ انتخاب Repository فورک‌شده
```

Railway می‌تواند یک Repository را به‌عنوان Service Source استفاده کند و با Push شدن Commit جدید، Deployment جدید انجام دهد. citeturn521299search1turn521299search2

### مرحله ۳ — Variables

داخل Service بخش **Variables** این مقادیر را تنظیم کنید:

```env
ADMIN_USERNAME=omid
ADMIN_PASSWORD=یک_رمز_قوی
SECRET_KEY=یک_کلید_طولانی_و_تصادفی
DATA_DIR=/data

TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_IDS=

SUPPORT_URL=https://t.me/omid_gamingORG
```

`PORT` را لازم نیست دستی قرار دهید؛ Railway در محیط اجرا پورت سرویس را فراهم می‌کند و برنامه از متغیر `PORT` استفاده می‌کند.

### مرحله ۴ — Volume

برای نگهداری State پروژه، یک **Volume** بسازید و آن را روی این مسیر Mount کنید:

```text
/data
```

مهم‌ترین اطلاعات پایدار پروژه در همین مسیر نگهداری می‌شوند.

### مرحله ۵ — Deploy

بعد از ذخیره‌ی Variables و Volume، Deployment را اجرا کنید.

بعد از موفق شدن Deployment از بخش **Networking** یک Domain بسازید. Railway برای سرویس‌ها امکان Generate Domain از تنظیمات Networking را فراهم می‌کند. citeturn521299search3

---

## 2️⃣ نصب مستقیم Container در Railway

این روش برای وقتی مناسب است که نخواهید Repository را Fork کنید و مستقیماً Image آماده‌ی پروژه را اجرا کنید.

Image پروژه:

```text
ghcr.io/omidiran-gaming/omidiran:latest
```

### مرحله ۱ — ساخت پروژه خالی

در Railway:

```text
New Project
→ Empty Project
```

### مرحله ۲ — ساخت Service

در Project Canvas:

```text
Add a Service
→ Docker Image
```

سپس Image زیر را وارد کنید:

```text
ghcr.io/omidiran-gaming/omidiran:latest
```

Railway از GitHub Container Registry پشتیبانی می‌کند و می‌توان Image را مستقیماً از Dashboard به‌عنوان Service اجرا کرد. citeturn521299search0turn521299search1

### مرحله ۳ — Variables

همان Variables روش اول را قرار دهید:

```env
ADMIN_USERNAME=omid
ADMIN_PASSWORD=یک_رمز_قوی
SECRET_KEY=یک_کلید_طولانی_و_تصادفی
DATA_DIR=/data

TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_IDS=

SUPPORT_URL=https://t.me/omid_gamingORG
```

### مرحله ۴ — Volume

یک Railway Volume بسازید و Mount Path را روی:

```text
/data
```

قرار دهید.

### مرحله ۵ — Deploy و Domain

روی **Deploy** بزنید و بعد از بالا آمدن سرویس:

```text
Settings
→ Networking
→ Generate Domain
```

را انجام دهید. citeturn521299search3

---

## ⚙️ متغیرهای محیطی

| متغیر | مقدار پیشنهادی | توضیح |
|---|---|---|
| `ADMIN_USERNAME` | `omid` | نام کاربری پنل |
| `ADMIN_PASSWORD` | یک مقدار قوی | رمز پنل |
| `SECRET_KEY` | مقدار تصادفی طولانی | Secret مربوط به Session و Hash |
| `DATA_DIR` | `/data` | مسیر State و Secret |
| `TELEGRAM_BOT_TOKEN` | خالی / Token | توکن ربات تلگرام |
| `TELEGRAM_ADMIN_IDS` | خالی / IDها | Admin IDهای ربات |
| `SUPPORT_URL` | لینک پشتیبانی | لینک پشتیبانی |
| `PORT` | توسط Railway | پورت اجرای سرویس |

### 🔐 نکته مهم درباره Secret

`SECRET_KEY` را ثابت و طولانی انتخاب کنید. تغییر آن می‌تواند روی Sessionها و داده‌هایی که به Secret وابسته هستند اثر بگذارد.

---

# 🌐 مسیرهای مهم

| مسیر | کاربرد |
|---|---|
| `/` | صفحه ورود |
| `/dashboard` | پنل مدیریت |
| `/sub/{uuid}` | Subscription یک کانفیگ |
| `/sub-all` | Subscription همه‌ی کانفیگ‌های فعال |
| `/sub-group/{key}` | Subscription گروه |
| `/p/{key}` | Public Page گروه |
| `/ws/{uuid}` | WebSocket Tunnel |
| `/xhttp-siz10/{mode}/{uuid}` | XHTTP |
| `/health` | Health Check |
| `/stats` | API آمار |
| `/api/links` | API مدیریت کانفیگ |

---

# 📁 ساختار پروژه

```text
omidiran/
├── main.py
├── pages.py
├── public_page.py
├── relay_vless.py
├── relay_vmess.py
├── relay_trojan.py
├── xhttp_siz10.py
├── telegram_bot.py
├── requirements.txt
├── Dockerfile
└── README.md
```

### نقش فایل‌ها

| فایل | توضیح |
|---|---|
| `main.py` | هسته FastAPI، APIها، State و لینک‌سازی |
| `pages.py` | Login و Dashboard |
| `public_page.py` | Public Page و صفحات اشتراک |
| `relay_vless.py` | Relay مربوط به VLESS |
| `relay_vmess.py` | Relay مربوط به VMess |
| `relay_trojan.py` | Relay مربوط به Trojan |
| `xhttp_siz10.py` | موتور XHTTP برای سه خانواده پروتکل |
| `telegram_bot.py` | ربات مدیریت تلگرام |
| `requirements.txt` | وابستگی‌های Python |
| `Dockerfile` | ساخت Image پروژه |

---

# 🧪 بررسی بعد از نصب

بعد از Deploy این موارد را بررسی کنید:

### Health

```text
https://DOMAIN/health
```

باید پاسخ سرویس را دریافت کنید.

### پنل

```text
https://DOMAIN/
```

با Username و Password تنظیم‌شده وارد شوید.

### اولین کارهای پیشنهادی

1. یک کانفیگ VLESS / WebSocket بسازید.
2. لینک را تست کنید.
3. یک کانفیگ VMess بسازید و لینک را بررسی کنید.
4. Trojan را تست کنید.
5. هر دو حالت XHTTP را تست کنید:
   - `packet-up`
   - `stream-up`
6. Public Page و Sub Group را بررسی کنید.
7. در صورت فعال بودن ربات، `/start` را بفرستید و زبان را انتخاب کنید.

---

# 💾 پشتیبان‌گیری

فایل State اصلی:

```text
/data/gateway_state.json
```

Secret پایدار:

```text
/data/gateway_secret.key
```

برای Railway، داشتن Volume روی `/data` مهم است؛ بدون Storage پایدار، با حذف یا بازسازی سرویس ممکن است فایل‌های محلی State و Secret باقی نمانند.

---

# ⚠️ نکات مهم برای Railway

- `ADMIN_PASSWORD` را از مقدار پیش‌فرض تغییر دهید.
- `SECRET_KEY` را یک مقدار قوی و ثابت قرار دهید.
- برای `/data` حتماً Volume بسازید.
- بعد از Deploy یک Domain عمومی ایجاد کنید.
- Deployment Logs را بعد از اولین راه‌اندازی بررسی کنید.
- قبل از تغییرات بزرگ، از `gateway_state.json` نسخه پشتیبان بگیرید.
- اگر از روش Fork استفاده می‌کنید، تغییرات Repository شما می‌تواند Deploymentهای بعدی را ایجاد کند.

---

# 💬 پشتیبانی و لینک‌ها

- 📢 کانال تلگرام: [@omid_gamingORG](https://t.me/omid_gamingORG)
- 💬 پشتیبانی: [@iran5090](https://t.me/iran5090)
- 🐙 GitHub: https://github.com/omidiran-gaming/omidiran
- 📦 Container: https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran

### 📚 مستندات Railway

- Deploy از GitHub: https://docs.railway.com/quick-start
- سرویس‌ها و Source: https://docs.railway.com/services
- Deploy از Docker Image: https://docs.railway.com/quick-start

---

## ❤️ پروژه

**OMID-IRAN PANEL**  
مدیریت ساده‌تر، رابط تمیزتر و پشتیبانی از چند خانواده‌ی پروتکل در یک پنل.

</div>
