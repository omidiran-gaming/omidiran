# telegram_bot.py — OMID-IRAN PANEL v2.0
# ══════════════════════════════════════════════════════════════════════════════
# ربات مدیریت تلگرام — کامل، حرفه‌ای، همه‌کاره
# ══════════════════════════════════════════════════════════════════════════════
#
# 🎯 قابلیت‌ها:
#   • مدیریت کانفیگ (ساخت/حذف/ویرایش/فعال‌غیرفعال/ریست)
#   • مدیریت گروه‌های ساب (لینک حرفه‌ای)
#   • مدیریت ادمین‌ها از داخل ربات
#   • جستجو و فیلتر کانفیگ‌ها
#   • Export (JSON/CSV) + Backup/Restore
#   • آمار کامل + نمودار ترافیک (quickchart.io)
#   • آمار امروز / هفته / ماه
#   • TOP مصرف‌کننده‌ها
#   • نوتیفیکیشن خودکار (انقضا / اتمام حجم)
#   • گزارش‌های زمان‌بندی‌شده (روزانه / هفتگی)
#   • QR Code به‌صورت عکس + لینک Webapp
#   • Inline Mode (استفاده در هر چتی)
#   • ویرایش Sub Token / Fingerprint / ALPN / Port
# ══════════════════════════════════════════════════════════════════════════════
#
# 📌 پیش‌نیاز Inline Mode (اختیاری):
#   توی @BotFather → /setinline → placeholder رو ست کن
#   حالا کاربر می‌تونه از @YourBot توی هر چتی استفاده کنه
# ══════════════════════════════════════════════════════════════════════════════

import asyncio
import os
import re
import io
import csv
import json
import time

import qrcode
from PIL import Image, ImageDraw

from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

import httpx

from main import (
    LINKS, SUBS,
    make_link, remove_link, set_link_active, vless_link_for_link,
    get_host, fmt_bytes, is_link_allowed, is_link_expired,
    logger, save_state,
    PROTOCOLS, DEFAULT_PROTOCOL, FINGERPRINTS, DEFAULT_FINGERPRINT,
    normalize_protocol, split_protocol,
    DEFAULT_ALPN_BY_PROTOCOL, DEFAULT_PORT, DEFAULT_SPEED_LIMIT,
    MIN_PORT, MAX_PORT, parse_size_to_bytes, parse_speed_to_bytes,
    create_sub_group, set_link_sub, remove_sub_group,
    connections, stats, uptime, activity_logs,
    update_link_field, reset_link_usage,
    hourly_traffic,
)

# ═══════════════════════════════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════════════════════════════
def _get_token() -> str:
    try:
        from main import TELEGRAM
        return str(TELEGRAM.get("bot_token") or "").strip()
    except Exception:
        return os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

def _get_admin_ids() -> set:
    try:
        from main import TELEGRAM
        raw = str(TELEGRAM.get("admin_ids") or "").strip()
    except Exception:
        raw = os.environ.get("TELEGRAM_ADMIN_IDS", "").strip()
    return {int(x) for x in raw.replace(" ", "").split(",") if x.strip().lstrip("-").isdigit()}

async def _save_admins(ids: set):
    """ذخیره‌ی ادمین‌های جدید توی main.TELEGRAM + save_state."""
    try:
        from main import TELEGRAM
        TELEGRAM["admin_ids"] = ",".join(str(i) for i in sorted(ids))
        await save_state()
    except Exception as e:
        logger.warning(f"save admins failed: {e}")

async def add_admin(uid: int) -> bool:
    ids = _get_admin_ids()
    if uid in ids:
        return False
    ids.add(uid)
    await _save_admins(ids)
    return True

async def remove_admin(uid: int) -> bool:
    ids = _get_admin_ids()
    if uid not in ids:
        return False
    ids.discard(uid)
    await _save_admins(ids)
    return True

async def validate_token(token: str):
    if not token:
        return False, None
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(10.0, connect=5.0)) as client:
            r = await client.get(f"https://api.telegram.org/bot{token}/getMe")
            data = r.json()
            if data.get("ok"):
                return True, data["result"].get("username")
            return False, None
    except Exception as e:
        logger.warning(f"Telegram validate_token failed: {e}")
        return False, None

def is_running() -> bool:
    return bool(_running and _poll_task and not _poll_task.done())

def _api_base() -> str:
    return f"https://api.telegram.org/bot{_get_token()}"

# ═══════════════════════════════════════════════════════════════════════════
#  GLOBALS
# ═══════════════════════════════════════════════════════════════════════════
PAGE_SIZE = 6
SEARCH_PAGE_SIZE = 8

_client: httpx.AsyncClient | None = None
_poll_task: asyncio.Task | None = None
_notify_task: asyncio.Task | None = None
_report_task: asyncio.Task | None = None
_traffic_task: asyncio.Task | None = None
_running = False
_pending: dict = {}          # chat_id -> wizard/edit state
_notified: dict = {}         # uid -> {"expiry": unix_ts, "quota": unix_ts}
_bot_username: str = ""      # for inline mode
_default_report_time = "09:00"   # ساعت گزارش روزانه
_report_last_sent_date = ""      # YYYY-MM-DD

# ═══════════════════════════════════════════════════════════════════════════
#  BILINGUAL TELEGRAM UI · English is the canonical source language
# ═══════════════════════════════════════════════════════════════════════════
_DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
_LANG_FILE = _DATA_DIR / "telegram_languages.json"
_user_languages: dict[int, str] = {}
_lang_lock = asyncio.Lock()
_callback_chats: dict[str, int] = {}

# Persistent traffic history for the Telegram chart.
# main.hourly_traffic is kept in-memory and uses only HH:00 keys, so it disappears
# on restart and cannot distinguish the same hour across different days.
_TRAFFIC_HISTORY_FILE = _DATA_DIR / "telegram_traffic_history.json"
_TRAFFIC_HISTORY: dict[str, int] = {}  # YYYY-MM-DD HH:00 -> bytes
_TRAFFIC_LAST_TOTAL: int | None = None
_TRAFFIC_LOCK = asyncio.Lock()
_TRAFFIC_SAMPLE_INTERVAL = 15
_TRAFFIC_RETENTION_HOURS = 72

# Persian -> English map. Persian remains the canonical text in this legacy
# source file; outbound messages/keyboards are translated at the last mile.
# Long phrases are intentionally listed before short tokens.
_FA_EN = {
    "ذخیره‌\u200cی ادمین‌\u200cهای جدید توی main.TELEGRAM + save_state.": "Save new admins to main.TELEGRAM + save_state.",
    "جمع ترافیک ساعت‌\u200cهای داده‌شده.": "Sum traffic for the selected hours.",
    "URL عکس نمودار از quickchart.io.": "Chart image URL from quickchart.io.",
    "♾ نامحدود": "♾ Unlimited",
    "Inline mode: کاربر @bot name رو تایپ می‌\u200cکنه، لیست کانفیگ‌ها برمی‌گرده.": "Inline mode: type @bot name to return the configuration list.",
    "هر ۱ ساعت چک می‌\u200cکنه: انقضا نزدیک، اتمام حجم.": "Checks every hour for upcoming expiry and quota exhaustion.",
    "هر ساعت چک می‌\u200cکنه، اگه ساعت گزارش رسیده بود یه گزارش کامل می‌فرسته.": "Checks hourly and sends the scheduled report when the report time is reached.",
    "🟢 فعال": "🟢 Active",
    "🔴 غیرفعال/منقضی": "🔴 Disabled/Expired",
    "نامحدود": "Unlimited",
    "بدون انقضا": "No expiry",
    "وضعیت: ": "Status: ",
    "مصرف: ": "Usage: ",
    "سرعت: ": "Speed: ",
    "آی‌\u200cپی: ": "IP limit: ",
    "پروتکل: ": "Protocol: ",
    "پورت: ": "Port: ",
    "انقضا: ": "Expiry: ",
    "🔒 دارد": "🔒 Yes",
    "بدون رمز": "No password",
    "ساب": "Sub",
    "توضیحات: ": "Description: ",
    "کانفیگ‌\u200cها: ": "Configurations: ",
    "رمز: ": "Password: ",
    "ساب حرفه‌\u200cای:": "Premium subscription:",
    "لینک ساب خام:": "Raw subscription link:",
    "» توی هیچ گروهی نیست.\nبرای داشتن لینک ساب حرفه‌\u200cای، یه گروه انتخاب کن:": "» is not in a group.\nChoose a group to create a premium subscription link:",
    "🧩 ساخت کانفیگ — ": "🧩 Create Configuration — ",
    "✏️ اسم کانفیگ:": "✏️ Configuration name:",
    "🌐 خانواده پروتکل:": "🌐 Protocol family:",
    "🚚 ترنسپورت:": "🚚 Transport:",
    "🔤 ALPN (یا تایپ کن):": "🔤 ALPN (or type it):",
    "📦 حجم: مثلاً <code>10GB</code> یا <code>500MB</code>": "📦 Traffic: e.g. <code>10GB</code> or <code>500MB</code>",
    "🚀 سرعت (Mbps): مثلاً <code>20</code>": "🚀 Speed (Mbps): e.g. <code>20</code>",
    "👥 حداکثر آی‌\u200cپی:": "👥 Maximum IPs:",
    "📅 تعداد روز اعتبار:": "📅 Validity in days:",
    "پیش‌\u200cفرض": "Default",
    "🧩 خلاصه — تایید کن:\n\nبرچسب: <b>": "🧩 Summary — confirm:\n\nLabel: <b>",
    "حجم: ": "Traffic: ",
    "انقضا: ": "Expiry: ",
    "📊 <b>آمار سیستم</b>\n": "📊 <b>System Statistics</b>\n",
    "🔌 اتصالات فعال: <b>": "🔌 Active connections: <b>",
    "📡 ترافیک امروز: <b>": "📡 Today's traffic: <b>",
    "📡 کل ترافیک عبوری: <b>": "📡 Total traffic: <b>",
    "📦 مجموع مصرف کانفیگ‌\u200cها: <b>": "📦 Total configuration usage: <b>",
    "🗂 کل: <b>": "🗂 Total: <b>",
    "✅ فعال: <b>": "✅ Active: <b>",
    "⏰ منقضی: <b>": "⏰ Expired: <b>",
    "❌ غیرفعال: <b>": "❌ Disabled: <b>",
    "👥 گروه‌\u200cها: <b>": "👥 Groups: <b>",
    "⏱ آپتایم: <b>": "⏱ Uptime: <b>",
    "» توی گروه «": "» is in group «",
    "» هست.\n\n🔗 ": "» is in it.\n\n🔗 ",
    "🔌 پورت (": "🔌 Port (",
    " روز": " days",
    "از دکمه‌\u200cها استفاده کن:": "Use the buttons below:",
    "📋 <b>آخرین رخدادها:</b>\n": "📋 <b>Recent activity:</b>\n",
    "🏆 <b>TOP 10 مصرف‌\u200cکننده:</b>\n": "🏆 <b>TOP 10 Consumers:</b>\n",
    "\nدرصد: <b>": "\nPercentage: <b>",
    "\n\nاتصالات فعال: <b>": "\n\nActive connections: <b>",
    "\nآی‌\u200cپی‌\u200cهای یکتا: <b>": "\nUnique IPs: <b>",
    "\nسقف آی‌\u200cپی: <b>": "\nIP limit: <b>",
    "👥 <b>ادمین‌\u200cهای فعلی (": "👥 <b>Current Admins (",
    "پیدا نشد.": "not found.",
    "Telegram bot: توکن تنظیم نشده — غیرفعاله.": "Telegram bot: token is not configured — disabled.",
    "Telegram bot: TELEGRAM_ADMIN_IDS خالیه — کسی نمی‌\u200cتونه مدیریت کنه.": "Telegram bot: TELEGRAM_ADMIN_IDS is empty — nobody can manage the bot.",
    "◀ قبلی": "◀ Previous",
    "بعدی ▶": "Next ▶",
    "➕ کانفیگ جدید": "➕ New Config",
    "🔍 جستجو": "🔍 Search",
    "⬅ منو": "⬅ Menu",
    "⬅ بازگشت": "⬅ Back",
    "➕ گروه جدید": "➕ New Group",
    "🆕 ساخت گروه جدید + افزودن": "🆕 Create New Group + Add",
    "❌ انصراف": "❌ Cancel",
    "⬅ خانواده پروتکل": "⬅ Protocol Family",
    " روز)": " days)",
    "👋 منوی مدیریت:": "👋 Admin Menu:",
    "لغو شد.": "Cancelled.",
    "📚 <b>راهنما</b>\n\n/start یا /menu — منوی اصلی\n/cancel — لغو عملیات\n/id — نمایش آیدی تلگرام شما\n/stats — آمار سریع\n/export — دانلود بکاپ\n\nهمه‌\u200cی قابلیت‌\u200cها از طریق دکمه‌\u200cها در دسترسه.": "📚 <b>Help</b>\n\n/start or /menu — main menu\n/cancel — cancel the current operation\n/id — show your Telegram ID\n/stats — quick statistics\n/export — download backup\n\nAll features are available through the buttons.",
    "💾 پشتیبان کامل": "💾 Full Backup",
    "کانفیگ": "config",
    "⚠️ فقط فایل JSON قبول می‌\u200cشه.": "⚠️ Only JSON files are accepted.",
    "❌ دانلود فایل نشد.": "❌ Failed to download the file.",
    "❌ ساختار فایل درست نیست.": "❌ Invalid file structure.",
    "📥 <b>فایل بارگذاری شد</b>\n\nکانفیگ‌\u200cها: ": "📥 <b>File uploaded</b>\n\nConfigurations: ",
    "\nگروه‌\u200cها: ": "\nGroups: ",
    "چطور اعمال کنم؟": "How should it be applied?",
    "• <b>افزودن</b>: کانفیگ‌\u200cهای جدید اضافه میشن، هم‌نام‌\u200cها دست‌\u200cنخورده می‌\u200cمونن": "• <b>Add</b>: new configs are added; duplicates are kept unchanged",
    "• <b>جایگزینی</b>: همه‌\u200cچی پاک و از فایل بازسازی می‌\u200cشه": "• <b>Replace</b>: everything is cleared and rebuilt from the file",
    "🌐 سرور: ": "🌐 Server: ",
    "⛔ دسترسی نداری": "⛔ Access denied",
    "🔍 عبارت جستجو رو بفرست\n(اسم، یادداشت، Sub Token یا بخشی از UUID)": "🔍 Send a search term\n(name, note, Sub Token, or part of a UUID)",
    "🏷 فیلتر:": "🏷 Filter:",
    "🔌 اتصالات (": "🔌 Connections (",
    " آی‌\u200cپی)\n": " IPs)\n",
    "📈 نمودار ترافیک ۲۴ ساعت اخیر": "📈 Traffic — Last 24 Hours",
    "📦 مثلاً <code>10GB</code> یا <code>0</code> برای نامحدود:": "📦 e.g. <code>10GB</code> or <code>0</code> for unlimited:",
    "➕ چند روز اضافه بشه؟": "➕ How many days should be added?",
    "📅 تعداد روز (0=بدون انقضا):": "📅 Number of days (0 = no expiry):",
    "🚀 عدد به Mbps (0=نامحدود):": "🚀 Value in Mbps (0 = unlimited):",
    "👥 عدد (0=نامحدود):": "👥 Number (0 = unlimited):",
    "🔤 مقدار ALPN دلخواه (خالی = پیش‌\u200cفرض):": "🔤 Custom ALPN value (empty = default):",
    "✏️ اسم گروه جدید:": "✏️ New group name:",
    "✏️ اسم گروه:": "✏️ Group name:",
    "کدوم کانفیگ؟ (✅ = الان توی گروهه)": "Which config? (✅ = already in the group)",
    "🆔 آیدی عددی ادمین جدید رو بفرست:": "🆔 Send the new admin's numeric ID:",
    "کدوم حذف بشه؟": "Which one should be removed?",
    "💾 <b>پشتیبان‌\u200cگیری</b>\n\n• <b>دانلود پشتیبان</b>: فایل JSON کامل از همه‌\u200cی کانفیگ‌\u200cها و گروه‌\u200cها\n• <b>برگرداندن</b>: فایل JSON رو بفرست تا بازیابی کنم": "💾 <b>Backup</b>\n\n• <b>Download Backup</b>: full JSON of all configs and groups\n• <b>Restore</b>: send a JSON file to restore it",
    "📥 فایل JSON پشتیبان رو بفرست 👇": "📥 Send the backup JSON file 👇",
    "📤 فرمت Export:": "📤 Export format:",
    "🔔 <b>تست نوتیفیکیشن</b>\n\n✅ سیستم اطلاع‌\u200cرسانی فعاله.": "🔔 <b>Notification Test</b>\n\n✅ Notification system is active.",
    "دکمه منقضی شده": "This button has expired.",
    "📋 کانفیگ‌\u200cها": "📋 Configs",
    "🏷 فیلتر": "🏷 Filter",
    "🗂 گروه‌\u200cهای ساب": "🗂 Subscription Groups",
    "📊 آمار": "📊 Statistics",
    "🔌 اتصالات": "🔌 Connections",
    "📈 نمودار ترافیک": "📈 Traffic Chart",
    "🏆 TOP مصرف": "🏆 Top Usage",
    "📋 لاگ‌\u200cها": "📋 Logs",
    "💾 پشتیبان/برگرداندن": "💾 Backup/Restore",
    "👥 ادمین‌\u200cها": "👥 Admins",
    "🔔 تست نوتیفیکیشن": "🔔 Test Notifications",
    "🌐 زبان / Language": "🌐 Language",
    "⬅ Menu / منو": "⬅ Menu",
    "🔄 رفرش": "🔄 Refresh",
    "همه": "All",
    "فعال": "Active",
    "منقضی": "Expired",
    "غیرفعال": "Disabled",
    "بدون گروه": "No Group",
    "دارای گروه": "In Group",
    "🔗 نمایش لینک": "🔗 Show Link",
    "✏️ ویرایش": "✏️ Edit",
    "🔄 ریست مصرف": "🔄 Reset Usage",
    "🗂 گروه ساب": "🗂 Sub Group",
    "📊 آمار کانفیگ": "📊 Config Stats",
    "📤 Export این کانفیگ": "📤 Export This Config",
    "🗑 حذف": "🗑 Delete",
    "⬅ لیست": "⬅ List",
    "✅ بله": "✅ Yes",
    "🏷 نام": "🏷 Name",
    "📦 سهمیه": "📦 Quota",
    "📅 انقضا": "📅 Expiry",
    "🚀 سرعت": "🚀 Speed",
    "👥 آی‌\u200cپی": "👥 IP Limit",
    "🔌 پورت": "🔌 Port",
    "✏️ دلخواه": "✏️ Custom",
    "۷ روز": "7 days",
    "۳۰ روز": "30 days",
    "۹۰ روز": "90 days",
    "۱ روز": "1 day",
    "۱۸۰ روز": "180 days",
    "۳۶۵ روز": "365 days",
    "♾ بدون انقضا": "♾ No Expiry",
    "➕ تمدید (افزودن روز)": "➕ Extend (Add Days)",
    "۱ Mbps": "1 Mbps",
    "۵ Mbps": "5 Mbps",
    "۱۰ Mbps": "10 Mbps",
    "۲۰ Mbps": "20 Mbps",
    "۵۰ Mbps": "50 Mbps",
    "۱۰۰ Mbps": "100 Mbps",
    "⏭ پیش‌\u200cفرض پروتکل": "⏭ Protocol Default",
    "➕ افزودن کانفیگ": "➕ Add Config",
    "🔗 نمایش لینک حرفه‌\u200cای": "🔗 Show Premium Link",
    "🗑 حذف گروه": "🗑 Delete Group",
    "➕ افزودن ادمین": "➕ Add Admin",
    "➖ حذف ادمین": "➖ Remove Admin",
    "💾 دانلود پشتیبان (JSON)": "💾 Download Backup (JSON)",
    "📥 برگرداندن از فایل": "📥 Restore From File",
    "📃 لیست متنی لینک‌\u200cها": "📃 Text List of Links",
    "⏭ پیش‌\u200cفرض": "⏭ Default",
    "✅ ساخت کانفیگ": "✅ Create Config",
    "آیدی شما: <code>": "Your ID: <code>",
    " نتیجه:": " results:",
    "کانفیگ حذف شده.": "The config was deleted.",
    "✅ تغییر اعمال شد.\n\n": "✅ Changes applied.\n\n",
    "از دکمه‌\u200cها 👆": "Use the buttons above 👆",
    "هنوز کانفیگی نیست.": "No configurations yet.",
    "📋 کانفیگ‌\u200cها (": "📋 Configs (",
    "چیزی با این فیلتر نیست.": "Nothing matches this filter.",
    " مورد:": " items:",
    "امروز": "Today",
    "این هفته": "This Week",
    "این ماه": "This Month",
    "📊 ترافیک ": "📊 Traffic ",
    "🔌 اتصالی نیست.": "🔌 No active connections.",
    " سشن": " sessions",
    "\n<i>... و ": "\n<i>... and ",
    " مورد</i>": " more</i>",
    "📋 لاگی نیست.": "📋 No logs.",
    "📈 داده‌\u200cای برای نمودار نیست.": "📈 No chart data available.",
    "کانفیگی نیست.": "No configuration.",
    "پیدا نشد": "Not found",
    "❗️ حذف «": "❗️ Delete «",
    "»؟": "»?",
    "قبلاً حذف شده.": "It was already deleted.",
    "🔄 مصرف فعلی: <b>": "🔄 Current usage: <b>",
    "</b>\nمطمئنی؟": "</b>\nAre you sure?",
    "✅ ریست شد.\n\n": "✅ Reset.\n\n",
    "✏️ ویرایش «": "✏️ Edit «",
    "🏷 نام فعلی: <b>": "🏷 Current name: <b>",
    "</b>\nنام جدید:": "</b>\nNew name:",
    "📦 فعلی: <b>": "📦 Current: <b>",
    "</b>\nجدید:": "</b>\nNew:",
    "✅ اعمال شد.\n\n": "✅ Applied.\n\n",
    "📅 فعلی: <b>": "📅 Current: <b>",
    "🚀 فعلی: <b>": "🚀 Current: <b>",
    "👥 فعلی: <b>": "👥 Current: <b>",
    "🌐 پروتکل فعلی: <b>": "🌐 Current protocol: <b>",
    "</b>\n\nخانواده جدید رو انتخاب کن:": "</b>\n\nChoose the new family:",
    "</b>\n\nترنسپورت رو انتخاب کن:": "</b>\n\nChoose the new transport:",
    "پروتکل نامعتبر": "Invalid protocol",
    "✅ پروتکل تغییر کرد.\n\n": "✅ Protocol changed.\n\n",
    "🔑 Sub Token فعلی: <code>": "🔑 Current Sub Token: <code>",
    "</code>\n\nجدید (۳ تا ۳۲ حرف، فقط a-z A-Z 0-9 _ -):\nبرای پاک کردن، <code>-</code> بفرست.": "</code>\n\nNew value (3–32 chars, only a-z A-Z 0-9 _ -):\nSend <code>-</code> to clear it.",
    "🎭 فعلی: <b>": "🎭 Current: <b>",
    "🔤 فعلی: <b>": "🔤 Current: <b>",
    "🔌 فعلی: <b>": "🔌 Current: <b>",
    "منقضی شده": "Expired",
    "گروه نیست": "No group",
    "✅ اضافه شد.\n\n": "✅ Added.\n\n",
    "هنوز گروهی نیست.": "No groups yet.",
    " گروه:": " groups:",
    "🔗 <b>لینک ساب حرفه‌\u200cای «": "🔗 <b>Premium Subscription «",
    "»</b>\n\nصفحه‌\u200cی پابلیک:\n<code>": "»</b>\n\nPublic page:\n<code>",
    "</code>\n\nلینک ساب خام:\n<code>": "</code>\n\nRaw subscription link:\n<code>",
    "📷 ساب «": "📷 Sub «",
    "کانفیگ نیست": "No configuration",
    "❗️ حذف گروه «": "❗️ Delete group «",
    "»؟\n(کانفیگ‌\u200cها حذف نمی‌شن، فقط از گروه خارج می‌شن)": "»?\n(Configs are not deleted; they are only removed from the group.)",
    "ادمینی نیست.": "No admins.",
    "خودت رو نمی‌\u200cتونی حذف کنی!": "You cannot remove yourself!",
    "✅ بازیابی انجام شد.\n\nافزوده‌\u200cشده: <b>": "✅ Restore completed.\n\nAdded: <b>",
    "</b>\nرد‌\u200cشده (تکراری): <b>": "</b>\nSkipped (duplicate): <b>",
    "</b>\nکل الان: <b>": "</b>\nCurrent total: <b>",
    "📃 لینک‌\u200cها": "📃 Links",
    "🔔 نوتیفیکیشن‌\u200cها فعالن:\n\n• انقضا: ۲۴ ساعت قبل\n• اتمام حجم: بلافاصله بعد از رسیدن به سقف\n• بررسی: هر ۱ ساعت": "🔔 Notifications enabled:\n\n• Expiry: 24 hours before\n• Quota: immediately after reaching the limit\n• Check interval: every hour",
    "این مرحله منقضی شده.": "This step has expired.",
    "📅 <b>گزارش روزانه ": "📅 <b>Daily Report ",
    "⛔ غیرفعال": "⛔ Disabled",
    "✅ فعال": "✅ Active",
    "➖ خروج از گروه": "➖ Remove From Group",
    "⛔ شما ادمین نیستید.\nآیدی تلگرام شما: <code>": "⛔ You are not an admin.\nYour Telegram ID: <code>",
    "</code>\nاز ادمین اصلی بخواید این آیدی رو اضافه کنه.": "</code>\nAsk the main admin to add this ID.",
    "🔍 نتیجه‌\u200cای برای «": "🔍 No result for «",
    "» پیدا نشد.": "» was found.",
    "✅ گروه ساخته و کانفیگ اضافه شد.\n\n": "✅ Group created and config added.\n\n",
    "✅ گروه ساخته شد.\n\n": "✅ Group created.\n\n",
    "❗️ فرمت: <code>10GB</code> یا <code>500MB</code>": "❗️ Format: <code>10GB</code> or <code>500MB</code>",
    "❗️ عدد (Mbps):": "❗️ Number (Mbps):",
    "❗️ عدد صحیح:": "❗️ Integer required:",
    "❗️ عدد صحیح (روز):": "❗️ Integer required (days):",
    "❌ JSON نامعتبر: ": "❌ Invalid JSON: ",
    "✅ افزودن ": "✅ Add ",
    " کانفیگ": " config(s)",
    "🔄 جایگزینی کامل": "🔄 Full Replace",
    "📅 امروز": "📅 Today",
    "📆 هفته": "📆 Week",
    "🗓 ماه": "🗓 Month",
    "🔄 بروزرسانی": "🔄 Refresh",
    "» حذف شد.": "» deleted.",
    "آیدی نامعتبر": "Invalid ID",
    "📃 <b>لینک‌\u200cها:</b>\n\n<code>": "📃 <b>Links:</b>\n\n<code>",
    "✅ ساخته شد.\n\n": "✅ Created.\n\n",
    "🚫 کانفیگ «": "🚫 Config «",
    "» به سقف حجم رسید!\nمصرف: ": "» reached its quota limit!\nUsage: ",
    "❌ خطا: ": "❌ Error: ",
    "⏭ پیش‌\u200cفرض (": "⏭ Default (",
    "❗️ پورت ": "❗️ Port ",
    "🔔 ارسال تست": "🔔 Send Test",
    "📋 کپی": "📋 Copy",
    "⚠️ کانفیگ «": "⚠️ Config «",
    "» تا ": "» expires in ",
    " ساعت دیگه منقضی می‌\u200cشه!": " hours!",
    "❗️ یه عدد صحیح:": "❗️ Enter an integer:",
    "❗️ عدد مثبت:": "❗️ Enter a positive number:",
    "❗️ عدد به Mbps:": "❗️ Enter a value in Mbps:",
    "❗️ فقط حروف/عدد/-/_ (۳ تا ۳۲ کاراکتر)": "❗️ Only letters/numbers/-/_ (3–32 characters)",
    "» قبلاً استفاده شده": "» is already in use",
    "فیلد ناشناخته.": "Unknown field.",
    "❗️ پورت بین ": "❗️ Port must be between ",
    "❗️ آیدی عددی بفرست:": "❗️ Send a numeric ID:",
    "✅ ادمین <code>": "✅ Admin <code>",
    "</code> اضافه شد.": "</code> added.",
    "</code> از قبل ادمین بود.": "</code> was already an admin.",
}

# Extra compact replacements for common Persian words/labels that can occur
# inside dynamic strings. Longest replacements above run first.

_FA_EN.update({
    "ذخیره‌\u200cی ادمین‌\u200cهای جدید توی main.TELEGRAM + save_state.": "Save new admins to main.TELEGRAM + save_state.",
    "جمع ترافیک ساعت‌\u200cهای داده‌\u200cشده.": "Sum traffic for the selected hours.",
    "Inline mode: کاربر @bot name رو تایپ می‌\u200cکنه، لیست کانفیگ‌\u200cها برمی‌\u200cگرده.": "Inline mode: type @bot name to return the configuration list.",
    "هر ۱ ساعت چک می‌\u200cکنه: انقضا نزدیک، اتمام حجم.": "Checks every hour for upcoming expiry and quota exhaustion.",
    "هر ساعت چک می‌\u200cکنه، اگه ساعت گزارش رسیده بود یه گزارش کامل می‌\u200cفرسته.": "Checks hourly and sends the full report when the scheduled time is reached.",
    "\nآی‌\u200cپی: ": "\nIP limit: ",
    "\n\n🔗 ساب حرفه‌\u200cای:\n<code>": "\n\n🔗 Premium subscription:\n<code>",
    "» توی هیچ گروهی نیست.\nبرای داشتن لینک ساب حرفه‌\u200cای، یه گروه انتخاب کن:": "» is not in any group.\nChoose a group to create a premium subscription link:",
    "👥 حداکثر آی‌\u200cپی:": "👥 Maximum IPs:",
    "</b>\n📦 مجموع مصرف کانفیگ‌\u200cها: <b>": "</b>\n📦 Total configuration usage: <b>",
    "از دکمه‌\u200cها استفاده کن:": "Use the buttons below:",
    "</b>\nآی‌\u200cپی‌\u200cهای یکتا: <b>": "</b>\nUnique IPs: <b>",
    "</b>\nسقف آی‌\u200cپی: <b>": "</b>\nIP limit: <b>",
    "👥 <b>ادمین‌\u200cهای فعلی (": "👥 <b>Current Admins (",
    "Telegram bot: TELEGRAM_ADMIN_IDS خالیه — کسی نمی‌\u200cتونه مدیریت کنه.": "Telegram bot: TELEGRAM_ADMIN_IDS is empty — nobody can manage the bot.",
    "📚 <b>راهنما</b>\n\n/start یا /menu — منوی اصلی\n/cancel — لغو عملیات\n/id — نمایش آیدی تلگرام شما\n/stats — آمار سریع\n/export — دانلود بکاپ\n\nهمه‌\u200cی قابلیت‌\u200cها از طریق دکمه‌\u200cها در دسترسه.": "📚 <b>Help</b>\n\n/start or /menu — main menu\n/cancel — cancel the current operation\n/id — show your Telegram ID\n/stats — quick statistics\n/export — download backup\n\nAll features are available through the buttons.",
    "⚠️ فقط فایل JSON قبول می‌\u200cشه.": "⚠️ Only JSON files are accepted.",
    "📥 <b>فایل بارگذاری شد</b>\n\nکانفیگ‌\u200cها: ": "📥 <b>File uploaded</b>\n\nConfigurations: ",
    "\n\nچطور اعمال کنم؟\n• <b>افزودن</b>: کانفیگ‌\u200cهای جدید اضافه میشن، هم‌نام‌\u200cها دست‌\u200cنخورده می‌\u200cمونن\n• <b>جایگزینی</b>: همه‌\u200cچی پاک و از فایل بازسازی می‌\u200cشه": "\n\nHow should it be applied?\n• <b>Add</b>: new configs are added; duplicates stay unchanged\n• <b>Replace</b>: everything is cleared and rebuilt from the file",
    " آی‌\u200cپی)\n": " IPs)\n",
    "🔤 مقدار ALPN دلخواه (خالی = پیش‌\u200cفرض):": "🔤 Custom ALPN value (empty = default):",
    "</code> حذف شد.\n\n👥 <b>ادمین‌\u200cهای فعلی:</b>\n": "</code> deleted.\n\n👥 <b>Current Admins:</b>\n",
    "💾 <b>پشتیبان‌\u200cگیری</b>\n\n• <b>دانلود پشتیبان</b>: فایل JSON کامل از همه‌\u200cی کانفیگ‌\u200cها و گروه‌\u200cها\n• <b>برگرداندن</b>: فایل JSON رو بفرست تا بازیابی کنم": "💾 <b>Backup</b>\n\n• <b>Download Backup</b>: full JSON of all configs and groups\n• <b>Restore</b>: send a JSON file to restore it",
    "🔔 <b>تست نوتیفیکیشن</b>\n\n✅ سیستم اطلاع‌\u200cرسانی فعاله.": "🔔 <b>Notification Test</b>\n\n✅ Notification system is active.",
    "🗂 گروه‌\u200cهای ساب": "🗂 Subscription Groups",
    "📋 لاگ‌\u200cها": "📋 Logs",
    "👥 ادمین‌\u200cها": "👥 Admins",
    "👥 آی‌\u200cپی": "👥 IP Limit",
    "⏭ پیش‌\u200cفرض پروتکل": "⏭ Protocol Default",
    "🔗 نمایش لینک حرفه‌\u200cای": "🔗 Show Premium Link",
    "📃 لیست متنی لینک‌\u200cها": "📃 Text List of Links",
    "⏭ پیش‌\u200cفرض": "⏭ Default",
    "از دکمه‌\u200cها 👆": "Use the buttons above 👆",
    "زبان تغییر کرد": "Language changed",
    "📈 داده‌\u200cای برای نمودار نیست.": "📈 No chart data available.",
    "🔗 <b>لینک ساب حرفه‌\u200cای «": "🔗 <b>Premium subscription «",
    "»</b>\n\nصفحه‌\u200cی پابلیک:\n<code>": "»</b>\n\nPublic page:\n<code>",
    "»؟\n(کانفیگ‌\u200cها حذف نمی‌شن، فقط از گروه خارج می‌شن)": "»?\n(Configs are not deleted; they are only removed from the group.)",
    "خودت رو نمی‌\u200cتونی حذف کنی!": "You cannot remove yourself!",
    "✅ بازیابی انجام شد.\n\nافزوده‌\u200cشده: <b>": "✅ Restore completed.\n\nAdded: <b>",
    "</b>\nرد‌\u200cشده (تکراری): <b>": "</b>\nSkipped (duplicate): <b>",
    "📃 لینک‌\u200cها": "📃 Links",
    "🔔 نوتیفیکیشن‌\u200cها فعالن:\n\n• انقضا: ۲۴ ساعت قبل\n• اتمام حجم: بلافاصله بعد از رسیدن به سقف\n• بررسی: هر ۱ ساعت": "🔔 Notifications enabled:\n\n• Expiry: 24 hours before\n• Quota: immediately after reaching the limit\n• Check: every hour",
    "🔍 نتیجه‌\u200cای برای «": "🔍 No result for «",
    "📃 <b>لینک‌\u200cها:</b>\n\n<code>": "📃 <b>Links:</b>\n\n<code>",
    "⏭ پیش‌\u200cفرض (": "⏭ Default (",
    " ساعت دیگه منقضی می‌\u200cشه!": " hours!",
})
_PERSIAN_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")

def _norm_fa(s: str) -> str:
    # Normalize Persian ZWNJ so old/new strings with one or more ZWNJ characters
    # always resolve to the same canonical translation key.
    return str(s).replace("\u200c", "")

_FA_EN_NORM = {_norm_fa(k): v for k, v in _FA_EN.items()}

def _localize_text(text: str, lang: str) -> str:
    if not isinstance(text, str) or lang != "en":
        return text
    out = _norm_fa(text)
    for src in sorted(_FA_EN_NORM, key=len, reverse=True):
        out = out.replace(src, _FA_EN_NORM[src])
    return out.translate(_PERSIAN_DIGITS)


def _localize_kb(obj: dict | None, lang: str):
    if not obj or lang != "en":
        return obj
    def walk(v, key=None):
        if isinstance(v, dict):
            return {k: walk(val, k) for k, val in v.items()}
        if isinstance(v, list):
            return [walk(x, key) for x in v]
        if key in {"text", "caption", "description", "title", "message_text"} and isinstance(v, str):
            return _localize_text(v, lang)
        return v
    return walk(obj)


async def _load_languages():
    global _user_languages
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        if _LANG_FILE.exists():
            data = json.loads(_LANG_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                _user_languages = {int(k): v for k, v in data.items() if v in ("fa", "en")}
    except Exception as e:
        logger.warning(f"Telegram language settings load failed: {e}")


async def _save_languages():
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        tmp = _LANG_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps({str(k): v for k, v in _user_languages.items()}, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(_LANG_FILE)
    except Exception as e:
        logger.warning(f"Telegram language settings save failed: {e}")


def _get_lang(chat_id: int | None) -> str | None:
    return _user_languages.get(int(chat_id)) if chat_id is not None else None


async def _set_lang(chat_id: int, lang: str):
    if lang not in ("fa", "en"):
        return
    _user_languages[int(chat_id)] = lang
    await _save_languages()


def _language_choice_kb(back_to_menu: bool = False):
    rows = [
        [{"text": "🇬🇧 English", "callback_data": "setlang:en"},
         {"text": "🇮🇷 فارسی", "callback_data": "setlang:fa"}],
    ]
    if back_to_menu:
        rows.append([{"text": "⬅ Menu / منو", "callback_data": "menu"}])
    return {"inline_keyboard": rows}


def _language_choice_text():
    return "🌐 <b>Choose your language</b>\n\nSelect the language for this bot:"

# ═══════════════════════════════════════════════════════════════════════════
#  PERSISTENT TRAFFIC HISTORY
# ═══════════════════════════════════════════════════════════════════════════
def _traffic_hour_key(dt: datetime | None = None) -> str:
    dt = dt or datetime.now()
    return dt.strftime("%Y-%m-%d %H:00")


def _traffic_prune_unlocked() -> None:
    cutoff = datetime.now() - timedelta(hours=_TRAFFIC_RETENTION_HOURS)
    keep = {}
    for key, value in _TRAFFIC_HISTORY.items():
        try:
            dt = datetime.strptime(key, "%Y-%m-%d %H:%M")
        except ValueError:
            continue
        if dt >= cutoff:
            keep[key] = max(0, int(value or 0))
    _TRAFFIC_HISTORY.clear()
    _TRAFFIC_HISTORY.update(keep)


async def _load_traffic_history() -> None:
    global _TRAFFIC_LAST_TOTAL
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        if _TRAFFIC_HISTORY_FILE.exists():
            raw = json.loads(_TRAFFIC_HISTORY_FILE.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                source = raw.get("hours", raw)
                if isinstance(source, dict):
                    async with _TRAFFIC_LOCK:
                        _TRAFFIC_HISTORY.clear()
                        for key, value in source.items():
                            try:
                                _TRAFFIC_HISTORY[str(key)] = max(0, int(value or 0))
                            except (TypeError, ValueError):
                                pass
                        _traffic_prune_unlocked()
        _TRAFFIC_LAST_TOTAL = int(stats.get("total_bytes", 0) or 0)
    except Exception as e:
        logger.warning(f"Telegram traffic history load failed: {e}")
        _TRAFFIC_LAST_TOTAL = int(stats.get("total_bytes", 0) or 0)


async def _save_traffic_history() -> None:
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        async with _TRAFFIC_LOCK:
            _traffic_prune_unlocked()
            payload = {
                "version": 1,
                "hours": dict(sorted(_TRAFFIC_HISTORY.items())),
                "saved_at": datetime.now().isoformat(),
            }
        tmp = _TRAFFIC_HISTORY_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(_TRAFFIC_HISTORY_FILE)
    except Exception as e:
        logger.warning(f"Telegram traffic history save failed: {e}")


async def _traffic_history_loop() -> None:
    """Persist real relay traffic from main.stats into date-aware hourly buckets."""
    global _TRAFFIC_LAST_TOTAL
    while _running:
        try:
            current_total = int(stats.get("total_bytes", 0) or 0)
            hour_key = _traffic_hour_key()

            async with _TRAFFIC_LOCK:
                # main.hourly_traffic may already contain the current hour.
                # Seed from it once so starting the bot after traffic has begun
                # does not show an empty chart.
                source_current = int(hourly_traffic.get(datetime.now().strftime("%H:00"), 0) or 0)
                existing = int(_TRAFFIC_HISTORY.get(hour_key, 0) or 0)
                if source_current > existing:
                    _TRAFFIC_HISTORY[hour_key] = source_current
                else:
                    _TRAFFIC_HISTORY.setdefault(hour_key, existing)

                if _TRAFFIC_LAST_TOTAL is None:
                    _TRAFFIC_LAST_TOTAL = current_total
                elif current_total >= _TRAFFIC_LAST_TOTAL:
                    delta = current_total - _TRAFFIC_LAST_TOTAL
                    if delta:
                        _TRAFFIC_HISTORY[hour_key] = int(_TRAFFIC_HISTORY.get(hour_key, 0)) + delta
                    _TRAFFIC_LAST_TOTAL = current_total
                else:
                    # Main process restarted/reset its counter. Do not create
                    # a huge negative/positive spike; just re-baseline.
                    _TRAFFIC_LAST_TOTAL = current_total

                _traffic_prune_unlocked()

            await _save_traffic_history()
            await asyncio.sleep(_TRAFFIC_SAMPLE_INTERVAL)
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.warning(f"traffic history loop error: {e}")
            await asyncio.sleep(_TRAFFIC_SAMPLE_INTERVAL)


def _traffic_chart_points(hours: int = 24) -> tuple[list[str], list[int]]:
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    labels = []
    values = []
    for offset in range(hours - 1, -1, -1):
        dt = now - timedelta(hours=offset)
        key = dt.strftime("%Y-%m-%d %H:00")
        labels.append(dt.strftime("%m-%d %H:00"))
        values.append(int(_TRAFFIC_HISTORY.get(key, 0) or 0))
    return labels, values


# ═══════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════
WIZARD_STEPS = ["label", "protocol", "transport", "fingerprint", "alpn", "port", "volume", "speed", "iplimit", "days"]

PROTOCOL_LABELS = {
    "vless-ws": "VLESS + WebSocket",
    "vless-xhttp-packet-up": "VLESS + XHTTP · packet-up",
    "vless-xhttp-stream-up": "VLESS + XHTTP · stream-up",
    "vmess-ws": "VMess + WebSocket",
    "vmess-xhttp-packet-up": "VMess + XHTTP · packet-up",
    "vmess-xhttp-stream-up": "VMess + XHTTP · stream-up",
    "trojan-ws": "Trojan + WebSocket",
    "trojan-xhttp-packet-up": "Trojan + XHTTP · packet-up",
    "trojan-xhttp-stream-up": "Trojan + XHTTP · stream-up",
}

PROTOCOL_FAMILY_LABELS = {
    "vless": "🔵 VLESS",
    "vmess": "🟣 VMess",
    "trojan": "🟠 Trojan",
}

TRANSPORT_LABELS = {
    "ws": "🌐 WebSocket",
    "packet-up": "⚡ XHTTP · packet-up",
    "stream-up": "🚀 XHTTP · stream-up",
}
ALPN_PRESET_MAP = {"p1": "http/1.1", "p2": "h2,http/1.1", "p3": "h2"}
_VOLUME_RE = re.compile(r"^([\d.]+)\s*(GB|MB|KB)?$", re.IGNORECASE)
_SPEED_RE = re.compile(r"^([\d.]+)\s*(MBIT|MBPS|MB|KB)?$", re.IGNORECASE)

def _protocol_label(p):
    p = normalize_protocol(p)
    return PROTOCOL_LABELS.get(p, p)
def _fp_label(fp): return fp.capitalize()

def _parse_volume_text(text):
    m = _VOLUME_RE.match(text.strip())
    if not m: return None
    try: v = float(m.group(1))
    except ValueError: return None
    if v <= 0: return 0
    return parse_size_to_bytes(v, (m.group(2) or "GB").upper())

def _parse_speed_text(text):
    m = _SPEED_RE.match(text.strip())
    if not m: return None
    try: v = float(m.group(1))
    except ValueError: return None
    if v <= 0: return 0
    u = (m.group(2) or "MBIT").upper()
    return parse_speed_to_bytes(v, "MBIT" if u in ("MBIT","MBPS") else u)

def _parse_nonneg_int(text):
    try: return max(0, int(text.strip()))
    except ValueError: return None

def _sum_hourly(period_hours: list[str]) -> int:
    """جمع ترافیک ساعت‌های داده‌شده."""
    return sum(hourly_traffic.get(h, 0) for h in period_hours)

def _hours_today() -> list[str]:
    now = datetime.now()
    return [f"{h:02d}:00" for h in range(0, now.hour + 1)]

def _hours_this_week() -> list[str]:
    now = datetime.now()
    wd = now.weekday()  # 0=Mon
    days = [now - timedelta(days=i) for i in range(wd + 1)]
    # این approximation هست چون hourly_traffic فقط بر اساس ساعت‌ها ذخیره شده
    return [f"{h:02d}:00" for h in range(24)]

def _hours_this_month() -> list[str]:
    return [f"{h:02d}:00" for h in range(24)]

def _link_sub_url(l: dict, uid: str) -> str:
    host = get_host()
    slug = (l.get("sub_token") or "").strip() or uid
    return f"https://{host}/sub/{slug}"

def _group_public_url(s: dict) -> str:
    return f"https://{get_host()}/p/{s.get('uuid_key','')}"

def _group_sub_url(s: dict) -> str:
    return f"https://{get_host()}/sub-group/{s.get('uuid_key','')}"

def _quickchart_url(config: dict, w=900, h=400) -> str:
    """URL عکس نمودار از quickchart.io."""
    import urllib.parse
    c = json.dumps(config, separators=(",", ":"))
    return f"https://quickchart.io/chart?c={urllib.parse.quote(c)}&w={w}&h={h}&bkg=white&devicePixelRatio=2"

# ═══════════════════════════════════════════════════════════════════════════
#  TELEGRAM API HELPERS
# ═══════════════════════════════════════════════════════════════════════════
async def _call(method: str, **params):
    if _client is None: return None
    try:
        r = await _client.post(f"{_api_base()}/{method}", json=params, timeout=40)
        data = r.json()
        if not data.get("ok"):
            logger.warning(f"Telegram API {method} failed: {data}")
        return data
    except Exception as e:
        logger.warning(f"Telegram API {method} error: {e}")
        return None

async def _send(chat_id: int, text: str, kb: dict | None = None):
    lang = _get_lang(chat_id) or "en"
    payload = {"chat_id": chat_id, "text": _localize_text(text, lang), "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb: payload["reply_markup"] = _localize_kb(kb, lang)
    return await _call("sendMessage", **payload)

async def _edit(chat_id: int, message_id: int, text: str, kb: dict | None = None):
    lang = _get_lang(chat_id) or "en"
    payload = {"chat_id": chat_id, "message_id": message_id, "text": _localize_text(text, lang),
               "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb: payload["reply_markup"] = _localize_kb(kb, lang)
    res = await _call("editMessageText", **payload)
    if res is None or not res.get("ok"):
        await _send(chat_id, text, kb)

async def _answer_cb(cb_id: str, text: str = "", alert: bool = False):
    chat_id = _callback_chats.get(cb_id)
    lang = _get_lang(chat_id) or "en"
    await _call("answerCallbackQuery", callback_query_id=cb_id, text=_localize_text(text, lang), show_alert=alert)

async def _send_photo(chat_id: int, photo_url: str, caption: str = "", kb: dict | None = None):
    lang = _get_lang(chat_id) or "en"
    payload = {"chat_id": chat_id, "photo": photo_url, "parse_mode": "HTML"}
    if caption: payload["caption"] = _localize_text(caption, lang)
    if kb: payload["reply_markup"] = _localize_kb(kb, lang)
    return await _call("sendPhoto", **payload)


async def _send_photo_bytes(chat_id: int, filename: str, content: bytes, caption: str = "", kb: dict | None = None):
    """Send an in-memory PNG to Telegram (used for the panel-style QR)."""
    if _client is None:
        return None
    try:
        lang = _get_lang(chat_id) or "en"
        data = {"chat_id": str(chat_id), "parse_mode": "HTML"}
        if caption:
            data["caption"] = _localize_text(caption, lang)
        if kb:
            data["reply_markup"] = json.dumps(_localize_kb(kb, lang), ensure_ascii=False, separators=(",", ":"))
        files = {"photo": (filename, content, "image/png")}
        r = await _client.post(f"{_api_base()}/sendPhoto", data=data, files=files, timeout=60)
        result = r.json()
        if not result.get("ok"):
            logger.warning(f"sendPhoto(bytes) failed: {result}")
        return result
    except Exception as e:
        logger.warning(f"sendPhoto(bytes) error: {e}")
        return None


def _build_styled_qr_png(data: str, size: int = 560) -> bytes:
    """Build a Telegram-friendly QR close to the OMID web-panel style.

    Scanner safety is prioritized over exact visual parity:
    the three finder patterns stay structurally standard, while the data
    modules use rounded blue->purple styling like the web panel.
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    n = len(matrix)

    supersample = 3
    work = size * supersample
    quiet = max(24, int(size * 0.055)) * supersample
    usable = work - 2 * quiet
    cell = usable / n

    img = Image.new("RGB", (work, work), "white")
    draw = ImageDraw.Draw(img)

    c0 = (74, 144, 255)   # #4a90ff
    c1 = (176, 38, 255)   # #b026ff

    def color_at(x: float, y: float):
        t = max(0.0, min(1.0, (x + y) / (work * 1.42)))
        return tuple(round(c0[i] * (1.0 - t) + c1[i] * t) for i in range(3))

    def in_finder(row: int, col: int) -> bool:
        return (
            (row < 7 and col < 7)
            or (row < 7 and col >= n - 7)
            or (row >= n - 7 and col < 7)
        )

    # Standard finder patterns: keep their exact 7x7 structure for scanners.
    # They still use the same blue->purple gradient as the panel.
    for row, line in enumerate(matrix):
        for col, dark in enumerate(line):
            if not dark or not in_finder(row, col):
                continue
            x0 = quiet + col * cell
            y0 = quiet + row * cell
            x1 = quiet + (col + 1) * cell
            y1 = quiet + (row + 1) * cell
            draw.rectangle((x0, y0, x1, y1), fill=color_at((x0 + x1) / 2, (y0 + y1) / 2))

    # Rounded data modules, with a small white separation like QRCodeStyling.
    gap = max(cell * 0.07, 0.9 * supersample)
    radius = max(cell * 0.24, 1.5 * supersample)
    for row, line in enumerate(matrix):
        for col, dark in enumerate(line):
            if not dark or in_finder(row, col):
                continue
            x0 = quiet + col * cell + gap
            y0 = quiet + row * cell + gap
            x1 = quiet + (col + 1) * cell - gap
            y1 = quiet + (row + 1) * cell - gap
            draw.rounded_rectangle(
                (x0, y0, x1, y1),
                radius=radius,
                fill=color_at((x0 + x1) / 2, (y0 + y1) / 2),
            )

    # Smooth edges while keeping the QR modules crisp enough for camera scans.
    img = img.resize((size, size), Image.Resampling.LANCZOS)

    out = io.BytesIO()
    img.save(out, format="PNG", optimize=True)
    return out.getvalue()

async def _send_document(chat_id: int, filename: str, content: bytes, caption: str = ""):
    if _client is None: return None
    try:
        lang = _get_lang(chat_id) or "en"
        files = {"document": (filename, content, "application/octet-stream")}
        data = {"chat_id": str(chat_id), "parse_mode": "HTML"}
        if caption: data["caption"] = _localize_text(caption, lang)
        r = await _client.post(f"{_api_base()}/sendDocument", data=data, files=files, timeout=60)
        return r.json()
    except Exception as e:
        logger.warning(f"sendDocument error: {e}")
        return None

async def _get_file_url(file_id: str):
    res = await _call("getFile", file_id=file_id)
    if not res or not res.get("ok"): return None
    path = res["result"].get("file_path")
    if not path: return None
    return f"https://api.telegram.org/file/bot{_get_token()}/{path}"

async def _download_file(file_id: str):
    url = await _get_file_url(file_id)
    if not url or _client is None: return None
    try:
        r = await _client.get(url, timeout=60)
        if r.status_code == 200: return r.content
    except Exception as e:
        logger.warning(f"download file error: {e}")
    return None

def _is_admin(chat_id: int) -> bool:
    return chat_id in _get_admin_ids()

# ═══════════════════════════════════════════════════════════════════════════
#  KEYBOARDS
# ═══════════════════════════════════════════════════════════════════════════
def _main_menu_kb():
    return {"inline_keyboard": [
        [{"text": "📋 کانفیگ‌ها", "callback_data": "list:0"},
         {"text": "➕ کانفیگ جدید", "callback_data": "newcfg"}],
        [{"text": "🔍 جستجو", "callback_data": "search"},
         {"text": "🏷 فیلتر", "callback_data": "filter"}],
        [{"text": "🗂 گروه‌های ساب", "callback_data": "subs:0"}],
        [{"text": "📊 آمار", "callback_data": "stats"},
         {"text": "🔌 اتصالات", "callback_data": "conns"}],
        [{"text": "📈 نمودار ترافیک", "callback_data": "chart"},
         {"text": "🏆 TOP مصرف", "callback_data": "top"}],
        [{"text": "📋 لاگ‌ها", "callback_data": "logs"}],
        [{"text": "💾 پشتیبان/برگرداندن", "callback_data": "backup"},
         {"text": "📤 Export", "callback_data": "export"}],
        [{"text": "👥 ادمین‌ها", "callback_data": "admins"},
         {"text": "🔔 تست نوتیفیکیشن", "callback_data": "testnotif"}],
        [{"text": "🌐 زبان / Language", "callback_data": "langmenu"}],
        [{"text": "🔄 رفرش", "callback_data": "menu"}],
    ]}

def _links_list_kb(page: int, uids: list | None = None):
    if uids is None:
        uids = sorted(LINKS.keys(), key=lambda u: LINKS[u].get("created_at",""), reverse=True)
    total = len(uids)
    start = page * PAGE_SIZE
    chunk = uids[start:start + PAGE_SIZE]
    rows = []
    for uid in chunk:
        l = LINKS.get(uid)
        if not l: continue
        dot = "🟢" if is_link_allowed(l) else "🔴"
        rows.append([{"text": f"{dot} {l.get('label','?')[:28]}", "callback_data": f"view:{uid}"}])
    nav = []
    if start > 0: nav.append({"text": "◀ قبلی", "callback_data": f"list:{page-1}"})
    if start + PAGE_SIZE < total: nav.append({"text": "بعدی ▶", "callback_data": f"list:{page+1}"})
    if nav: rows.append(nav)
    rows.append([{"text": "➕ کانفیگ جدید", "callback_data": "newcfg"},
                 {"text": "🔍 جستجو", "callback_data": "search"}])
    rows.append([{"text": "⬅ منو", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

def _filter_kb(active_filter: str = "all"):
    def mk(label, key):
        prefix = "✅ " if active_filter == key else ""
        return {"text": f"{prefix}{label}", "callback_data": f"filter:{key}"}
    return {"inline_keyboard": [
        [mk("همه", "all"), mk("فعال", "active")],
        [mk("منقضی", "expired"), mk("غیرفعال", "disabled")],
        [mk("بدون گروه", "nogroup"), mk("دارای گروه", "hasgroup")],
        [{"text": "⬅ منو", "callback_data": "menu"}],
    ]}

def _link_detail_kb(uid: str, active: bool):
    return {"inline_keyboard": [
        [{"text": "🔗 نمایش لینک", "callback_data": f"link:{uid}"},
         {"text": "📷 QR", "callback_data": f"qr:{uid}"}],
        [{"text": "✏️ ویرایش", "callback_data": f"edit:{uid}"},
         {"text": "🔄 ریست مصرف", "callback_data": f"reset:{uid}"}],
        [{"text": "🗂 گروه ساب", "callback_data": f"cfggroup:{uid}"},
         {"text": "📊 آمار کانفیگ", "callback_data": f"cfgstats:{uid}"}],
        [{"text": "📤 Export این کانفیگ", "callback_data": f"expone:{uid}"}],
        [{"text": ("⛔ غیرفعال" if active else "✅ فعال"), "callback_data": f"toggle:{uid}"},
         {"text": "🗑 حذف", "callback_data": f"del:{uid}"}],
        [{"text": "⬅ لیست", "callback_data": "list:0"}],
    ]}

def _confirm_delete_kb(uid: str):
    return {"inline_keyboard": [
        [{"text": "✅ بله", "callback_data": f"delok:{uid}"},
         {"text": "❌ انصراف", "callback_data": f"view:{uid}"}],
    ]}

def _confirm_reset_kb(uid: str):
    return {"inline_keyboard": [
        [{"text": "✅ بله", "callback_data": f"resetok:{uid}"},
         {"text": "❌ انصراف", "callback_data": f"view:{uid}"}],
    ]}

def _edit_menu_kb(uid: str):
    return {"inline_keyboard": [
        [{"text": "🏷 نام", "callback_data": f"e:label:{uid}"},
         {"text": "📦 سهمیه", "callback_data": f"e:quota:{uid}"}],
        [{"text": "📅 انقضا", "callback_data": f"e:expiry:{uid}"},
         {"text": "🚀 سرعت", "callback_data": f"e:speed:{uid}"}],
        [{"text": "👥 آی‌پی", "callback_data": f"e:iplimit:{uid}"},
         {"text": "🔑 Sub Token", "callback_data": f"e:token:{uid}"}],
        [{"text": "🎭 Fingerprint", "callback_data": f"e:fp:{uid}"},
         {"text": "🔤 ALPN", "callback_data": f"e:alpn:{uid}"}],
        [{"text": "🔌 پورت", "callback_data": f"e:port:{uid}"}],
        [{"text": "⬅ بازگشت", "callback_data": f"view:{uid}"}],
    ]}

def _quota_kb(uid):
    return {"inline_keyboard": [
        [{"text":"500 MB","callback_data":f"eq:500mb:{uid}"},
         {"text":"1 GB","callback_data":f"eq:1gb:{uid}"},
         {"text":"5 GB","callback_data":f"eq:5gb:{uid}"}],
        [{"text":"10 GB","callback_data":f"eq:10gb:{uid}"},
         {"text":"50 GB","callback_data":f"eq:50gb:{uid}"},
         {"text":"100 GB","callback_data":f"eq:100gb:{uid}"}],
        [{"text":"♾ نامحدود","callback_data":f"eq:0:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:quota_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _expiry_kb(uid):
    return {"inline_keyboard": [
        [{"text":"۷ روز","callback_data":f"ex:7:{uid}"},
         {"text":"۳۰ روز","callback_data":f"ex:30:{uid}"},
         {"text":"۹۰ روز","callback_data":f"ex:90:{uid}"}],
        [{"text":"۱ روز","callback_data":f"ex:1:{uid}"},
         {"text":"۱۸۰ روز","callback_data":f"ex:180:{uid}"},
         {"text":"۳۶۵ روز","callback_data":f"ex:365:{uid}"}],
        [{"text":"♾ بدون انقضا","callback_data":f"ex:0:{uid}"}],
        [{"text":"➕ تمدید (افزودن روز)","callback_data":f"e:expiry_add:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:expiry_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _speed_kb(uid):
    return {"inline_keyboard": [
        [{"text":"۱ Mbps","callback_data":f"es:1:{uid}"},
         {"text":"۵ Mbps","callback_data":f"es:5:{uid}"},
         {"text":"۱۰ Mbps","callback_data":f"es:10:{uid}"}],
        [{"text":"۲۰ Mbps","callback_data":f"es:20:{uid}"},
         {"text":"۵۰ Mbps","callback_data":f"es:50:{uid}"},
         {"text":"۱۰۰ Mbps","callback_data":f"es:100:{uid}"}],
        [{"text":"♾ نامحدود","callback_data":f"es:0:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:speed_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _iplimit_kb(uid):
    return {"inline_keyboard": [
        [{"text":"۱","callback_data":f"ei:1:{uid}"},
         {"text":"۲","callback_data":f"ei:2:{uid}"},
         {"text":"۳","callback_data":f"ei:3:{uid}"},
         {"text":"۵","callback_data":f"ei:5:{uid}"}],
        [{"text":"۱۰","callback_data":f"ei:10:{uid}"},
         {"text":"۲۰","callback_data":f"ei:20:{uid}"}],
        [{"text":"♾ نامحدود","callback_data":f"ei:0:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:iplimit_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _fp_presets_kb(uid):
    rows, row = [], []
    for fp in FINGERPRINTS:
        row.append({"text": _fp_label(fp), "callback_data": f"efp:{fp}:{uid}"})
        if len(row) == 3: rows.append(row); row = []
    if row: rows.append(row)
    rows.append([{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}])
    return {"inline_keyboard": rows}

def _alpn_presets_kb(uid):
    return {"inline_keyboard": [
        [{"text":"http/1.1","callback_data":f"ealpn:p1:{uid}"},
         {"text":"h2,http/1.1","callback_data":f"ealpn:p2:{uid}"},
         {"text":"h2","callback_data":f"ealpn:p3:{uid}"}],
        [{"text":"⏭ پیش‌فرض پروتکل","callback_data":f"ealpn:default:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:alpn_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _port_presets_kb(uid):
    return {"inline_keyboard": [
        [{"text":"443","callback_data":f"ep:443:{uid}"},
         {"text":"80","callback_data":f"ep:80:{uid}"},
         {"text":"8080","callback_data":f"ep:8080:{uid}"}],
        [{"text":"8443","callback_data":f"ep:8443:{uid}"},
         {"text":"2053","callback_data":f"ep:2053:{uid}"},
         {"text":"2087","callback_data":f"ep:2087:{uid}"}],
        [{"text":"✏️ دلخواه","callback_data":f"e:port_custom:{uid}"}],
        [{"text":"⬅ بازگشت","callback_data":f"edit:{uid}"}],
    ]}

def _edit_cancel_kb(uid):
    return {"inline_keyboard": [[{"text":"❌ انصراف","callback_data":f"edit:{uid}"}]]}

# ── Sub Group keyboards ──────────────────────────────────────────────────
def _subs_list_kb(page: int):
    items = sorted(SUBS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for sid, s in chunk:
        cnt = len(s.get("link_ids", []))
        rows.append([{"text": f"🗂 {s.get('name','?')[:26]} ({cnt})", "callback_data": f"subview:{sid}"}])
    nav = []
    if start > 0: nav.append({"text": "◀ قبلی", "callback_data": f"subs:{page-1}"})
    if start + PAGE_SIZE < total: nav.append({"text": "بعدی ▶", "callback_data": f"subs:{page+1}"})
    if nav: rows.append(nav)
    rows.append([{"text": "➕ گروه جدید", "callback_data": "newsub"}])
    rows.append([{"text": "⬅ منو", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

def _sub_detail_kb(sid: str):
    return {"inline_keyboard": [
        [{"text": "➕ افزودن کانفیگ", "callback_data": f"subaddlink:{sid}:0"}],
        [{"text": "🔗 نمایش لینک حرفه‌ای", "callback_data": f"subsublink:{sid}"},
         {"text": "📷 QR", "callback_data": f"subqr:{sid}"}],
        [{"text": "🗑 حذف گروه", "callback_data": f"subdel:{sid}"}],
        [{"text": "⬅ لیست", "callback_data": "subs:0"}],
    ]}

def _confirm_subdel_kb(sid):
    return {"inline_keyboard": [
        [{"text": "✅ بله", "callback_data": f"subdelok:{sid}"},
         {"text": "❌ انصراف", "callback_data": f"subview:{sid}"}],
    ]}

def _pick_link_for_group_kb(sid: str, page: int):
    items = sorted(LINKS.items(), key=lambda kv: kv[1].get("created_at",""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for uid, l in chunk:
        pre = "✅ " if l.get("sub_id") == sid else ""
        rows.append([{"text": f"{pre}{l.get('label','?')[:28]}", "callback_data": f"subaddlinkdo:{uid}"}])
    nav = []
    if start > 0: nav.append({"text": "◀ قبلی", "callback_data": f"subaddlink:{sid}:{page-1}"})
    if start + PAGE_SIZE < total: nav.append({"text": "بعدی ▶", "callback_data": f"subaddlink:{sid}:{page+1}"})
    if nav: rows.append(nav)
    rows.append([{"text": "⬅ بازگشت", "callback_data": f"subview:{sid}"}])
    return {"inline_keyboard": rows}

def _cfg_group_kb(uid: str):
    link = LINKS.get(uid, {})
    sid = link.get("sub_id")
    if sid and sid in SUBS:
        return {"inline_keyboard": [
            [{"text": "➖ خروج از گروه", "callback_data": f"cfgungroup:{uid}"}],
            [{"text": "⬅ بازگشت", "callback_data": f"view:{uid}"}],
        ]}
    rows = []
    for sid2, s in sorted(SUBS.items(), key=lambda kv: kv[1].get("created_at",""), reverse=True)[:8]:
        rows.append([{"text": f"➕ «{s.get('name','?')[:24]}»", "callback_data": f"cfgaddgroup:{sid2}"}])
    rows.append([{"text":"🆕 ساخت گروه جدید + افزودن", "callback_data": f"cfgnewgroup:{uid}"}])
    rows.append([{"text": "⬅ بازگشت", "callback_data": f"view:{uid}"}])
    return {"inline_keyboard": rows}

# ── Admin management ────────────────────────────────────────────────────
def _admins_kb():
    return {"inline_keyboard": [
        [{"text": "➕ افزودن ادمین", "callback_data": "admin:add"}],
        [{"text": "➖ حذف ادمین", "callback_data": "admin:remove_menu"}],
        [{"text": "⬅ منو", "callback_data": "menu"}],
    ]}

def _remove_admin_kb(ids: set):
    rows = []
    for uid in sorted(ids):
        rows.append([{"text": f"❌ {uid}", "callback_data": f"admin:remove_do:{uid}"}])
    rows.append([{"text": "⬅ بازگشت", "callback_data": "admins"}])
    return {"inline_keyboard": rows}

# ── Backup/Export keyboards ─────────────────────────────────────────────
def _backup_kb():
    return {"inline_keyboard": [
        [{"text": "💾 دانلود پشتیبان (JSON)", "callback_data": "backup:download"}],
        [{"text": "📥 برگرداندن از فایل", "callback_data": "backup:restore"}],
        [{"text": "⬅ منو", "callback_data": "menu"}],
    ]}

def _export_kb():
    return {"inline_keyboard": [
        [{"text": "📄 JSON", "callback_data": "export:json"},
         {"text": "📊 CSV", "callback_data": "export:csv"}],
        [{"text": "📃 لیست متنی لینک‌ها", "callback_data": "export:txt"}],
        [{"text": "⬅ منو", "callback_data": "menu"}],
    ]}

# ── Wizard keyboards ────────────────────────────────────────────────────
def _wizard_cancel_kb():
    return {"inline_keyboard": [[{"text":"❌ انصراف","callback_data":"w:cancel"}]]}

def _wizard_protocol_kb():
    rows = [
        [{"text": PROTOCOL_FAMILY_LABELS[family], "callback_data": f"w:family:{family}"}]
        for family in ("vless", "vmess", "trojan")
    ]
    rows.append([{"text":"❌ انصراف","callback_data":"w:cancel"}])
    return {"inline_keyboard": rows}


def _wizard_transport_kb(family: str):
    rows = [
        [{"text": TRANSPORT_LABELS[transport], "callback_data": f"w:transport:{family}:{transport}"}]
        for transport in ("ws", "packet-up", "stream-up")
    ]
    rows.append([{"text":"⬅ خانواده پروتکل", "callback_data":"w:back:family"}])
    rows.append([{"text":"❌ انصراف","callback_data":"w:cancel"}])
    return {"inline_keyboard": rows}


def _edit_protocol_family_kb(uid: str):
    rows = [
        [{"text": PROTOCOL_FAMILY_LABELS[family], "callback_data": f"epfamily:{family}:{uid}"}]
        for family in ("vless", "vmess", "trojan")
    ]
    rows.append([{"text":"⬅ بازگشت", "callback_data":f"edit:{uid}"}])
    return {"inline_keyboard": rows}


def _edit_protocol_transport_kb(uid: str, family: str):
    current = normalize_protocol(LINKS.get(uid, {}).get("protocol", DEFAULT_PROTOCOL))
    cur_family, cur_transport = split_protocol(current)
    rows = []
    for transport in ("ws", "packet-up", "stream-up"):
        mark = "✅ " if (family == cur_family and transport == cur_transport) else ""
        rows.append([{
            "text": mark + TRANSPORT_LABELS[transport],
            "callback_data": f"eptrans:{family}:{transport}:{uid}"
        }])
    rows.append([{ "text":"⬅ خانواده پروتکل", "callback_data":f"e:protocol:{uid}" }])
    return {"inline_keyboard": rows}

def _wizard_fp_kb():
    rows, row = [], []
    for fp in FINGERPRINTS:
        row.append({"text": _fp_label(fp), "callback_data": f"w:fp:{fp}"})
        if len(row) == 3: rows.append(row); row = []
    if row: rows.append(row)
    rows.append([{"text":"❌ انصراف","callback_data":"w:cancel"}])
    return {"inline_keyboard": rows}

def _wizard_alpn_kb():
    return {"inline_keyboard": [
        [{"text":"http/1.1","callback_data":"w:alpnpreset:p1"}],
        [{"text":"h2,http/1.1","callback_data":"w:alpnpreset:p2"}],
        [{"text":"h2","callback_data":"w:alpnpreset:p3"}],
        [{"text":"⏭ پیش‌فرض","callback_data":"w:skip:alpn"}],
        [{"text":"❌ انصراف","callback_data":"w:cancel"}],
    ]}

def _wizard_unlimited_kb(step_key: str, label: str = "♾ نامحدود"):
    return {"inline_keyboard": [
        [{"text": label, "callback_data": f"w:skip:{step_key}"}],
        [{"text": "❌ انصراف", "callback_data": "w:cancel"}],
    ]}

def _wizard_confirm_kb():
    return {"inline_keyboard": [
        [{"text":"✅ ساخت کانفیگ","callback_data":"w:confirm"}],
        [{"text":"❌ انصراف","callback_data":"w:cancel"}],
    ]}

# ═══════════════════════════════════════════════════════════════════════════
#  VIEW BUILDERS
# ═══════════════════════════════════════════════════════════════════════════
def _format_detail(uid: str, l: dict) -> str:
    status = "🟢 فعال" if is_link_allowed(l) else "🔴 غیرفعال/منقضی"
    limit = "نامحدود" if not l.get("limit_bytes") else fmt_bytes(l["limit_bytes"])
    speed = "نامحدود" if not l.get("speed_limit_bytes") else f"{l['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    exp = l.get("expires_at")
    if exp:
        try:
            dl = max(0, int((datetime.fromisoformat(exp) - datetime.now()).total_seconds() // 86400))
            exp_txt = f"{exp.split('T')[0]} ({dl} روز)"
        except Exception:
            exp_txt = exp
    else:
        exp_txt = "بدون انقضا"
    proto = l.get("protocol", DEFAULT_PROTOCOL)
    alpn = l.get("alpn") or f"پیش‌فرض"
    tok = (l.get("sub_token") or "").strip() or "—"
    return (
        f"<b>{l.get('label','?')}</b>\n"
        f"وضعیت: {status}\n"
        f"مصرف: {fmt_bytes(l.get('used_bytes',0))} / {limit}\n"
        f"سرعت: {speed}\n"
        f"آی‌پی: {l.get('ip_limit',0) or 'نامحدود'}\n"
        f"پروتکل: {_protocol_label(proto)}\n"
        f"Fingerprint: {_fp_label(l.get('fingerprint', DEFAULT_FINGERPRINT))}\n"
        f"ALPN: {alpn}\n"
        f"پورت: {l.get('port', DEFAULT_PORT)}\n"
        f"Sub Token: <code>{tok}</code>\n"
        f"انقضا: {exp_txt}\n"
        f"UUID: <code>{uid}</code>"
    )

def _format_sub_detail(sid: str, s: dict) -> str:
    cnt = len(s.get("link_ids", []))
    pw = "🔒 دارد" if s.get("password_hash") else "بدون رمز"
    desc = s.get("desc") or "—"
    return (
        f"🗂 <b>{s.get('name','?')}</b>\n"
        f"توضیحات: {desc}\n"
        f"کانفیگ‌ها: {cnt}\n"
        f"رمز: {pw}\n\n"
        f"🔗 ساب حرفه‌ای:\n<code>{_group_public_url(s)}</code>\n\n"
        f"🔗 لینک ساب خام:\n<code>{_group_sub_url(s)}</code>"
    )

def _format_cfg_group(uid: str) -> str:
    link = LINKS.get(uid, {})
    sid = link.get("sub_id")
    if sid and sid in SUBS:
        s = SUBS[sid]
        return (
            f"🗂 «{link.get('label','?')}» توی گروه «{s.get('name','?')}» هست.\n\n"
            f"🔗 {_group_public_url(s)}"
        )
    return (
        f"«{link.get('label','?')}» توی هیچ گروهی نیست.\n"
        f"برای داشتن لینک ساب حرفه‌ای، یه گروه انتخاب کن:"
    )

def _wizard_prompt(step: str, data: dict) -> str:
    n = WIZARD_STEPS.index(step) + 1 if step in WIZARD_STEPS else len(WIZARD_STEPS)
    head = f"🧩 ساخت کانفیگ — {n}/{len(WIZARD_STEPS)}\n\n"
    m = {
        "label": "✏️ اسم کانفیگ:",
        "protocol": "🌐 خانواده پروتکل:",
        "transport": "🚚 ترنسپورت:",
        "fingerprint": "🖐 Fingerprint:",
        "alpn": "🔤 ALPN (یا تایپ کن):",
        "port": f"🔌 پورت ({MIN_PORT}-{MAX_PORT}):",
        "volume": "📦 حجم: مثلاً <code>10GB</code> یا <code>500MB</code>",
        "speed": "🚀 سرعت (Mbps): مثلاً <code>20</code>",
        "iplimit": "👥 حداکثر آی‌پی:",
        "days": "📅 تعداد روز اعتبار:",
    }
    return head + m.get(step, "")

def _wizard_summary(data: dict) -> str:
    limit = "نامحدود" if not data.get("limit_bytes") else fmt_bytes(data["limit_bytes"])
    speed = "نامحدود" if not data.get("speed_limit_bytes") else f"{data['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    iplim = data.get("ip_limit", 0) or "نامحدود"
    days = data.get("expires_days", 0)
    days_txt = "بدون انقضا" if not days else f"{days} روز"
    proto = data.get("protocol", DEFAULT_PROTOCOL)
    alpn = data.get("alpn") or "پیش‌فرض"
    return (
        "🧩 خلاصه — تایید کن:\n\n"
        f"برچسب: <b>{data.get('label','?')}</b>\n"
        f"پروتکل: {_protocol_label(proto)}\n"
        f"Fingerprint: {_fp_label(data.get('fingerprint', DEFAULT_FINGERPRINT))}\n"
        f"ALPN: {alpn}\n"
        f"پورت: {data.get('port', DEFAULT_PORT)}\n"
        f"حجم: {limit}\n"
        f"سرعت: {speed}\n"
        f"آی‌پی: {iplim}\n"
        f"انقضا: {days_txt}"
    )

# ═══════════════════════════════════════════════════════════════════════════
#  EXPORT HELPERS
# ═══════════════════════════════════════════════════════════════════════════
def _export_json(only_uid: str | None = None) -> bytes:
    data = {"exported_at": datetime.now().isoformat(), "links": {}, "subs": {}}
    if only_uid:
        if only_uid in LINKS: data["links"][only_uid] = LINKS[only_uid]
    else:
        data["links"] = dict(LINKS)
        data["subs"] = dict(SUBS)
    return json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")

def _export_csv(only_uid: str | None = None) -> bytes:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["UUID","Label","Note","SubToken","Protocol","Fingerprint","ALPN","Port",
                "LimitBytes","UsedBytes","IPLimit","SpeedLimitBytes",
                "Active","ExpiresAt","CreatedAt","SubGroup","ShareLink"])
    host = get_host()
    items = [(only_uid, LINKS.get(only_uid))] if only_uid else LINKS.items()
    for uid, l in items:
        if not l: continue
        sid = l.get("sub_id"); sg = SUBS.get(sid,{}).get("name","") if sid else ""
        try: vless = vless_link_for_link(l, uid, host)
        except Exception: vless = ""
        w.writerow([uid, l.get("label",""), l.get("note",""),
                    l.get("sub_token",""), l.get("protocol",""), l.get("fingerprint",""),
                    l.get("alpn",""), l.get("port",443),
                    l.get("limit_bytes",0), l.get("used_bytes",0),
                    l.get("ip_limit",0), l.get("speed_limit_bytes",0),
                    l.get("active",True), l.get("expires_at",""),
                    l.get("created_at",""), sg, vless])
    return buf.getvalue().encode("utf-8-sig")

def _export_txt(only_uid: str | None = None) -> bytes:
    host = get_host()
    lines = []
    items = [(only_uid, LINKS.get(only_uid))] if only_uid else LINKS.items()
    for uid, l in items:
        if not l or not is_link_allowed(l): continue
        try: lines.append(vless_link_for_link(l, uid, host))
        except Exception: pass
    return "\n".join(lines).encode("utf-8")

# ═══════════════════════════════════════════════════════════════════════════
#  MESSAGE HANDLER
# ═══════════════════════════════════════════════════════════════════════════
async def _handle_message(msg: dict):
    chat_id = msg.get("chat", {}).get("id")
    text = (msg.get("text") or "").strip()
    if chat_id is None: return

    # First contact: ask for the language before showing anything else.
    if text == "/start" and _get_lang(chat_id) is None:
        await _send(chat_id, _language_choice_text(), _language_choice_kb())
        return

    if text == "/language":
        await _send(chat_id, _language_choice_text(), _language_choice_kb(back_to_menu=_is_admin(chat_id)))
        return

    if not _is_admin(chat_id):
        # Keep /start useful for non-admins after language selection.
        if text == "/start":
            await _send(chat_id, f"⛔ شما ادمین نیستید.\nآیدی تلگرام شما: <code>{chat_id}</code>\n"
                                  f"از ادمین اصلی بخواید این آیدی رو اضافه کنه.")
        return

    if text in ("/start", "/menu"):
        _pending.pop(chat_id, None)
        await _send(chat_id, "👋 منوی مدیریت:", _main_menu_kb())
        return

    if text == "/cancel":
        _pending.pop(chat_id, None)
        await _send(chat_id, "لغو شد.", _main_menu_kb())
        return

    if text == "/help":
        await _send(chat_id,
            "📚 <b>راهنما</b>\n\n"
            "/start یا /menu — منوی اصلی\n"
            "/cancel — لغو عملیات\n"
            "/id — نمایش آیدی تلگرام شما\n"
            "/stats — آمار سریع\n"
            "/export — دانلود بکاپ\n\n"
            "همه‌ی قابلیت‌ها از طریق دکمه‌ها در دسترسه.", _main_menu_kb())
        return

    if text == "/id":
        await _send(chat_id, f"آیدی شما: <code>{chat_id}</code>")
        return

    if text == "/stats":
        await _send(chat_id, _stats_text())
        return

    if text == "/export":
        await _send_document(chat_id, "backup.json", _export_json(), "💾 پشتیبان کامل")
        return

    pending = _pending.get(chat_id)
    if not pending:
        await _send(chat_id, "از دکمه‌ها استفاده کن:", _main_menu_kb())
        return

    action = pending.get("action")

    # ── جستجو ──────────────────────────────────────────────────────────
    if action == "search_text" and text:
        q = text.strip().lower()
        matches = [uid for uid, l in LINKS.items()
                   if q in (l.get("label","").lower()) or q in (l.get("note","").lower())
                   or q in uid.lower() or q in (l.get("sub_token","").lower())]
        _pending.pop(chat_id, None)
        if not matches:
            await _send(chat_id, f"🔍 نتیجه‌ای برای «{text}» پیدا نشد.", _main_menu_kb())
            return
        await _send(chat_id, f"🔍 {len(matches)} نتیجه:", _links_list_kb(0, uids=matches))
        return

    # ── ویرایش فیلد متنی ────────────────────────────────────────────────
    if action == "edit_text" and text:
        uid = pending.get("uid"); field = pending.get("field")
        link = LINKS.get(uid)
        if not link:
            _pending.pop(chat_id, None)
            await _send(chat_id, "کانفیگ حذف شده.", _main_menu_kb()); return
        try:
            if field == "label":
                updated = await update_link_field(uid, "label", text[:60] or link.get("label"))
            elif field == "quota_custom":
                p = _parse_volume_text(text)
                if p is None:
                    await _send(chat_id, "❗️ فرمت: <code>10GB</code> یا <code>500MB</code>", _edit_cancel_kb(uid)); return
                updated = await update_link_field(uid, "limit_bytes", p)
            elif field == "expiry_custom":
                n = _parse_nonneg_int(text)
                if n is None:
                    await _send(chat_id, "❗️ یه عدد صحیح:", _edit_cancel_kb(uid)); return
                exp = None if n == 0 else (datetime.now() + timedelta(days=n)).isoformat()
                updated = await update_link_field(uid, "expires_at", exp)
            elif field == "expiry_add":
                n = _parse_nonneg_int(text)
                if n is None or n <= 0:
                    await _send(chat_id, "❗️ عدد مثبت:", _edit_cancel_kb(uid)); return
                base = datetime.now()
                cur = link.get("expires_at")
                if cur:
                    try:
                        d = datetime.fromisoformat(cur)
                        if d > base: base = d
                    except Exception: pass
                updated = await update_link_field(uid, "expires_at", (base + timedelta(days=n)).isoformat())
            elif field == "speed_custom":
                p = _parse_speed_text(text)
                if p is None:
                    await _send(chat_id, "❗️ عدد به Mbps:", _edit_cancel_kb(uid)); return
                updated = await update_link_field(uid, "speed_limit_bytes", p)
            elif field == "iplimit_custom":
                n = _parse_nonneg_int(text)
                if n is None:
                    await _send(chat_id, "❗️ عدد صحیح:", _edit_cancel_kb(uid)); return
                updated = await update_link_field(uid, "ip_limit", n)
            elif field == "token":
                tok = text.strip()[:32]
                if tok and not re.match(r"^[A-Za-z0-9_-]{3,32}$", tok):
                    await _send(chat_id, "❗️ فقط حروف/عدد/-/_ (۳ تا ۳۲ کاراکتر)", _edit_cancel_kb(uid)); return
                # چک یکتایی
                for u2, l2 in LINKS.items():
                    if u2 != uid and (l2.get("sub_token") or "").strip() == tok and tok:
                        await _send(chat_id, f"❗️ «{tok}» قبلاً استفاده شده", _edit_cancel_kb(uid)); return
                updated = await update_link_field(uid, "sub_token", tok)
            elif field == "alpn_custom":
                val = text.strip()[:100]
                updated = await update_link_field(uid, "alpn", val)
            elif field == "port_custom":
                try: p = int(text.strip())
                except ValueError: p = None
                if p is None or not (MIN_PORT <= p <= MAX_PORT):
                    await _send(chat_id, f"❗️ پورت بین {MIN_PORT}-{MAX_PORT}", _edit_cancel_kb(uid)); return
                updated = await update_link_field(uid, "port", p)
            elif field == "admin_add":
                try: new_id = int(text.strip())
                except ValueError:
                    await _send(chat_id, "❗️ آیدی عددی بفرست:", _edit_cancel_kb(uid)); return
                ok = await add_admin(new_id)
                _pending.pop(chat_id, None)
                if ok:
                    await _send(chat_id, f"✅ ادمین <code>{new_id}</code> اضافه شد.", _admins_kb())
                else:
                    await _send(chat_id, f"ℹ️ <code>{new_id}</code> از قبل ادمین بود.", _admins_kb())
                return
            else:
                _pending.pop(chat_id, None)
                await _send(chat_id, "فیلد ناشناخته.", _main_menu_kb()); return
        except Exception as e:
            logger.warning(f"edit_text error: {e}")
            _pending.pop(chat_id, None)
            await _send(chat_id, f"❌ خطا: {e}", _main_menu_kb()); return
        _pending.pop(chat_id, None)
        await _send(chat_id, f"✅ تغییر اعمال شد.\n\n{_format_detail(uid, updated)}",
                    _link_detail_kb(uid, updated["active"]))
        return

    # ── ساخت گروه جدید با اسم ───────────────────────────────────────────
    if action == "newsub" and pending.get("step") == "name" and text:
        sid, s = await create_sub_group(name=text[:60])
        link_uid = pending.get("link_uid")
        _pending.pop(chat_id, None)
        if link_uid and link_uid in LINKS:
            await set_link_sub(link_uid, sid)
            await _send(chat_id, f"✅ گروه ساخته و کانفیگ اضافه شد.\n\n{_format_cfg_group(link_uid)}",
                        _cfg_group_kb(link_uid))
        else:
            await _send(chat_id, f"✅ گروه ساخته شد.\n\n{_format_sub_detail(sid, s)}",
                        _sub_detail_kb(sid))
        return

    # ── ویزارد ساخت کانفیگ ──────────────────────────────────────────────
    if action == "wizard" and text:
        step = pending["step"]; data = pending["data"]
        if step == "label":
            data["label"] = text[:60] or "کانفیگ"
            pending["step"] = "protocol"
            await _send(chat_id, _wizard_prompt("protocol", data), _wizard_protocol_kb()); return
        if step in ("protocol", "transport", "fingerprint"):
            if step == "protocol":
                kb = _wizard_protocol_kb()
            elif step == "transport":
                kb = _wizard_transport_kb(data.get("protocol_family", "vless"))
            else:
                kb = _wizard_fp_kb()
            await _send(chat_id, "از دکمه‌ها 👆", kb); return
        if step == "alpn":
            data["alpn"] = text[:100]
            pending["step"] = "port"
            await _send(chat_id, _wizard_prompt("port", data),
                        _wizard_unlimited_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})")); return
        if step == "port":
            try: p = int(text.strip())
            except ValueError: p = None
            if p is None or not (MIN_PORT <= p <= MAX_PORT):
                await _send(chat_id, f"❗️ پورت {MIN_PORT}-{MAX_PORT}:",
                            _wizard_unlimited_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})")); return
            data["port"] = p; pending["step"] = "volume"
            await _send(chat_id, _wizard_prompt("volume", data), _wizard_unlimited_kb("volume")); return
        if step == "volume":
            p = _parse_volume_text(text)
            if p is None:
                await _send(chat_id, "❗️ فرمت: <code>10GB</code> یا <code>500MB</code>",
                            _wizard_unlimited_kb("volume")); return
            data["limit_bytes"] = p; pending["step"] = "speed"
            await _send(chat_id, _wizard_prompt("speed", data), _wizard_unlimited_kb("speed")); return
        if step == "speed":
            p = _parse_speed_text(text)
            if p is None:
                await _send(chat_id, "❗️ عدد (Mbps):", _wizard_unlimited_kb("speed")); return
            data["speed_limit_bytes"] = p; pending["step"] = "iplimit"
            await _send(chat_id, _wizard_prompt("iplimit", data), _wizard_unlimited_kb("iplimit")); return
        if step == "iplimit":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗️ عدد صحیح:", _wizard_unlimited_kb("iplimit")); return
            data["ip_limit"] = n; pending["step"] = "days"
            await _send(chat_id, _wizard_prompt("days", data), _wizard_unlimited_kb("days")); return
        if step == "days":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗️ عدد صحیح (روز):", _wizard_unlimited_kb("days")); return
            data["expires_days"] = n; pending["step"] = "confirm"
            await _send(chat_id, _wizard_summary(data), _wizard_confirm_kb()); return

    await _send(chat_id, "از دکمه‌ها استفاده کن:", _main_menu_kb())

# ═══════════════════════════════════════════════════════════════════════════
#  DOCUMENT HANDLER (RESTORE)
# ═══════════════════════════════════════════════════════════════════════════
async def _handle_document(msg: dict):
    chat_id = msg.get("chat", {}).get("id")
    if chat_id is None or not _is_admin(chat_id): return
    doc = msg.get("document")
    if not doc: return
    fname = (doc.get("file_name") or "").lower()
    if not fname.endswith(".json"):
        await _send(chat_id, "⚠️ فقط فایل JSON قبول می‌شه.")
        return
    content = await _download_file(doc["file_id"])
    if not content:
        await _send(chat_id, "❌ دانلود فایل نشد.")
        return
    try:
        data = json.loads(content)
    except Exception as e:
        await _send(chat_id, f"❌ JSON نامعتبر: {e}")
        return
    links = data.get("links") or {}
    subs = data.get("subs") or {}
    if not isinstance(links, dict):
        await _send(chat_id, "❌ ساختار فایل درست نیست."); return
    _pending[chat_id] = {"action": "restore_confirm", "data": {"links": links, "subs": subs}}
    kb = {"inline_keyboard": [
        [{"text": f"✅ افزودن {len(links)} کانفیگ", "callback_data": "restore:merge"},
         {"text": f"🔄 جایگزینی کامل", "callback_data": "restore:replace"}],
        [{"text": "❌ انصراف", "callback_data": "restore:cancel"}],
    ]}
    await _send(chat_id,
        f"📥 <b>فایل بارگذاری شد</b>\n\n"
        f"کانفیگ‌ها: {len(links)}\n"
        f"گروه‌ها: {len(subs)}\n\n"
        f"چطور اعمال کنم؟\n"
        f"• <b>افزودن</b>: کانفیگ‌های جدید اضافه میشن، هم‌نام‌ها دست‌نخورده می‌مونن\n"
        f"• <b>جایگزینی</b>: همه‌چی پاک و از فایل بازسازی می‌شه",
        kb)

# ═══════════════════════════════════════════════════════════════════════════
#  STATS TEXT
# ═══════════════════════════════════════════════════════════════════════════
def _stats_text() -> str:
    total_used = sum(l.get("used_bytes", 0) for l in LINKS.values())
    active_cfgs = sum(1 for l in LINKS.values() if is_link_allowed(l))
    expired_cfgs = sum(1 for l in LINKS.values() if is_link_expired(l))
    disabled = sum(1 for l in LINKS.values() if not l.get("active", True))
    tt = stats.get("total_bytes", 0)
    today = _sum_hourly(_hours_today())

    # 🌐 اطلاعات سرور (اگه cache شده باشه)
    server_line = ""
    try:
        from main import _server_info_cache as _si
        if _si and not _si.get("error") and _si.get("ip"):
            flag = _si.get("flag", "🌐")
            ip = _si.get("ip", "")
            city = _si.get("city") or _si.get("region") or ""
            country = _si.get("country_fa") or _si.get("country") or ""
            loc = " · ".join(p for p in [country, city] if p)
            server_line = f"\n🌐 سرور: {flag} <code>{ip}</code>"
            if loc:
                server_line += f"\n     {loc}"
            server_line += "\n"
    except Exception:
        pass

    return (
        "📊 <b>آمار سیستم</b>\n"
        f"{server_line}\n"
        f"🔌 اتصالات فعال: <b>{len(connections)}</b>\n"
        f"📡 ترافیک امروز: <b>{fmt_bytes(today)}</b>\n"
        f"📡 کل ترافیک عبوری: <b>{fmt_bytes(tt)}</b>\n"
        f"📦 مجموع مصرف کانفیگ‌ها: <b>{fmt_bytes(total_used)}</b>\n\n"
        f"🗂 کل: <b>{len(LINKS)}</b>\n"
        f"✅ فعال: <b>{active_cfgs}</b>\n"
        f"⏰ منقضی: <b>{expired_cfgs}</b>\n"
        f"❌ غیرفعال: <b>{disabled}</b>\n\n"
        f"👥 گروه‌ها: <b>{len(SUBS)}</b>\n"
        f"⏱ آپتایم: <b>{uptime()}</b>\n"
        f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

# ═══════════════════════════════════════════════════════════════════════════
#  CALLBACK HANDLER
# ═══════════════════════════════════════════════════════════════════════════
async def _handle_callback(cb: dict):
    chat_id = cb.get("message", {}).get("chat", {}).get("id")
    message_id = cb.get("message", {}).get("message_id")
    data = cb.get("data", "")
    cb_id = cb.get("id")
    if chat_id is None:
        return
    if cb_id:
        _callback_chats[cb_id] = int(chat_id)

    # Language selection is available even before admin authorization so the
    # first /start flow can be completed in the user's preferred language.
    if data == "langmenu":
        await _answer_cb(cb_id)
        await _edit(chat_id, message_id, _language_choice_text(), _language_choice_kb(back_to_menu=_is_admin(chat_id)))
        return
    if data.startswith("setlang:"):
        lang = data.split(":", 1)[1]
        if lang not in ("fa", "en"):
            await _answer_cb(cb_id, "Invalid language")
            return
        await _set_lang(chat_id, lang)
        await _answer_cb(cb_id, "Language changed" if lang == "en" else "زبان تغییر کرد")
        if _is_admin(chat_id):
            await _edit(chat_id, message_id, "👋 منوی مدیریت:", _main_menu_kb())
        else:
            await _edit(chat_id, message_id, "⛔ شما ادمین نیستید.\nآیدی تلگرام شما: <code>" + str(chat_id) + "</code>\nاز ادمین اصلی بخواید این آیدی رو اضافه کنه.", _language_choice_kb())
        return

    if not _is_admin(chat_id):
        await _answer_cb(cb_id, "⛔ دسترسی نداری"); return
    await _answer_cb(cb_id)

    # ── منو ─────────────────────────────────────────────────────────────
    if data == "menu":
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, "👋 منوی مدیریت:", _main_menu_kb()); return

    # ── لیست ────────────────────────────────────────────────────────────
    if data.startswith("list:"):
        page = int(data.split(":", 1)[1] or 0)
        if not LINKS:
            await _edit(chat_id, message_id, "هنوز کانفیگی نیست.", _main_menu_kb()); return
        await _edit(chat_id, message_id, f"📋 کانفیگ‌ها ({len(LINKS)}):", _links_list_kb(page)); return

    # ── جستجو ───────────────────────────────────────────────────────────
    if data == "search":
        _pending[chat_id] = {"action": "search_text"}
        await _edit(chat_id, message_id, "🔍 عبارت جستجو رو بفرست\n(اسم، یادداشت، Sub Token یا بخشی از UUID)",
                    {"inline_keyboard": [[{"text":"❌ انصراف","callback_data":"menu"}]]}); return

    # ── فیلتر ───────────────────────────────────────────────────────────
    if data == "filter":
        await _edit(chat_id, message_id, "🏷 فیلتر:", _filter_kb("all")); return

    if data.startswith("filter:"):
        key = data.split(":", 1)[1]
        uids = []
        for uid, l in LINKS.items():
            if key == "all": uids.append(uid)
            elif key == "active" and is_link_allowed(l): uids.append(uid)
            elif key == "expired" and is_link_expired(l): uids.append(uid)
            elif key == "disabled" and not l.get("active", True): uids.append(uid)
            elif key == "nogroup" and not l.get("sub_id"): uids.append(uid)
            elif key == "hasgroup" and l.get("sub_id"): uids.append(uid)
        uids.sort(key=lambda u: LINKS[u].get("created_at",""), reverse=True)
        if not uids:
            await _edit(chat_id, message_id, "چیزی با این فیلتر نیست.", _filter_kb(key)); return
        await _edit(chat_id, message_id, f"🏷 {len(uids)} مورد:", _links_list_kb(0, uids=uids)); return

    # ── آمار ────────────────────────────────────────────────────────────
    if data == "stats":
        kb = {"inline_keyboard": [
            [{"text":"📅 امروز","callback_data":"stats:today"},
             {"text":"📆 هفته","callback_data":"stats:week"},
             {"text":"🗓 ماه","callback_data":"stats:month"}],
            [{"text":"🔄 رفرش","callback_data":"stats"}],
            [{"text":"⬅ منو","callback_data":"menu"}],
        ]}
        await _edit(chat_id, message_id, _stats_text(), kb); return

    if data.startswith("stats:"):
        period = data.split(":", 1)[1]
        hours = _hours_today() if period=="today" else (_hours_this_week() if period=="week" else _hours_this_month())
        total = _sum_hourly(hours)
        label = {"today":"امروز","week":"این هفته","month":"این ماه"}.get(period,"")
        await _send(chat_id, f"📊 ترافیک {label}: <b>{fmt_bytes(total)}</b>"); return

    # ── اتصالات ─────────────────────────────────────────────────────────
    if data == "conns":
        if not connections:
            await _edit(chat_id, message_id, "🔌 اتصالی نیست.", {"inline_keyboard": [
                [{"text":"🔄","callback_data":"conns"}],[{"text":"⬅ منو","callback_data":"menu"}]]}); return
        grouped = {}
        for c in connections.values():
            ip = c.get("ip","?"); g = grouped.setdefault(ip, {"bytes":0,"sessions":0,"labels":set()})
            g["bytes"] += c.get("bytes",0); g["sessions"] += 1
            link = LINKS.get(c.get("uuid"))
            if link: g["labels"].add(link.get("label","?"))
        lines = [f"🔌 اتصالات ({len(grouped)} آی‌پی)\n"]
        for ip, g in sorted(grouped.items(), key=lambda x:-x[1]["bytes"])[:15]:
            labels_txt = " · ".join(list(g["labels"])[:2]) or "?"
            lines.append(f"• <code>{ip}</code>\n  {labels_txt} · {fmt_bytes(g['bytes'])} · {g['sessions']} سشن")
        if len(grouped) > 15: lines.append(f"\n<i>... و {len(grouped)-15} مورد</i>")
        await _edit(chat_id, message_id, "\n".join(lines), {"inline_keyboard": [
            [{"text":"🔄","callback_data":"conns"}],[{"text":"⬅ منو","callback_data":"menu"}]]}); return

    # ── لاگ ─────────────────────────────────────────────────────────────
    if data == "logs":
        recent = list(activity_logs)[-15:][::-1]
        if not recent:
            await _edit(chat_id, message_id, "📋 لاگی نیست.", {"inline_keyboard": [
                [{"text":"⬅ منو","callback_data":"menu"}]]}); return
        icons = {"ok":"✅","err":"❌","warn":"⚠️","info":"ℹ️"}
        lines = ["📋 <b>آخرین رخدادها:</b>\n"]
        for log in recent:
            t = log.get("time","")[11:16]; lvl = log.get("level","info")
            lines.append(f"{icons.get(lvl,'•')} <code>{t}</code> {log.get('message','')}")
        await _edit(chat_id, message_id, "\n".join(lines), {"inline_keyboard": [
            [{"text":"🔄","callback_data":"logs"}],[{"text":"⬅ منو","callback_data":"menu"}]]}); return

    # ── نمودار ترافیک ───────────────────────────────────────────────────
    if data == "chart":
        labels, raw_values = _traffic_chart_points(24)

        if not any(raw_values):
            # Fallback for an already-running process whose current hour has
            # traffic but the persistence loop has not sampled yet.
            current_key = _traffic_hour_key()
            current_live = int(hourly_traffic.get(datetime.now().strftime("%H:00"), 0) or 0)
            if current_live > 0:
                async with _TRAFFIC_LOCK:
                    _TRAFFIC_HISTORY[current_key] = max(
                        int(_TRAFFIC_HISTORY.get(current_key, 0) or 0),
                        current_live,
                    )
                await _save_traffic_history()
                labels, raw_values = _traffic_chart_points(24)

        if not any(raw_values):
            await _edit(
                chat_id, message_id,
                "📈 داده‌ای برای نمودار نیست.",
                _main_menu_kb(),
            ); return

        values = [round(v / 1024**2, 2) for v in raw_values]
        cfg = {
            "type":"line",
            "data":{"labels":labels,"datasets":[{
                "label":"MB","data":values,
                "borderColor":"#60a5fa","backgroundColor":"rgba(96,165,250,0.25)",
                "fill":True,"tension":0.35,"borderWidth":3,"pointRadius":3,
            }]},
            "options":{
                "title":{"display":True,"text":"Traffic (last 24h)","fontSize":16},
                "legend":{"display":False},
                "scales":{
                    "yAxes":[{"ticks":{"beginAtZero":True}}],
                    "xAxes":[{"ticks":{"autoSkip":True,"maxTicksLimit":12}}]
                }
            }
        }
        url = _quickchart_url(cfg)
        kb = {"inline_keyboard": [
            [{"text":"🔄 بروزرسانی","callback_data":"chart"}],
            [{"text":"⬅ منو","callback_data":"menu"}]]}
        await _send_photo(chat_id, url, "📈 نمودار ترافیک ۲۴ ساعت اخیر", kb); return

    # ── TOP مصرف ────────────────────────────────────────────────────────
    if data == "top":
        if not LINKS:
            await _edit(chat_id, message_id, "کانفیگی نیست.", _main_menu_kb()); return
        items = sorted(LINKS.items(), key=lambda kv: kv[1].get("used_bytes",0), reverse=True)[:10]
        lines = ["🏆 <b>TOP 10 مصرف‌کننده:</b>\n"]
        for i, (uid, l) in enumerate(items, 1):
            icon = ["🥇","🥈","🥉"][i-1] if i <= 3 else f"{i}."
            lines.append(f"{icon} <b>{l.get('label','?')}</b> — {fmt_bytes(l.get('used_bytes',0))}")
        await _edit(chat_id, message_id, "\n".join(lines), {"inline_keyboard": [
            [{"text":"🔄","callback_data":"top"}],[{"text":"⬅ منو","callback_data":"menu"}]]}); return

    # ── جزئیات کانفیگ ──────────────────────────────────────────────────
    # لیست کانفیگ‌ها با callback داده‌ی view:<uuid> ساخته می‌شود؛ این handler
    # نمایش جزئیات همان کانفیگ را به‌صورت مستقیم انجام می‌دهد.
    if data.startswith("view:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb())
            return
        await _edit(
            chat_id,
            message_id,
            _format_detail(uid, l),
            _link_detail_kb(uid, bool(l.get("active", True))),
        )
        return

    # ── آمار یک کانفیگ ──────────────────────────────────────────────────
    if data.startswith("cfgstats:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "کانفیگ حذف شده.", _main_menu_kb()); return
        used = l.get("used_bytes", 0); limit = l.get("limit_bytes", 0)
        pct = 0 if limit == 0 else min(100, used / limit * 100)
        # اتصالات همین کانفیگ
        conns = [c for c in connections.values() if c.get("uuid") == uid]
        ips = {c.get("ip") for c in conns if c.get("ip")}
        txt = (
            f"📊 <b>{l.get('label','?')}</b>\n\n"
            f"مصرف: <b>{fmt_bytes(used)}</b> / {('∞' if limit==0 else fmt_bytes(limit))}\n"
            f"درصد: <b>{pct:.1f}%</b>\n\n"
            f"اتصالات فعال: <b>{len(conns)}</b>\n"
            f"آی‌پی‌های یکتا: <b>{len(ips)}</b>\n"
            f"سقف آی‌پی: <b>{l.get('ip_limit',0) or '∞'}</b>\n\n"
            f"UUID: <code>{uid}</code>"
        )
        await _edit(chat_id, message_id, txt, _link_detail_kb(uid, l.get("active", True))); return

    # ── QR Code ─────────────────────────────────────────────────────────
    if data.startswith("qr:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "پیدا نشد"); return
        share_link = vless_link_for_link(l, uid, get_host())
        qr_png = _build_styled_qr_png(share_link, 560)
        await _send_photo_bytes(
            chat_id,
            f"qr-{uid[:8]}.png",
            qr_png,
            f"📷 QR — <b>{l.get('label','?')}</b>\n\n<code>{share_link}</code>",
        )
        return

    # ── لینک ────────────────────────────────────────────────────────────
    if data.startswith("link:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "پیدا نشد"); return
        host = get_host()
        share_link = vless_link_for_link(l, uid, host)
        sub_url = _link_sub_url(l, uid)
        msg = f"🔗 <b>{l.get('label')}</b>\n\n<code>{share_link}</code>\n\nساب: <code>{sub_url}</code>"
        sid = l.get("sub_id")
        if sid and sid in SUBS:
            msg += f"\n\n✨ گروه: <code>{_group_public_url(SUBS[sid])}</code>"
        await _send(chat_id, msg); return

    # ── Toggle ──────────────────────────────────────────────────────────
    if data.startswith("toggle:"):
        uid = data.split(":", 1)[1]
        l = await set_link_active(uid, not LINKS.get(uid, {}).get("active", True))
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"])); return

    # ── حذف ─────────────────────────────────────────────────────────────
    if data.startswith("del:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, f"❗️ حذف «{l.get('label')}»؟", _confirm_delete_kb(uid)); return

    if data.startswith("delok:"):
        uid = data.split(":", 1)[1]
        name = await remove_link(uid)
        if name is None:
            await _edit(chat_id, message_id, "قبلاً حذف شده.", _main_menu_kb())
        else:
            await _edit(chat_id, message_id, f"🗑 «{name}» حذف شد.", _main_menu_kb())
        return

    # ── ریست ────────────────────────────────────────────────────────────
    if data.startswith("reset:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id,
            f"🔄 مصرف فعلی: <b>{fmt_bytes(l.get('used_bytes',0))}</b>\nمطمئنی؟",
            _confirm_reset_kb(uid)); return

    if data.startswith("resetok:"):
        uid = data.split(":", 1)[1]
        u = await reset_link_usage(uid)
        if not u:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, f"✅ ریست شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    # ── Export تک ───────────────────────────────────────────────────────
    if data.startswith("expone:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "پیدا نشد"); return
        fname = f"config-{(l.get('label','cfg') or 'cfg').replace(' ','_')[:30]}.json"
        await _send_document(chat_id, fname, _export_json(uid), f"📤 {l.get('label')}"); return

    # ── ویرایش ──────────────────────────────────────────────────────────
    if data.startswith("edit:"):
        uid = data.split(":", 1)[1]; l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, f"✏️ ویرایش «{l.get('label','?')}»", _edit_menu_kb(uid)); return

    # ── ویرایش: نام ─────────────────────────────────────────────────────
    if data.startswith("e:label:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"label"}
        await _edit(chat_id, message_id, f"🏷 نام فعلی: <b>{LINKS[uid].get('label','?')}</b>\nنام جدید:",
                    _edit_cancel_kb(uid)); return

    # ── ویرایش: سهمیه ───────────────────────────────────────────────────
    if data.startswith("e:quota:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        cur = LINKS[uid].get("limit_bytes",0)
        await _edit(chat_id, message_id,
            f"📦 فعلی: <b>{'نامحدود' if not cur else fmt_bytes(cur)}</b>\nجدید:",
            _quota_kb(uid)); return

    if data.startswith("eq:"):
        _, preset, uid = data.split(":", 2)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        MAP = {"0":0,"500mb":500*1024**2,"1gb":1024**3,"5gb":5*1024**3,
               "10gb":10*1024**3,"50gb":50*1024**3,"100gb":100*1024**3}
        u = await update_link_field(uid, "limit_bytes", MAP.get(preset,0))
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:quota_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"quota_custom"}
        await _edit(chat_id, message_id, "📦 مثلاً <code>10GB</code> یا <code>0</code> برای نامحدود:",
                    _edit_cancel_kb(uid)); return

    # ── ویرایش: انقضا ───────────────────────────────────────────────────
    if data.startswith("e:expiry:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        exp = LINKS[uid].get("expires_at")
        if exp:
            try:
                dl = max(0, int((datetime.fromisoformat(exp) - datetime.now()).total_seconds() // 86400))
                cur_txt = f"{exp.split('T')[0]} ({dl} روز)"
            except Exception: cur_txt = exp
        else: cur_txt = "بدون انقضا"
        await _edit(chat_id, message_id, f"📅 فعلی: <b>{cur_txt}</b>", _expiry_kb(uid)); return

    if data.startswith("ex:"):
        _, d, uid = data.split(":", 2); d = int(d)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        exp = None if d == 0 else (datetime.now() + timedelta(days=d)).isoformat()
        u = await update_link_field(uid, "expires_at", exp)
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:expiry_add:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"expiry_add"}
        await _edit(chat_id, message_id, "➕ چند روز اضافه بشه؟", _edit_cancel_kb(uid)); return

    if data.startswith("e:expiry_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"expiry_custom"}
        await _edit(chat_id, message_id, "📅 تعداد روز (0=بدون انقضا):", _edit_cancel_kb(uid)); return

    # ── ویرایش: سرعت ────────────────────────────────────────────────────
    if data.startswith("e:speed:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        sp = LINKS[uid].get("speed_limit_bytes", 0)
        await _edit(chat_id, message_id,
            f"🚀 فعلی: <b>{'نامحدود' if not sp else f'{sp*8/1024/1024:.1f} Mbps'}</b>",
            _speed_kb(uid)); return

    if data.startswith("es:"):
        _, mbps, uid = data.split(":", 2); mbps = int(mbps)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        b = 0 if mbps == 0 else int(mbps * 1024 * 1024 / 8)
        u = await update_link_field(uid, "speed_limit_bytes", b)
        try:
            from speed_limit import reset_bucket
            reset_bucket(uid)
        except Exception: pass
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:speed_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"speed_custom"}
        await _edit(chat_id, message_id, "🚀 عدد به Mbps (0=نامحدود):", _edit_cancel_kb(uid)); return

    # ── ویرایش: IP ──────────────────────────────────────────────────────
    if data.startswith("e:iplimit:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        cur = LINKS[uid].get("ip_limit", 0)
        await _edit(chat_id, message_id,
            f"👥 فعلی: <b>{cur or 'نامحدود'}</b>", _iplimit_kb(uid)); return

    if data.startswith("ei:"):
        _, n, uid = data.split(":", 2); n = int(n)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        u = await update_link_field(uid, "ip_limit", n)
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:iplimit_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"iplimit_custom"}
        await _edit(chat_id, message_id, "👥 عدد (0=نامحدود):", _edit_cancel_kb(uid)); return

    # ── ویرایش: پروتکل/ترنسپورت ────────────────────────────────────────
    if data.startswith("e:protocol:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        l = LINKS[uid]
        await _edit(
            chat_id, message_id,
            f"🌐 پروتکل فعلی: <b>{_protocol_label(l.get('protocol', DEFAULT_PROTOCOL))}</b>\n\nخانواده جدید رو انتخاب کن:",
            _edit_protocol_family_kb(uid),
        ); return

    if data.startswith("epfamily:"):
        _, family, uid = data.split(":", 2)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        if family not in ("vless", "vmess", "trojan"):
            family = "vless"
        await _edit(
            chat_id, message_id,
            f"🌐 <b>{PROTOCOL_FAMILY_LABELS[family]}</b>\n\nترنسپورت رو انتخاب کن:",
            _edit_protocol_transport_kb(uid, family),
        ); return

    if data.startswith("eptrans:"):
        _, family, transport, uid = data.split(":", 3)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        if family not in ("vless", "vmess", "trojan"):
            family = "vless"
        if transport not in ("ws", "packet-up", "stream-up"):
            transport = "ws"
        proto = f"{family}-ws" if transport == "ws" else f"{family}-xhttp-{transport}"
        if proto not in PROTOCOLS:
            await _answer_cb(cb_id, "پروتکل نامعتبر")
            return
        u = await update_link_field(uid, "protocol", proto)
        if not u:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, f"✅ پروتکل تغییر کرد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    # ── ویرایش: Sub Token ───────────────────────────────────────────────
    if data.startswith("e:token:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"token"}
        cur = (LINKS[uid].get("sub_token") or "").strip() or "—"
        await _edit(chat_id, message_id,
            f"🔑 Sub Token فعلی: <code>{cur}</code>\n\nجدید (۳ تا ۳۲ حرف، فقط a-z A-Z 0-9 _ -):\n"
            f"برای پاک کردن، <code>-</code> بفرست.",
            _edit_cancel_kb(uid)); return

    # ── ویرایش: Fingerprint ─────────────────────────────────────────────
    if data.startswith("e:fp:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        cur = LINKS[uid].get("fingerprint", DEFAULT_FINGERPRINT)
        await _edit(chat_id, message_id, f"🎭 فعلی: <b>{cur}</b>", _fp_presets_kb(uid)); return

    if data.startswith("efp:"):
        _, fp, uid = data.split(":", 2)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        if fp not in FINGERPRINTS: fp = DEFAULT_FINGERPRINT
        u = await update_link_field(uid, "fingerprint", fp)
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    # ── ویرایش: ALPN ────────────────────────────────────────────────────
    if data.startswith("e:alpn:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        cur = LINKS[uid].get("alpn") or "—"
        await _edit(chat_id, message_id, f"🔤 فعلی: <b>{cur}</b>", _alpn_presets_kb(uid)); return

    if data.startswith("ealpn:"):
        parts = data.split(":", 2)
        code, uid = parts[1], parts[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        if code == "default":
            val = ""
        elif code in ALPN_PRESET_MAP:
            val = ALPN_PRESET_MAP[code]
        else:
            val = ""
        u = await update_link_field(uid, "alpn", val)
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:alpn_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"alpn_custom"}
        await _edit(chat_id, message_id, "🔤 مقدار ALPN دلخواه (خالی = پیش‌فرض):",
                    _edit_cancel_kb(uid)); return

    # ── ویرایش: پورت ────────────────────────────────────────────────────
    if data.startswith("e:port:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        cur = LINKS[uid].get("port", DEFAULT_PORT)
        await _edit(chat_id, message_id, f"🔌 فعلی: <b>{cur}</b>", _port_presets_kb(uid)); return

    if data.startswith("ep:"):
        _, p, uid = data.split(":", 2); p = int(p)
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        u = await update_link_field(uid, "port", p)
        await _edit(chat_id, message_id, f"✅ اعمال شد.\n\n{_format_detail(uid, u)}",
                    _link_detail_kb(uid, u["active"])); return

    if data.startswith("e:port_custom:"):
        uid = data.split(":", 2)[2]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"edit_text","uid":uid,"field":"port_custom"}
        await _edit(chat_id, message_id, f"🔌 پورت ({MIN_PORT}-{MAX_PORT}):", _edit_cancel_kb(uid)); return

    # ── گروه یک کانفیگ ──────────────────────────────────────────────────
    if data.startswith("cfggroup:"):
        uid = data.split(":", 1)[1]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"cfg_group_ctx","uid":uid}
        await _edit(chat_id, message_id, _format_cfg_group(uid), _cfg_group_kb(uid)); return

    if data.startswith("cfgungroup:"):
        uid = data.split(":", 1)[1]
        await set_link_sub(uid, None)
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, _format_detail(uid, l),
                    _link_detail_kb(uid, l["active"])); return

    if data.startswith("cfgaddgroup:"):
        sid = data.split(":", 1)[1]
        ctx = _pending.get(chat_id) or {}
        uid = ctx.get("uid") if ctx.get("action") == "cfg_group_ctx" else None
        if not uid or uid not in LINKS:
            await _answer_cb(cb_id, "منقضی شده"); return
        ok = await set_link_sub(uid, sid)
        if not ok:
            await _answer_cb(cb_id, "گروه نیست"); return
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, f"✅ اضافه شد.\n\n{_format_cfg_group(uid)}",
                    _cfg_group_kb(uid)); return

    if data.startswith("cfgnewgroup:"):
        uid = data.split(":", 1)[1]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        _pending[chat_id] = {"action":"newsub","step":"name","link_uid":uid}
        await _edit(chat_id, message_id, "✏️ اسم گروه جدید:", _wizard_cancel_kb()); return

    # ── گروه‌های ساب ────────────────────────────────────────────────────
    if data.startswith("subs:"):
        page = int(data.split(":", 1)[1] or 0)
        if not SUBS:
            await _edit(chat_id, message_id, "هنوز گروهی نیست.", _subs_list_kb(0)); return
        await _edit(chat_id, message_id, f"🗂 {len(SUBS)} گروه:", _subs_list_kb(page)); return

    if data == "newsub":
        _pending[chat_id] = {"action":"newsub","step":"name","link_uid":None}
        await _edit(chat_id, message_id, "✏️ اسم گروه:", _wizard_cancel_kb()); return

    if data.startswith("subview:"):
        sid = data.split(":", 1)[1]; s = SUBS.get(sid)
        if not s:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id, _format_sub_detail(sid, s), _sub_detail_kb(sid)); return

    if data.startswith("subsublink:"):
        sid = data.split(":", 1)[1]; s = SUBS.get(sid)
        if not s:
            await _answer_cb(cb_id, "پیدا نشد"); return
        await _send(chat_id,
            f"🔗 <b>لینک ساب حرفه‌ای «{s.get('name','?')}»</b>\n\n"
            f"صفحه‌ی پابلیک:\n<code>{_group_public_url(s)}</code>\n\n"
            f"لینک ساب خام:\n<code>{_group_sub_url(s)}</code>"); return

    if data.startswith("subqr:"):
        sid = data.split(":", 1)[1]; s = SUBS.get(sid)
        if not s:
            await _answer_cb(cb_id, "پیدا نشد"); return
        url = _group_sub_url(s)
        qr_png = _build_styled_qr_png(url, 560)
        await _send_photo_bytes(
            chat_id,
            f"qr-sub-{sid[:8]}.png",
            qr_png,
            f"📷 ساب «{s.get('name','?')}»\n\n<code>{url}</code>",
        )
        return

    if data.startswith("subaddlink:"):
        _, sid, page_s = data.split(":", 2)
        if sid not in SUBS:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        if not LINKS:
            await _edit(chat_id, message_id, "کانفیگی نیست.", _sub_detail_kb(sid)); return
        _pending[chat_id] = {"action":"subaddlink_ctx","sid":sid}
        await _edit(chat_id, message_id, "کدوم کانفیگ؟ (✅ = الان توی گروهه)",
                    _pick_link_for_group_kb(sid, int(page_s or 0))); return

    if data.startswith("subaddlinkdo:"):
        uid = data.split(":", 1)[1]
        ctx = _pending.get(chat_id) or {}
        sid = ctx.get("sid") if ctx.get("action") == "subaddlink_ctx" else None
        if not sid or sid not in SUBS:
            await _answer_cb(cb_id, "منقضی شده"); return
        ok = await set_link_sub(uid, sid)
        if not ok:
            await _answer_cb(cb_id, "کانفیگ نیست"); return
        _pending.pop(chat_id, None)
        s = SUBS.get(sid)
        await _edit(chat_id, message_id, f"✅ اضافه شد.\n\n{_format_sub_detail(sid, s)}",
                    _sub_detail_kb(sid)); return

    if data.startswith("subdel:"):
        sid = data.split(":", 1)[1]; s = SUBS.get(sid)
        if not s:
            await _edit(chat_id, message_id, "پیدا نشد.", _main_menu_kb()); return
        await _edit(chat_id, message_id,
            f"❗️ حذف گروه «{s.get('name')}»؟\n(کانفیگ‌ها حذف نمی‌شن، فقط از گروه خارج می‌شن)",
            _confirm_subdel_kb(sid)); return

    if data.startswith("subdelok:"):
        sid = data.split(":", 1)[1]
        name = await remove_sub_group(sid)
        if name is None:
            await _edit(chat_id, message_id, "قبلاً حذف شده.", _main_menu_kb())
        else:
            await _edit(chat_id, message_id, f"🗑 «{name}» حذف شد.", _main_menu_kb())
        return

    # ── ادمین‌ها ────────────────────────────────────────────────────────
    if data == "admins":
        ids = _get_admin_ids()
        lst = "\n".join(f"• <code>{i}</code>" for i in sorted(ids)) or "—"
        txt = f"👥 <b>ادمین‌های فعلی ({len(ids)}):</b>\n\n{lst}"
        await _edit(chat_id, message_id, txt, _admins_kb()); return

    if data == "admin:add":
        _pending[chat_id] = {"action":"edit_text","uid":"","field":"admin_add"}
        await _edit(chat_id, message_id, "🆔 آیدی عددی ادمین جدید رو بفرست:",
                    {"inline_keyboard":[[{"text":"❌ انصراف","callback_data":"admins"}]]}); return

    if data == "admin:remove_menu":
        ids = _get_admin_ids()
        if not ids:
            await _edit(chat_id, message_id, "ادمینی نیست.", _admins_kb()); return
        await _edit(chat_id, message_id, "کدوم حذف بشه؟", _remove_admin_kb(ids)); return

    if data.startswith("admin:remove_do:"):
        try: uid = int(data.split(":", 2)[2])
        except ValueError:
            await _answer_cb(cb_id, "آیدی نامعتبر"); return
        if uid == chat_id:
            await _answer_cb(cb_id, "خودت رو نمی‌تونی حذف کنی!", alert=True); return
        ok = await remove_admin(uid)
        ids = _get_admin_ids()
        lst = "\n".join(f"• <code>{i}</code>" for i in sorted(ids)) or "—"
        msg = f"✅ <code>{uid}</code> حذف شد.\n\n👥 <b>ادمین‌های فعلی:</b>\n{lst}" if ok else "پیدا نشد."
        await _edit(chat_id, message_id, msg, _admins_kb()); return

    # ── Backup / Restore ────────────────────────────────────────────────
    if data == "backup":
        await _edit(chat_id, message_id,
            "💾 <b>پشتیبان‌گیری</b>\n\n"
            "• <b>دانلود پشتیبان</b>: فایل JSON کامل از همه‌ی کانفیگ‌ها و گروه‌ها\n"
            "• <b>برگرداندن</b>: فایل JSON رو بفرست تا بازیابی کنم",
            _backup_kb()); return

    if data == "backup:download":
        await _send_document(chat_id,
            f"backup-{datetime.now().strftime('%Y%m%d-%H%M')}.json",
            _export_json(), "💾 پشتیبان کامل"); return

    if data == "backup:restore":
        await _edit(chat_id, message_id,
            "📥 فایل JSON پشتیبان رو بفرست 👇",
            {"inline_keyboard":[[{"text":"❌ انصراف","callback_data":"menu"}]]}); return

    if data.startswith("restore:"):
        action = data.split(":", 1)[1]
        ctx = _pending.get(chat_id) or {}
        if ctx.get("action") != "restore_confirm":
            await _answer_cb(cb_id, "منقضی شده"); return
        _pending.pop(chat_id, None)
        if action == "cancel":
            await _edit(chat_id, message_id, "لغو شد.", _main_menu_kb()); return
        incoming = ctx.get("data") or {}
        new_links = incoming.get("links") or {}
        new_subs = incoming.get("subs") or {}
        if action == "replace":
            LINKS.clear(); SUBS.clear()
        added = 0; skipped = 0
        for uid, l in new_links.items():
            if uid in LINKS:
                skipped += 1; continue
            LINKS[uid] = l; added += 1
        for sid, s in new_subs.items():
            if sid not in SUBS: SUBS[sid] = s
        await save_state()
        await _edit(chat_id, message_id,
            f"✅ بازیابی انجام شد.\n\n"
            f"افزوده‌شده: <b>{added}</b>\n"
            f"رد‌شده (تکراری): <b>{skipped}</b>\n"
            f"کل الان: <b>{len(LINKS)}</b>",
            _main_menu_kb()); return

    # ── Export ──────────────────────────────────────────────────────────
    if data == "export":
        await _edit(chat_id, message_id, "📤 فرمت Export:", _export_kb()); return

    if data == "export:json":
        await _send_document(chat_id,
            f"export-{datetime.now().strftime('%Y%m%d-%H%M')}.json",
            _export_json(), "📄 JSON"); return
    if data == "export:csv":
        await _send_document(chat_id,
            f"export-{datetime.now().strftime('%Y%m%d-%H%M')}.csv",
            _export_csv(), "📊 CSV"); return
    if data == "export:txt":
        txt = _export_txt()
        if len(txt) < 4000:
            await _send(chat_id, f"📃 <b>لینک‌ها:</b>\n\n<code>{txt.decode('utf-8')}</code>")
        else:
            await _send_document(chat_id,
                f"links-{datetime.now().strftime('%Y%m%d')}.txt", txt, "📃 لینک‌ها")
        return

    # ── تست نوتیفیکیشن ──────────────────────────────────────────────────
    if data == "testnotif":
        await _edit(chat_id, message_id,
            "🔔 نوتیفیکیشن‌ها فعالن:\n\n"
            f"• انقضا: ۲۴ ساعت قبل\n"
            f"• اتمام حجم: بلافاصله بعد از رسیدن به سقف\n"
            f"• بررسی: هر ۱ ساعت",
            {"inline_keyboard":[[{"text":"🔔 ارسال تست","callback_data":"testnotif:go"}],
                                 [{"text":"⬅ منو","callback_data":"menu"}]]}); return

    if data == "testnotif:go":
        await _send(chat_id, "🔔 <b>تست نوتیفیکیشن</b>\n\n✅ سیستم اطلاع‌رسانی فعاله.")
        return

    # ── ویزارد ──────────────────────────────────────────────────────────
    if data == "newcfg":
        _pending[chat_id] = {"action":"wizard","step":"label","data":{}}
        await _edit(chat_id, message_id, _wizard_prompt("label", {}), _wizard_cancel_kb()); return

    if data == "w:cancel":
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, "لغو شد.", _main_menu_kb()); return

    if data.startswith("w:"):
        pending = _pending.get(chat_id)
        if not pending or pending.get("action") != "wizard":
            await _edit(chat_id, message_id, "این مرحله منقضی شده.", _main_menu_kb()); return
        step = pending["step"]; wd = pending["data"]

        if data == "w:back:family" and step == "transport":
            wd.pop("protocol_family", None)
            pending["step"] = "protocol"
            await _edit(chat_id, message_id, _wizard_prompt("protocol", wd), _wizard_protocol_kb()); return

        if data.startswith("w:family:") and step == "protocol":
            family = data.split(":", 2)[2]
            if family not in ("vless", "vmess", "trojan"):
                family = "vless"
            wd["protocol_family"] = family
            pending["step"] = "transport"
            await _edit(chat_id, message_id, _wizard_prompt("transport", wd), _wizard_transport_kb(family)); return

        if data.startswith("w:transport:") and step == "transport":
            _, _, family, transport = data.split(":", 3)
            if family not in ("vless", "vmess", "trojan"):
                family = "vless"
            if transport not in ("ws", "packet-up", "stream-up"):
                transport = "ws"
            proto = f"{family}-ws" if transport == "ws" else f"{family}-xhttp-{transport}"
            wd["protocol"] = proto if proto in PROTOCOLS else DEFAULT_PROTOCOL
            pending["step"] = "fingerprint"
            await _edit(chat_id, message_id, _wizard_prompt("fingerprint", wd), _wizard_fp_kb()); return

        if data.startswith("w:fp:") and step == "fingerprint":
            fp = data.split(":", 2)[2]
            wd["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
            pending["step"] = "alpn"
            await _edit(chat_id, message_id, _wizard_prompt("alpn", wd), _wizard_alpn_kb()); return

        if data.startswith("w:alpnpreset:") and step == "alpn":
            code = data.split(":", 2)[2]
            wd["alpn"] = ALPN_PRESET_MAP.get(code, "")
            pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wd),
                        _wizard_unlimited_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})")); return

        if data == "w:skip:alpn" and step == "alpn":
            wd["alpn"] = ""; pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wd),
                        _wizard_unlimited_kb("port", f"⏭ پیش‌فرض ({DEFAULT_PORT})")); return
        if data == "w:skip:port" and step == "port":
            wd["port"] = DEFAULT_PORT; pending["step"] = "volume"
            await _edit(chat_id, message_id, _wizard_prompt("volume", wd), _wizard_unlimited_kb("volume")); return
        if data == "w:skip:volume" and step == "volume":
            wd["limit_bytes"] = 0; pending["step"] = "speed"
            await _edit(chat_id, message_id, _wizard_prompt("speed", wd), _wizard_unlimited_kb("speed")); return
        if data == "w:skip:speed" and step == "speed":
            wd["speed_limit_bytes"] = 0; pending["step"] = "iplimit"
            await _edit(chat_id, message_id, _wizard_prompt("iplimit", wd), _wizard_unlimited_kb("iplimit")); return
        if data == "w:skip:iplimit" and step == "iplimit":
            wd["ip_limit"] = 0; pending["step"] = "days"
            await _edit(chat_id, message_id, _wizard_prompt("days", wd), _wizard_unlimited_kb("days")); return
        if data == "w:skip:days" and step == "days":
            wd["expires_days"] = 0; pending["step"] = "confirm"
            await _edit(chat_id, message_id, _wizard_summary(wd), _wizard_confirm_kb()); return

        if data == "w:confirm" and step == "confirm":
            ed = wd.get("expires_days", 0)
            exp = (datetime.now() + timedelta(days=ed)).isoformat() if ed > 0 else None
            uid, link = await make_link(
                label=wd.get("label") or "کانفیگ",
                limit_bytes=wd.get("limit_bytes", 0),
                expires_at=exp,
                protocol=wd.get("protocol", DEFAULT_PROTOCOL),
                fingerprint=wd.get("fingerprint", DEFAULT_FINGERPRINT),
                alpn=wd.get("alpn", ""),
                port=wd.get("port", DEFAULT_PORT),
                ip_limit=wd.get("ip_limit", 0),
                speed_limit_bytes=wd.get("speed_limit_bytes", 0),
            )
            _pending.pop(chat_id, None)
            await _edit(chat_id, message_id, f"✅ ساخته شد.\n\n{_format_detail(uid, link)}",
                        _link_detail_kb(uid, link["active"])); return

        await _answer_cb(cb_id, "دکمه منقضی شده"); return

# ═══════════════════════════════════════════════════════════════════════════
#  INLINE QUERY HANDLER
# ═══════════════════════════════════════════════════════════════════════════
async def _handle_inline(q: dict):
    """Inline mode: کاربر @bot name رو تایپ می‌کنه، لیست کانفیگ‌ها برمی‌گرده."""
    qid = q.get("id"); query = (q.get("query") or "").strip().lower()
    from_id = q.get("from", {}).get("id")
    if not _is_admin(from_id):
        await _call("answerInlineQuery", inline_query_id=qid, results=[], cache_time=0)
        return

    results = []
    for uid, l in list(LINKS.items())[:50]:
        label = l.get("label", "?")
        if query and query not in label.lower() and query not in uid.lower():
            continue
        if not is_link_allowed(l): continue
        try:
            share_link = vless_link_for_link(l, uid, get_host())
        except Exception: continue
        lang = _get_lang(from_id) or "en"
        results.append({
            "type": "article",
            "id": uid,
            "title": label,
            "description": f"{fmt_bytes(l.get('used_bytes',0))} / {('∞' if not l.get('limit_bytes') else fmt_bytes(l['limit_bytes']))}",
            "input_message_content": {
                "message_text": f"<b>{label}</b>\n<code>{share_link}</code>",
                "parse_mode": "HTML",
            },
            "reply_markup": {"inline_keyboard": [[
                {"text": _localize_text("📋 کپی", lang), "switch_inline_query_current_chat": ""}
            ]]},
        })
        if len(results) >= 20: break

    await _call("answerInlineQuery", inline_query_id=qid, results=results,
                cache_time=5, is_personal=True)

# ═══════════════════════════════════════════════════════════════════════════
#  BACKGROUND: NOTIFICATIONS
# ═══════════════════════════════════════════════════════════════════════════
async def _notification_loop():
    """هر ۱ ساعت چک می‌کنه: انقضا نزدیک، اتمام حجم."""
    global _notified
    while _running:
        try:
            await asyncio.sleep(3600)
            admins = _get_admin_ids()
            if not admins: continue
            now = time.time()
            for uid, l in list(LINKS.items()):
                rec = _notified.setdefault(uid, {})

                # انقضا نزدیک (< 24h)
                exp = l.get("expires_at")
                if exp:
                    try:
                        exp_ts = datetime.fromisoformat(exp).timestamp()
                        if 0 < exp_ts - now < 86400 and not rec.get("expiry"):
                            rec["expiry"] = now
                            days_left = max(0, int((exp_ts - now) // 3600))
                            msg = f"⚠️ کانفیگ «{l.get('label','?')}» تا {days_left} ساعت دیگه منقضی می‌شه!"
                            for a in admins: await _send(a, msg)
                    except Exception: pass

                # اتمام حجم
                lim = l.get("limit_bytes", 0)
                used = l.get("used_bytes", 0)
                if lim > 0 and used >= lim and not rec.get("quota"):
                    rec["quota"] = now
                    msg = (f"🚫 کانفیگ «{l.get('label','?')}» به سقف حجم رسید!\n"
                           f"مصرف: {fmt_bytes(used)} / {fmt_bytes(lim)}")
                    for a in admins: await _send(a, msg)
        except asyncio.CancelledError: break
        except Exception as e:
            logger.warning(f"notification loop error: {e}")
            await asyncio.sleep(60)

# ═══════════════════════════════════════════════════════════════════════════
#  BACKGROUND: SCHEDULED REPORT
# ═══════════════════════════════════════════════════════════════════════════
async def _scheduled_report_loop():
    """هر ساعت چک می‌کنه، اگه ساعت گزارش رسیده بود یه گزارش کامل می‌فرسته."""
    global _report_last_sent_date
    while _running:
        try:
            await asyncio.sleep(600)  # هر ۱۰ دقیقه چک کن
            admins = _get_admin_ids()
            if not admins: continue
            now = datetime.now()
            today = now.strftime("%Y-%m-%d")
            target_h, target_m = 9, 0  # ساعت ۹:۰۰ صبح
            try:
                hh, mm = _default_report_time.split(":"); target_h, target_m = int(hh), int(mm)
            except Exception: pass
            if now.hour == target_h and now.minute < 10 and _report_last_sent_date != today:
                _report_last_sent_date = today
                msg = f"📅 <b>گزارش روزانه {today}</b>\n\n{_stats_text()}"
                for a in admins: await _send(a, msg)
        except asyncio.CancelledError: break
        except Exception as e:
            logger.warning(f"scheduled report error: {e}")
            await asyncio.sleep(60)

# ═══════════════════════════════════════════════════════════════════════════
#  POLLING LOOP
# ═══════════════════════════════════════════════════════════════════════════
async def _poll_loop():
    global _running, _bot_username
    offset = 0
    logger.info(f"🤖 Telegram bot polling started (admins: {len(_get_admin_ids())})")
    while _running:
        try:
            res = await _call("getUpdates", offset=offset, timeout=30,
                              allowed_updates=["message", "callback_query", "inline_query"])
            if not res or not res.get("ok"):
                await asyncio.sleep(3); continue
            for upd in res.get("result", []):
                offset = upd["update_id"] + 1
                try:
                    if "message" in upd:
                        m = upd["message"]
                        if m.get("document"):
                            await _handle_document(m)
                        else:
                            await _handle_message(m)
                    elif "callback_query" in upd:
                        await _handle_callback(upd["callback_query"])
                    elif "inline_query" in upd:
                        await _handle_inline(upd["inline_query"])
                except Exception as e:
                    logger.warning(f"Telegram update error: {e}")
        except asyncio.CancelledError: break
        except Exception as e:
            logger.warning(f"poll loop error: {e}")
            await asyncio.sleep(3)

# ═══════════════════════════════════════════════════════════════════════════
#  LIFECYCLE
# ═══════════════════════════════════════════════════════════════════════════
async def start_bot():
    global _client, _poll_task, _notify_task, _report_task, _traffic_task, _running, _bot_username
    token = _get_token()
    admins = _get_admin_ids()
    if not token:
        logger.info("Telegram bot: توکن تنظیم نشده — غیرفعاله.")
        return
    if not admins:
        logger.warning("Telegram bot: TELEGRAM_ADMIN_IDS خالیه — کسی نمی‌تونه مدیریت کنه.")

    if _running and _poll_task and not _poll_task.done():
        await stop_bot()

    await _load_languages()
    await _load_traffic_history()
    _client = httpx.AsyncClient(timeout=httpx.Timeout(40.0, connect=10.0))

    # 🌐 pre-fetch server info (برای نمایش توی آمار)
    try:
        from main import _server_info_cache, _server_info_lock, _cc_to_flag, _cc_to_fa
        import main as _main_mod
        if _main_mod._server_info_cache is None:
            async with _server_info_lock:
                if _main_mod._server_info_cache is None:
                    r = await _client.get(
                        "http://ip-api.com/json/?fields=status,country,countryCode,regionName,city,isp,org,as,query,timezone",
                        timeout=10,
                    )
                    data = r.json()
                    if data.get("status") == "success":
                        cc = data.get("countryCode", "")
                        _main_mod._server_info_cache = {
                            "ip": data.get("query", ""),
                            "country": data.get("country", ""),
                            "country_fa": _cc_to_fa(cc),
                            "country_code": (cc or "").lower(),
                            "flag": _cc_to_flag(cc),
                            "region": data.get("regionName", ""),
                            "city": data.get("city", ""),
                            "isp": data.get("isp", ""),
                            "org": data.get("org", ""),
                            "asn": data.get("as", ""),
                            "timezone": data.get("timezone", ""),
                        }
                        logger.info(f"Server info cached: {_main_mod._server_info_cache['ip']}")
    except Exception as e:
        logger.warning(f"prefetch server info failed: {e}")

    # پاک کردن webhook (رفع 409)
    try:
        r = await _client.post(f"{_api_base()}/deleteWebhook", params={"drop_pending_updates": "false"})
        data = r.json()
        if data.get("ok"): logger.info("Telegram webhook cleared")
    except Exception as e:
        logger.warning(f"deleteWebhook error: {e}")

    # کشف username برای inline
    ok, username = await validate_token(token)
    if ok and username: _bot_username = username

    _running = True
    _poll_task = asyncio.create_task(_poll_loop())
    _notify_task = asyncio.create_task(_notification_loop())
    _report_task = asyncio.create_task(_scheduled_report_loop())
    _traffic_task = asyncio.create_task(_traffic_history_loop())
    logger.info(f"🤖 Telegram bot started (admins: {len(admins)}, bot: @{_bot_username or '?'})")

async def stop_bot():
    global _running, _client, _poll_task, _notify_task, _report_task, _traffic_task
    _running = False
    for t in (_poll_task, _notify_task, _report_task, _traffic_task):
        if t:
            t.cancel()
            try: await t
            except (asyncio.CancelledError, Exception): pass
    _poll_task = _notify_task = _report_task = _traffic_task = None
    if _client:
        try: await _client.aclose()
        except Exception: pass
        _client = None