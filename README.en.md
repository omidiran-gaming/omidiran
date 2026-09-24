<div align="center">

<img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/Docs/logo.png" width="120" alt="OMID-IRAN PANEL">

# 🚀 OMID-IRAN PANEL

**Modern VLESS/WS + XHTTP Ultra Management Panel**

[![Docker](https://img.shields.io/badge/Docker-ghcr.io-blue?logo=docker)](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran)
[![Railway](https://img.shields.io/badge/Deploy-Railway-blueviolet?logo=railway&logoColor=white)](https://railway.app)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@omid__gamingORG-26A5E4?logo=telegram&logoColor=white)](https://t.me/omid_gamingORG)

[🇮🇷 فارسی](README.md) · ** English ** · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Support](https://t.me/omid_gamingORG)

</div>

---

## ✨ About

**OMID-IRAN PANEL** is a modern, fast, and secure management panel for **VLESS/WebSocket** and **XHTTP Ultra (Siz10a)** protocols. Clean design, bilingual UI, and FastAPI-based architecture make it suitable for both personal and small-team use.

---

## 🎯 Key Features

### 🔐 Connection Core
- **VLESS over WebSocket** — stable, CDN-compatible transport
- **XHTTP Ultra (Siz10a)** — 3 modes: `packet-up`, `stream-up`, `stream-one`
- **Strict UUID Auth** — only registered UUIDs can connect
- **uTLS Fingerprint** — chrome, firefox, safari, ios, android, edge, 360, qq, random, randomized
- **Custom ALPN** — per-config (h2, http/1.1, ...)
- **Custom Port** — every config has its own port

### 🎛️ Config Management
- **Traffic Quota** — GB / MB / KB (or unlimited)
- **Expiry Date** — days from now or unlimited
- **IP Limit** — concurrent user limit
- **Speed Limit** — Mbps / KB/s / MB/s
- **Custom Sub Token** — instead of long UUID
- **Sub Groups** — organize configs with unique URLs
- **Usage Reset** — without deleting config
- **Enable/Disable** — with one click
- **Full Edit** — all parameters
- **Styled QR Code** — per config

### 👥 Subscriptions
- **Sub Group** — group configs with unique URL
- **Public Page** — beautiful public page per group
- **Optional Password** — for public pages
- **All-in-one Sub Link** — `/sub-all`
- **Auto-import** to: v2rayNG, NekoBox, Sing-Box, Streisand, Shadowrocket, Clash, Hiddify, FoXray, v2rayN

### 🎨 UI/UX
- **Two full themes:**
  - 🌙 **OMID Glass Premium** (Dark) — purple/pink glassmorphism
  - ☀️ **Arctic Premium** (Light) — frosted blue/lavender
- **Bilingual** — Persian (RTL) & English (LTR) with instant switching, no reload
- **App-like UI** — bottom nav on mobile
- **Dynamic Sidebar** — based on language
- **Fully Responsive** — mobile, tablet, desktop
- **PWA-friendly**

### 🤖 Telegram Bot (optional)
- **Bot management from panel**
- **Create/Delete configs from Telegram**
- **View stats & connections**
- **Token validation** via BotFather

### 📊 Monitoring
- **Hourly traffic chart** — with Chart.js
- **Live connections** — with IP & duration
- **Activity Log**
- **Error Log**
- **Built-in WebSocket Test**

### 🔒 Security
- Session Cookie with `HttpOnly` + `SameSite=Lax`
- **SHA-256 + Salt** for passwords
- **Persistent SECRET_KEY** on disk — no reset after restart
- **Configurable CORS**
- **Full input validation**

---

## 🚂 Deploy on Railway

**Railway** is a cloud platform that deploys the panel in one click. **No server, no technical knowledge, no complex setup required.** The panel runs on a **Netherlands (Amsterdam) server**.

### ✅ Why Railway?

- 🆓 Free plan ($5 monthly credit)
- ⚡ 3-minute auto-deploy
- 🔄 Auto-redeploy on every `git push`
- 🌐 Automatic HTTPS domain
- 💾 Volume for persistent data
- 🇳🇱 Runs on Amsterdam, Netherlands

---

## 🎯 Two Deployment Methods

### 🍴 Method 1: Fork the Repo (fully automatic from GitHub)

The panel builds from GitHub source, and any change you push auto-updates on Railway.

---

#### 📌 Step 1: Fork the repo

Go to 👇

🔗 [github.com/omidiran-gaming/omidiran](https://github.com/omidiran-gaming/omidiran)

Click the **Fork** button (top-right).

After forking, you'll have a copy at:

```
github.com/YOUR-USERNAME/omidiran
```

---

#### 📌 Step 2: Create Railway account

Go to 👇

🔗 [railway.app](https://railway.app)

Click **Login with GitHub** and authorize Railway.

---

#### 📌 Step 3: Create a new project

In the Railway dashboard:

1. Click **+ New Project**
2. Choose **Deploy from GitHub repo**
3. If this is your first time, click **Configure GitHub App** and authorize
4. Select your forked repo (`YOUR-USERNAME/omidiran`)
5. Click **Deploy Now**

> ⏳ Wait **2-4 minutes** for the build. Railway auto-detects and runs the `Dockerfile`.

---

#### 📌 Step 4: Set environment variables (⚡ CRITICAL!)

Without this step, the panel runs with default weak credentials — **insecure**.

1. In the service page, go to the **Variables** tab
2. Click **+ New Variable** and add:

| Name | Suggested Value | Status | Description |
|------|-----------------|--------|-------------|
| `ADMIN_USERNAME` | `omid` (or your choice) | 🟢 Required | Panel username |
| `ADMIN_PASSWORD` | **A strong password** | 🟢 Required | Panel password |
| `SECRET_KEY` | **A random 64-char string** | 🟡 Recommended | Session security key — auto-generated if not set |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | 🔵 Optional | Support link |
| `TELEGRAM_BOT_TOKEN` | (empty) | 🔵 Optional | For Telegram bot |
| `TELEGRAM_ADMIN_IDS` | (empty) | 🔵 Optional | Bot admin IDs |

##### 🤔 Should I set SECRET_KEY?

**Yes, strongly recommended.** Because:

- If you **don't** set `SECRET_KEY` **and** don't attach a Volume to `/data` → the panel generates a new secret on every restart → **your password stops working** and you have to reset it
- If you **do** set `SECRET_KEY` → you're safe from restarts, even without a Volume
- If you attach a Volume → the panel auto-generates and stores a secret in `/data`, but it's still **best practice** to set both

> 💡 **TL;DR:** Set `SECRET_KEY` **and** attach a Volume to `/data`. Belt and suspenders.

##### 🔑 Generate a random `SECRET_KEY`

**Linux / macOS:**
```bash
openssl rand -hex 32
```

**Windows PowerShell:**
```powershell
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 64 | % {[char]$_})
```

**Or online:** [random.org/strings](https://www.random.org/strings/)

> ⚠️ **Warning:** Default `ADMIN_PASSWORD` is `omid` — change it!

> 💡 Railway auto-sets `PORT` — no need to add it manually.

---

#### 📌 Step 5: Add a Volume (for persistent storage)

Without a Volume, **all configs, groups, and settings are lost** on every redeploy.

1. In the service page, click the **Volumes** tab
2. Click **+ Add Volume**
3. Configure:
   - **Mount Path:** `/data` ← **exactly this**
   - **Size:** `1 GB` (free)
4. Click **Add**

> 🔁 Railway will auto-redeploy and data becomes persistent.

> ⚠️ **Important:** If a Volume is attached, changing region causes downtime and requires Volume migration. Set the region **before** adding the Volume.

---

#### 📌 Step 6: Set Region to Netherlands (optional — default is Amsterdam)

1. Go to **Settings** → **Deploy** → **Regions**
2. Ensure **EU West Metal (Amsterdam)** is selected
3. Click **Apply Changes**

---

#### 📌 Step 7: Get an HTTPS domain

1. Go to **Settings** → **Networking**
2. Click **Generate Domain**
3. You'll get:

```
https://omidiran-production.up.railway.app
```

4. (Optional) Add a **Custom Domain**

---

#### 📌 Step 8: Log in

1. Open the HTTPS domain in your browser
2. Log in with your `ADMIN_USERNAME` and `ADMIN_PASSWORD`
3. **Done! 🎉**

---

### 🐳 Method 2: Using Pre-built Docker Image (faster, no build)

This uses the **pre-built GHCR image**. No fork needed — just point Railway to the image.

> ⚡ **Benefit:** Faster deploy, smaller size, no Dockerfile needed

---

#### 📌 Step 1: Create empty project

In Railway dashboard:

1. Click **+ New Project**
2. Choose **Empty Project**

---

#### 📌 Step 2: Add Docker Image

In the empty project:

1. Click **+ Create**
2. Choose **Docker Image**
3. Enter the image address:

```
ghcr.io/omidiran-gaming/omidiran:latest
```

4. Click **Add** or **Deploy**

> ⏳ Wait **1-2 minutes** — image is ready, just pull & run.

---

#### 📌 Step 3: Set environment variables

Same as Method 1:

1. Go to **Variables** tab
2. Add:

| Name | Value | Status |
|------|-------|--------|
| `ADMIN_USERNAME` | `omid` (or your choice) | 🟢 Required |
| `ADMIN_PASSWORD` | A strong password | 🟢 Required |
| `SECRET_KEY` | A random 64-char string | 🟡 Recommended |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | 🔵 Optional |

---

#### 📌 Step 4: Add Volume

Same as Method 1:

1. **Volumes** tab → **+ Add Volume**
2. **Mount Path:** `/data`
3. **Size:** `1 GB`
4. **Add**

---

#### 📌 Step 5: Set Region to Netherlands

1. Go to **Settings** → **Deploy** → **Regions**
2. Select **EU West Metal (Amsterdam)**

---

#### 📌 Step 6: Get domain and log in

1. Go to **Settings** → **Networking** → **Generate Domain**
2. Open the HTTPS domain
3. Log in with `ADMIN_USERNAME` and `ADMIN_PASSWORD`
4. **Done! 🎉**

---

## 📊 Comparison

| Feature | 🍴 Fork Method | 🐳 Docker Image |
|---------|----------------|-----------------|
| **Deploy speed** | 2-4 min | 1-2 min |
| **Requires GitHub** | ✅ Yes | ❌ No |
| **Auto-update** | ✅ Auto on push | ⚠️ Manual redeploy |
| **Customizable** | ✅ Full | ❌ Env only |
| **Best for** | Developers | Regular users |

> 💡 **Recommendation:** Want to customize the code? → **Fork**. Just want it running fast? → **Docker Image**.

---

## ⚙️ Environment Variables

| Variable | Default | Status | Description |
|----------|---------|--------|-------------|
| `PORT` | `8000` | 🔵 auto | Server port (Railway auto-sets to `8080`) |
| `ADMIN_USERNAME` | `omid` | 🟢 Required | Panel username |
| `ADMIN_PASSWORD` | `omid` | 🟢 Required | Panel password |
| `SECRET_KEY` | auto | 🟡 Recommended | Session key — auto-persisted to disk if not set |
| `DATA_DIR` | `/data` | 🔵 auto | State storage directory |
| `RAILWAY_PUBLIC_DOMAIN` | `localhost` | 🔵 auto | Public domain |
| `TELEGRAM_BOT_TOKEN` | — | 🔵 Optional | Bot token |
| `TELEGRAM_ADMIN_IDS` | — | 🔵 Optional | Admin IDs (comma-separated) |
| `SUPPORT_URL` | `https://t.me/omid_gamingORG` | 🔵 Optional | Support link |

> ⚠️ **Important:** For production, always change `ADMIN_PASSWORD` and set `SECRET_KEY`.

### 🔑 How SECRET_KEY Works

The panel looks for `SECRET_KEY` in this order:

1. **Environment variable** `SECRET_KEY` → used if set
2. **File** `/data/gateway_secret.key` → read if the file exists
3. **Auto-generate** → new random string written to the file

**Implications:**

| Scenario | Result |
|----------|--------|
| ✅ `SECRET_KEY` set in env | Always stable — best case |
| ✅ Volume mounted at `/data`, env NOT set | Stable — persisted to disk |
| ⚠️ No Volume, env NOT set | **Password resets on every restart!** |

> 💡 **Best practice:** Set `SECRET_KEY` **and** attach a Volume at `/data`. Belt and suspenders.

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Build fails** | Go to **Deployments** tab → click latest build → check logs |
| **Panel not loading** | Ensure domain is generated in **Networking** |
| **Data lost after redeploy** | Set Volume Mount Path to exactly `/data` |
| **502 Bad Gateway** | Wait 2 minutes — service is still starting |
| **Password not working** | Check `ADMIN_PASSWORD` in Variables |
| **`SECRET_KEY` changes on restart** | Set `SECRET_KEY` manually in Variables |
| **Region not Netherlands** | Settings → Deploy → Regions → Amsterdam |
| **Forgot password** | Update `ADMIN_PASSWORD` in Variables → redeploy |
| **Bot not responding** | Check `TELEGRAM_BOT_TOKEN` and `TELEGRAM_ADMIN_IDS` |

---

## ✅ Final Checklist

After deployment, verify:

- [ ] Panel opens with HTTPS domain
- [ ] Login works with strong password
- [ ] Volume mounted at `/data`
- [ ] `SECRET_KEY` set in Variables
- [ ] Region set to **Amsterdam**
- [ ] Created a test config and tested the link
- [ ] QR Code and Sub Link work
- [ ] (Optional) Telegram bot responding

---

## 💬 Support

- 📢 **Telegram Channel:** [@omid_gamingORG](https://t.me/omid_gamingORG)
- 💬 **Support:** [@iran5090](https://t.me/iran5090)
- 🐛 **Report Bug:** [GitHub Issues](https://github.com/omidiran-gaming/omidiran/issues)

---

<div align="center">

**Made with ❤️ by OMID Network**

⭐ Star this repo if it helps you!

[🐙 GitHub](https://github.com/omidiran-gaming/omidiran) · [📦 Docker](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran) · [💬 Telegram](https://t.me/omid_gamingORG) · [🇮🇷 فارسی](README.md)

</div>
