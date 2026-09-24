<div align="center">

<img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/Docs/logo.png" width="120" alt="OMID-IRAN PANEL">

# 🚀 OMID-IRAN PANEL

**پنل مدیریت کانفیگ VLESS/WS + XHTTP Ultra**

[![Docker](https://img.shields.io/badge/Docker-ghcr.io-blue?logo=docker)](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran)
[![Railway](https://img.shields.io/badge/Deploy-Railway-blueviolet?logo=railway&logoColor=white)](https://railway.app)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@omid__gamingORG-26A5E4?logo=telegram&logoColor=white)](https://t.me/omid_gamingORG)

**🇮🇷 فارسی** · [🇬🇧 English](README.en.md) · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Support](https://t.me/omid_gamingORG)

</div>

---

## ✨ درباره‌ی پروژه

**OMID-IRAN PANEL** یه پنل مدیریت کانفیگ مدرن، سریع و امن برای پروتکل‌های **VLESS/WebSocket** و **XHTTP Ultra (Siz10a)** هست. طراحی تمیز، رابط دوزبانه، و معماری مبتنی بر FastAPI باعث می‌شه هم برای استفاده‌ی شخصی و هم برای تیم‌های کوچک مناسب باشه.

---

## 🎯 ویژگی‌های کلیدی

### 🔐 هسته‌ی اتصال
- **VLESS over WebSocket** — ترابرد پایدار و سازگار با CDN
- **XHTTP Ultra (Siz10a)** — سه مود کامل: `packet-up`, `stream-up`, `stream-one`
- **UUID Auth سخت‌گیرانه** — فقط UUIDهای ثبت‌شده اجازه‌ی اتصال دارند
- **uTLS Fingerprint** — chrome, firefox, safari, ios, android, edge, 360, qq, random, randomized
- **ALPN سفارشی** — قابل تنظیم برای هر کانفیگ (h2, http/1.1, ...)
- **پورت سفارشی** — هر کانفیگ پورت خودش رو داره

### 🎛️ مدیریت کانفیگ
- **سهمیه‌ی ترافیک** — GB / MB / KB (یا نامحدود)
- **تاریخ انقضا** — روز از الان یا نامحدود
- **محدودیت IP** — تعداد کاربر هم‌زمان
- **محدودیت سرعت** — Mbps / KB/s / MB/s
- **Sub Token سفارشی** — به‌جای UUID طولانی
- **گروه‌بندی** — Sub Groups با URL یکتا
- **ریست مصرف** — بدون حذف کانفیگ
- **فعال/غیرفعال‌سازی** — با یه کلیک
- **ویرایش کامل** — همه‌ی پارامترها
- **QR Code استایل‌دار** — برای هر کانفیگ

### 👥 اشتراک‌گذاری
- **Sub Group** — گروه‌بندی کانفیگ‌ها با URL یکتا
- **Public Page** — صفحه‌ی پابلیک زیبا برای هر گروه
- **رمز عبور اختیاری** — برای صفحه‌ی پابلیک
- **لینک ساب همه‌کاره** — `/sub-all`
- **Auto-import** به: v2rayNG, NekoBox, Sing-Box, Streisand, Shadowrocket, Clash, Hiddify, FoXray, v2rayN

### 🎨 رابط کاربری
- **دو تم کامل:**
  - 🌙 **OMID Glass Premium** (Dark) — purple/pink glassmorphism
  - ☀️ **Arctic Premium** (Light) — frosted blue/lavender
- **دوزبانه** — فارسی (RTL) و انگلیسی (LTR)، تغییر لحظه‌ای بدون reload
- **App-like UI** — با bottom nav روی موبایل
- **Sidebar داینامیک** — بر اساس زبان
- **Responsive کامل** — موبایل، تبلت، دسکتاپ
- **PWA-friendly**

### 🤖 ربات تلگرام (اختیاری)
- **مدیریت ربات از داخل پنل**
- **ساخت/حذف کانفیگ از تلگرام**
- **مشاهده‌ی آمار و اتصالات**
- **اعتبارسنجی توکن** از BotFather

### 📊 مانیتورینگ
- **نمودار ترافیک ساعتی** — با Chart.js
- **اتصالات زنده** — با IP و مدت زمان
- **لاگ فعالیت‌ها** (Activity Log)
- **لاگ خطاها** (Error Log)
- **WebSocket Test داخلی**

### 🔒 امنیت
- Session Cookie با `HttpOnly` + `SameSite=Lax`
- **SHA-256 + Salt** برای رمز عبور
- **SECRET_KEY پایدار** روی دیسک — بدون reset بعد از restart
- **CORS قابل تنظیم**
- **اعتبارسنجی کامل ورودی‌ها**

---

## 🚂 نصب روی Railway

**Railway** یه پلتفرم ابری هست که پنل رو با یه کلیک deploy می‌کنه. **نیازی به سرور، دانش فنی، یا تنظیمات پیچیده نداری.** پنل روی سرور **هلند (آمستردام)** بالا میاد.

### ✅ چرا Railway؟

- 🆓 پلن رایگان ($5 credit ماهانه)
- ⚡ Deploy خودکار در ۳ دقیقه
- 🔄 Redeploy خودکار با هر `git push`
- 🌐 دامنه‌ی HTTPS خودکار
- 💾 Volume برای ذخیره‌ی دائمی داده‌ها
- 🇳🇱 روی سرور آمستردام، هلند

---

## 🎯 دو روش برای نصب

### 🍴 روش ۱: Fork کردن ریپو (کاملاً خودکار از GitHub)

با این روش، پنل از کد گیت‌هاب ساخته می‌شه و هر تغییری که توی ریپو بدی، خودکار روی Railway آپدیت می‌شه.

---

#### 📌 گام ۱: Fork کردن ریپو

برو به 👇

🔗 [github.com/omidiran-gaming/omidiran](https://github.com/omidiran-gaming/omidiran)

روی دکمه‌ی **Fork** (بالا-راست صفحه) کلیک کن.

بعد از fork، یه کپی از ریپو توی حساب گیت‌هاب خودت ساخته می‌شه — مثلاً:

```
github.com/YOUR-USERNAME/omidiran
```

---

#### 📌 گام ۲: ساخت حساب Railway

برو به 👇

🔗 [railway.app](https://railway.app)

روی **Login with GitHub** کلیک کن و به Railway اجازه بده به گیت‌هاب دسترسی داشته باشه.

---

#### 📌 گام ۳: ساخت پروژه‌ی جدید

توی داشبورد Railway:

۱. روی **+ New Project** کلیک کن
۲. گزینه‌ی **Deploy from GitHub repo** رو انتخاب کن
۳. اگه اولین باره، روی **Configure GitHub App** بزن و دسترسی بده
۴. ریپوی fork شده‌ی خودت (`YOUR-USERNAME/omidiran`) رو انتخاب کن
۵. روی **Deploy Now** کلیک کن

> ⏳ صبر کن حدود **۲ تا ۴ دقیقه** تا build تموم بشه. Railway خودکار `Dockerfile` رو پیدا می‌کنه و اجرا می‌کنه.

---
#### 📌 گام ۴: تنظیم متغیرهای محیطی (⚡ خیلی مهم!)

۱. توی صفحه‌ی سرویس، برو به تب **Variables**
۲. روی **+ New Variable** کلیک کن و این‌ها رو یکی‌یکی اضافه کن:

| نام | مقدار پیشنهادی | وضعیت | توضیح |
|-----|---------------|-------|-------|
| `ADMIN_USERNAME` | `omid` (یا هرچی می‌خوای) | 🟢 اجباری | نام کاربری ورود |
| `ADMIN_PASSWORD` | یه رمز قوی | 🟢 اجباری | رمز عبور پنل |
| `SECRET_KEY` | یه رشته‌ی تصادفی ۶۴ حرفی | 🟡 توصیه‌شده | اگه ندی، پنل خودکار می‌سازه |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | 🔵 اختیاری | لینک پشتیبانی |
| `TELEGRAM_BOT_TOKEN` | (خالی) | 🔵 اختیاری | برای ربات تلگرام |
| `TELEGRAM_ADMIN_IDS` | (خالی) | 🔵 اختیاری | Admin IDهای ربات |

##### 🤔 SECRET_KEY رو حتماً بذارم؟

**بله، شدیداً توصیه می‌شه.** چون:

- اگه `SECRET_KEY` نداری و Volume هم به `/data` وصل نکردی → با هر restart پسورد پنل عوض می‌شه و باید از اول ست کنی
- اگه `SECRET_KEY` ست کنی → دیگه نگران restart نیستی، حتی بدون Volume

اگه Volume رو وصل کردی، پنل خودش یه secret می‌سازه و توی `/data` ذخیره می‌کنه، ولی **بهتره هم Volume داشته باشی هم SECRET_KEY**.
---

#### 📌 گام ۵: اضافه کردن Volume (برای ذخیره‌ی دائمی)

بدون Volume، با هر redeploy **همه‌ی کانفیگ‌ها، گروه‌ها، و تنظیمات از بین می‌رن**.

۱. توی صفحه‌ی سرویس، روی تب **Volumes** کلیک کن
۲. روی **+ Add Volume** بزن
۳. تنظیم کن:
   - **Mount Path:** `/data`  ← **حتماً دقیقاً همین**
   - **Size:** `1 GB` (رایگان)
۴. روی **Add** کلیک کن

> 🔁 Railway خودکار redeploy می‌کنه و داده‌ها دائمی می‌شن.

---

#### 📌 گام ۶: تنظیم Region به هلند (اختیاری — پیش‌فرض هم آمستردامه)

۱. توی صفحه‌ی سرویس، برو به **Settings** → **Deploy** → **Regions**
۲. مطمئن شو **EU West Metal (Amsterdam)** انتخاب شده
۳. روی **Apply Changes** کلیک کن

---

#### 📌 گام ۷: دریافت دامنه‌ی HTTPS

۱. برو به تب **Settings** → **Networking**
۲. روی **Generate Domain** کلیک کن
۳. یه دامنه‌ی HTTPS می‌گیری مثل:

```
https://omidiran-production.up.railway.app
```

۴. (اختیاری) می‌تونی **Custom Domain** خودت رو هم اضافه کنی

---

#### 📌 گام ۸: ورود به پنل

۱. دامنه‌ی HTTPS رو توی مرورگر باز کن
۲. با `ADMIN_USERNAME` و `ADMIN_PASSWORD` که ست کردی وارد شو
۳. **تمام! 🎉** پنل آماده‌ست

---

### 🐳 روش ۲: با Docker Image آماده (سریع‌تر، بدون Build)

با این روش، از **image آماده‌ی GHCR** استفاده می‌کنی. نیازی به fork کردن ریپو نداری — فقط image رو به Railway می‌دی و بالا میاد.

> ⚡ **مزیت:** build سریع‌تر (چون از پیش ساخته شده)، حجم کمتر، بدون نیاز به Dockerfile

---

#### 📌 گام ۱: ساخت پروژه‌ی خالی

توی داشبورد Railway:

۱. روی **+ New Project** کلیک کن
۲. گزینه‌ی **Empty Project** رو انتخاب کن

---

#### 📌 گام ۲: اضافه کردن Docker Image

توی صفحه‌ی پروژه‌ی خالی:

۱. روی **+ Create** کلیک کن
۲. گزینه‌ی **Docker Image** رو انتخاب کن
۳. توی فیلد image، این آدرس رو دقیقاً کپی کن:

```
ghcr.io/omidiran-gaming/omidiran:latest
```

۴. روی **Add** یا **Deploy** کلیک کن

> ⏳ صبر کن حدود **۱ تا ۲ دقیقه** — image آماده‌ست، فقط pull و اجرا می‌شه.

---

#### 📌 گام ۳: تنظیم متغیرهای محیطی

مثل روش اول:

۱. برو به تب **Variables**
۲. این‌ها رو اضافه کن:

| نام | مقدار |
|-----|-------|
| `ADMIN_USERNAME` | `omid` (یا هرچی می‌خوای) |
| `ADMIN_PASSWORD` | یه رمز قوی |
| `SECRET_KEY` | یه رشته‌ی تصادفی |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` (اختیاری) |

---

#### 📌 گام ۴: اضافه کردن Volume

دقیقاً مثل روش اول:

۱. تب **Volumes** → **+ Add Volume**
۲. **Mount Path:** `/data`
۳. **Size:** `1 GB`
۴. **Add**

---

#### 📌 گام ۵: تنظیم Region به هلند

۱. برو به **Settings** → **Deploy** → **Regions**
۲. **EU West Metal (Amsterdam)** رو انتخاب کن

---

#### 📌 گام ۶: دریافت دامنه و ورود

۱. برو به **Settings** → **Networking** → **Generate Domain**
۲. دامنه‌ی HTTPS رو باز کن
۳. با `ADMIN_USERNAME` و `ADMIN_PASSWORD` وارد شو
۴. **تموم! 🎉**

---

## 📊 مقایسه‌ی دو روش

| ویژگی | 🍴 Fork کردن ریپو | 🐳 Docker Image |
|-------|-------------------|-----------------|
| **سرعت deploy** | ۲-۴ دقیقه | ۱-۲ دقیقه |
| **نیاز به GitHub** | ✅ بله | ❌ نه |
| **آپدیت خودکار** | ✅ خودکار با push | ⚠️ دستی (redeploy) |
| **قابل شخصی‌سازی** | ✅ کامل | ❌ فقط env |
| **مناسب برای** | توسعه‌دهنده | کاربر عادی |

> 💡 **توصیه:** اگه می‌خوای کد رو دستکاری کنی → **Fork**. اگه فقط می‌خوای پنل رو سریع بالا بیاری → **Docker Image**.

---

## ⚙️ متغیرهای محیطی

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

## 🐛 عیب‌یابی

| مشکل | راه‌حل |
|------|--------|
| **Build fail** | برو به تب **Deployments** → روی آخرین build کلیک کن → لاگ رو چک کن |
| **پنل باز نمی‌شه** | مطمئن شو دامنه توی **Networking** ساخته شده |
| **داده‌ها بعد از redeploy می‌پرن** | Volume رو با Mount Path دقیقاً `/data` ست کن |
| **خطای 502 Bad Gateway** | ۲ دقیقه صبر کن — سرویس هنوز در حال بالا اومدنه |
| **رمز کار نمی‌کنه** | برو به Variables → `ADMIN_PASSWORD` رو چک کن |
| **`SECRET_KEY` بعد از restart تغییر می‌کنه** | `SECRET_KEY` رو دستی توی Variables ست کن |
| **Region هلند نیست** | Settings → Deploy → Regions → Amsterdam |

---

## ✅ چک‌لیست نهایی

بعد از نصب، اینا رو چک کن:

- [ ] پنل با دامنه‌ی HTTPS باز می‌شه
- [ ] با رمز قوی وارد می‌شم
- [ ] Volume به `/data` وصل هست
- [ ] Region روی **Amsterdam** هست
- [ ] یه کانفیگ تستی ساختم و لینکش رو تست کردم
- [ ] QR Code و Sub Link کار می‌کنه

---

## 💬 پشتیبانی

- 📢 **کانال تلگرام:** [@omid_gamingORG](https://t.me/omid_gamingORG)
- 💬 **پشتیبانی:** [@iran5090](https://t.me/iran5090)
- 🐛 **گزارش باگ:** [GitHub Issues](https://github.com/omidiran-gaming/omidiran/issues)

---

<div align="center">

**Made with ❤️ by OMID Network**

⭐ اگه برات مفید بود، یه ستاره بده!

[🐙 GitHub](https://github.com/omidiran-gaming/omidiran) · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Telegram](https://t.me/omid_gamingORG) · [🇬🇧 English](README.en.md)

</div>
