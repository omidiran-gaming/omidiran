<div align="center">

<img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/Docs/logo.png" width="120" alt="OMID-IRAN PANEL">

# 🚀 OMID-IRAN PANEL

**Modern VLESS / VMess / Trojan Management Panel with WebSocket / XHTTP Ultra**

[![Railway](https://img.shields.io/badge/Deploy-Railway-7B61FF?logo=railway&logoColor=white)](https://railway.app/)
[![Docker](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=white)](https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@omid__gamingORG-26A5E4?logo=telegram&logoColor=white)](https://t.me/omid_gamingORG)

**Railway only • Two deployment methods: GitHub Fork or Direct Container Deployment**

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-mobile.png" width="30%" alt="Mobile">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-configs.png" width="30%" alt="Configs">
  <img src="https://raw.githubusercontent.com/omidiran-gaming/omidiran/main/docs/preview-stats.png" width="30%" alt="Stats">
</p>

---

## 🇬🇧 English

### ✨ Introduction

**OMID-IRAN PANEL** is a modern management panel for creating, managing, and sharing **VLESS, VMess, and Trojan** configurations with **WebSocket** and **XHTTP Ultra (Siz10a)** transports.

The core is built with **FastAPI**, with an administration panel, Public Page, and Telegram bot designed for both English and Persian. **English is the primary interface language**, while Persian is translated from the same canonical English strings so language switching does not cause duplicated or chained translations.

---

## 🔐 Protocols and Transports

This version supports all **9 combinations** below:

| Protocol | WebSocket | XHTTP packet-up | XHTTP stream-up |
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
- VMess share-link generation compatible with common clients and XHTTP importers

### Trojan
- WebSocket
- XHTTP `packet-up`
- XHTTP `stream-up`
- Password-based authentication
- TCP and UDP relay support

### Connection Options
- **uTLS Fingerprint:** `chrome`, `firefox`, `safari`, `ios`, `android`, `edge`, `360`, `qq`, `random`, `randomized`
- **ALPN:** `http/1.1`, `h2`, and `h2,http/1.1`
- Configurable port
- UUID-based authentication for UUID-based configurations

---

## 🎛️ Configuration Management

Each configuration can include:

- Name and description
- Protocol and transport
- Traffic quota
- Expiration date or unlimited lifetime
- Concurrent IP limit
- Speed limit
- Fingerprint
- ALPN
- Port
- Custom Sub Token
- Enable / disable
- Usage reset
- Full editing and deletion

A share link matching the selected protocol is generated automatically.

---

## 👥 Sub Groups and Sharing

- Create **Sub Groups**
- Add multiple configurations to a group
- Dedicated Public Page URL
- Dedicated Subscription URL
- Optional group password
- Custom Sub Tokens for shorter subscription links
- Client-friendly subscription output
- Styled QR Code generation for share links

Supported clients in the import interface:

`v2rayNG` · `NekoBox` · `Sing-Box` · `Streisand` · `Shadowrocket` · `Clash` · `Hiddify` · `FoXray` · `v2rayN`

---

## 🎨 User Interface

### Administration Panel
- English and Persian
- English as the canonical language
- Instant language switching without reload
- Full RTL / LTR support
- Responsive design for mobile, tablet, and desktop
- Language-aware Sidebar and Navigation
- Modern app-like interface

### Themes
- 🌙 **OMID Glass Premium** for Dark Mode
- ☀️ **Arctic Premium** for Light Mode

### Public Page
- Modern lightweight subscription page
- Configuration status and usage overview
- QR Code
- Client import
- Language selection
- Theme selection

---

## 🤖 Telegram Bot

The Telegram bot is optional and provides:

- Create configurations
- Delete configurations
- Edit configurations
- Enable / disable
- View configuration details
- View statistics and connections
- Manage Sub Groups
- Search and Filter
- Backup and Restore
- Export as JSON / CSV / TXT
- Traffic charts
- Notifications
- Admin management
- Styled QR Code
- Inline Mode

### 🌐 Bot Languages

The bot is fully bilingual:

- 🇬🇧 English
- 🇮🇷 Persian

On the first `/start`, the user is asked to choose a language and the selection is saved. After that, the **🌐 Language** option is available in the main menu at any time.

---

## 📊 Monitoring

- Total traffic
- Hourly traffic
- Total configurations
- Active and expired configurations
- Live connections
- Connected IPs
- Session counts
- Activity Log
- Error Log
- Uptime
- WebSocket Test

---

## 🔒 Security and Persistence

- `HttpOnly` session cookies
- `SameSite=Lax`
- Panel authentication
- SHA-256 based password hashing with a persistent secret
- Persistent secret storage when required
- Per-configuration IP limits
- Active / Expiry / Quota checks before allowing connections
- State stored in `gateway_state.json`

For Railway deployment, mount `/data` as a persistent Volume so State and Secret files survive restarts and redeployments.

---

# 🚀 Deploy on Railway

This project is documented with **Railway only** and provides two deployment methods:

1. **Fork the GitHub repository and deploy from the repository**
2. **Deploy the official container directly from GitHub Container Registry**

---

## 1️⃣ Deploy with a GitHub Fork

### Step 1 — Fork the Repository

Open the project repository:

```text
https://github.com/omidiran-gaming/omidiran
```

Click **Fork** and create your own copy of the repository.

### Step 2 — Create a Railway Project

Open Railway:

```text
https://railway.com/
```

Then select:

```text
New Project
→ Deploy from GitHub Repo
→ Connect GitHub
→ Select your forked repository
```

### Step 3 — Set Variables

Inside the service, open **Variables** and configure:

```env
ADMIN_USERNAME=omid
ADMIN_PASSWORD=your_strong_password
SECRET_KEY=your_long_random_secret
DATA_DIR=/data

TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_IDS=

SUPPORT_URL=https://t.me/omid_gamingORG
```

You normally do not need to hard-code `PORT`; Railway provides the runtime port through the `PORT` environment variable.

### Step 4 — Add a Volume

Create a Railway Volume and mount it at:

```text
/data
```

This keeps the project's persistent State and Secret files across restarts and redeployments.

### Step 5 — Deploy

Save the Variables and Volume settings, then deploy the service.

After deployment, open **Networking** and generate a public domain.

---

## 2️⃣ Deploy the Container Directly

Use this method when you do not want to fork the repository and prefer to run the published container image directly.

Image:

```text
ghcr.io/omidiran-gaming/omidiran:latest
```

### Step 1 — Create an Empty Railway Project

In Railway:

```text
New Project
→ Empty Project
```

### Step 2 — Add the Service

In the Project Canvas:

```text
Add a Service
→ Docker Image
```

Use:

```text
ghcr.io/omidiran-gaming/omidiran:latest
```

### Step 3 — Set Variables

Use the same variables as the GitHub deployment method:

```env
ADMIN_USERNAME=omid
ADMIN_PASSWORD=your_strong_password
SECRET_KEY=your_long_random_secret
DATA_DIR=/data

TELEGRAM_BOT_TOKEN=
TELEGRAM_ADMIN_IDS=

SUPPORT_URL=https://t.me/omid_gamingORG
```

### Step 4 — Add a Volume

Create a Railway Volume and set the Mount Path to:

```text
/data
```

### Step 5 — Deploy and Generate a Domain

Deploy the service and then go to:

```text
Settings
→ Networking
→ Generate Domain
```

---

## ⚙️ Environment Variables

| Variable | Recommended Value | Description |
|---|---|---|
| `ADMIN_USERNAME` | `omid` | Panel username |
| `ADMIN_PASSWORD` | Strong value | Panel password |
| `SECRET_KEY` | Long random value | Session and password hashing secret |
| `DATA_DIR` | `/data` | State and Secret storage path |
| `TELEGRAM_BOT_TOKEN` | Empty / Token | Telegram bot token |
| `TELEGRAM_ADMIN_IDS` | Empty / IDs | Telegram admin IDs |
| `SUPPORT_URL` | Support URL | Support link |
| `PORT` | Provided by Railway | Runtime service port |

### 🔐 Important Secret Note

Keep `SECRET_KEY` stable and sufficiently long. Changing it may invalidate sessions and affect data that depends on the secret.

---

# 🌐 Important Endpoints

| Path | Purpose |
|---|---|
| `/` | Login page |
| `/dashboard` | Admin panel |
| `/sub/{uuid}` | Single configuration subscription |
| `/sub-all` | Subscription for all active configurations |
| `/sub-group/{key}` | Group subscription |
| `/p/{key}` | Group Public Page |
| `/ws/{uuid}` | WebSocket Tunnel |
| `/xhttp-siz10/{mode}/{uuid}` | XHTTP |
| `/health` | Health Check |
| `/stats` | Statistics API |
| `/api/links` | Configuration management API |

---

# 📁 Project Structure

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

### File Roles

| File | Description |
|---|---|
| `main.py` | FastAPI core, APIs, State, and link generation |
| `pages.py` | Login and Dashboard UI |
| `public_page.py` | Public subscription pages |
| `relay_vless.py` | VLESS relay |
| `relay_vmess.py` | VMess relay |
| `relay_trojan.py` | Trojan relay |
| `xhttp_siz10.py` | XHTTP engine for all three protocol families |
| `telegram_bot.py` | Telegram management bot |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Project image build definition |

---

# 🧪 Post-Deployment Checks

After deploying, verify the following:

### Health

```text
https://DOMAIN/health
```

You should receive a successful service response.

### Panel

```text
https://DOMAIN/
```

Sign in with the configured username and password.

### Recommended First Tests

1. Create a VLESS / WebSocket configuration.
2. Test the generated share link.
3. Create a VMess configuration and verify the generated link.
4. Test Trojan.
5. Test both XHTTP modes:
   - `packet-up`
   - `stream-up`
6. Open the Public Page and verify Sub Groups.
7. If the Telegram bot is enabled, send `/start` and choose a language.

---

# 💾 Backup and Persistent Data

Main State file:

```text
/data/gateway_state.json
```

Persistent Secret file:

```text
/data/gateway_secret.key
```

For Railway, keeping a Volume mounted at `/data` is important. Without persistent storage, local State and Secret files may be lost when the service is rebuilt or recreated.

---

# ⚠️ Railway Production Notes

- Change the default `ADMIN_PASSWORD`.
- Set a strong, stable `SECRET_KEY`.
- Always mount a Volume at `/data`.
- Generate a public Domain after deployment.
- Check Deployment Logs after the first startup.
- Back up `gateway_state.json` before major changes.
- With the GitHub Fork method, future repository changes can trigger new deployments.

---

# 💬 Support and Links

- 📢 Telegram: [@omid_gamingORG](https://t.me/omid_gamingORG)
- 💬 Support: [@iran5090](https://t.me/iran5090)
- 🐙 GitHub: https://github.com/omidiran-gaming/omidiran
- 📦 Container: https://github.com/omidiran-gaming/omidiran/pkgs/container/omidiran

### 📚 Railway Documentation

- GitHub deployments: https://docs.railway.com/quick-start
- Services: https://docs.railway.com/services
- Docker image deployments: https://docs.railway.com/quick-start

---

## ❤️ Project

**OMID-IRAN PANEL**  
Simpler management, a cleaner interface, and multiple protocol families in one panel.
