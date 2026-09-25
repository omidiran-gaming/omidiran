# pages.py - OMID-IRAN PANEL v1.2.5
# شامل: LOGIN_HTML, DASHBOARD_HTML
# (get_public_page_html به public_page.py منتقل شد)

# لوگوی OMID (به‌صورت base64 داخلی)
LOGO_B64 = "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"

# Central bilingual dictionary. Edit LANG_FA / LANG_EN below; injected into Login and Dashboard.
LANG_CENTER_JS = r"""/* ═══════════════════════════════════════════════════════════════════════
   OMID LANGUAGE CENTER · ENGLISH IS THE CANONICAL UI LANGUAGE
   The HTML/JS UI is authored in English. Persian is a runtime translation.
   IMPORTANT: Never translate already-translated DOM text. Each text node and
   UI attribute is anchored to its original English source string.
   ═══════════════════════════════════════════════════════════════════════ */
const OMID_EN_TO_FA = {"optional":"اختیاری","e.g.":"مثلاً","Test Connection":"تست اتصال","Save & Start":"ذخیره و روشن کردن","Stop Bot":"توقف ربات","comma separated: 123,456":"با کاما جدا کن: 123,456","To get your Admin ID, start":"برای دریافت Admin ID، توی ربات","on Telegram. If left empty, nobody can use the bot.":"رو استارت کن. اگه خالی بذاری، هیچ‌کس نمی‌تونه از ربات استفاده کنه.","(via @BotFather)":"(از @BotFather)","Checking...":"در حال بررسی...","Online & Running":"روشن و در حال کار","Stopped (token saved)":"متوقف (توکن ذخیره‌شده)","Enter the token":"توکن را وارد کنید","Testing...":"در حال تست...","Token is valid":"توکن معتبر است","Invalid token":"توکن نامعتبر است","Token is required":"توکن الزامی است","Enter at least one Admin ID":"حداقل یک Admin ID وارد کنید","Saving and starting bot...":"در حال ذخیره و روشن کردن ربات...","Bot started":"ربات روشن شد","Bot stopped":"ربات متوقف شد","Stopping...":"در حال توقف...","Stop the bot? (token will be saved)":"مطمئنی ربات رو متوقف کنم؟ (توکن ذخیره می‌مونه)","Failed to stop":"خطا در توقف","Delete":"حذف","UUID is generated randomly":"UUID به‌صورت تصادفی تولید می‌شود","Only registered UUIDs may connect":"فقط UUIDهای ثبت‌شده اجازه اتصال دارند","Random UUID · pick quota, expiry and protocol":"UUID تصادفی · سهمیه، انقضا و پروتکل را انتخاب کنید","Protocol cannot be changed after creation":"پروتکل پس از ساخت قابل تغییر نیست","Link copied":"لینک کپی شد","Sub link copied":"لینک ساب کپی شد","UUID copied":"UUID کپی شد","IP copied":"IP کپی شد","IP · Server Location":"IP · لوکیشن سرور","Activated ✓":"فعال شد ✓","Activated":"فعال شد","Deactivated":"غیرفعال شد","Error":"خطا","Usage reset ✓":"مصرف ریست شد ✓","Refreshed":"رفرش شد","Enter UUID":"UUID را وارد کنید","No changes to save":"تغییری برای ذخیره وجود ندارد","Group configurations saved ✓":"کانفیگ‌های گروه ذخیره شدند ✓","✓ Connected - Valid UUID":"✓ متصل - UUID معتبر","✗ Error - Invalid or inactive UUID":"✗ خطا - UUID نامعتبر یا غیرفعال","Copied":"کپی شد","Sign in to Control Center":"ورود به مرکز کنترل","SYSTEM ONLINE":"سیستم آنلاین","Test message...":"پیام تست...","Connected: ":"اتصال: ","Sent: ":"ارسال: ","Received ":"دریافت ","Closed (":"قطع (","Subscription":"سابسکریپشن","Session":"سشن","Disconnect":"قطع","Strong":"قوی","PANEL":"پنل","Help":"کمک","Copy":"کپی","Logout":"خروج","Refresh":"رفرش","Live":"زنده","Weak":"ضعیف","Active":"فعال","Usage":"مصرف","Version":"نسخه","Unit":"واحد","Sign In":"ورود","Group":"گروه","1 GB":"۱ GB","5 GB":"۵ GB","Connect":"اتصال","Send":"ارسال","of total":"از کل","Security":"امنیت","Night Mode":"تم شب","Distribution":"توزیع","Errors":"خطاها","SYSTEM":"سیستم","Title":"عنوان","Medium":"متوسط","Expired":"منقضی","All":"همه","10 GB":"۱۰ GB","50 GB":"۵۰ GB","7 days":"۷ روز","Online":"آنلاین","Uptime":"آپتایم","Cancel":"انصراف","Traffic":"ترافیک","Protected":"رمزدار","Password hash":"هش رمز","Edit":"ویرایش","Public":"پابلیک","Platform":"پلتفرم","Configurations":"کانفیگ‌ها","Copy IP":"کپی IP","0 groups":"۰ گروه","1 Mbps":"۱ Mbps","30 days":"۳۰ روز","5 Mbps":"۵ Mbps","500 MB":"۵۰۰ MB","90 days":"۹۰ روز","Connections":"اتصالات","Light Mode":"تم روشن","Settings":"تنظیمات","Dashboard":"داشبورد","Custom...":"دستی...","Inactive":"غیرفعال","Active v9":"فعال v9","Clear All":"لغو همه","Average":"میانگین","Unlimited":"نامحدود","Sign in to":"ورود به","Copy all":"کپی همه","GitHub":"گیت‌هاب","Note":"یادداشت","1 user":"۱ کاربر","10 Mbps":"۱۰ Mbps","2 users":"۲ کاربر","25 Mbps":"۲۵ Mbps","5 users":"۵ کاربر","Relative Load":"بار نسبی","Open":"باز کردن","Dark Mode":"تم تاریک","Deleted ✓":"حذف شد ✓","New Password":"رمز جدید","Password":"رمز عبور","Current Password":"رمز فعلی","Encryption":"رمزنگاری","Framework":"فریم‌ورک","Password strength":"قدرت رمز","Group Name":"نام گروه","Support":"پشتیبانی","Usage peak":"پیک مصرف","Copied ✓":"کپی شد ✓","Copy link":"کپی لینک","Very weak":"خیلی ضعیف","Reset usage":"ریست مصرف","Create Group":"ساخت گروه","Error Logs":"لاگ خطاها","Connection duration":"مدت اتصال","Protocols":"پروتکل‌ها","Support:":"پشتیبانی:","Total Traffic":"کل ترافیک","New Group":"گروه جدید","MB per hour":"MB در ساعت","Theme":"تم","Account Security":"امنیت حساب","selected":"انتخاب شده","Select All":"انتخاب همه","Storage":"ذخیره‌سازی","Subscriptions":"سابسکریپشن","Free For All":"رایگان برای همه","Username":"نام کاربری","Connection Port":"پورت اتصال","icon.":"کلیک کنید.","0 = Unlimited":"0 = نامحدود","Expiry date":"تاریخ انقضا","Creation failed":"خطا در ساخت","Create Configuration":"ساخت کانفیگ","Service Status":"وضعیت سرویس","Active Configs":"کانفیگ فعال","Lowest usage":"کمترین مصرف","Access Group":"گروه دسترسی","Close":"بستن","Save":"ذخیره","Active Connections":"اتصالات فعال","No description":"بدون توضیحات","Save failed":"خطا در ذخیره","Traffic Quota":"سهمیه ترافیک","Configuration ID":"شناسه کانفیگ","Enable/Disable":"فعال/غیرفعال","Connection List":"لیست اتصالات","Speed Limit":"محدودیت سرعت","Enter Group":"ورود به گروه","Default port":"پورت پیش‌فرض","Telegram Channel":"کانال تلگرام","Limited Config":"کانفیگ محدود","Access Control":"کنترل دسترسی","Copy subscription link":"کپی لینک ساب","Subscription Groups":"گروه‌های ساب","0 selected":"۰ انتخاب شده","● Active (443)":"● فعال (443)","Since startup":"از راه‌اندازی","Peak hour":"بالاترین ساعت","WebSocket Test":"تست WebSocket","Update failed":"خطا در ویرایش","Save Changes":"ذخیره تغییرات","CDN compatible":"سازگار با CDN","Active · 3 modes":"فعال · 3 mode","Activity Logs":"لاگ فعالیت‌ها","Link copied ✓":"لینک کپی شد ✓","IP Limit":"محدودیت آی‌پی","Hourly average":"میانگین ساعتی","All configurations":"همه کانفیگ‌ها","Edit Configuration":"ویرایش کانفیگ","Configuration Type":"نوع کانفیگ","Transport":"ترابرد","Lightweight & versatile":"سبک و همه‌منظوره","Compatible with clients":"سازگار با کلاینت‌ها","TLS · Password · lightweight":"TLS · رمزعبور · سبک","Stable & widely supported":"پایدار و شناخته‌شده","Highly CDN-compatible":"سازگاری بالا با CDN","Stream-based upload & download":"آپلود و دانلود جریان‌محور","Transport Protocol":"پروتکل انتقال","Configuration deleted":"کانفیگ حذف شد","Group deleted ✓":"گروه حذف شد ✓","— No group —":"— بدون گروه —","Unique IPs":"آی‌پی‌های یکتا","Lower latency":"تاخیر پایین‌تر","Confirm New Password":"تکرار رمز جدید","Signing in...":"در حال ورود...","Wrong password":"رمز اشتباه است","Waiting for connection...":"منتظر اتصال...","No errors":"هیچ خطایی نیست","Protocol default":"پیش‌فرض پروتکل","Language":"زبان","Delete this configuration?":"حذف این کانفیگ؟","Load failed":"خطا در بارگذاری","Configuration Summary":"خلاصه کانفیگ‌ها","Contact Channels":"راه‌های ارتباطی","Subscription link copied":"لینک ساب کپی شد","Custom ALPN":"مقدار دستی ALPN","New Username":"نام کاربری جدید","Hide link":"پنهان کردن لینک","Active configurations":"کانفیگ‌های فعال","Total traffic usage":"کل ترافیک مصرفی","Group created ✓":"گروه ساخته شد ✓","HttpOnly · 7 days":"HttpOnly · 7 روز","Last update:":"آخرین بروزرسانی:","Online · OMIDIRAN":"آنلاین · OMIDIRAN","Search configurations...":"جستجوی کانفیگ...","Group creation failed":"خطا در ساخت گروه","Loading...":"در حال بارگذاری...","Save Account Security":"ذخیره امنیت حساب","Traffic usage trend":"روند مصرف ترافیک","e.g. User Ali":"مثلاً: کاربر علی","Subscription group & expiry":"گروه ساب و انقضا","Hourly Traffic (MB)":"ترافیک ساعتی (MB)","Description (optional)":"توضیحات (اختیاری)","Contains a number · Number":"شامل عدد · Number","Active · strict":"فعال · سخت‌گیرانه","Manage Configurations":"مدیریت کانفیگ‌ها","Average connection duration":"میانگین مدت اتصال","Show configuration link":"نمایش لینک کانفیگ","No groups yet":"هنوز گروهی ندارید","Configuration created ✓":"کانفیگ ساخته شد ✓","Note (optional)":"یادداشت (اختیاری)","FA / EN · Bilingual":"FA / EN · دو زبانه","Public link copied":"لینک پابلیک کپی شد","No activity logs yet":"هنوز لاگی ثبت نشده","Configuration updated ✓":"کانفیگ ویرایش شد ✓","No configuration exists":"کانفیگی وجود ندارد","UUID of an active configuration":"UUID یک کانفیگ فعال","Search groups...":"جستجو در گروه‌ها...","Public subscription page password":"رمز صفحه پابلیک ساب","Current password is required":"رمز فعلی الزامی است","Quota (0 = Unlimited)":"سهمیه (0 = نامحدود)","Configuration enabled/disabled":"فعال/غیرفعال کانفیگ","Stable & general purpose":"پایدار و همه‌منظوره","● Optional · SHA-256":"● اختیاری · SHA-256","Strict UUID Auth":"UUID Auth سخت‌گیرانه","Realtime traffic total":"مجموع ترافیک لحظه‌ای","No active connections":"هیچ اتصال فعالی نیست","ALPN (blank = default)":"ALPN (خالی = پیش‌فرض)","Total Usage":"کل مصرف","Enter password":"رمز عبور را وارد کنید","Only when changing the password":"فقط در صورت تغییر رمز","No configuration to copy":"کانفیگی برای کپی نیست","Leave empty = no password":"خالی بگذارید = بدون رمز","NEW PASSWORD":"رمز جدید","Full subscription (admin)":"سابسکریپشن کامل (ادمین)","Group subscription links":"لینک سابسکریپشن گروه‌ها","Enter username":"نام کاربری را وارد کنید","No configurations yet":"هنوز کانفیگی وجود ندارد","Expiry (days) · 0 = unlimited":"انقضا (روز) · 0 = نامحدود","New passwords do not match":"تکرار رمز جدید یکسان نیست","Admin Account":"حساب مدیر","Public Page Password (optional)":"رمز صفحه پابلیک (اختیاری)","Your connection is encrypted":"اتصال شما رمزنگاری‌شده است","Based on megabytes per hour":"بر اساس مگابایت در هر ساعت","Minimum 4 characters · 4+ chars":"حداقل ۴ کاراکتر · 4+ chars","Single subscription (per configuration)":"سابسکریپشن تکی (هر کانفیگ)","Create New Group":"ساخت گروه جدید","Includes all active configurations.":"شامل تمام کانفیگ‌های فعال.","Speed Limit (0 = Unlimited)":"محدودیت سرعت (0 = نامحدود)","Auto-refresh every 5 seconds":"بروزرسانی خودکار هر ۵ ثانیه","Complete panel event history":"تاریخچه کامل رخدادهای پنل","Mixed case":"حروف بزرگ/کوچک","CURRENT PASSWORD":"رمز فعلی","Default Link (Unlimited)":"لینک پیش‌فرض (بدون محدودیت)","IP Limit (0 = Unlimited)":"محدودیت آی‌پی (0 = نامحدود)","Enter to save changes":"برای ذخیره تغییرات وارد کنید","Changes apply immediately":"تغییرات بلافاصله اعمال می‌شود","New password must be at least 4 characters":"رمز جدید باید حداقل ۴ کاراکتر باشد","Concurrent IP / user limit":"محدودیت آی‌پی / کاربر هم‌زمان","NEW USERNAME":"نام کاربری جدید","Live Connections":"اتصالات زنده","Manage panel login credentials":"اطلاعات ورود پنل را مدیریت کنید","Account updated successfully ✓":"اطلاعات حساب با موفقیت ذخیره شد ✓","CONFIRM PASSWORD":"تکرار رمز جدید","Save account information":"ذخیره اطلاعات حساب","Subscription links for v2ray apps":"لینک‌های اشتراک برای اپ‌های v2ray","Username cannot contain spaces":"نام کاربری نباید فاصله داشته باشد","Bandwidth usage analysis & monitoring":"تحلیل و مانیتورینگ مصرف پهنای باند","443 (TLS) · configurable per configuration":"443 (TLS) · قابل تغییر در هر کانفیگ","Empty = no change · minimum 4 characters":"خالی = بدون تغییر · حداقل ۴ کاراکتر","Delete this group? Configurations will not be deleted.":"حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.","UUID (must exist in configurations)":"UUID (باید در کانفیگ‌ها وجود داشته باشد)","Username must be 3–32 characters":"نام کاربری باید بین ۳ تا ۳۲ کاراکتر باشد","Live IP and traffic monitoring for each connection":"مانیتورینگ زنده آی‌پی و ترافیک هر اتصال","Expiry (days from now, 0 = unchanged/unlimited)":"انقضا (روز از الان، 0 = بدون تغییر/نامحدود)","Copy all active links in this group":"تمام لینک‌های فعال این گروه را یک‌جا کپی کن","Copy all configurations":"کپی همه کانفیگ‌ها","Enter your credentials to access the control panel":"برای ورود به پنل مشخصات دسترسی خود را وارد کنید","Leave expiry at zero to keep the current expiry.":"برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.","Connections appear here as clients connect":"به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند","Create and manage configs with quota, expiry and groups":"ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی","Create a dedicated public page for managing configurations":"یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید","Manage panel username and password here":"نام کاربری و رمز عبور پنل را از همین‌جا مدیریت کنید","Each group has a separate public page with its own configurations":"هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد","Select the configurations for this group":"کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید","Each configuration has its own subscription URL. From the configuration card, click the":"هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون","Create a new group to organize configurations":"یک New Group / گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید","This group is password protected. Enter the password to view its configurations.":"این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز را وارد کنید.","This URL only works in the browser signed in to the panel (session cookie required).":"این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).","This group public page will be available through a unique internet link.":"صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.","Current password is required to change username or password. Existing sessions will be closed when saved.":"برای تغییر نام کاربری یا رمز، رمز فعلی الزامی است. با ذخیره تغییرات، نشست‌های قبلی بسته می‌شوند.","Only registered active UUIDs may connect (this is a VLESS/WS test; XHTTP is tested from the client).":"فقط UUIDهای ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).","Telegram Bot":"ربات تلگرام","Manage Telegram bot for remote panel control":"مدیریت ربات تلگرام برای کنترل پنل از راه دور","Status:":"وضعیت:","Random":"تصادفی","Short description for this group":"توضیح کوتاه درباره این گروه","Server IP":"IP سرور","Clear":"پاک کردن","New Configuration":"کانفیگ جدید","Connected IPs / limit":"آی‌پی‌های متصل / محدودیت","Default Link":"لینک پیش‌فرض","MB":"مگابایت","Bot:":"ربات:","Protocol":"پروتکل"};
Object.assign(OMID_EN_TO_FA, {
  'Access denied':'دسترسی رد شد',
  'Connections':'اتصالات',
  'Connection':'اتصال',
  'seconds':'ثانیه',
  'minutes':'دقیقه',
  'hours':'ساعت',
  'errors':'خطا',
  'Error':'خطا',
  'OMID-IRAN PANEL · Login':'OMID-IRAN PANEL · ورود'
});

const OMID_EN_RULES = Object.entries(OMID_EN_TO_FA)
  .sort((a,b)=>b[0].length-a[0].length);
const OMID_TEXT_SOURCE = new WeakMap();
const OMID_ATTR_SOURCE = new WeakMap();

function omidFaDigits(value){
  return String(value).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);
}
function omidPreserveOuterSpace(raw, core){
  const s=String(raw??'');
  const lead=(s.match(/^\s*/)||[''])[0];
  const trail=(s.match(/\s*$/)||[''])[0];
  return lead+core+trail;
}
function omidTranslateDynamic(core){
  let m;
  if((m=core.match(/^(\d+)\s+selected$/i))) return `${omidFaDigits(m[1])} انتخاب شده`;
  if((m=core.match(/^(\d+)\s+configurations$/i))) return `${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^of\s+(\d+)\s+configurations$/i))) return `از کل ${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^(\d+)\s+groups$/i))) return `${omidFaDigits(m[1])} گروه`;
  if((m=core.match(/^(\d+)\s+connections$/i))) return `${omidFaDigits(m[1])} اتصال`;
  if((m=core.match(/^(\d+)\s+errors$/i))) return `${omidFaDigits(m[1])} خطا`;
  if((m=core.match(/^(\d+)\s+seconds$/i))) return `${omidFaDigits(m[1])} ثانیه`;
  if((m=core.match(/^(\d+)\s+minutes$/i))) return `${omidFaDigits(m[1])} دقیقه`;
  if((m=core.match(/^(\d+)\s+hours$/i))) return `${omidFaDigits(m[1])} ساعت`;
  if((m=core.match(/^(\d+)\s+days remaining$/i))) return `${omidFaDigits(m[1])} روز مانده`;
  if((m=core.match(/^Last update:\s*(.*)$/i))) return `آخرین بروزرسانی: ${m[1]}`;
  if((m=core.match(/^Connected:\s*(.*)$/i))) return `اتصال: ${m[1]}`;
  if((m=core.match(/^Sent:\s*(.*)$/i))) return `ارسال: ${m[1]}`;
  if((m=core.match(/^Received\s+(.*)$/i))) return `دریافت ${m[1]}`;
  if((m=core.match(/^Closed \((.*)$/i))) return `قطع (${m[1]}`;
  if((m=core.match(/^\[(.+)\] (.+)$/s))) return `[${m[1]}] ${m[2]}`;
  return null;
}
function omidTranslateText(raw, lang){
  const s=String(raw??'');
  if(lang==='en' || !s.trim()) return s;
  const core=s.trim();
  if(Object.prototype.hasOwnProperty.call(OMID_EN_TO_FA,core)){
    return omidPreserveOuterSpace(s,OMID_EN_TO_FA[core]);
  }
  const dynamic=omidTranslateDynamic(core);
  if(dynamic!==null) return omidPreserveOuterSpace(s,dynamic);

  // Safe phrase translation: only known English phrases are replaced, and
  // only against the immutable English source string stored for the node.
  let out=core;
  for(const [en,fa] of OMID_EN_RULES){
    if(out.includes(en)) out=out.split(en).join(fa);
  }
  return omidPreserveOuterSpace(s,out);
}
function omidRememberText(node){
  if(!OMID_TEXT_SOURCE.has(node)) OMID_TEXT_SOURCE.set(node,node.nodeValue);
  return OMID_TEXT_SOURCE.get(node);
}
function omidRememberAttr(el,attr){
  let rec=OMID_ATTR_SOURCE.get(el);
  if(!rec){rec={};OMID_ATTR_SOURCE.set(el,rec);}
  if(rec[attr]===undefined) rec[attr]=el.getAttribute(attr) || '';
  return rec[attr];
}
function omidApplyLanguage(root,lang){
  const target=root||document.body;
  if(!target) return;
  const walker=document.createTreeWalker(target,NodeFilter.SHOW_TEXT);
  const nodes=[];
  while(walker.nextNode()){
    const n=walker.currentNode;
    const p=n.parentElement;
    if(!p || !n.nodeValue || !n.nodeValue.trim()) continue;
    if(['SCRIPT','STYLE','NOSCRIPT','CODE','PRE'].includes(p.tagName)) continue;
    if(p.closest('[data-i18n-ignore="true"]')) continue;
    nodes.push(n);
  }
  for(const n of nodes){
    const source=omidRememberText(n);
    n.nodeValue=omidTranslateText(source,lang);
  }
  const attrs=['placeholder','title','aria-label'];
  target.querySelectorAll('input,button,select,textarea,[title],[aria-label]').forEach(el=>{
    for(const attr of attrs){
      if(!el.hasAttribute(attr)) continue;
      el.setAttribute(attr,omidTranslateText(omidRememberAttr(el,attr),lang));
    }
  });
  document.documentElement.lang=lang;
  document.documentElement.dir=lang==='en'?'ltr':'rtl';
}
"""




# ── Shared theme CSS: injected into LOGIN_HTML and DASHBOARD_HTML ──
_THEME_CSS = '/* ═══════════════════════════════════════════════════════════════════════\n   OMID-IRAN PANEL · SHARED THEME TOKENS\n   Dark  → OMID Glass Premium (purple / pink)\n   Light → Arctic Premium (frosted blue / lavender / ice)\n   Both LOGIN_HTML and DASHBOARD_HTML consume these exact tokens.\n   ═══════════════════════════════════════════════════════════════════════ */\n\n:root{\n  color-scheme:dark;\n\n  /* ── Background ── */\n  --bg:#0a0416;\n  --bg-2:#10061f;\n  --bg-gradient:\n    radial-gradient(ellipse 62% 52% at 18% 16%,rgba(167,139,250,.30),transparent 62%),\n    radial-gradient(ellipse 56% 48% at 84% 22%,rgba(236,72,153,.22),transparent 62%),\n    radial-gradient(ellipse 62% 54% at 50% 96%,rgba(59,130,246,.18),transparent 66%);\n  --grid:rgba(167,139,250,.026);\n\n  /* ── Glass surfaces ── */\n  --surface:rgba(255,255,255,.065);\n  --surface-2:rgba(255,255,255,.045);\n  --surface-3:rgba(8,4,20,.34);\n  --surface-solid:#17172a;\n  --glass:rgba(20,10,40,.74);\n  --glass-strong:rgba(17,8,34,.86);\n  --overlay:rgba(0,0,0,.70);\n\n  /* ── Borders ── */\n  --card-b:rgba(255,255,255,.10);\n  --card-bh:rgba(255,255,255,.22);\n  --hairline:rgba(255,255,255,.07);\n\n  /* ── Accent / OMID Glass Premium ── */\n  --accent:#a78bfa;\n  --accent-2:#ec4899;\n  --accent-3:#7c3aed;\n  --accent-soft:rgba(167,139,250,.15);\n  --accent-soft-2:rgba(236,72,153,.11);\n  --accent-grad:linear-gradient(135deg,#a78bfa 0%,#ec4899 100%);\n  --accent-grad-reverse:linear-gradient(135deg,#ec4899 0%,#7c3aed 100%);\n  --accent-shadow:0 12px 30px rgba(167,139,250,.42);\n  --accent-glow:0 0 10px rgba(167,139,250,.55);\n  --info:#29a2dc;\n  --info-2:#186ea5;\n  --info-grad:linear-gradient(135deg,#29a2dc,#186ea5);\n  --info-soft:rgba(41,162,220,.12);\n\n  /* ── Status ── */\n  --green:#4ade80;\n  --green-bg:rgba(74,222,128,.14);\n  --green-t:#4ade80;\n  --red:#f87171;\n  --red-bg:rgba(248,113,113,.14);\n  --red-t:#f87171;\n  --amber:#fbbf24;\n  --amber-bg:rgba(251,191,36,.14);\n  --amber-t:#fbbf24;\n  --purple:#a78bfa;\n  --purple-bg:rgba(167,139,250,.14);\n\n  /* ── Text ── */\n  --t1:#ffffff;\n  --t2:rgba(255,255,255,.66);\n  --t3:rgba(255,255,255,.45);\n  --muted:rgba(255,255,255,.36);\n\n  /* ── Shape / shadow ── */\n  --radius:20px;\n  --radius-sm:14px;\n  --radius-xs:11px;\n  --sidebar-w:280px;\n  --shadow:0 20px 60px rgba(0,0,0,.50);\n  --shadow-sm:0 8px 24px rgba(0,0,0,.28);\n  --glass-shadow:0 22px 60px rgba(0,0,0,.30),inset 0 1px 0 rgba(255,255,255,.15);\n  --focus-ring:0 0 0 3px rgba(167,139,250,.12);\n\n  /* ── Login-only helpers ── */\n  --login-card:linear-gradient(145deg,rgba(255,255,255,.085),rgba(255,255,255,.025));\n  --login-input:rgba(0,0,0,.18);\n  --login-textarea:rgba(0,0,0,.16);\n}\n\n/* ═══════════════════════════════════════════════════════════════════════\n   LIGHT · ARCTIC PREMIUM ❄️\n   Reference palette: frosted white + ice blue + lavender.\n   This replaces the previous light theme completely.\n   ═══════════════════════════════════════════════════════════════════════ */\nhtml[data-theme="light"],\nhtml[data-login-theme="light"]{\n  color-scheme:light;\n\n  /* Arctic Premium — muted turquoise / ice cyan */\n  --bg:#e7f2f4;\n  --bg-2:#d9ecef;\n  --bg-gradient:\n    radial-gradient(ellipse 58% 48% at 14% 10%,rgba(92,166,177,.28),transparent 60%),\n    radial-gradient(ellipse 56% 46% at 88% 18%,rgba(110,142,206,.18),transparent 62%),\n    radial-gradient(ellipse 58% 48% at 50% 94%,rgba(127,190,207,.22),transparent 64%),\n    linear-gradient(135deg,#e6f1f3 0%,#eaf5f6 48%,#e8eff6 100%);\n  --grid:rgba(58,126,140,.035);\n\n  /* Frosted surfaces — intentionally not pure white */\n  --surface:rgba(240,249,250,.74);\n  --surface-2:rgba(231,245,247,.62);\n  --surface-3:rgba(210,231,235,.34);\n  --surface-solid:#eaf5f6;\n  --glass:linear-gradient(145deg,rgba(241,249,250,.82),rgba(221,239,242,.70));\n  --glass-strong:rgba(237,247,248,.92);\n  --overlay:rgba(25,67,75,.20);\n\n  --card-b:rgba(65,130,143,.18);\n  --card-bh:rgba(65,130,143,.34);\n  --hairline:rgba(65,130,143,.10);\n\n  /* Cool turquoise + muted cornflower accent */\n  --accent:#4f9da8;\n  --accent-2:#7188d5;\n  --accent-3:#3f7f8a;\n  --accent-soft:rgba(79,157,168,.13);\n  --accent-soft-2:rgba(113,136,213,.10);\n  --accent-grad:linear-gradient(135deg,#4f9da8 0%,#7188d5 100%);\n  --accent-grad-reverse:linear-gradient(135deg,#7188d5 0%,#4f9da8 100%);\n  --accent-shadow:0 12px 28px rgba(79,157,168,.24);\n  --accent-glow:0 0 12px rgba(79,157,168,.30);\n\n  --info:#4d9fbe;\n  --info-2:#397b99;\n  --info-grad:linear-gradient(135deg,#69bdd4,#4f8fb2);\n  --info-soft:rgba(77,159,190,.10);\n\n  --green:#149273;\n  --green-bg:rgba(20,146,115,.10);\n  --green-t:#087158;\n  --red:#cf5b5b;\n  --red-bg:rgba(207,91,91,.08);\n  --red-t:#ab4141;\n  --amber:#c58a2c;\n  --amber-bg:rgba(197,138,44,.10);\n  --amber-t:#9f6a17;\n  --purple:#7779bf;\n  --purple-bg:rgba(119,121,191,.09);\n\n  --t1:#27454c;\n  --t2:#4d6970;\n  --t3:#7e969c;\n  --muted:#7e969c;\n\n  --shadow:0 18px 46px rgba(60,112,121,.13);\n  --shadow-sm:0 8px 24px rgba(60,112,121,.09);\n  --glass-shadow:0 20px 60px rgba(60,112,121,.13),inset 0 1px 0 rgba(255,255,255,.72);\n  --focus-ring:0 0 0 3px rgba(79,157,168,.10);\n\n  --login-card:linear-gradient(145deg,rgba(241,249,250,.88),rgba(222,239,242,.76));\n  --login-input:rgba(235,247,248,.86);\n  --login-textarea:rgba(225,241,243,.78);\n}\n\nhtml[data-theme="light"] body,\nhtml[data-login-theme="light"] body{\n  background-color:var(--bg);\n  background-image:var(--bg-gradient);\n}\n\nhtml[data-theme="light"] body::before,\nhtml[data-login-theme="light"] body::before{\n  background-image:\n    linear-gradient(rgba(124,140,248,.035) 1px,transparent 1px),\n    linear-gradient(90deg,rgba(124,140,248,.035) 1px,transparent 1px),\n    radial-gradient(circle at 50% 8%,rgba(202,235,239,.45),transparent 46%);\n  background-size:44px 44px,44px 44px,auto;\n}\n'
_LOGIN_CSS = '/* ═════════ LOGIN LAYOUT · shared token based ═════════ */\n*{box-sizing:border-box;margin:0;padding:0}\nhtml,body{min-height:100%;font-family:\'Vazirmatn\',sans-serif}\nhtml{background:var(--bg);background-image:var(--bg-gradient);background-attachment:fixed;scroll-behavior:smooth}\nbody{\n  display:grid;place-items:center;overflow:hidden;position:relative;\n  background-color:var(--bg);background-image:var(--bg-gradient);\n  background-attachment:fixed;color:var(--t1);\n  -webkit-font-smoothing:antialiased;\n  transition:background-color .3s,color .3s;\n}\nbody::before{\n  content:"";position:fixed;inset:0;pointer-events:none;\n  background-image:\n    linear-gradient(var(--grid) 1px,transparent 1px),\n    linear-gradient(90deg,var(--grid) 1px,transparent 1px),\n    radial-gradient(circle at 50% 24%,rgba(255,255,255,.035),transparent 46%);\n  background-size:44px 44px,44px 44px,auto;\n  mask-image:radial-gradient(ellipse at center,black 12%,transparent 78%);\n  -webkit-mask-image:radial-gradient(ellipse at center,black 12%,transparent 78%);\n}\nbody::after{\n  content:"";position:fixed;inset:0;pointer-events:none;\n  background:\n    radial-gradient(circle at 10% 0%,var(--accent-soft),transparent 28%),\n    radial-gradient(circle at 92% 100%,var(--accent-soft-2),transparent 30%);\n  opacity:.65;\n}\n.scan{\n  position:fixed;left:0;right:0;top:0;height:1px;\n  background:linear-gradient(90deg,transparent,var(--accent),var(--accent-2),transparent);\n  box-shadow:0 0 22px var(--accent);\n  animation:scan 6s linear infinite;opacity:.55;z-index:4;\n}\n@keyframes scan{0%{transform:translateY(0)}100%{transform:translateY(100vh)}}\n\n.shell{width:min(460px,calc(100% - 28px));position:relative;z-index:2}\n.hud{\n  display:flex;justify-content:space-between;align-items:center;\n  margin-bottom:13px;gap:8px;\n}\n.kicker{\n  font-size:9px;letter-spacing:.18em;color:var(--t3);\n  font-weight:800;text-transform:uppercase;\n}\n.lang{\n  border:1px solid var(--card-b);background:var(--surface-2);color:var(--accent);\n  border-radius:11px;padding:8px 10px;font:700 10px Vazirmatn,sans-serif;\n  cursor:pointer;transition:.18s;backdrop-filter:blur(18px);\n}\n.lang:hover{background:var(--accent-soft);border-color:var(--card-bh);transform:translateY(-1px)}\n#theme-login{min-width:34px}\n\n.card{\n  background:var(--login-card);\n  border:1px solid var(--card-b);\n  border-radius:28px;padding:28px;\n  box-shadow:var(--glass-shadow);\n  backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);\n  position:relative;overflow:hidden;\n  transition:background .3s,border-color .3s,box-shadow .3s;\n}\n.card::before{\n  content:"";position:absolute;inset:0;pointer-events:none;\n  background:\n    linear-gradient(120deg,transparent 0 34%,rgba(205,235,239,.10) 47%,transparent 57%),\n    radial-gradient(circle at 0% 0%,var(--accent-soft),transparent 34%);\n}\n.card::after{\n  content:"";position:absolute;top:0;inset-inline-start:12%;\n  width:76%;height:1px;pointer-events:none;\n  background:linear-gradient(90deg,transparent,var(--accent),var(--accent-2),transparent);\n  opacity:.55;box-shadow:0 0 12px var(--accent);\n}\n.brand{display:flex;align-items:center;gap:13px;margin-bottom:25px;position:relative;z-index:1}\n.brand-img{\n  width:56px;height:56px;border-radius:16px;overflow:hidden;\n  background:var(--accent-grad);border:1px solid var(--card-bh);\n  box-shadow:var(--accent-shadow),inset 0 1px 0 rgba(255,255,255,.28);\n}\n.brand-img img{width:100%;height:100%;object-fit:cover}\n.brand-name{font-size:15px;font-weight:900;letter-spacing:.04em;color:var(--t1)}\n.brand-sub{font-size:9px;color:var(--t3);margin-top:3px;text-transform:uppercase;letter-spacing:.13em}\n\nh1{\n  font-size:24px;line-height:1.35;font-weight:900;letter-spacing:-.03em;\n  margin-bottom:8px;color:var(--t1);position:relative;z-index:1;\n}\np.sub{font-size:11px;color:var(--t2);line-height:1.9;margin-bottom:20px;position:relative;z-index:1}\n.accent{color:var(--accent);text-shadow:0 0 18px rgba(167,139,250,.14)}\n\n.err{\n  display:none;align-items:center;gap:8px;\n  background:var(--red-bg);border:1px solid rgba(248,113,113,.24);\n  color:var(--red-t);border-radius:12px;padding:10px 12px;\n  font-size:11px;margin-bottom:14px;position:relative;z-index:1;\n}\n.err.show{display:flex}\n.field{margin-bottom:14px;position:relative;z-index:1}\n.field label{display:block;font-size:10px;color:var(--t2);margin-bottom:6px;font-weight:700}\n\n.input-shell{position:relative}\n.input-shell input{\n  width:100%;height:48px;\n  background:var(--login-input);\n  border:1px solid var(--card-b);\n  border-radius:13px;color:var(--t1);\n  padding:0 44px 0 14px;outline:none;\n  font:500 13px Vazirmatn,sans-serif;\n  transition:.18s;\n  box-shadow:inset 0 1px 0 rgba(255,255,255,.05);\n}\n.input-shell input::placeholder{color:var(--t3)}\n.input-shell input:focus{\n  border-color:var(--card-bh);\n  box-shadow:var(--focus-ring),0 0 28px var(--accent-soft);\n}\n.ic{\n  position:absolute;right:15px;top:50%;transform:translateY(-50%);\n  color:var(--accent);font-size:17px;\n}\n\n.btn{\n  width:100%;height:50px;border:none;border-radius:13px;\n  background:var(--accent-grad);color:#fff;\n  font:800 13px Vazirmatn,sans-serif;cursor:pointer;\n  display:flex;align-items:center;justify-content:center;gap:8px;\n  box-shadow:var(--accent-shadow);transition:.18s;\n  position:relative;overflow:hidden;z-index:1;\n}\n.btn::after{\n  content:"";position:absolute;inset:0;pointer-events:none;\n  background:linear-gradient(110deg,transparent 30%,rgba(255,255,255,.24) 50%,transparent 70%);\n  transform:translateX(-120%);transition:transform .7s ease;\n}\n.btn:hover{transform:translateY(-2px);filter:brightness(1.07)}\n.btn:hover::after{transform:translateX(120%)}\n.btn:disabled{opacity:.6;transform:none}\n.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:16px;position:relative;z-index:1}\n.meta{\n  padding:10px 11px;border-radius:12px;border:1px solid var(--card-b);\n  background:var(--surface-2);backdrop-filter:blur(18px);\n}\n.meta span{display:block;font-size:7px;color:var(--t3);letter-spacing:.12em;margin-bottom:3px}\n.meta b{font-size:9px;color:var(--t2)}\n.ok{color:var(--green)!important}\n.foot{\n  display:flex;justify-content:space-between;gap:10px;margin-top:14px;\n  color:var(--t3);font-size:8.5px;position:relative;z-index:1;\n}\n.card a{color:var(--accent);text-decoration:none}\n.card a:hover{text-decoration:underline}\n@keyframes spin{to{transform:rotate(360deg)}}\n\n@media(max-width:520px){\n  .card{padding:22px;border-radius:23px}\n  h1{font-size:21px}\n  .shell{width:min(460px,calc(100% - 20px))}\n}\n\n/* deterministic English login layout */\nbody.login-en .card,\nbody.login-en .hud{direction:ltr;text-align:left}\nbody.login-en .brand{direction:ltr}\nbody.login-en .field label{text-align:left}\nbody.login-en .input-shell input{text-align:left;padding-left:44px;padding-right:44px}\nbody.login-en .ic{left:15px;right:auto}\n\n/* Light-mode refinements */\nhtml[data-login-theme="light"] body::before{\n  background-image:\n    linear-gradient(rgba(124,140,248,.055) 1px,transparent 1px),\n    linear-gradient(90deg,rgba(124,140,248,.045) 1px,transparent 1px),\n    radial-gradient(circle at 50% 18%,rgba(255,255,255,.74),transparent 46%);\n  background-size:38px 38px,38px 38px,auto;\n  opacity:.95;\n}\nhtml[data-login-theme="light"] .card{\n  box-shadow:0 22px 65px rgba(55,75,120,.13),inset 0 1px 0 rgba(255,255,255,.96);\n}\nhtml[data-login-theme="light"] .accent{color:#6978e8}\nhtml[data-login-theme="light"] .input-shell input{box-shadow:inset 0 1px 0 rgba(255,255,255,.92)}\nhtml[data-login-theme="light"] .btn{box-shadow:0 12px 30px rgba(124,140,248,.24)}\n'
_DASHBOARD_CSS = '/* ═════════ GLOBAL ═════════ */\nhtml{background:var(--bg);background-image:var(--bg-gradient);background-attachment:fixed;scroll-behavior:smooth}\nhtml,body{min-height:100%}\nbody{\n  font-family:\'Vazirmatn\',sans-serif;\n  background-color:var(--bg);\n  background-image:var(--bg-gradient);\n  background-attachment:fixed;\n  color:var(--t1);\n  font-size:14px;min-height:100vh;display:flex;\n  transition:background-color .3s,color .3s;\n  -webkit-font-smoothing:antialiased;\n}\nbody::before{\n  content:"";position:fixed;inset:0;pointer-events:none;z-index:0;\n  background-image:\n    linear-gradient(var(--grid) 1px, transparent 1px),\n    linear-gradient(90deg, var(--grid) 1px, transparent 1px);\n  background-size:44px 44px;\n  mask-image:radial-gradient(ellipse at center, black 15%, transparent 75%);\n  -webkit-mask-image:radial-gradient(ellipse at center, black 15%, transparent 75%);\n}\n::-webkit-scrollbar{width:5px;height:5px}\n::-webkit-scrollbar-track{background:transparent}\n::-webkit-scrollbar-thumb{background:var(--surface-2);border-radius:3px}\na{color:inherit;text-decoration:none}\nbutton{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}\ninput,select,textarea{font-family:inherit}\n\n/* Sidebar position by language */\nbody.ui-fa{direction:rtl}\nbody.ui-en{direction:ltr}\nbody.ui-fa .sidebar{right:0;left:auto}\nbody.ui-en .sidebar{left:0;right:auto}\nbody.ui-fa .main{margin-right:var(--sidebar-w);margin-left:0}\nbody.ui-en .main{margin-left:var(--sidebar-w);margin-right:0}\n\n/* ═════════ SIDEBAR ═════════ */\n.sidebar{\n  width:var(--sidebar-w);min-height:100vh;\n  background:var(--glass);\n  backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);\n  border-inline-end:1px solid var(--card-b);\n  display:flex;flex-direction:column;flex-shrink:0;\n  position:fixed;top:0;bottom:0;z-index:200;\n  transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s;\n}\n.sb-close{\n  display:none;position:absolute;top:20px;inset-inline-end:12px;\n  background:var(--surface);border:1px solid var(--card-b);\n  color:var(--t2);width:30px;height:30px;border-radius:9px;\n  font-size:16px;align-items:center;justify-content:center;cursor:pointer;\n  transition:.15s;\n}\n.sb-close:hover{background:var(--red-bg);color:var(--red-t)}\n\n.logo{\n  display:flex;align-items:center;gap:12px;\n  padding:20px 16px 16px;\n  border-bottom:1px solid var(--card-b);\n}\n.logo-img{\n  width:42px;height:42px;border-radius:13px;overflow:hidden;\n  background:var(--accent-grad);\n  box-shadow:var(--accent-shadow);\n  flex-shrink:0;\n}\n.logo-img img{width:100%;height:100%;object-fit:cover}\n.logo-name{font-size:13px;font-weight:800;color:var(--t1);letter-spacing:.02em}\n.logo-sub{font-size:9.5px;color:var(--t3);margin-top:2px}\n.logo-meta{font-size:8px;color:var(--t3);margin-top:3px;letter-spacing:.12em;font-weight:700;opacity:.7}\n\n.side-telemetry{\n  margin:12px 12px 4px;padding:11px 13px;\n  border:1px solid var(--card-b);border-radius:13px;\n  background:var(--surface-2);\n}\n.telemetry-head{display:flex;justify-content:space-between;align-items:center;font-size:8px;color:var(--t3);letter-spacing:.14em;font-weight:800;margin-bottom:9px}\n.telemetry-led{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green);animation:pulse 2s infinite}\n.telemetry-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}\n.telemetry-grid div{display:flex;flex-direction:column;gap:2px}\n.telemetry-grid span{font-size:7px;color:var(--t3);letter-spacing:.11em}\n.telemetry-grid b{font-size:9px;color:var(--t2);font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n\n.nav-wrap{flex:1;overflow-y:auto;padding:8px 8px 12px}\n.nav-sec{padding:14px 10px 6px;font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--t3);font-weight:700}\n.nav-it{\n  display:flex;align-items:center;gap:10px;\n  padding:10px 12px;color:var(--t2);font-size:12.5px;\n  cursor:pointer;border-radius:12px;margin:2px 0;\n  transition:.18s;position:relative;overflow:hidden;\n}\n.nav-it i{font-size:17px;width:20px;text-align:center;flex-shrink:0;color:var(--t3);transition:.18s}\n.nav-it:hover{background:var(--surface);color:var(--t1);transform:translateX(2px)}\n.nav-it:hover i{color:var(--accent)}\n.nav-it.on{\n  background:linear-gradient(90deg,var(--accent-soft),transparent 80%);\n  color:var(--t1);font-weight:700;\n  box-shadow:inset 0 0 30px var(--accent-soft);\n}\nbody.ui-fa .nav-it.on{background:linear-gradient(270deg,var(--accent-soft),transparent 80%)}\n.nav-it.on i{color:var(--accent)}\n.nav-it.on::before{\n  content:"";position:absolute;top:8px;bottom:8px;inset-inline-start:0;\n  width:3px;border-radius:3px;\n  background:var(--accent-grad);\n  box-shadow:var(--accent-glow);\n}\n.nav-label{min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.nav-badge{display:none !important}\n\n.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}\n.side-lang,.theme-btn,.logout-btn{\n  display:flex;align-items:center;justify-content:center;gap:7px;\n  width:100%;padding:9px;border-radius:11px;\n  font:700 11.5px Vazirmatn,sans-serif;\n  border:1px solid var(--card-b);cursor:pointer;transition:.18s;\n}\n.side-lang,.lang-btn{background:var(--surface);color:var(--accent);margin-bottom:7px}\n.side-lang:hover,.lang-btn:hover{background:var(--accent-soft);transform:translateY(-1px)}\n.theme-btn{background:var(--surface);color:var(--t2);margin-bottom:7px}\n.theme-btn:hover{background:var(--surface-2);color:var(--t1)}\n.logout-btn{background:var(--red-bg);color:var(--red-t);border-color:rgba(248,113,113,.2)}\n.logout-btn:hover{background:rgba(248,113,113,.22)}\n\n/* ═════════ MOBILE TOP ═════════ */\n.mob-top{\n  display:none;position:fixed;top:0;left:0;right:0;height:62px;\n  background:var(--glass);\n  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);\n  border-bottom:1px solid var(--card-b);\n  z-index:150;align-items:center;justify-content:space-between;\n  padding:0 14px;\n  transition:background .3s,border-color .3s;\n}\n.mob-top .ml{display:flex;align-items:center;gap:10px}\n.mob-logo{width:34px;height:34px;border-radius:10px;overflow:hidden;background:var(--accent-grad);box-shadow:var(--accent-shadow);flex-shrink:0}\n.mob-logo img{width:100%;height:100%;object-fit:cover}\n.mob-brand-copy{display:flex;flex-direction:column;gap:1px}\n.mob-title{color:var(--t1);font-size:12.5px;font-weight:800;letter-spacing:.02em}\n.mob-subtitle{color:var(--t3);font-size:8px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}\n.mob-right{display:flex;align-items:center;gap:6px}\n.top-status{\n  display:inline-flex;align-items:center;gap:5px;\n  font-size:8px;font-weight:800;letter-spacing:.08em;\n  padding:6px 9px;border-radius:20px;\n  background:var(--green-bg);color:var(--green-t);\n  border:1px solid var(--green-bg);\n}\n.menu-btn,.theme-mob{\n  background:var(--surface);border:1px solid var(--card-b);\n  color:var(--t2);width:36px;height:36px;border-radius:10px;\n  font-size:17px;display:flex;align-items:center;justify-content:center;\n  cursor:pointer;transition:.15s;\n}\n.menu-btn:hover,.theme-mob:hover{background:var(--accent-soft);color:var(--accent)}\n.mob-right .lang-btn{width:auto;height:36px;margin:0;padding:0 11px;font-size:10px}\n\n.overlay{display:none;position:fixed;inset:0;background:var(--overlay);z-index:190;backdrop-filter:blur(4px)}\n.overlay.show{display:block}\n\n/* ═════════ MAIN ═════════ */\n.main{\n  flex:1;padding:28px 28px 60px;min-width:0;\n  position:relative;z-index:1;\n  transition:margin .25s;\n}\n.pg{display:none}\n.pg.on{display:block;animation:fi .22s ease}\n@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}\n\n/* Topbar */\n.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}\n.tb-title{font-size:19px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:9px;letter-spacing:-.02em}\n.tb-title i{color:var(--accent);font-size:20px}\n.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}\n.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}\n\n/* Badges */\n.badge{\n  font-size:10px;padding:4px 11px;border-radius:20px;font-weight:700;\n  display:inline-flex;align-items:center;gap:5px;white-space:nowrap;\n}\n.bg-green{background:var(--green-bg);color:var(--green-t)}\n.bg-blue{background:var(--accent-soft);color:var(--accent)}\n.bg-amber{background:var(--amber-bg);color:var(--amber-t)}\n.bg-red{background:var(--red-bg);color:var(--red-t)}\n.bg-purple{background:var(--purple-bg);color:var(--purple)}\n\n.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}\n.dg{background:var(--green)}\n.dr{background:var(--red)}\n.da{background:var(--amber)}\n.db{background:var(--accent)}\n.pulse{animation:pulse 2s infinite}\n@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}\n\n/* Metrics */\n.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}\n.metric{\n  background:var(--surface);\n  border:1px solid var(--card-b);border-radius:var(--radius);\n  padding:18px;transition:.22s;position:relative;overflow:hidden;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n  min-height:140px;\n}\n.metric::before{\n  content:"";position:absolute;inset:0;pointer-events:none;\n  background:linear-gradient(125deg,transparent 0 42%,var(--accent-soft) 49%,transparent 57%);\n  opacity:.5;\n}\n.metric::after{\n  content:"";position:absolute;top:18px;inset-inline-end:0;\n  width:3px;height:45%;border-radius:3px;\n  background:var(--accent-grad);\n  box-shadow:var(--accent-glow);\n  transition:.22s;\n}\n.metric:hover{\n  border-color:var(--card-bh);\n  transform:translateY(-4px);\n  box-shadow:0 20px 46px rgba(0,0,0,.22),0 0 30px var(--accent-soft);\n}\n.m-icon{\n  width:38px;height:38px;border-radius:11px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:18px;margin-bottom:13px;flex-shrink:0;\n}\n.m-icon.suc{background:var(--green-bg);color:var(--green-t)}\n.m-icon.dan{background:var(--red-bg);color:var(--red-t)}\n.m-icon.pur{background:var(--purple-bg);color:var(--purple)}\n.m-label{font-size:10px;color:var(--t3);margin-bottom:5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}\n.m-val{font-size:27px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;font-family:ui-monospace,\'JetBrains Mono\',monospace}\n.m-unit{font-size:12px;font-weight:400;color:var(--t3);font-family:inherit}\n.m-sub{font-size:10px;color:var(--t3);margin-top:7px;display:flex;align-items:center;gap:4px}\n\n/* VLESS Box */\n.vless-box{\n  background:var(--surface);\n  border:1px solid var(--card-b);border-radius:var(--radius);\n  padding:22px 24px;margin-bottom:18px;\n  box-shadow:var(--shadow-sm);\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n  position:relative;overflow:hidden;\n}\n.vless-box::before{\n  content:"";position:absolute;top:-60px;inset-inline-start:-60px;\n  width:200px;height:200px;pointer-events:none;\n  background:radial-gradient(circle, var(--accent-soft), transparent 70%);\n}\n.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}\n.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:7px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}\n.vl-title i{color:var(--accent);font-size:15px}\n.vl-code{\n  background:var(--surface-3);\n  border:1px solid var(--card-b);border-radius:11px;\n  padding:13px 15px;\n  font:11.5px ui-monospace,monospace;\n  color:var(--accent-2);\n  word-break:break-all;line-height:1.9;\n  position:relative;z-index:1;\n}\n.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap;position:relative;z-index:1}\n\n/* Buttons */\n.btn{\n  font-family:inherit;font-size:12px;font-weight:700;\n  border-radius:11px;padding:9px 15px;\n  cursor:pointer;display:inline-flex;align-items:center;gap:6px;\n  border:1px solid transparent;transition:.18s;white-space:nowrap;\n  position:relative;overflow:hidden;\n}\n.btn i{font-size:14px}\n.btn::after{\n  content:"";position:absolute;inset:0;pointer-events:none;\n  background:linear-gradient(110deg,transparent 30%,rgba(255,255,255,.22) 50%,transparent 70%);\n  transform:translateX(-120%);transition:transform .7s ease;\n}\n.btn:hover::after{transform:translateX(120%)}\n.btn:disabled{opacity:.4;cursor:not-allowed}\n.btn-p{background:var(--accent-grad);color:#fff;box-shadow:var(--accent-shadow);border:none}\n.btn-p:hover{filter:brightness(1.08);transform:translateY(-1px)}\n.btn-o{background:var(--surface);border-color:var(--card-b);color:var(--t2)}\n.btn-o:hover{background:var(--accent-soft);color:var(--accent);border-color:var(--card-bh)}\n.btn-g{background:var(--accent-soft);color:var(--accent);border-color:var(--card-b)}\n.btn-g:hover{background:rgba(167,139,250,.25);color:var(--accent)}\n.btn-d{background:var(--red-bg);color:var(--red-t);border-color:rgba(248,113,113,.2)}\n.btn-d:hover{background:rgba(248,113,113,.22)}\n.btn-pur{background:var(--purple-bg);color:var(--purple);border-color:var(--card-b)}\n.btn-pur:hover{background:rgba(167,139,250,.22)}\n.btn-amber{background:var(--amber-bg);color:var(--amber-t);border-color:rgba(251,191,36,.2)}\n.btn-amber:hover{background:rgba(251,191,36,.22)}\n.btn-sm{padding:6px 10px;font-size:10.5px;border-radius:8px}\n.btn-icon{width:32px;height:32px;padding:0;justify-content:center;border-radius:9px}\n\n/* Cards */\n.card{\n  background:var(--surface);\n  border:1px solid var(--card-b);border-radius:var(--radius);\n  padding:20px 22px;transition:.22s;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n  position:relative;\n}\n.card:hover{border-color:var(--card-bh)}\n.card-title{\n  font-size:13px;font-weight:800;color:var(--t1);\n  margin-bottom:16px;display:flex;align-items:center;gap:8px;\n}\n.card-title i{font-size:16px;color:var(--accent)}\n.ml-auto{margin-inline-start:auto}\n\n.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px}\n.g3{display:grid;grid-template-columns:2fr 1fr;gap:14px;margin-bottom:16px}\n.mb16{margin-bottom:16px}\n\n.sr{\n  display:flex;align-items:center;justify-content:space-between;\n  padding:10px 0;border-bottom:1px solid var(--card-b);\n  font-size:12px;\n}\n.sr:last-child{border-bottom:none}\n.sr-k{color:var(--t2);display:flex;align-items:center;gap:7px}\n.sr-k i{font-size:14px;color:var(--t3)}\n.sr-v{color:var(--t1);font-weight:700;font-size:11.5px}\n\n.ch{position:relative;height:240px}\n.ch-lg{position:relative;height:330px}\n.ch-sm{position:relative;height:210px;min-width:0;overflow:hidden;}\n\n/* ═════════ TRAFFIC PAGE ═════════ */\n.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}\n.traf-main-stat{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:20px;padding:22px 24px;\n  position:relative;overflow:hidden;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.traf-main-stat::before{\n  content:"";position:absolute;top:-60px;inset-inline-start:-60px;\n  width:220px;height:220px;pointer-events:none;\n  background:radial-gradient(circle, var(--accent-soft), transparent 70%);\n}\n.traf-main-label{\n  font-size:10.5px;color:var(--t3);font-weight:700;\n  text-transform:uppercase;letter-spacing:.08em;\n  display:flex;align-items:center;gap:6px;margin-bottom:11px;\n  position:relative;z-index:1;\n}\n.traf-main-val{\n  font-size:34px;font-weight:800;color:var(--t1);\n  line-height:1;letter-spacing:-.02em;\n  display:flex;align-items:baseline;gap:6px;\n  position:relative;z-index:1;\n  font-family:ui-monospace,\'JetBrains Mono\',monospace;\n}\n.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3);font-family:inherit}\n.traf-trend{\n  display:inline-flex;align-items:center;gap:4px;\n  font-size:11px;font-weight:700;padding:5px 11px;border-radius:20px;\n  margin-top:12px;position:relative;z-index:1;\n}\n.traf-trend.up{background:var(--green-bg);color:var(--green-t)}\n.traf-trend.down{background:var(--red-bg);color:var(--red-t)}\n\n.traf-mini{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:20px;padding:18px 19px;\n  display:flex;flex-direction:column;justify-content:space-between;\n  transition:.22s;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}\n.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}\n.traf-mini-icon{\n  width:32px;height:32px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;font-size:16px;\n}\n.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber-t)}\n.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}\n.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}\n.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em;font-family:ui-monospace,monospace}\n.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}\n\n.traf-chart-card{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:20px;padding:22px 24px 18px;\n  box-shadow:var(--shadow-sm);margin-bottom:16px;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}\n.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}\n.traf-chart-title i{color:var(--accent);font-size:18px}\n.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}\n.traf-legend{display:flex;gap:14px;align-items:center}\n.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}\n.traf-legend-dot{width:8px;height:8px;border-radius:3px}\n.traf-range-tabs{display:flex;gap:4px;background:var(--accent-soft);padding:3px;border-radius:10px;border:1px solid var(--card-b)}\n.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}\n.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px var(--accent-soft)}\n.traf-chart-body{height:320px;margin-top:14px;position:relative}\n\n/* ═════════ CREATE PANEL ═════════ */\n.create-panel{\n  background:var(--surface);\n  border:1px solid var(--card-b);border-radius:22px;\n  padding:0;overflow:hidden;box-shadow:var(--shadow-sm);\n  margin-bottom:16px;position:relative;\n  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);\n}\n.create-panel::before{\n  content:"";position:absolute;top:-60px;inset-inline-start:-60px;\n  width:220px;height:220px;pointer-events:none;\n  background:radial-gradient(circle, var(--accent-soft), transparent 70%);\n}\n.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}\n.cp-head-icon{\n  width:46px;height:46px;border-radius:14px;\n  background:var(--accent-grad);color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:21px;flex-shrink:0;\n  box-shadow:var(--accent-shadow);\n}\n.cp-head-text{flex:1;min-width:0}\n.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}\n.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}\n.cp-body{padding:2px 24px 22px;position:relative;z-index:1}\n.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}\n.cp-block{\n  background:var(--surface-2);\n  border:1px solid var(--card-b);border-radius:14px;\n  padding:14px 16px;\n}\n.cp-block-label{\n  font-size:10px;font-weight:800;color:var(--t2);\n  text-transform:uppercase;letter-spacing:.08em;\n  display:flex;align-items:center;gap:6px;margin-bottom:11px;\n}\n.cp-block-label i{color:var(--accent);font-size:14px}\n.cp-input-full{\n  width:100%;padding:10px 13px;border-radius:11px;\n  border:1px solid var(--card-b);background:var(--surface-3);\n  color:var(--t1);font-family:inherit;font-size:12.5px;\n  outline:none;transition:.15s;\n}\n.cp-input-full:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.cp-input-full::placeholder{color:var(--t3)}\n.cp-mini-row{display:flex;gap:8px;margin-top:9px}\n.cp-quota-inputs{display:flex;gap:8px}\n.cp-quota-inputs .cp-input-full{flex:1}\n.cp-quota-inputs select.cp-input-full{flex:0 0 76px}\n\n.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}\n.chip{\n  font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:9px;\n  background:var(--surface-2);color:var(--t2);\n  border:1px solid var(--card-b);cursor:pointer;transition:.15s;\n  white-space:nowrap;\n}\n.chip:hover{background:var(--accent-soft);color:var(--accent)}\n.chip.active{background:var(--accent-grad);color:#fff;border-color:transparent;box-shadow:var(--accent-shadow)}\n\n.proto-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:9px}\n.proto-card{\n  border:1.5px solid var(--card-b);border-radius:13px;\n  padding:13px 12px;cursor:pointer;transition:.18s;\n  text-align:center;position:relative;background:var(--surface-2);\n}\n.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}\n.proto-card.active{\n  border-color:var(--accent);background:var(--accent-soft);\n  box-shadow:0 0 0 3px var(--accent-soft);\n}\n.proto-card-check{\n  position:absolute;top:7px;inset-inline-end:7px;\n  width:18px;height:18px;border-radius:50%;\n  background:var(--accent-grad);color:#fff;font-size:11px;\n  display:flex;align-items:center;justify-content:center;\n  opacity:0;transform:scale(.5);transition:.18s;\n  box-shadow:var(--accent-shadow);\n}\n.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}\n.proto-card-icon{\n  width:34px;height:34px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:17px;margin:0 auto 8px;\n}\n.proto-card.active .proto-card-icon{background:var(--accent-grad);color:#fff}\n.trojan-proto-logo{width:22px;height:22px;display:block;filter:drop-shadow(0 1px 2px rgba(0,0,0,.18))}\n.proto-card-icon-trojan{overflow:hidden}\n.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}\n.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}\n\n.cp-footer{\n  display:flex;align-items:center;justify-content:space-between;\n  gap:12px;padding-top:16px;\n  border-top:1px solid var(--card-b);flex-wrap:wrap;\n}\n.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}\n.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}\n.cp-submit-btn{\n  background:var(--accent-grad);color:#fff;border:none;\n  border-radius:13px;padding:13px 26px;\n  font-family:inherit;font-size:13px;font-weight:800;\n  cursor:pointer;display:flex;align-items:center;gap:8px;\n  box-shadow:var(--accent-shadow);transition:.18s;white-space:nowrap;\n}\n.cp-submit-btn:hover{transform:translateY(-2px);filter:brightness(1.08)}\n.cp-submit-btn:active{transform:translateY(0) scale(.98)}\n\n/* ═════════ SERVER / PASSWORD / TELEGRAM PANELS ═════════ */\n.srv-panel,.pw-panel,.tg-panel{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:22px;overflow:hidden;\n  box-shadow:var(--shadow-sm);position:relative;\n  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);\n}\n.srv-panel::before,.tg-panel::before{\n  content:"";position:absolute;top:-60px;inset-inline-start:-60px;\n  width:200px;height:200px;pointer-events:none;\n  background:radial-gradient(circle, var(--accent-soft), transparent 70%);\n}\n.pw-panel::before{\n  content:"";position:absolute;top:-60px;inset-inline-end:-60px;\n  width:200px;height:200px;pointer-events:none;\n  background:radial-gradient(circle, var(--purple-bg), transparent 70%);\n}\n.srv-hero,.pw-hero,.tg-hero{\n  display:flex;align-items:center;gap:14px;\n  padding:22px 24px 18px;position:relative;z-index:1;\n}\n.srv-hero{border-bottom:1px solid var(--card-b)}\n.srv-hero-icon,.pw-hero-icon,.tg-hero-icon{\n  width:50px;height:50px;border-radius:14px;\n  background:var(--accent-grad);color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:22px;flex-shrink:0;\n  box-shadow:var(--accent-shadow);\n}\n.pw-hero-icon{background:linear-gradient(135deg,var(--accent),var(--accent-3));box-shadow:0 12px 30px rgba(167,139,250,.4)}\n.tg-hero-icon{background:var(--info-grad);box-shadow:0 12px 30px var(--info-soft)}\n.srv-hero-text,.pw-hero-text,.tg-hero-text{flex:1;min-width:0}\n.srv-hero-domain,.pw-hero-title,.tg-hero-title{font-size:15px;font-weight:800;color:var(--t1);word-break:break-word}\n.srv-hero-sub,.pw-hero-sub,.tg-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px;display:flex;align-items:center;gap:6px}\n\n.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}\n.srv-tile{\n  display:flex;align-items:center;gap:11px;\n  background:var(--surface-2);border:1px solid var(--card-b);\n  border-radius:13px;padding:12px 14px;transition:.18s;\n}\n.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}\n.srv-tile-icon{\n  width:36px;height:36px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:16px;flex-shrink:0;\n}\n.srv-tile-text{min-width:0}\n.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:3px}\n.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}\n\n.pw-body{padding:2px 24px 22px;position:relative;z-index:1}\n.pw-field{position:relative;margin-bottom:13px}\n.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}\n.pw-input{\n  width:100%;padding:11px 42px 11px 14px;\n  border-radius:11px;border:1px solid var(--card-b);\n  background:var(--surface-3);color:var(--t1);\n  font-family:inherit;font-size:12.5px;outline:none;transition:.15s;\n}\n.pw-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.pw-eye{position:absolute;inset-inline-end:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}\n.pw-eye:hover{color:var(--accent)}\n.pw-strength{height:4px;border-radius:3px;background:var(--accent-soft);margin-top:8px;overflow:hidden;display:flex;gap:3px}\n.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:var(--surface-2);transition:.25s}\n.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}\n.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}\n.pw-req{\n  font-size:9.5px;padding:4px 10px;border-radius:8px;\n  background:var(--surface-2);color:var(--t3);font-weight:600;\n  display:flex;align-items:center;gap:4px;transition:.18s;\n}\n.pw-req.met{background:var(--green-bg);color:var(--green-t)}\n.pw-submit{\n  width:100%;justify-content:center;\n  background:linear-gradient(135deg,var(--accent),var(--accent-3));\n  color:#fff;border:none;border-radius:12px;padding:13px;\n  font-family:inherit;font-size:13px;font-weight:800;\n  cursor:pointer;display:flex;align-items:center;gap:8px;\n  box-shadow:0 12px 30px rgba(167,139,250,.4);transition:.18s;\n}\n.pw-submit:hover{transform:translateY(-2px);filter:brightness(1.08)}\n\n.tg-hero{padding:22px 24px 18px}\n.tg-hero-status{width:12px;height:12px;border-radius:50%;background:var(--t3);flex-shrink:0;transition:.2s}\n.tg-hero-status.on{background:var(--green);box-shadow:0 0 12px var(--green),0 0 0 4px var(--green-bg);animation:pulse 2s infinite}\n.tg-hero-status.off{background:var(--red);box-shadow:0 0 0 4px var(--red-bg)}\n.tg-body{padding:2px 24px 22px;position:relative;z-index:1}\n.tg-field{margin-bottom:13px}\n.tg-field label{display:flex;align-items:center;gap:6px;font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}\n.tg-field label i{color:var(--info);font-size:14px}\n.tg-hint{font-weight:500;color:var(--t3);text-transform:none;letter-spacing:0;font-size:9.5px}\n.tg-input-wrap{position:relative}\n.tg-input{\n  width:100%;padding:11px 42px 11px 14px;\n  border-radius:11px;border:1px solid var(--card-b);\n  background:var(--surface-3);color:var(--t1);\n  font-family:ui-monospace,monospace;font-size:12.5px;\n  outline:none;transition:.15s;\n}\n.tg-input:focus{border-color:var(--info);box-shadow:0 0 0 3px var(--info-soft)}\n.tg-eye{position:absolute;inset-inline-end:12px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}\n.tg-eye:hover{color:#29A2DC}\n.tg-actions{display:flex;gap:8px;flex-wrap:wrap}\n.tg-result{margin-top:12px;padding:11px 14px;border-radius:11px;font-size:12px;font-weight:700;display:flex;align-items:center;gap:8px}\n.tg-result.ok{background:var(--green-bg);color:var(--green-t);border:1px solid var(--green-bg)}\n.tg-result.err{background:var(--red-bg);color:var(--red-t);border:1px solid var(--red-bg)}\n.tg-result.wait{background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent-soft)}\n\n/* ═════════ CONNECTIONS PAGE ═════════ */\n.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}\n.conn-hero-tile{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:16px;padding:16px 18px;\n  position:relative;overflow:hidden;transition:.2s;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow-sm)}\n.conn-hero-tile::after{\n  content:"";position:absolute;bottom:0;inset-inline-start:0;inset-inline-end:0;\n  height:2px;background:linear-gradient(90deg,var(--accent),transparent);\n}\n.conn-hero-icon{\n  width:34px;height:34px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:16px;margin-bottom:10px;\n}\n.conn-hero-tile:nth-child(1) .conn-hero-icon{background:var(--green-bg);color:var(--green-t)}\n.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-soft);color:var(--accent)}\n.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}\n.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber-t)}\n.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}\n.conn-hero-val{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;font-family:ui-monospace,monospace}\n.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}\n\n.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}\n.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}\n.conn-toolbar-title i{color:var(--green);font-size:15px}\n.conn-live-badge{\n  display:flex;align-items:center;gap:6px;\n  font-size:10.5px;font-weight:700;color:var(--green-t);\n  background:var(--green-bg);padding:6px 12px;border-radius:20px;\n  border:1px solid var(--green-bg);\n}\n.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}\n\n.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}\n.conn-card-v2{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:18px;padding:0;overflow:hidden;\n  transition:.22s;position:relative;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow-sm)}\n.conn-card-v2::after{\n  content:"";position:absolute;top:-100%;left:0;right:0;height:100%;\n  pointer-events:none;\n  background:linear-gradient(180deg,transparent,var(--accent-soft),transparent);\n  animation:cardScan 4.5s linear infinite;opacity:.5;\n}\n@keyframes cardScan{0%{top:-100%}100%{top:100%}}\n.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}\n.conn-avatar{\n  width:42px;height:42px;border-radius:13px;\n  background:linear-gradient(135deg,var(--green),#059669);color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:18px;flex-shrink:0;\n  box-shadow:0 8px 20px rgba(16,185,129,.35);\n}\n.conn-card-v2-id{flex:1;min-width:0}\n.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}\n.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}\n.conn-ip-copy:hover{color:var(--accent)}\n.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.conn-status-pill{\n  font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;\n  background:var(--green-bg);color:var(--green-t);\n  display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0;\n}\n.conn-card-v2-divider{height:1px;background:var(--card-b);margin:0 17px}\n.conn-card-v2-body{padding:14px 17px 16px}\n.conn-proto-row{margin-bottom:12px}\n.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}\n.conn-stat-box{display:flex;align-items:center;gap:8px}\n.conn-stat-icon{\n  width:28px;height:28px;border-radius:9px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0;\n}\n.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}\n.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}\n.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}\n.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-soft);overflow:hidden}\n.conn-duration-fill{\n  height:100%;border-radius:4px;\n  background:linear-gradient(90deg,var(--accent),var(--accent-2));\n  transition:width .4s;\n}\n.conn-duration-fill::after{\n  content:"";position:absolute;inset:0;\n  background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);\n  animation:shimmer 1.8s linear infinite;\n}\n\n.conn-empty-v2{\n  text-align:center;padding:70px 20px;\n  background:var(--surface);border:1px dashed var(--card-b);\n  border-radius:20px;\n}\n.conn-empty-v2-icon{\n  width:64px;height:64px;border-radius:18px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:28px;margin:0 auto 16px;\n}\n.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}\n.conn-empty-v2-sub{font-size:11px;color:var(--t3)}\n\n/* ═════════ CONFIG CARDS (links page) ═════════ */\n.cfg-grid{display:flex;flex-direction:column;gap:10px}\n.cfg-card{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:16px;padding:0;overflow:hidden;\n  transition:.22s;position:relative;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.cfg-card:hover{border-color:var(--card-bh);box-shadow:var(--shadow-sm);transform:translateY(-1px)}\n.cfg-card.is-off{opacity:.55}\n.cfg-card.is-exp{opacity:.75}\n.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}\n.cfg-status-dot{\n  width:9px;height:9px;border-radius:50%;\n  background:var(--green);flex-shrink:0;\n  box-shadow:0 0 0 3px var(--green-bg),0 0 8px var(--green);\n}\n.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}\n.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}\n.cfg-identity{display:flex;flex-direction:column;gap:4px;min-width:150px;flex-shrink:0}\n.cfg-label{font-size:13.5px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:7px}\n.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}\n.cfg-uuid-mini{\n  font-family:ui-monospace,monospace;font-size:9.5px;\n  color:var(--accent);background:var(--accent-soft);\n  padding:2px 7px;border-radius:6px;cursor:pointer;transition:.15s;\n}\n.cfg-uuid-mini:hover{background:var(--accent-soft);filter:brightness(1.15)}\n.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}\n.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}\n.ubar{height:5px;border-radius:4px;background:var(--accent-soft);overflow:hidden;position:relative}\n.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}\n.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}\n.cfg-exp-col{flex-shrink:0;min-width:110px}\n.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}\n.cfg-actions{display:flex;gap:5px;flex-shrink:0}\n.proto-chip{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:700;white-space:nowrap}\n.pc-trojan{background:rgba(239,68,68,.12);color:#F87171}\n.pc-ws{background:var(--accent-soft);color:var(--accent)}\n.pc-xhttp{background:var(--purple-bg);color:var(--purple)}\n.pc-ultra{background:var(--green-bg);color:var(--green-t)}\n.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}\n.cfg-sub-tag i{color:var(--purple);font-size:11px}\n\n.exp-chip{font-size:9px;padding:4px 9px;border-radius:8px;font-weight:700;display:inline-flex;align-items:center;gap:4px}\n.ec-ok{background:var(--green-bg);color:var(--green-t)}\n.ec-warn{background:var(--amber-bg);color:var(--amber-t)}\n.ec-exp{background:var(--red-bg);color:var(--red-t)}\n.ec-inf{background:var(--accent-soft);color:var(--accent)}\n\n/* Toggle switch */\n.tog{\n  width:19px;height:32px;border-radius:19px;\n  background:var(--surface-2);position:relative;\n  cursor:pointer;transition:.22s;flex-shrink:0;border:none;\n}\n.tog::after{\n  content:\'\';position:absolute;\n  width:13px;height:13px;border-radius:50%;\n  background:#fff;left:3px;top:3px;\n  transition:.22s;box-shadow:0 1px 3px rgba(0,0,0,.3);\n}\n.tog.on{background:var(--accent-grad)}\n.tog.on::after{top:16px}\n\n/* ═════════ SUBSCRIPTION GROUPS ═════════ */\n.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}\n.subs-search{flex:1;min-width:200px;position:relative}\n.subs-search input{\n  width:100%;padding:11px 40px 11px 15px;\n  border-radius:12px;border:1px solid var(--card-b);\n  background:var(--surface);color:var(--t1);\n  font-family:inherit;font-size:12.5px;outline:none;transition:.15s;\n}\n.subs-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.subs-search i{position:absolute;inset-inline-start:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}\n\n.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}\n.sub-card{\n  background:var(--surface);border:1px solid var(--card-b);\n  border-radius:20px;padding:0;overflow:hidden;\n  transition:.25s;position:relative;\n  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);\n}\n.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:var(--shadow-sm)}\n.sub-card-top{\n  background:linear-gradient(155deg, var(--purple-bg) 0%, transparent 65%);\n  padding:20px 20px 16px;position:relative;\n}\n.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}\n.sub-card-icon{\n  width:46px;height:46px;border-radius:14px;\n  background:linear-gradient(135deg,var(--accent),var(--accent-3));color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:20px;flex-shrink:0;\n  box-shadow:0 8px 20px rgba(167,139,250,.4);\n}\n.sub-card-titles{flex:1;min-width:0}\n.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}\n.sub-card-lock-badge{flex-shrink:0;width:28px;height:28px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:13px}\n.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}\n.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}\n\n.sub-card-stats{\n  display:grid;grid-template-columns:repeat(3,1fr);\n  margin-top:16px;background:var(--surface-2);\n  border:1px solid var(--card-b);border-radius:13px;overflow:hidden;\n  position:relative;z-index:1;\n}\n.sub-card-stat{padding:11px 8px;text-align:center;border-inline-start:1px solid var(--card-b)}\n.sub-card-stat:first-child{border-inline-start:none}\n.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2;font-family:ui-monospace,monospace}\n.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}\n.sub-card-url-row{\n  margin:14px 20px 0;\n  background:var(--accent-soft);\n  border:1px dashed var(--card-bh);\n  border-radius:11px;padding:9px 12px;\n  display:flex;align-items:center;gap:8px;\n}\n.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent);flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.sub-card-url-copy{background:none;border:none;color:var(--accent);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}\n.sub-card-url-copy:hover{transform:scale(1.1)}\n.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}\n.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}\n\n.subs-empty-v2{\n  text-align:center;padding:70px 20px;\n  background:var(--surface);border:1px dashed var(--card-b);\n  border-radius:20px;grid-column:1/-1;\n}\n.subs-empty-v2-icon{\n  width:64px;height:64px;border-radius:18px;\n  background:var(--purple-bg);color:var(--purple);\n  display:flex;align-items:center;justify-content:center;\n  font-size:28px;margin:0 auto 16px;\n}\n.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}\n.subs-empty-v2-sub{font-size:11px;color:var(--t3)}\n\n/* ═════════ MODALS ═════════ */\n.modal-bg{\n  display:none;position:fixed;inset:0;\n  background:var(--overlay);z-index:500;\n  align-items:center;justify-content:center;\n  backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);\n}\n.modal-bg.open{display:flex;animation:fi .2s ease}\n\n.modal{\n  background:var(--surface-solid);border:1px solid var(--card-b);\n  border-radius:22px;padding:28px 26px;\n  max-width:520px;width:calc(100% - 32px);\n  max-height:90vh;overflow-y:auto;\n  position:relative;animation:fi .25s ease;\n  box-shadow:var(--shadow);\n}\n.modal-close{\n  position:absolute;top:14px;inset-inline-end:14px;\n  background:var(--surface);border:1px solid var(--card-b);\n  color:var(--t2);width:32px;height:32px;border-radius:10px;\n  font-size:16px;display:flex;align-items:center;justify-content:center;\n  cursor:pointer;transition:.15s;\n}\n.modal-close:hover{background:var(--red-bg);color:var(--red-t)}\n.modal-title{font-size:16px;font-weight:800;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}\n.modal-title i{color:var(--accent)}\n\n/* Modal v2 (create sub) */\n.modal-v2{\n  background:var(--surface-solid);border:1px solid var(--card-b);\n  border-radius:22px;padding:0;\n  max-width:430px;width:calc(100% - 32px);\n  max-height:92vh;overflow-y:auto;\n  position:relative;animation:fi .25s ease;\n  box-shadow:var(--shadow);\n}\n.modal-v2-head{\n  background:linear-gradient(155deg, var(--purple-bg) 0%, transparent 65%);\n  padding:18px 22px 14px;position:relative;overflow:hidden;\n}\n.modal-v2-close{\n  position:absolute;top:14px;inset-inline-end:14px;\n  background:var(--surface);border:1px solid var(--card-b);\n  color:var(--t2);width:32px;height:32px;border-radius:10px;\n  font-size:15px;display:flex;align-items:center;justify-content:center;\n  cursor:pointer;z-index:2;transition:.15s;\n}\n.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t)}\n.modal-v2-icon{\n  width:44px;height:44px;border-radius:13px;\n  background:linear-gradient(135deg,var(--accent),var(--accent-3));color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:20px;margin-bottom:10px;position:relative;z-index:1;\n  box-shadow:0 10px 24px rgba(167,139,250,.4);\n}\n.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}\n.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}\n.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}\n.modal-v2-field{margin-bottom:11px}\n.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}\n.modal-v2-field label i{color:var(--purple);font-size:13px}\n.modal-v2-input{\n  width:100%;padding:10px 13px;border-radius:11px;\n  border:1px solid var(--card-b);background:var(--surface-3);\n  color:var(--t1);font-family:inherit;font-size:12.5px;\n  outline:none;transition:.18s;\n}\n.modal-v2-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.modal-v2-input::placeholder{color:var(--t3)}\n.modal-v2-footer{display:flex;gap:8px;margin-top:15px}\n\n/* Link picker modal */\n.lmodal-head{\n  background:linear-gradient(155deg, var(--accent-soft) 0%, transparent 70%);\n  padding:22px 24px 18px;position:relative;\n  border-bottom:1px solid var(--card-b);\n}\n.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}\n.lmodal-icon{\n  width:44px;height:44px;border-radius:13px;\n  background:var(--accent-grad);color:#fff;\n  display:flex;align-items:center;justify-content:center;\n  font-size:19px;flex-shrink:0;\n  box-shadow:var(--accent-shadow);\n}\n.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}\n.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}\n.lmodal-search{margin-top:14px;position:relative}\n.lmodal-search input{\n  width:100%;padding:10px 38px 10px 13px;\n  border-radius:11px;border:1px solid var(--card-b);\n  background:var(--surface-3);color:var(--t1);\n  font-family:inherit;font-size:12px;outline:none;\n}\n.lmodal-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.lmodal-search i{position:absolute;inset-inline-start:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}\n.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}\n.lmodal-qbtn{\n  font-size:10px;font-weight:700;padding:6px 12px;border-radius:9px;\n  background:var(--accent-soft);color:var(--accent);\n  border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit;\n}\n.lmodal-qbtn:hover{background:var(--accent-soft);filter:brightness(1.15)}\n.lmodal-count{margin-inline-start:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}\n.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}\n.lrow-v2{\n  display:flex;align-items:center;gap:11px;\n  padding:11px 12px;border-radius:13px;\n  cursor:pointer;transition:.15s;margin-bottom:4px;\n  border:1px solid transparent;\n}\n.lrow-v2:hover{background:var(--accent-soft)}\n.lrow-v2.checked{background:var(--accent-soft);border-color:var(--card-bh)}\n.lrow-v2-check{\n  width:20px;height:20px;border-radius:7px;\n  border:2px solid var(--card-b);flex-shrink:0;\n  display:flex;align-items:center;justify-content:center;\n  transition:.15s;background:var(--surface-2);\n}\n.lrow-v2.checked .lrow-v2-check{background:var(--accent-grad);border-color:transparent}\n.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}\n.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}\n.lrow-v2-avatar{\n  width:34px;height:34px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  display:flex;align-items:center;justify-content:center;\n  font-size:14px;flex-shrink:0;\n}\n.lrow-v2.checked .lrow-v2-avatar{background:var(--accent-grad);color:#fff}\n.lrow-v2-info{flex:1;min-width:0}\n.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}\n.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}\n.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}\n.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}\n.lmodal-footer{\n  display:flex;align-items:center;justify-content:space-between;gap:10px;\n  padding:16px 24px;border-top:1px solid var(--card-b);\n}\n.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}\n.lmodal-footer-info i{color:var(--accent)}\n.lmodal-footer-btns{display:flex;gap:8px}\n\n/* ═════════ FORM FIELDS ═════════ */\n.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}\n.fg{display:flex;flex-direction:column;gap:6px}\n.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}\n.fi,.fs{\n  padding:10px 13px;border-radius:11px;\n  border:1px solid var(--card-b);background:var(--surface-3);\n  color:var(--t1);font-family:inherit;font-size:12.5px;\n  outline:none;transition:.15s;min-width:100px;\n}\n.fi::placeholder{color:var(--t3)}\n.fi:focus,.fs:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}\n.fs option{background:var(--surface-solid);color:var(--t1)}\n\n/* Custom select styling */\nselect.cp-input-full,select.fs,select.fi{\n  -webkit-appearance:none;-moz-appearance:none;appearance:none;\n  background-color:var(--surface-3);\n  color:var(--t1);\n  background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'13\' height=\'13\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'%23a78bfa\' stroke-width=\'2.5\' stroke-linecap=\'round\' stroke-linejoin=\'round\'%3E%3Cpolyline points=\'6 9 12 15 18 9\'/%3E%3C/svg%3E");\n  background-repeat:no-repeat;\n  background-position:left 12px center;\n  padding-inline-start:38px;\n  padding-inline-end:13px;\n}\nbody.ui-en select.cp-input-full,body.ui-en select.fs,body.ui-en select.fi{\n  background-position:right 12px center;\n  padding-inline-start:13px;\n  padding-inline-end:38px;\n}\n\n/* Info box */\n.cl{\n  background:var(--accent-soft);\n  border:1px solid var(--card-b);\n  border-radius:12px;padding:12px 14px;\n  font-size:11px;color:var(--t2);\n  display:flex;gap:9px;align-items:flex-start;\n  line-height:1.8;margin-top:12px;\n}\n.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}\n.cl.amber{background:var(--amber-bg);border-color:var(--amber-bg);color:var(--amber-t)}\n.cl.amber i{color:var(--amber-t)}\n.cl a{color:var(--accent);text-decoration:none}\n.cl a:hover{text-decoration:underline}\n\n/* ═════════ SUBSCRIPTION URL BOX ═════════ */\n.sub-box{\n  background:var(--purple-bg);\n  border:1px solid var(--card-b);\n  border-radius:12px;padding:14px 16px;\n  display:flex;align-items:center;justify-content:space-between;\n  gap:10px;flex-wrap:wrap;margin-top:11px;\n}\n.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--purple);word-break:break-all;flex:1}\n\n/* Progress bars */\n.spbar{height:5px;border-radius:3px;background:var(--accent-soft);margin-top:6px;overflow:hidden;position:relative}\n.spfill{\n  height:100%;border-radius:3px;\n  background:var(--accent-grad);\n  transition:width 1s;position:relative;overflow:hidden;\n}\n.spfill::after{\n  content:"";position:absolute;inset:0;\n  background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);\n  animation:shimmer 2.2s linear infinite;\n}\n@keyframes shimmer{0%{transform:translateX(-100%)}100%{transform:translateX(220%)}}\n\n/* ═════════ LOGS / ERRORS ═════════ */\n.log-timeline{display:flex;flex-direction:column}\n.log-item{\n  display:flex;gap:12px;padding:11px 0;\n  border-bottom:1px solid var(--card-b);position:relative;\n}\n.log-item:last-child{border-bottom:none}\n.log-ic{\n  width:32px;height:32px;border-radius:10px;\n  display:flex;align-items:center;justify-content:center;\n  font-size:15px;flex-shrink:0;\n}\n.log-ic.ok{background:var(--green-bg);color:var(--green-t)}\n.log-ic.err{background:var(--red-bg);color:var(--red-t)}\n.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}\n.log-ic.info{background:var(--accent-soft);color:var(--accent)}\n.log-body{flex:1;min-width:0}\n.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}\n.log-time{font-size:9.5px;color:var(--t3);margin-top:3px;display:flex;align-items:center;gap:5px}\n.log-kind{\n  font-size:8.5px;padding:2px 8px;border-radius:10px;\n  background:var(--accent-soft);color:var(--accent);\n  font-weight:700;text-transform:uppercase;letter-spacing:.04em;\n}\n.erow{padding:10px 0;border-bottom:1px solid var(--card-b)}\n.erow:last-child{border-bottom:none}\n.etime{color:var(--t3);font-size:9.5px;margin-bottom:4px;display:flex;align-items:center;gap:4px}\n.emsg{\n  color:var(--red-t);font-family:ui-monospace,monospace;\n  background:var(--red-bg);padding:7px 10px;\n  border-radius:8px;word-break:break-all;font-size:10.5px;\n}\n\n/* ═════════ TOAST ═════════ */\n.toast{\n  position:fixed;bottom:24px;inset-inline-start:50%;\n  transform:translateX(-50%) translateY(80px);\n  z-index:999;padding:12px 22px;\n  background:var(--surface-solid);border:1px solid var(--card-bh);\n  border-radius:14px;color:var(--t1);\n  font-size:12.5px;font-weight:700;\n  box-shadow:var(--shadow);\n  display:flex;align-items:center;gap:8px;\n  opacity:0;transition:all .3s cubic-bezier(.34,1.56,.64,1);\n  pointer-events:none;white-space:nowrap;\n  backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);\n}\n.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}\n.toast.ok{background:var(--green-bg);border-color:var(--green);color:var(--green-t)}\n.toast.err{background:var(--red-bg);border-color:var(--red);color:var(--red-t)}\n\n/* ═════════ EMPTY ═════════ */\n.empty{text-align:center;padding:50px 20px;color:var(--t3)}\n.empty i{font-size:44px;opacity:.35;margin-bottom:12px;display:block}\n.empty p{font-size:12.5px;margin-top:4px}\n\n/* ═════════ DASHBOARD FOOTER ═════════ */\n.dash-footer{\n  border-top:1px solid var(--card-b);\n  margin-top:14px;padding-top:14px;\n  display:flex;align-items:center;justify-content:space-between;\n  flex-wrap:wrap;gap:8px;\n}\n.df-text{font-size:10px;color:var(--t3)}\n.df-link{font-size:11.5px;color:var(--accent);display:flex;align-items:center;gap:5px;font-weight:600}\n\n/* ═════════ RESPONSIVE ═════════ */\n@media(max-width:1050px){\n  .sidebar{transform:translateX(-105%)}\n  body.ui-fa .sidebar{transform:translateX(105%)}\n  .sidebar.open{transform:translateX(0) !important;box-shadow:0 0 55px rgba(0,0,0,.55)}\n  .sb-close{display:flex}\n  body.ui-fa .main,body.ui-en .main{margin-inline-start:0;margin-inline-end:0;padding-top:80px}\n  .mob-top{display:flex}\n  .metrics{grid-template-columns:1fr 1fr}\n  .g2,.g3{grid-template-columns:1fr}\n  .traf-hero{grid-template-columns:1fr 1fr}\n  .conn-hero{grid-template-columns:1fr 1fr}\n}\n@media(max-width:768px){\n  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}\n  .cfg-card{border-radius:18px}\n  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}\n  .cfg-identity{min-width:0}\n  .cfg-usage-col{min-width:0}\n  .cfg-exp-col{min-width:0}\n  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}\n  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}\n  .cfg-divider-v{display:none}\n  .cp-row{grid-template-columns:1fr}\n  .proto-cards{grid-template-columns:repeat(2,1fr)}\n  .cp-footer{flex-direction:column;align-items:stretch}\n  .cp-submit-btn{justify-content:center}\n}\n@media(max-width:640px){\n  .traf-hero{grid-template-columns:1fr}\n  .traf-chart-body{height:260px}\n  .hero-stats{grid-template-columns:1fr 1fr}\n}\n@media(max-width:560px){\n  .top-status{display:none}\n  .main{padding:76px 12px 44px}\n  .tb-title{font-size:17px}\n  .metrics{grid-template-columns:1fr !important;gap:10px}\n  .metric{min-height:120px;padding:15px}\n  .m-val{font-size:23px}\n  .srv-tiles{grid-template-columns:1fr}\n  .sub-grid,.conn-grid-v2{grid-template-columns:1fr}\n}\n@media(max-width:500px){\n  .conn-hero{grid-template-columns:1fr}\n  .sub-card-stats{grid-template-columns:repeat(3,1fr)}\n}\n\n/* ═════════ BILINGUAL PROTOCOL CARD SAFETY ═════════ */\n.proto-card-title,.proto-card-desc{min-width:0;max-width:100%;white-space:normal;overflow-wrap:anywhere;word-break:normal;text-align:center;unicode-bidi:plaintext;}\n.proto-card-title{line-height:1.25;}\n.proto-card-desc{line-height:1.65;}\n/* ═════════ INPUT OVERFLOW FIX ═════════ */\ninput,textarea,select{box-sizing:border-box!important;max-width:100%!important;min-width:0!important}\n.cp-input-full,.modal-v2-input,.pw-input,.tg-input,.fi,.fs,.lmodal-search input,.subs-search input,.lock-input,#nl-token,#nl-label,#nl-note,#nl-val,#nl-exp,#nl-port,#nl-iplimit,#nl-speed,#el-label,#el-token,#el-val,#el-exp,#el-note,#el-alpn,#el-port,#el-iplimit,#el-speed,#ws-uuid,#ws-msg,#tg-token,#tg-admins,#cp-user,#cp-cur,#cp-new,#cp-cf,#ns-name,#ns-desc,#ns-pw{width:100%!important;max-width:100%!important;box-sizing:border-box!important;min-width:0!important}\n.cp-block,.modal-v2-body,.modal-v2-field,.modal-v2-input-wrap,.pw-body,.tg-body,.lmodal-search,.subs-search,.fg,.cp-mini-row,.cp-quota-inputs,.form-row{overflow:hidden;min-width:0}\n.cp-mini-row,.cp-quota-inputs,.form-row{display:flex;flex-wrap:wrap;gap:8px;min-width:0}\n.cp-mini-row>*,.cp-quota-inputs>*,.form-row>*{min-width:0;flex:1 1 auto}\n.cp-quota-inputs select.cp-input-full{flex:0 0 76px!important;max-width:76px!important}\n.subs-search input,.lmodal-search input{padding-inline-start:42px!important;padding-inline-end:14px!important}\n.subs-search i,.lmodal-search i{inset-inline-start:14px!important;inset-inline-end:auto!important;top:50%!important;transform:translateY(-50%)!important;pointer-events:none}\nselect.cp-input-full,select.fs,select.fi{box-sizing:border-box!important;background-repeat:no-repeat!important;background-size:13px 13px!important}\nbody.ui-fa select.cp-input-full,body.ui-fa select.fs,body.ui-fa select.fi{background-position:left 12px center!important;padding-inline-start:38px!important;padding-inline-end:13px!important}\nbody.ui-en select.cp-input-full,body.ui-en select.fs,body.ui-en select.fi{background-position:right 12px center!important;padding-inline-start:13px!important;padding-inline-end:38px!important}\n/* ═════════ WEBSOCKET TEST · COMPACT ═════════ */\n#pg-testws .form-row{align-items:stretch !important;gap:8px !important;margin-bottom:10px !important}\n#pg-testws .form-row .fi{padding:9px 13px !important;font-size:12px !important;height:auto !important;min-height:38px !important}\n#pg-testws .form-row .btn{padding:9px 16px !important;font-size:11.5px !important;min-height:38px !important;border-radius:10px !important;flex:0 0 auto !important;white-space:nowrap !important}\n#pg-testws .form-row .btn i{font-size:13px !important}\n#pg-testws .card{padding:16px 18px !important}\n#pg-testws .cl{margin-bottom:10px !important;padding:9px 12px !important;font-size:10.5px !important}\n#pg-testws .fg label{font-size:9.5px !important;margin-bottom:5px !important}\n#pg-testws #ws-log{height:200px !important;padding:12px !important;font-size:10px !important}\n/* ═════════ WEBSOCKET TEST · EQUAL BUTTONS ═════════ */\n#pg-testws .form-row .btn{align-self:flex-end !important;height:38px !important;min-height:38px !important;max-height:38px !important;padding:0 16px !important;display:inline-flex !important;align-items:center !important;justify-content:center !important}\n#pg-testws .form-row .fg{align-self:flex-end !important}\n#pg-testws .form-row .fg input{height:38px !important}\n/* ═════════ LEGACY VAR ALIASES ═════════ */\n:root{--accent2:var(--accent-2);--accent-d:var(--accent-soft);--card:var(--surface-solid)}\n/* ═════════ CHART.JS IN CSS GRID FIX ═════════ */\n.g2>*,.g3>*{min-width:0 !important;max-width:100% !important;overflow:hidden}\n.ch,.ch-sm,.ch-lg{position:relative !important;width:100% !important;max-width:100% !important;overflow:hidden !important;contain:layout size paint}\n.ch>canvas,.ch-sm>canvas,.ch-lg>canvas{display:block !important;max-width:100% !important;max-height:100% !important}\n.bg-purple{background:rgba(167,139,250,.15);color:#a78bfa}\n.server-ip-badge{padding:4px 10px 4px 8px!important;gap:7px!important}\n.server-ip-flag-wrap{width:28px;height:20px;border-radius:5px;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;background:rgba(255,255,255,.08);box-shadow:0 0 0 1px rgba(255,255,255,.08)}\n.server-ip-flag{width:28px;height:20px;object-fit:cover;display:block;image-rendering:auto}\n.server-ip-badge #server-ip-text{font-weight:800;letter-spacing:.01em}\n.srv-info-main{display:flex;align-items:center;gap:10px;min-width:0;flex-wrap:wrap}\n.srv-info-flag-wrap{width:56px;height:38px;border-radius:8px;overflow:hidden;display:inline-flex;align-items:center;justify-content:center;flex:0 0 auto;background:rgba(255,255,255,.08);box-shadow:0 0 0 1px rgba(255,255,255,.08)}\n.srv-info-flag{width:56px;height:38px;object-fit:cover;display:block;image-rendering:auto}\n.srv-info-copy{display:flex;flex-direction:column;gap:3px;min-width:0}\n.srv-info-ip{font-weight:800;color:var(--t1);font-size:13px;line-height:1.25}\n.srv-info-meta{font-size:10.5px;color:var(--t2);line-height:1.55;display:flex;align-items:center;flex-wrap:wrap;gap:3px 7px;word-break:break-word}\n.srv-info-meta b{color:var(--t1)}\n.srv-info-meta .srv-info-part{unicode-bidi:isolate;white-space:nowrap;max-width:100%}\n.srv-info-meta .srv-info-sep{color:var(--t3);opacity:.8;user-select:none}\nbody.ui-fa .srv-info-meta{direction:rtl}\nbody.ui-en .srv-info-meta{direction:ltr}\n\n'

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OMID-IRAN PANEL · Login</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>__THEME_CSS__
__LOGIN_CSS__
</style>
</head>
<body>
<div class="scan"></div><div class="shell">
  <div class="hud"><span class="kicker">OMID-01 / SECURE ACCESS GATE</span><div style="display:flex;gap:6px"><button class="lang" id="lang-login" type="button">EN</button><button class="lang" id="theme-login" type="button">☼</button></div></div>
  <div class="card">
    <div class="brand"><div class="brand-img"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div><div><div class="brand-name">OMID-IRAN PANEL</div><div class="brand-sub">Free For All · v2.0.0</div></div></div>
    <h1>Sign in to <span class="accent">OMID-IRAN PANEL</span></h1>
    <p class="sub">Enter your credentials to access the control panel</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field"><label>Username</label><div class="input-shell"><input type="text" id="username" placeholder="Enter username" autocomplete="username" autofocus required><i class="ti ti-user ic"></i></div></div>
      <div class="field"><label>Password</label><div class="input-shell"><input type="password" id="pw" placeholder="Enter password" autocomplete="current-password" required><i class="ti ti-lock ic"></i></div></div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-terminal-2"></i> Sign in to Control Center</button>
    </form>
    <div class="meta-grid"><div class="meta"><span>NETWORK</span><b>OMID Network</b></div><div class="meta"><span>STATUS</span><b class="ok">● SYSTEM ONLINE</b></div></div>
    <div style="margin-top:10px;text-align:center;font-size:8.5px;color:var(--t3)">First run default: <b style="color:var(--accent)">omid / omid</b> · Support: <a href="https://t.me/omid_gamingORG" target="_blank" style="color:var(--accent-2);text-decoration:none">@omid_gamingORG</a></div>
    <div class="foot"><span>Free For All</span><span>OMID-IRAN PANEL · v2.0.0</span></div>
  </div>
</div>
<script>
/* ═══════════════════════════════════════════════════════════════════════
   OMID LANGUAGE CENTER · ENGLISH IS THE CANONICAL UI LANGUAGE
   The HTML/JS UI is authored in English. Persian is a runtime translation.
   IMPORTANT: Never translate already-translated DOM text. Each text node and
   UI attribute is anchored to its original English source string.
   ═══════════════════════════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════════════════════════
   OMID LANGUAGE CENTER · ENGLISH IS THE CANONICAL UI LANGUAGE
   The HTML/JS UI is authored in English. Persian is a runtime translation.
   IMPORTANT: Never translate already-translated DOM text. Each text node and
   UI attribute is anchored to its original English source string.
   ═══════════════════════════════════════════════════════════════════════ */
const OMID_EN_TO_FA = {"optional":"اختیاری","e.g.":"مثلاً","Test Connection":"تست اتصال","Save & Start":"ذخیره و روشن کردن","Stop Bot":"توقف ربات","comma separated: 123,456":"با کاما جدا کن: 123,456","To get your Admin ID, start":"برای دریافت Admin ID، توی ربات","on Telegram. If left empty, nobody can use the bot.":"رو استارت کن. اگه خالی بذاری، هیچ‌کس نمی‌تونه از ربات استفاده کنه.","(via @BotFather)":"(از @BotFather)","Checking...":"در حال بررسی...","Online & Running":"روشن و در حال کار","Stopped (token saved)":"متوقف (توکن ذخیره‌شده)","Enter the token":"توکن را وارد کنید","Testing...":"در حال تست...","Token is valid":"توکن معتبر است","Invalid token":"توکن نامعتبر است","Token is required":"توکن الزامی است","Enter at least one Admin ID":"حداقل یک Admin ID وارد کنید","Saving and starting bot...":"در حال ذخیره و روشن کردن ربات...","Bot started":"ربات روشن شد","Bot stopped":"ربات متوقف شد","Stopping...":"در حال توقف...","Stop the bot? (token will be saved)":"مطمئنی ربات رو متوقف کنم؟ (توکن ذخیره می‌مونه)","Failed to stop":"خطا در توقف","Delete":"حذف","UUID is generated randomly":"UUID به‌صورت تصادفی تولید می‌شود","Only registered UUIDs may connect":"فقط UUIDهای ثبت‌شده اجازه اتصال دارند","Random UUID · pick quota, expiry and protocol":"UUID تصادفی · سهمیه، انقضا و پروتکل را انتخاب کنید","Protocol cannot be changed after creation":"پروتکل پس از ساخت قابل تغییر نیست","Link copied":"لینک کپی شد","Sub link copied":"لینک ساب کپی شد","UUID copied":"UUID کپی شد","IP copied":"IP کپی شد","IP · Server Location":"IP · لوکیشن سرور","Activated ✓":"فعال شد ✓","Activated":"فعال شد","Deactivated":"غیرفعال شد","Error":"خطا","Usage reset ✓":"مصرف ریست شد ✓","Refreshed":"رفرش شد","Enter UUID":"UUID را وارد کنید","No changes to save":"تغییری برای ذخیره وجود ندارد","Group configurations saved ✓":"کانفیگ‌های گروه ذخیره شدند ✓","✓ Connected - Valid UUID":"✓ متصل - UUID معتبر","✗ Error - Invalid or inactive UUID":"✗ خطا - UUID نامعتبر یا غیرفعال","Copied":"کپی شد","Sign in to Control Center":"ورود به مرکز کنترل","SYSTEM ONLINE":"سیستم آنلاین","Test message...":"پیام تست...","Connected: ":"اتصال: ","Sent: ":"ارسال: ","Received ":"دریافت ","Closed (":"قطع (","Subscription":"سابسکریپشن","Session":"سشن","Disconnect":"قطع","Strong":"قوی","PANEL":"پنل","Help":"کمک","Copy":"کپی","Logout":"خروج","Refresh":"رفرش","Live":"زنده","Weak":"ضعیف","Active":"فعال","Usage":"مصرف","Version":"نسخه","Unit":"واحد","Sign In":"ورود","Group":"گروه","1 GB":"۱ GB","5 GB":"۵ GB","Connect":"اتصال","Send":"ارسال","of total":"از کل","Security":"امنیت","Night Mode":"تم شب","Distribution":"توزیع","Errors":"خطاها","SYSTEM":"سیستم","Title":"عنوان","Medium":"متوسط","Expired":"منقضی","All":"همه","10 GB":"۱۰ GB","50 GB":"۵۰ GB","7 days":"۷ روز","Online":"آنلاین","Uptime":"آپتایم","Cancel":"انصراف","Traffic":"ترافیک","Protected":"رمزدار","Password hash":"هش رمز","Edit":"ویرایش","Public":"پابلیک","Platform":"پلتفرم","Configurations":"کانفیگ‌ها","Copy IP":"کپی IP","0 groups":"۰ گروه","1 Mbps":"۱ Mbps","30 days":"۳۰ روز","5 Mbps":"۵ Mbps","500 MB":"۵۰۰ MB","90 days":"۹۰ روز","Connections":"اتصالات","Light Mode":"تم روشن","Settings":"تنظیمات","Dashboard":"داشبورد","Custom...":"دستی...","Inactive":"غیرفعال","Active v9":"فعال v9","Clear All":"لغو همه","Average":"میانگین","Unlimited":"نامحدود","Sign in to":"ورود به","Copy all":"کپی همه","GitHub":"گیت‌هاب","Note":"یادداشت","1 user":"۱ کاربر","10 Mbps":"۱۰ Mbps","2 users":"۲ کاربر","25 Mbps":"۲۵ Mbps","5 users":"۵ کاربر","Relative Load":"بار نسبی","Open":"باز کردن","Dark Mode":"تم تاریک","Deleted ✓":"حذف شد ✓","New Password":"رمز جدید","Password":"رمز عبور","Current Password":"رمز فعلی","Encryption":"رمزنگاری","Framework":"فریم‌ورک","Password strength":"قدرت رمز","Group Name":"نام گروه","Support":"پشتیبانی","Usage peak":"پیک مصرف","Copied ✓":"کپی شد ✓","Copy link":"کپی لینک","Very weak":"خیلی ضعیف","Reset usage":"ریست مصرف","Create Group":"ساخت گروه","Error Logs":"لاگ خطاها","Connection duration":"مدت اتصال","Protocols":"پروتکل‌ها","Support:":"پشتیبانی:","Total Traffic":"کل ترافیک","New Group":"گروه جدید","MB per hour":"MB در ساعت","Theme":"تم","Account Security":"امنیت حساب","selected":"انتخاب شده","Select All":"انتخاب همه","Storage":"ذخیره‌سازی","Subscriptions":"سابسکریپشن","Free For All":"رایگان برای همه","Username":"نام کاربری","Connection Port":"پورت اتصال","icon.":"کلیک کنید.","0 = Unlimited":"0 = نامحدود","Expiry date":"تاریخ انقضا","Creation failed":"خطا در ساخت","Create Configuration":"ساخت کانفیگ","Service Status":"وضعیت سرویس","Active Configs":"کانفیگ فعال","Lowest usage":"کمترین مصرف","Access Group":"گروه دسترسی","Close":"بستن","Save":"ذخیره","Active Connections":"اتصالات فعال","No description":"بدون توضیحات","Save failed":"خطا در ذخیره","Traffic Quota":"سهمیه ترافیک","Configuration ID":"شناسه کانفیگ","Enable/Disable":"فعال/غیرفعال","Connection List":"لیست اتصالات","Speed Limit":"محدودیت سرعت","Enter Group":"ورود به گروه","Default port":"پورت پیش‌فرض","Telegram Channel":"کانال تلگرام","Limited Config":"کانفیگ محدود","Access Control":"کنترل دسترسی","Copy subscription link":"کپی لینک ساب","Subscription Groups":"گروه‌های ساب","0 selected":"۰ انتخاب شده","● Active (443)":"● فعال (443)","Since startup":"از راه‌اندازی","Peak hour":"بالاترین ساعت","WebSocket Test":"تست WebSocket","Update failed":"خطا در ویرایش","Save Changes":"ذخیره تغییرات","CDN compatible":"سازگار با CDN","Active · 3 modes":"فعال · 3 mode","Activity Logs":"لاگ فعالیت‌ها","Link copied ✓":"لینک کپی شد ✓","IP Limit":"محدودیت آی‌پی","Hourly average":"میانگین ساعتی","All configurations":"همه کانفیگ‌ها","Edit Configuration":"ویرایش کانفیگ","Configuration Type":"نوع کانفیگ","Transport":"ترابرد","Lightweight & versatile":"سبک و همه‌منظوره","Compatible with clients":"سازگار با کلاینت‌ها","TLS · Password · lightweight":"TLS · رمزعبور · سبک","Stable & widely supported":"پایدار و شناخته‌شده","Highly CDN-compatible":"سازگاری بالا با CDN","Stream-based upload & download":"آپلود و دانلود جریان‌محور","Transport Protocol":"پروتکل انتقال","Configuration deleted":"کانفیگ حذف شد","Group deleted ✓":"گروه حذف شد ✓","— No group —":"— بدون گروه —","Unique IPs":"آی‌پی‌های یکتا","Lower latency":"تاخیر پایین‌تر","Confirm New Password":"تکرار رمز جدید","Signing in...":"در حال ورود...","Wrong password":"رمز اشتباه است","Waiting for connection...":"منتظر اتصال...","No errors":"هیچ خطایی نیست","Protocol default":"پیش‌فرض پروتکل","Language":"زبان","Delete this configuration?":"حذف این کانفیگ؟","Load failed":"خطا در بارگذاری","Configuration Summary":"خلاصه کانفیگ‌ها","Contact Channels":"راه‌های ارتباطی","Subscription link copied":"لینک ساب کپی شد","Custom ALPN":"مقدار دستی ALPN","New Username":"نام کاربری جدید","Hide link":"پنهان کردن لینک","Active configurations":"کانفیگ‌های فعال","Total traffic usage":"کل ترافیک مصرفی","Group created ✓":"گروه ساخته شد ✓","HttpOnly · 7 days":"HttpOnly · 7 روز","Last update:":"آخرین بروزرسانی:","Online · OMIDIRAN":"آنلاین · OMIDIRAN","Search configurations...":"جستجوی کانفیگ...","Group creation failed":"خطا در ساخت گروه","Loading...":"در حال بارگذاری...","Save Account Security":"ذخیره امنیت حساب","Traffic usage trend":"روند مصرف ترافیک","e.g. User Ali":"مثلاً: کاربر علی","Subscription group & expiry":"گروه ساب و انقضا","Hourly Traffic (MB)":"ترافیک ساعتی (MB)","Description (optional)":"توضیحات (اختیاری)","Contains a number · Number":"شامل عدد · Number","Active · strict":"فعال · سخت‌گیرانه","Manage Configurations":"مدیریت کانفیگ‌ها","Average connection duration":"میانگین مدت اتصال","Show configuration link":"نمایش لینک کانفیگ","No groups yet":"هنوز گروهی ندارید","Configuration created ✓":"کانفیگ ساخته شد ✓","Note (optional)":"یادداشت (اختیاری)","FA / EN · Bilingual":"FA / EN · دو زبانه","Public link copied":"لینک پابلیک کپی شد","No activity logs yet":"هنوز لاگی ثبت نشده","Configuration updated ✓":"کانفیگ ویرایش شد ✓","No configuration exists":"کانفیگی وجود ندارد","UUID of an active configuration":"UUID یک کانفیگ فعال","Search groups...":"جستجو در گروه‌ها...","Public subscription page password":"رمز صفحه پابلیک ساب","Current password is required":"رمز فعلی الزامی است","Quota (0 = Unlimited)":"سهمیه (0 = نامحدود)","Configuration enabled/disabled":"فعال/غیرفعال کانفیگ","Stable & general purpose":"پایدار و همه‌منظوره","● Optional · SHA-256":"● اختیاری · SHA-256","Strict UUID Auth":"UUID Auth سخت‌گیرانه","Realtime traffic total":"مجموع ترافیک لحظه‌ای","No active connections":"هیچ اتصال فعالی نیست","ALPN (blank = default)":"ALPN (خالی = پیش‌فرض)","Total Usage":"کل مصرف","Enter password":"رمز عبور را وارد کنید","Only when changing the password":"فقط در صورت تغییر رمز","No configuration to copy":"کانفیگی برای کپی نیست","Leave empty = no password":"خالی بگذارید = بدون رمز","NEW PASSWORD":"رمز جدید","Full subscription (admin)":"سابسکریپشن کامل (ادمین)","Group subscription links":"لینک سابسکریپشن گروه‌ها","Enter username":"نام کاربری را وارد کنید","No configurations yet":"هنوز کانفیگی وجود ندارد","Expiry (days) · 0 = unlimited":"انقضا (روز) · 0 = نامحدود","New passwords do not match":"تکرار رمز جدید یکسان نیست","Admin Account":"حساب مدیر","Public Page Password (optional)":"رمز صفحه پابلیک (اختیاری)","Your connection is encrypted":"اتصال شما رمزنگاری‌شده است","Based on megabytes per hour":"بر اساس مگابایت در هر ساعت","Minimum 4 characters · 4+ chars":"حداقل ۴ کاراکتر · 4+ chars","Single subscription (per configuration)":"سابسکریپشن تکی (هر کانفیگ)","Create New Group":"ساخت گروه جدید","Includes all active configurations.":"شامل تمام کانفیگ‌های فعال.","Speed Limit (0 = Unlimited)":"محدودیت سرعت (0 = نامحدود)","Auto-refresh every 5 seconds":"بروزرسانی خودکار هر ۵ ثانیه","Complete panel event history":"تاریخچه کامل رخدادهای پنل","Mixed case":"حروف بزرگ/کوچک","CURRENT PASSWORD":"رمز فعلی","Default Link (Unlimited)":"لینک پیش‌فرض (بدون محدودیت)","IP Limit (0 = Unlimited)":"محدودیت آی‌پی (0 = نامحدود)","Enter to save changes":"برای ذخیره تغییرات وارد کنید","Changes apply immediately":"تغییرات بلافاصله اعمال می‌شود","New password must be at least 4 characters":"رمز جدید باید حداقل ۴ کاراکتر باشد","Concurrent IP / user limit":"محدودیت آی‌پی / کاربر هم‌زمان","NEW USERNAME":"نام کاربری جدید","Live Connections":"اتصالات زنده","Manage panel login credentials":"اطلاعات ورود پنل را مدیریت کنید","Account updated successfully ✓":"اطلاعات حساب با موفقیت ذخیره شد ✓","CONFIRM PASSWORD":"تکرار رمز جدید","Save account information":"ذخیره اطلاعات حساب","Subscription links for v2ray apps":"لینک‌های اشتراک برای اپ‌های v2ray","Username cannot contain spaces":"نام کاربری نباید فاصله داشته باشد","Bandwidth usage analysis & monitoring":"تحلیل و مانیتورینگ مصرف پهنای باند","443 (TLS) · configurable per configuration":"443 (TLS) · قابل تغییر در هر کانفیگ","Empty = no change · minimum 4 characters":"خالی = بدون تغییر · حداقل ۴ کاراکتر","Delete this group? Configurations will not be deleted.":"حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.","UUID (must exist in configurations)":"UUID (باید در کانفیگ‌ها وجود داشته باشد)","Username must be 3–32 characters":"نام کاربری باید بین ۳ تا ۳۲ کاراکتر باشد","Live IP and traffic monitoring for each connection":"مانیتورینگ زنده آی‌پی و ترافیک هر اتصال","Expiry (days from now, 0 = unchanged/unlimited)":"انقضا (روز از الان، 0 = بدون تغییر/نامحدود)","Copy all active links in this group":"تمام لینک‌های فعال این گروه را یک‌جا کپی کن","Copy all configurations":"کپی همه کانفیگ‌ها","Enter your credentials to access the control panel":"برای ورود به پنل مشخصات دسترسی خود را وارد کنید","Leave expiry at zero to keep the current expiry.":"برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.","Connections appear here as clients connect":"به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند","Create and manage configs with quota, expiry and groups":"ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی","Create a dedicated public page for managing configurations":"یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید","Manage panel username and password here":"نام کاربری و رمز عبور پنل را از همین‌جا مدیریت کنید","Each group has a separate public page with its own configurations":"هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد","Select the configurations for this group":"کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید","Each configuration has its own subscription URL. From the configuration card, click the":"هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون","Create a new group to organize configurations":"یک New Group / گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید","This group is password protected. Enter the password to view its configurations.":"این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز را وارد کنید.","This URL only works in the browser signed in to the panel (session cookie required).":"این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).","This group public page will be available through a unique internet link.":"صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.","Current password is required to change username or password. Existing sessions will be closed when saved.":"برای تغییر نام کاربری یا رمز، رمز فعلی الزامی است. با ذخیره تغییرات، نشست‌های قبلی بسته می‌شوند.","Only registered active UUIDs may connect (this is a VLESS/WS test; XHTTP is tested from the client).":"فقط UUIDهای ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).","Telegram Bot":"ربات تلگرام","Manage Telegram bot for remote panel control":"مدیریت ربات تلگرام برای کنترل پنل از راه دور","Status:":"وضعیت:","Random":"تصادفی","Short description for this group":"توضیح کوتاه درباره این گروه","Server IP":"IP سرور","Clear":"پاک کردن","New Configuration":"کانفیگ جدید","Connected IPs / limit":"آی‌پی‌های متصل / محدودیت","Default Link":"لینک پیش‌فرض","MB":"مگابایت","Bot:":"ربات:","Protocol":"پروتکل"};
Object.assign(OMID_EN_TO_FA, {
  'Access denied':'دسترسی رد شد',
  'Connections':'اتصالات',
  'Connection':'اتصال',
  'seconds':'ثانیه',
  'minutes':'دقیقه',
  'hours':'ساعت',
  'errors':'خطا',
  'Error':'خطا',
  'OMID-IRAN PANEL · Login':'OMID-IRAN PANEL · ورود'
});

const OMID_EN_RULES = Object.entries(OMID_EN_TO_FA)
  .sort((a,b)=>b[0].length-a[0].length);
const OMID_TEXT_SOURCE = new WeakMap();
const OMID_ATTR_SOURCE = new WeakMap();

function omidFaDigits(value){
  return String(value).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);
}
function omidPreserveOuterSpace(raw, core){
  const s=String(raw??'');
  const lead=(s.match(/^\s*/)||[''])[0];
  const trail=(s.match(/\s*$/)||[''])[0];
  return lead+core+trail;
}
function omidTranslateDynamic(core){
  let m;
  if((m=core.match(/^(\d+)\s+selected$/i))) return `${omidFaDigits(m[1])} انتخاب شده`;
  if((m=core.match(/^(\d+)\s+configurations$/i))) return `${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^of\s+(\d+)\s+configurations$/i))) return `از کل ${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^(\d+)\s+groups$/i))) return `${omidFaDigits(m[1])} گروه`;
  if((m=core.match(/^(\d+)\s+connections$/i))) return `${omidFaDigits(m[1])} اتصال`;
  if((m=core.match(/^(\d+)\s+errors$/i))) return `${omidFaDigits(m[1])} خطا`;
  if((m=core.match(/^(\d+)\s+seconds$/i))) return `${omidFaDigits(m[1])} ثانیه`;
  if((m=core.match(/^(\d+)\s+minutes$/i))) return `${omidFaDigits(m[1])} دقیقه`;
  if((m=core.match(/^(\d+)\s+hours$/i))) return `${omidFaDigits(m[1])} ساعت`;
  if((m=core.match(/^(\d+)\s+days remaining$/i))) return `${omidFaDigits(m[1])} روز مانده`;
  if((m=core.match(/^Last update:\s*(.*)$/i))) return `آخرین بروزرسانی: ${m[1]}`;
  if((m=core.match(/^Connected:\s*(.*)$/i))) return `اتصال: ${m[1]}`;
  if((m=core.match(/^Sent:\s*(.*)$/i))) return `ارسال: ${m[1]}`;
  if((m=core.match(/^Received\s+(.*)$/i))) return `دریافت ${m[1]}`;
  if((m=core.match(/^Closed \((.*)$/i))) return `قطع (${m[1]}`;
  if((m=core.match(/^\[(.+)\] (.+)$/s))) return `[${m[1]}] ${m[2]}`;
  return null;
}
function omidTranslateText(raw, lang){
  const s=String(raw??'');
  if(lang==='en' || !s.trim()) return s;
  const core=s.trim();
  if(Object.prototype.hasOwnProperty.call(OMID_EN_TO_FA,core)){
    return omidPreserveOuterSpace(s,OMID_EN_TO_FA[core]);
  }
  const dynamic=omidTranslateDynamic(core);
  if(dynamic!==null) return omidPreserveOuterSpace(s,dynamic);

  // Safe phrase translation: only known English phrases are replaced, and
  // only against the immutable English source string stored for the node.
  let out=core;
  for(const [en,fa] of OMID_EN_RULES){
    if(out.includes(en)) out=out.split(en).join(fa);
  }
  return omidPreserveOuterSpace(s,out);
}
function omidRememberText(node){
  if(!OMID_TEXT_SOURCE.has(node)) OMID_TEXT_SOURCE.set(node,node.nodeValue);
  return OMID_TEXT_SOURCE.get(node);
}
function omidRememberAttr(el,attr){
  let rec=OMID_ATTR_SOURCE.get(el);
  if(!rec){rec={};OMID_ATTR_SOURCE.set(el,rec);}
  if(rec[attr]===undefined) rec[attr]=el.getAttribute(attr) || '';
  return rec[attr];
}
function omidApplyLanguage(root,lang){
  const target=root||document.body;
  if(!target) return;
  const walker=document.createTreeWalker(target,NodeFilter.SHOW_TEXT);
  const nodes=[];
  while(walker.nextNode()){
    const n=walker.currentNode;
    const p=n.parentElement;
    if(!p || !n.nodeValue || !n.nodeValue.trim()) continue;
    if(['SCRIPT','STYLE','NOSCRIPT','CODE','PRE'].includes(p.tagName)) continue;
    if(p.closest('[data-i18n-ignore="true"]')) continue;
    nodes.push(n);
  }
  for(const n of nodes){
    const source=omidRememberText(n);
    n.nodeValue=omidTranslateText(source,lang);
  }
  const attrs=['placeholder','title','aria-label'];
  target.querySelectorAll('input,button,select,textarea,[title],[aria-label]').forEach(el=>{
    for(const attr of attrs){
      if(!el.hasAttribute(attr)) continue;
      el.setAttribute(attr,omidTranslateText(omidRememberAttr(el,attr),lang));
    }
  });
  document.documentElement.lang=lang;
  document.documentElement.dir=lang==='en'?'ltr':'rtl';
}

const lb=document.getElementById('lang-login');
let l=localStorage.getItem('omid-lang')||'en';
function setLoginUI(){
  document.documentElement.lang=l;
  document.documentElement.dir=l==='en'?'ltr':'rtl';
  document.body.classList.toggle('login-en',l==='en');
  if(lb)lb.textContent=l==='en'?'FA':'EN';
  omidApplyLanguage(document.body,l);
  document.title=omidTranslateText('OMID-IRAN PANEL · Login',l);
}
if(lb)lb.addEventListener('click',()=>{l=l==='en'?'fa':'en';localStorage.setItem('omid-lang',l);setLoginUI();});
setLoginUI();
const themeLogin=document.getElementById('theme-login');
let loginDark=localStorage.getItem('omid-login-theme')!=='light';
function applyLoginTheme(){document.documentElement.setAttribute('data-login-theme',loginDark?'dark':'light');themeLogin.textContent=loginDark?'☼':'☾';localStorage.setItem('omid-login-theme',loginDark?'dark':'light');}
themeLogin.addEventListener('click',()=>{loginDark=!loginDark;applyLoginTheme();});
applyLoginTheme();
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> '+(l==='en'?'Signing in...':'Signing in...');
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:document.getElementById('username').value.trim(),password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'Error');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');btn.disabled=false;
    btn.innerHTML='<i class="ti ti-terminal-2"></i> '+(l==='en'?'Sign in to Control Center':'Sign in to Control Center');
  }
});
</script></body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OMID-IRAN PANEL · OMID</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdn.jsdelivr.net/npm/qr-code-styling@1.6.0-rc.1/lib/qr-code-styling.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>__THEME_CSS__
__DASHBOARD_CSS__
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">Manage Configurations <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">Select the configurations for this group</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="Search configurations..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> Select All</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> Clear All</button>
        <span class="lmodal-count" id="lmodal-count">0 selected</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">Loading...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> Changes apply immediately</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">Close</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> Save</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">Create New Group</div>
      <div class="modal-v2-sub">Create a dedicated public page for managing configurations</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> Group Name</label>
        <input class="modal-v2-input" id="ns-name" placeholder="e.g. Telegram Channel">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> Description (optional)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="Short description for this group">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> Public Page Password (optional)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="Leave empty = no password">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>This group public page will be available through a unique internet link.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">Cancel</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> Create Group</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> Edit Configuration</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>Title</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>Sub Token (optional)</label><input class="fi" id="el-token" placeholder="e.g. OMIDIRAN" maxlength="32" pattern="[A-Za-z0-9_-]{3,32}" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Quota (0 = Unlimited)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>Expiry (days from now, 0 = unchanged/unlimited)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>Note</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (blank = default)</label><input class="fi" id="el-alpn" placeholder="e.g. h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>Connection Port</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>IP Limit (0 = Unlimited)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>Speed Limit (0 = Unlimited)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>Unit</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>Leave expiry at zero to keep the current expiry.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">Cancel</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> Save Changes</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div>
    <div class="mob-brand-copy"><span class="mob-title">OMID-IRAN PANEL</span><span class="mob-subtitle">Free For All · v2.0.0</span></div>
  </div>
  <div class="mob-right">
    <span class="top-status"><span class="dot dg pulse"></span> SYSTEM ONLINE</span>
    <button class="lang-btn" onclick="toggleUiLang()" id="lang-btn">FA / EN</button>
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div>
    <div><div class="logo-name">OMID-IRAN PANEL</div><div class="logo-sub">Free For All · v2.0.0</div><div class="logo-meta">OMID NETWORK NODE</div></div>
  </div>
  <div class="side-telemetry">
    <div class="telemetry-head"><span>CORE TELEMETRY</span><span class="telemetry-led"></span></div>
    <div class="telemetry-grid">
      <div><span>NODE</span><b>OMID-01</b></div>
      <div><span>ENGINE</span><b>VLESS / XHTTP</b></div>
    </div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec"><span class="nav-sec-label">PANEL</span></div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i><span class="nav-label">Dashboard</span></div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i><span class="nav-label">Configurations</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i><span class="nav-label">Subscription Groups</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i><span class="nav-label">Subscriptions</span></div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i><span class="nav-label">Traffic</span></div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i><span class="nav-label">Connections</span></div>
    <div class="nav-sec"><span class="nav-sec-label">SYSTEM</span></div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i><span class="nav-label">Security</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i><span class="nav-label">Activity Logs</span></div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i><span class="nav-label">Errors</span></div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i><span class="nav-label">WebSocket Test</span></div>
    <div class="nav-it" data-pg="telegram"><i class="ti ti-brand-telegram"></i><span class="nav-label">Telegram Bot</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i><span class="nav-label">Settings</span></div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i><span class="nav-label">Support</span></div>
  </div>
  <div class="sb-foot">
    <button class="side-lang" onclick="toggleUiLang()"><i class="ti ti-language"></i><span id="side-lang-label" data-i18n-fixed="true">FA / EN · Bilingual</span></button>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label" data-i18n-fixed="true">Light Mode</span></button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> Logout</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> Dashboard</div><div class="tb-sub" id="last-upd">Loading...</div></div>
    <div class="tb-right">
      <span class="badge bg-purple server-ip-badge" id="server-ip-badge" title="Server IP">
        <span class="server-ip-flag-wrap" id="server-ip-flag-wrap">
          <img id="server-ip-flag" class="server-ip-flag" alt="" title="Server IP" loading="lazy" decoding="async" referrerpolicy="no-referrer">
        </span>
        <span id="server-ip-text">…</span>
      </span>
      <span class="badge bg-green"><span class="dot dg pulse"></span> Active</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">Active Connections</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP Live</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">Total Traffic</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">Since startup</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">Active Configs</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">of total</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">Subscription Groups</div><div class="m-val" id="m-subs">—</div><div class="m-sub">Active</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> Default Link (Unlimited)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">Loading...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> Copy</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> Limited Config</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> Subscription Groups</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> Hourly Traffic (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> Distribution</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> Service Status</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● Active · strict</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● Active · 3 modes</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> Uptime</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> Relative Load</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> Configuration Summary <span class="ml-auto badge bg-blue" id="lsummary-badge">0</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">OMID-IRAN PANEL v2.0.0 · OMID Network</span>
    
    
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> Configurations</div><div class="tb-sub">Create and manage configs with quota, expiry and groups</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">0 Configurations</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">Create Configuration</div>
        <div class="cp-head-sub">Random UUID · pick quota, expiry and protocol</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> Configuration ID</div>
          <input class="cp-input-full" id="nl-label" placeholder="e.g. User Ali">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="Note (optional)">
          </div>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-token" placeholder="Sub Token (optional) — e.g. OMIDIRAN" maxlength="32" pattern="[A-Za-z0-9_-]{3,32}">
          </div>
          <div class="chip-row">
            <span class="chip" onclick="document.getElementById('nl-token').value='OMIDIRAN'">OMIDIRAN</span>
            <span class="chip" onclick="document.getElementById('nl-token').value='VIP'">VIP</span>
            <span class="chip" onclick="document.getElementById('nl-token').value='FREE'">FREE</span>
            <span class="chip" onclick="document.getElementById('nl-token').value=''">Clear</span>
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> Subscription group & expiry</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— No group —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="Expiry (days) · 0 = unlimited">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">Unlimited</span>
            <span class="chip" onclick="setExpiry(7,this)">7 days</span>
            <span class="chip active" onclick="setExpiry(30,this)">30 days</span>
            <span class="chip" onclick="setExpiry(90,this)">90 days</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> Traffic Quota</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = Unlimited">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">Unlimited</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">500 MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">1 GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">5 GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">10 GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">50 GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-stack-2"></i> Configuration Type</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="vless-xhttp-packet-up">VLESS / XHTTP · packet-up</option>
          <option value="vless-xhttp-stream-up">VLESS / XHTTP · stream-up</option>
          <option value="vmess-ws">VMess / WebSocket</option>
          <option value="vmess-xhttp-packet-up">VMess / XHTTP · packet-up</option>
          <option value="vmess-xhttp-stream-up">VMess / XHTTP · stream-up</option>
          <option value="trojan-ws">Trojan / WebSocket</option>
          <option value="trojan-xhttp-packet-up">Trojan / XHTTP · packet-up</option>
          <option value="trojan-xhttp-stream-up">Trojan / XHTTP · stream-up</option>
        </select>
        <div class="proto-cards proto-family-cards">
          <div class="proto-card active" data-family="vless" onclick="selectBaseProtocol('vless',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS</div>
            <div class="proto-card-desc">Lightweight & versatile</div>
          </div>
          <div class="proto-card" data-family="vmess" onclick="selectBaseProtocol('vmess',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-shield-lock"></i></div>
            <div class="proto-card-title">VMess</div>
            <div class="proto-card-desc">AEAD · Compatible with clients</div>
          </div>
          <div class="proto-card" data-family="trojan" onclick="selectBaseProtocol('trojan',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon proto-card-icon-trojan" aria-label="Trojan logo">
              <svg class="trojan-proto-logo" viewBox="0 0 64 64" aria-hidden="true">
                <path d="M20 14h24v8h5v8c0 9-5 17-17 21C20 47 15 39 15 30v-8h5v-8Z" fill="none" stroke="currentColor" stroke-width="4" stroke-linejoin="round"/>
                <path d="M22 24h20M32 22v23M25 31h14" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
                <path d="M16 14h32" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>
              </svg>
            </div>
            <div class="proto-card-title">Trojan</div>
            <div class="proto-card-desc">TLS · Password · lightweight</div>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-transfer"></i> Transport</div>
        <div class="proto-cards proto-transport-cards">
          <div class="proto-card active" data-transport="ws" onclick="selectTransport('ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-world-www"></i></div>
            <div class="proto-card-title">WebSocket</div>
            <div class="proto-card-desc">Stable & widely supported</div>
          </div>
          <div class="proto-card" data-transport="xhttp-packet-up" onclick="selectTransport('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">Highly CDN-compatible</div>
          </div>
          <div class="proto-card" data-transport="xhttp-stream-up" onclick="selectTransport('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">Stream-based upload & download</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">Protocol default</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">Custom...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="Custom ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> Connection Port</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> Concurrent IP / user limit</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = Unlimited" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">Unlimited</span>
            <span class="chip" onclick="setIpLimit(1,this)">1 user</span>
            <span class="chip" onclick="setIpLimit(2,this)">2 users</span>
            <span class="chip" onclick="setIpLimit(5,this)">5 users</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> Speed Limit</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = Unlimited" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">Unlimited</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">1 Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">5 Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">10 Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">25 Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID is generated randomly · Only registered UUIDs may connect · Protocol cannot be changed after creation.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> Create Configuration</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>No configurations yet</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> Subscription Groups</div><div class="tb-sub">Each group has a separate public page with its own configurations</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">0 groups</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> New Group</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="Search groups..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a new group to organize configurations</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> Subscriptions</div><div class="tb-sub">Subscription links for v2ray apps</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> Single subscription (per configuration)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">Each configuration has its own subscription URL. From the configuration card, click the <i class="ti ti-rss"></i> icon.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> Full subscription (admin)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">Includes all active configurations.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">Loading...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>This URL only works in the browser signed in to the panel (session cookie required).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> Group subscription links</div>
    <div id="sub-groups-list">Loading...</div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> Traffic</div><div class="tb-sub">Bandwidth usage analysis & monitoring</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> Total traffic usage</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">Hourly average</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">Usage peak</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">Peak hour</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">Lowest usage</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB per hour</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> Traffic usage trend</div>
        <div class="traf-chart-sub">Based on megabytes per hour</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> Usage</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> Average</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> Active Connections</div><div class="tb-sub">Live IP and traffic monitoring for each connection</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">Live Connections</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">Realtime traffic total</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">Average connection duration</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">Unique IPs</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> Connection List</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> Auto-refresh every 5 seconds</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">No active connections</div>
    <div class="conn-empty-v2-sub">Connections appear here as clients connect</div>
  </div>
</section>
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> Security</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> Encryption</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● Active (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> Protocols</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> Password hash</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> Session</span><span class="sr-v">HttpOnly · 7 days</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> Access Control</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> Strict UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● Active v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> Configuration enabled/disabled</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> Traffic Quota</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> Expiry date</span><span class="sr-v" style="color:var(--green-t)">● Active</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> Public subscription page password</span><span class="sr-v" style="color:var(--green-t)">● Optional · SHA-256</span></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> Activity Logs</div><div class="tb-sub">Complete panel event history</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>No activity logs yet</p></div></div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> Errors</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">0</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> Error Logs</div><div id="errs-full">—</div></div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> WebSocket Test</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>Only registered active UUIDs may connect (this is a VLESS/WS test; XHTTP is tested from the client).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (must exist in configurations)</label><input class="fi" id="ws-uuid" placeholder="UUID of an active configuration" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> Connect</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> Disconnect</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="Test message..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> Send</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">Waiting for connection...</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-telegram">
  <div class="topbar">
    <div>
      <div class="tb-title"><i class="ti ti-brand-telegram"></i> Telegram Bot</div>
      <div class="tb-sub">Manage Telegram bot for remote panel control</div>
    </div>
    <div class="tb-right">
      <button class="btn btn-p btn-sm" onclick="tgLoad()"><i class="ti ti-refresh"></i> Refresh</button>
    </div>
  </div>
  <!-- ══════ Telegram Bot Panel ══════ -->
  <div class="tg-panel" style="max-width:720px">
    <div class="tg-hero">
      <div class="tg-hero-icon"><i class="ti ti-brand-telegram"></i></div>
      <div class="tg-hero-text">
        <div class="tg-hero-title">Telegram Bot · Management</div>
        <div class="tg-hero-sub" id="tg-status-sub">Status: <span id="tg-status-badge">Checking...</span></div>
      </div>
      <div class="tg-hero-status" id="tg-hero-led"></div>
    </div>
    <div class="tg-body">
      <div class="tg-field">
        <label><i class="ti ti-key"></i> BOT TOKEN <span class="tg-hint">(via @BotFather)</span></label>
        <div class="tg-input-wrap">
          <input class="tg-input" type="password" id="tg-token" placeholder="1234567890:AAAA..." autocomplete="off">
          <button class="tg-eye" type="button" onclick="tgToggleToken()"><i class="ti ti-eye" id="tg-token-eye"></i></button>
        </div>
      </div>
      <div class="tg-field">
        <label><i class="ti ti-users"></i> ADMIN IDS <span class="tg-hint">(comma separated: 123,456)</span></label>
        <input class="tg-input" type="text" id="tg-admins" placeholder="123456789,987654321" autocomplete="off">
      </div>
      <div class="cl" style="margin:0 0 14px 0">
        <i class="ti ti-info-circle"></i>
        <span>To get your Admin ID, start <a href="https://t.me/userinfobot" target="_blank" style="color:var(--accent2)">@userinfobot</a> on Telegram. If left empty, nobody can use the bot.</span>
      </div>
      <div class="tg-actions">
        <button class="btn btn-g" onclick="tgTest()"><i class="ti ti-plug-connected"></i> Test Connection</button>
        <button class="btn btn-p" onclick="tgSave()"><i class="ti ti-device-floppy"></i> Save & Start</button>
        <button class="btn btn-d" onclick="tgStop()"><i class="ti ti-player-stop"></i> Stop Bot</button>
      </div>
      <div class="tg-result" id="tg-result" style="display:none"></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> Settings</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> Online · OMIDIRAN</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Default port</div><div class="srv-tile-val">443 (TLS) · configurable per configuration</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Version</div><div class="srv-tile-val">v2.0.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-bolt"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Framework</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">Storage</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1">
          <div class="srv-tile-icon"><i class="ti ti-world-pin"></i></div>
          <div class="srv-tile-text">
            <div class="srv-tile-label">IP · Server Location</div>
            <div class="srv-tile-val" id="srv-info-full">—</div>
          </div>
        </div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-user-cog"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">Admin Account</div>
          <div class="pw-hero-sub">Manage panel username and password here</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>NEW USERNAME</label>
          <input class="pw-input" type="text" id="cp-user" placeholder="New Username" autocomplete="username">
        </div>
        <div class="pw-field">
          <label>CURRENT PASSWORD</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="Enter to save changes" autocomplete="current-password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>NEW PASSWORD</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="Empty = no change · minimum 4 characters" autocomplete="new-password" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> Password strength</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> Minimum 4 characters · 4+ chars</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> Contains a number · Number</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> Mixed case</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>CONFIRM PASSWORD</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="Only when changing the password">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="cl" style="margin:0 0 12px 0"><i class="ti ti-info-circle"></i><span>Current password is required to change username or password. Existing sessions will be closed when saved.</span></div>
        <button class="pw-submit" onclick="changeCredentials()"><i class="ti ti-device-floppy"></i> Save account information</button>
      </div>
    </div>
  </div>
</section>
<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> Support</div></div></div>
  <div class="srv-panel">
    <div class="srv-hero">
      <div class="srv-hero-icon"><i class="ti ti-headset"></i></div>
      <div class="srv-hero-text">
        <div class="srv-hero-domain">Support</div>
        <div class="srv-hero-sub"><span class="dot dg pulse"></span> Contact Channels</div>
      </div>
    </div>
    <div class="srv-tiles">
      <a class="srv-tile" href="https://t.me/omid_gamingORG" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-speakerphone"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">Telegram Channel</div><div class="srv-tile-val">@omid_gamingORG</div></div>
      </a>
      <a class="srv-tile" href="https://github.com/omidiran-gaming/omidiran" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-brand-github"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">GitHub</div><div class="srv-tile-val">github.com/omidiran-gaming/omidiran</div></div>
      </a>
    </div>
  </div>
</section>
</main>
<script>
/* ═══════════════════════════════════════════════════════════════════════
   OMID UI CORE · ENGLISH CANONICAL / PERSIAN RUNTIME TRANSLATION
   ═══════════════════════════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════════════════════════
   OMID LANGUAGE CENTER · ENGLISH IS THE CANONICAL UI LANGUAGE
   The HTML/JS UI is authored in English. Persian is a runtime translation.
   IMPORTANT: Never translate already-translated DOM text. Each text node and
   UI attribute is anchored to its original English source string.
   ═══════════════════════════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════════════════════════
   OMID LANGUAGE CENTER · ENGLISH IS THE CANONICAL UI LANGUAGE
   The HTML/JS UI is authored in English. Persian is a runtime translation.
   IMPORTANT: Never translate already-translated DOM text. Each text node and
   UI attribute is anchored to its original English source string.
   ═══════════════════════════════════════════════════════════════════════ */
const OMID_EN_TO_FA = {"optional":"اختیاری","e.g.":"مثلاً","Test Connection":"تست اتصال","Save & Start":"ذخیره و روشن کردن","Stop Bot":"توقف ربات","comma separated: 123,456":"با کاما جدا کن: 123,456","To get your Admin ID, start":"برای دریافت Admin ID، توی ربات","on Telegram. If left empty, nobody can use the bot.":"رو استارت کن. اگه خالی بذاری، هیچ‌کس نمی‌تونه از ربات استفاده کنه.","(via @BotFather)":"(از @BotFather)","Checking...":"در حال بررسی...","Online & Running":"روشن و در حال کار","Stopped (token saved)":"متوقف (توکن ذخیره‌شده)","Enter the token":"توکن را وارد کنید","Testing...":"در حال تست...","Token is valid":"توکن معتبر است","Invalid token":"توکن نامعتبر است","Token is required":"توکن الزامی است","Enter at least one Admin ID":"حداقل یک Admin ID وارد کنید","Saving and starting bot...":"در حال ذخیره و روشن کردن ربات...","Bot started":"ربات روشن شد","Bot stopped":"ربات متوقف شد","Stopping...":"در حال توقف...","Stop the bot? (token will be saved)":"مطمئنی ربات رو متوقف کنم؟ (توکن ذخیره می‌مونه)","Failed to stop":"خطا در توقف","Delete":"حذف","UUID is generated randomly":"UUID به‌صورت تصادفی تولید می‌شود","Only registered UUIDs may connect":"فقط UUIDهای ثبت‌شده اجازه اتصال دارند","Random UUID · pick quota, expiry and protocol":"UUID تصادفی · سهمیه، انقضا و پروتکل را انتخاب کنید","Protocol cannot be changed after creation":"پروتکل پس از ساخت قابل تغییر نیست","Link copied":"لینک کپی شد","Sub link copied":"لینک ساب کپی شد","UUID copied":"UUID کپی شد","IP copied":"IP کپی شد","IP · Server Location":"IP · لوکیشن سرور","Activated ✓":"فعال شد ✓","Activated":"فعال شد","Deactivated":"غیرفعال شد","Error":"خطا","Usage reset ✓":"مصرف ریست شد ✓","Refreshed":"رفرش شد","Enter UUID":"UUID را وارد کنید","No changes to save":"تغییری برای ذخیره وجود ندارد","Group configurations saved ✓":"کانفیگ‌های گروه ذخیره شدند ✓","✓ Connected - Valid UUID":"✓ متصل - UUID معتبر","✗ Error - Invalid or inactive UUID":"✗ خطا - UUID نامعتبر یا غیرفعال","Copied":"کپی شد","Sign in to Control Center":"ورود به مرکز کنترل","SYSTEM ONLINE":"سیستم آنلاین","Test message...":"پیام تست...","Connected: ":"اتصال: ","Sent: ":"ارسال: ","Received ":"دریافت ","Closed (":"قطع (","Subscription":"سابسکریپشن","Session":"سشن","Disconnect":"قطع","Strong":"قوی","PANEL":"پنل","Help":"کمک","Copy":"کپی","Logout":"خروج","Refresh":"رفرش","Live":"زنده","Weak":"ضعیف","Active":"فعال","Usage":"مصرف","Version":"نسخه","Unit":"واحد","Sign In":"ورود","Group":"گروه","1 GB":"۱ GB","5 GB":"۵ GB","Connect":"اتصال","Send":"ارسال","of total":"از کل","Security":"امنیت","Night Mode":"تم شب","Distribution":"توزیع","Errors":"خطاها","SYSTEM":"سیستم","Title":"عنوان","Medium":"متوسط","Expired":"منقضی","All":"همه","10 GB":"۱۰ GB","50 GB":"۵۰ GB","7 days":"۷ روز","Online":"آنلاین","Uptime":"آپتایم","Cancel":"انصراف","Traffic":"ترافیک","Protected":"رمزدار","Password hash":"هش رمز","Edit":"ویرایش","Public":"پابلیک","Platform":"پلتفرم","Configurations":"کانفیگ‌ها","Copy IP":"کپی IP","0 groups":"۰ گروه","1 Mbps":"۱ Mbps","30 days":"۳۰ روز","5 Mbps":"۵ Mbps","500 MB":"۵۰۰ MB","90 days":"۹۰ روز","Connections":"اتصالات","Light Mode":"تم روشن","Settings":"تنظیمات","Dashboard":"داشبورد","Custom...":"دستی...","Inactive":"غیرفعال","Active v9":"فعال v9","Clear All":"لغو همه","Average":"میانگین","Unlimited":"نامحدود","Sign in to":"ورود به","Copy all":"کپی همه","GitHub":"گیت‌هاب","Note":"یادداشت","1 user":"۱ کاربر","10 Mbps":"۱۰ Mbps","2 users":"۲ کاربر","25 Mbps":"۲۵ Mbps","5 users":"۵ کاربر","Relative Load":"بار نسبی","Open":"باز کردن","Dark Mode":"تم تاریک","Deleted ✓":"حذف شد ✓","New Password":"رمز جدید","Password":"رمز عبور","Current Password":"رمز فعلی","Encryption":"رمزنگاری","Framework":"فریم‌ورک","Password strength":"قدرت رمز","Group Name":"نام گروه","Support":"پشتیبانی","Usage peak":"پیک مصرف","Copied ✓":"کپی شد ✓","Copy link":"کپی لینک","Very weak":"خیلی ضعیف","Reset usage":"ریست مصرف","Create Group":"ساخت گروه","Error Logs":"لاگ خطاها","Connection duration":"مدت اتصال","Protocols":"پروتکل‌ها","Support:":"پشتیبانی:","Total Traffic":"کل ترافیک","New Group":"گروه جدید","MB per hour":"MB در ساعت","Theme":"تم","Account Security":"امنیت حساب","selected":"انتخاب شده","Select All":"انتخاب همه","Storage":"ذخیره‌سازی","Subscriptions":"سابسکریپشن","Free For All":"رایگان برای همه","Username":"نام کاربری","Connection Port":"پورت اتصال","icon.":"کلیک کنید.","0 = Unlimited":"0 = نامحدود","Expiry date":"تاریخ انقضا","Creation failed":"خطا در ساخت","Create Configuration":"ساخت کانفیگ","Service Status":"وضعیت سرویس","Active Configs":"کانفیگ فعال","Lowest usage":"کمترین مصرف","Access Group":"گروه دسترسی","Close":"بستن","Save":"ذخیره","Active Connections":"اتصالات فعال","No description":"بدون توضیحات","Save failed":"خطا در ذخیره","Traffic Quota":"سهمیه ترافیک","Configuration ID":"شناسه کانفیگ","Enable/Disable":"فعال/غیرفعال","Connection List":"لیست اتصالات","Speed Limit":"محدودیت سرعت","Enter Group":"ورود به گروه","Default port":"پورت پیش‌فرض","Telegram Channel":"کانال تلگرام","Limited Config":"کانفیگ محدود","Access Control":"کنترل دسترسی","Copy subscription link":"کپی لینک ساب","Subscription Groups":"گروه‌های ساب","0 selected":"۰ انتخاب شده","● Active (443)":"● فعال (443)","Since startup":"از راه‌اندازی","Peak hour":"بالاترین ساعت","WebSocket Test":"تست WebSocket","Update failed":"خطا در ویرایش","Save Changes":"ذخیره تغییرات","CDN compatible":"سازگار با CDN","Active · 3 modes":"فعال · 3 mode","Activity Logs":"لاگ فعالیت‌ها","Link copied ✓":"لینک کپی شد ✓","IP Limit":"محدودیت آی‌پی","Hourly average":"میانگین ساعتی","All configurations":"همه کانفیگ‌ها","Edit Configuration":"ویرایش کانفیگ","Configuration Type":"نوع کانفیگ","Transport":"ترابرد","Lightweight & versatile":"سبک و همه‌منظوره","Compatible with clients":"سازگار با کلاینت‌ها","TLS · Password · lightweight":"TLS · رمزعبور · سبک","Stable & widely supported":"پایدار و شناخته‌شده","Highly CDN-compatible":"سازگاری بالا با CDN","Stream-based upload & download":"آپلود و دانلود جریان‌محور","Transport Protocol":"پروتکل انتقال","Configuration deleted":"کانفیگ حذف شد","Group deleted ✓":"گروه حذف شد ✓","— No group —":"— بدون گروه —","Unique IPs":"آی‌پی‌های یکتا","Lower latency":"تاخیر پایین‌تر","Confirm New Password":"تکرار رمز جدید","Signing in...":"در حال ورود...","Wrong password":"رمز اشتباه است","Waiting for connection...":"منتظر اتصال...","No errors":"هیچ خطایی نیست","Protocol default":"پیش‌فرض پروتکل","Language":"زبان","Delete this configuration?":"حذف این کانفیگ؟","Load failed":"خطا در بارگذاری","Configuration Summary":"خلاصه کانفیگ‌ها","Contact Channels":"راه‌های ارتباطی","Subscription link copied":"لینک ساب کپی شد","Custom ALPN":"مقدار دستی ALPN","New Username":"نام کاربری جدید","Hide link":"پنهان کردن لینک","Active configurations":"کانفیگ‌های فعال","Total traffic usage":"کل ترافیک مصرفی","Group created ✓":"گروه ساخته شد ✓","HttpOnly · 7 days":"HttpOnly · 7 روز","Last update:":"آخرین بروزرسانی:","Online · OMIDIRAN":"آنلاین · OMIDIRAN","Search configurations...":"جستجوی کانفیگ...","Group creation failed":"خطا در ساخت گروه","Loading...":"در حال بارگذاری...","Save Account Security":"ذخیره امنیت حساب","Traffic usage trend":"روند مصرف ترافیک","e.g. User Ali":"مثلاً: کاربر علی","Subscription group & expiry":"گروه ساب و انقضا","Hourly Traffic (MB)":"ترافیک ساعتی (MB)","Description (optional)":"توضیحات (اختیاری)","Contains a number · Number":"شامل عدد · Number","Active · strict":"فعال · سخت‌گیرانه","Manage Configurations":"مدیریت کانفیگ‌ها","Average connection duration":"میانگین مدت اتصال","Show configuration link":"نمایش لینک کانفیگ","No groups yet":"هنوز گروهی ندارید","Configuration created ✓":"کانفیگ ساخته شد ✓","Note (optional)":"یادداشت (اختیاری)","FA / EN · Bilingual":"FA / EN · دو زبانه","Public link copied":"لینک پابلیک کپی شد","No activity logs yet":"هنوز لاگی ثبت نشده","Configuration updated ✓":"کانفیگ ویرایش شد ✓","No configuration exists":"کانفیگی وجود ندارد","UUID of an active configuration":"UUID یک کانفیگ فعال","Search groups...":"جستجو در گروه‌ها...","Public subscription page password":"رمز صفحه پابلیک ساب","Current password is required":"رمز فعلی الزامی است","Quota (0 = Unlimited)":"سهمیه (0 = نامحدود)","Configuration enabled/disabled":"فعال/غیرفعال کانفیگ","Stable & general purpose":"پایدار و همه‌منظوره","● Optional · SHA-256":"● اختیاری · SHA-256","Strict UUID Auth":"UUID Auth سخت‌گیرانه","Realtime traffic total":"مجموع ترافیک لحظه‌ای","No active connections":"هیچ اتصال فعالی نیست","ALPN (blank = default)":"ALPN (خالی = پیش‌فرض)","Total Usage":"کل مصرف","Enter password":"رمز عبور را وارد کنید","Only when changing the password":"فقط در صورت تغییر رمز","No configuration to copy":"کانفیگی برای کپی نیست","Leave empty = no password":"خالی بگذارید = بدون رمز","NEW PASSWORD":"رمز جدید","Full subscription (admin)":"سابسکریپشن کامل (ادمین)","Group subscription links":"لینک سابسکریپشن گروه‌ها","Enter username":"نام کاربری را وارد کنید","No configurations yet":"هنوز کانفیگی وجود ندارد","Expiry (days) · 0 = unlimited":"انقضا (روز) · 0 = نامحدود","New passwords do not match":"تکرار رمز جدید یکسان نیست","Admin Account":"حساب مدیر","Public Page Password (optional)":"رمز صفحه پابلیک (اختیاری)","Your connection is encrypted":"اتصال شما رمزنگاری‌شده است","Based on megabytes per hour":"بر اساس مگابایت در هر ساعت","Minimum 4 characters · 4+ chars":"حداقل ۴ کاراکتر · 4+ chars","Single subscription (per configuration)":"سابسکریپشن تکی (هر کانفیگ)","Create New Group":"ساخت گروه جدید","Includes all active configurations.":"شامل تمام کانفیگ‌های فعال.","Speed Limit (0 = Unlimited)":"محدودیت سرعت (0 = نامحدود)","Auto-refresh every 5 seconds":"بروزرسانی خودکار هر ۵ ثانیه","Complete panel event history":"تاریخچه کامل رخدادهای پنل","Mixed case":"حروف بزرگ/کوچک","CURRENT PASSWORD":"رمز فعلی","Default Link (Unlimited)":"لینک پیش‌فرض (بدون محدودیت)","IP Limit (0 = Unlimited)":"محدودیت آی‌پی (0 = نامحدود)","Enter to save changes":"برای ذخیره تغییرات وارد کنید","Changes apply immediately":"تغییرات بلافاصله اعمال می‌شود","New password must be at least 4 characters":"رمز جدید باید حداقل ۴ کاراکتر باشد","Concurrent IP / user limit":"محدودیت آی‌پی / کاربر هم‌زمان","NEW USERNAME":"نام کاربری جدید","Live Connections":"اتصالات زنده","Manage panel login credentials":"اطلاعات ورود پنل را مدیریت کنید","Account updated successfully ✓":"اطلاعات حساب با موفقیت ذخیره شد ✓","CONFIRM PASSWORD":"تکرار رمز جدید","Save account information":"ذخیره اطلاعات حساب","Subscription links for v2ray apps":"لینک‌های اشتراک برای اپ‌های v2ray","Username cannot contain spaces":"نام کاربری نباید فاصله داشته باشد","Bandwidth usage analysis & monitoring":"تحلیل و مانیتورینگ مصرف پهنای باند","443 (TLS) · configurable per configuration":"443 (TLS) · قابل تغییر در هر کانفیگ","Empty = no change · minimum 4 characters":"خالی = بدون تغییر · حداقل ۴ کاراکتر","Delete this group? Configurations will not be deleted.":"حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.","UUID (must exist in configurations)":"UUID (باید در کانفیگ‌ها وجود داشته باشد)","Username must be 3–32 characters":"نام کاربری باید بین ۳ تا ۳۲ کاراکتر باشد","Live IP and traffic monitoring for each connection":"مانیتورینگ زنده آی‌پی و ترافیک هر اتصال","Expiry (days from now, 0 = unchanged/unlimited)":"انقضا (روز از الان، 0 = بدون تغییر/نامحدود)","Copy all active links in this group":"تمام لینک‌های فعال این گروه را یک‌جا کپی کن","Copy all configurations":"کپی همه کانفیگ‌ها","Enter your credentials to access the control panel":"برای ورود به پنل مشخصات دسترسی خود را وارد کنید","Leave expiry at zero to keep the current expiry.":"برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.","Connections appear here as clients connect":"به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند","Create and manage configs with quota, expiry and groups":"ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی","Create a dedicated public page for managing configurations":"یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید","Manage panel username and password here":"نام کاربری و رمز عبور پنل را از همین‌جا مدیریت کنید","Each group has a separate public page with its own configurations":"هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد","Select the configurations for this group":"کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید","Each configuration has its own subscription URL. From the configuration card, click the":"هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون","Create a new group to organize configurations":"یک New Group / گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید","This group is password protected. Enter the password to view its configurations.":"این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز را وارد کنید.","This URL only works in the browser signed in to the panel (session cookie required).":"این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).","This group public page will be available through a unique internet link.":"صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.","Current password is required to change username or password. Existing sessions will be closed when saved.":"برای تغییر نام کاربری یا رمز، رمز فعلی الزامی است. با ذخیره تغییرات، نشست‌های قبلی بسته می‌شوند.","Only registered active UUIDs may connect (this is a VLESS/WS test; XHTTP is tested from the client).":"فقط UUIDهای ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).","Telegram Bot":"ربات تلگرام","Manage Telegram bot for remote panel control":"مدیریت ربات تلگرام برای کنترل پنل از راه دور","Status:":"وضعیت:","Random":"تصادفی","Short description for this group":"توضیح کوتاه درباره این گروه","Server IP":"IP سرور","Clear":"پاک کردن","New Configuration":"کانفیگ جدید","Connected IPs / limit":"آی‌پی‌های متصل / محدودیت","Default Link":"لینک پیش‌فرض","MB":"مگابایت","Bot:":"ربات:","Protocol":"پروتکل"};
Object.assign(OMID_EN_TO_FA, {
  'Access denied':'دسترسی رد شد',
  'Connections':'اتصالات',
  'Connection':'اتصال',
  'seconds':'ثانیه',
  'minutes':'دقیقه',
  'hours':'ساعت',
  'errors':'خطا',
  'Error':'خطا',
  'OMID-IRAN PANEL · Login':'OMID-IRAN PANEL · ورود'
});

const OMID_EN_RULES = Object.entries(OMID_EN_TO_FA)
  .sort((a,b)=>b[0].length-a[0].length);
const OMID_TEXT_SOURCE = new WeakMap();
const OMID_ATTR_SOURCE = new WeakMap();

function omidFaDigits(value){
  return String(value).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);
}
function omidPreserveOuterSpace(raw, core){
  const s=String(raw??'');
  const lead=(s.match(/^\s*/)||[''])[0];
  const trail=(s.match(/\s*$/)||[''])[0];
  return lead+core+trail;
}
function omidTranslateDynamic(core){
  let m;
  if((m=core.match(/^(\d+)\s+selected$/i))) return `${omidFaDigits(m[1])} انتخاب شده`;
  if((m=core.match(/^(\d+)\s+configurations$/i))) return `${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^of\s+(\d+)\s+configurations$/i))) return `از کل ${omidFaDigits(m[1])} کانفیگ`;
  if((m=core.match(/^(\d+)\s+groups$/i))) return `${omidFaDigits(m[1])} گروه`;
  if((m=core.match(/^(\d+)\s+connections$/i))) return `${omidFaDigits(m[1])} اتصال`;
  if((m=core.match(/^(\d+)\s+errors$/i))) return `${omidFaDigits(m[1])} خطا`;
  if((m=core.match(/^(\d+)\s+seconds$/i))) return `${omidFaDigits(m[1])} ثانیه`;
  if((m=core.match(/^(\d+)\s+minutes$/i))) return `${omidFaDigits(m[1])} دقیقه`;
  if((m=core.match(/^(\d+)\s+hours$/i))) return `${omidFaDigits(m[1])} ساعت`;
  if((m=core.match(/^(\d+)\s+days remaining$/i))) return `${omidFaDigits(m[1])} روز مانده`;
  if((m=core.match(/^Last update:\s*(.*)$/i))) return `آخرین بروزرسانی: ${m[1]}`;
  if((m=core.match(/^Connected:\s*(.*)$/i))) return `اتصال: ${m[1]}`;
  if((m=core.match(/^Sent:\s*(.*)$/i))) return `ارسال: ${m[1]}`;
  if((m=core.match(/^Received\s+(.*)$/i))) return `دریافت ${m[1]}`;
  if((m=core.match(/^Closed \((.*)$/i))) return `قطع (${m[1]}`;
  if((m=core.match(/^\[(.+)\] (.+)$/s))) return `[${m[1]}] ${m[2]}`;
  return null;
}
function omidTranslateText(raw, lang){
  const s=String(raw??'');
  if(lang==='en' || !s.trim()) return s;
  const core=s.trim();
  if(Object.prototype.hasOwnProperty.call(OMID_EN_TO_FA,core)){
    return omidPreserveOuterSpace(s,OMID_EN_TO_FA[core]);
  }
  const dynamic=omidTranslateDynamic(core);
  if(dynamic!==null) return omidPreserveOuterSpace(s,dynamic);

  // Safe phrase translation: only known English phrases are replaced, and
  // only against the immutable English source string stored for the node.
  let out=core;
  for(const [en,fa] of OMID_EN_RULES){
    if(out.includes(en)) out=out.split(en).join(fa);
  }
  return omidPreserveOuterSpace(s,out);
}
function omidRememberText(node){
  if(!OMID_TEXT_SOURCE.has(node)) OMID_TEXT_SOURCE.set(node,node.nodeValue);
  return OMID_TEXT_SOURCE.get(node);
}
function omidRememberAttr(el,attr){
  let rec=OMID_ATTR_SOURCE.get(el);
  if(!rec){rec={};OMID_ATTR_SOURCE.set(el,rec);}
  if(rec[attr]===undefined) rec[attr]=el.getAttribute(attr) || '';
  return rec[attr];
}
function omidApplyLanguage(root,lang){
  const target=root||document.body;
  if(!target) return;
  const walker=document.createTreeWalker(target,NodeFilter.SHOW_TEXT);
  const nodes=[];
  while(walker.nextNode()){
    const n=walker.currentNode;
    const p=n.parentElement;
    if(!p || !n.nodeValue || !n.nodeValue.trim()) continue;
    if(['SCRIPT','STYLE','NOSCRIPT','CODE','PRE'].includes(p.tagName)) continue;
    if(p.closest('[data-i18n-ignore="true"]')) continue;
    nodes.push(n);
  }
  for(const n of nodes){
    const source=omidRememberText(n);
    n.nodeValue=omidTranslateText(source,lang);
  }
  const attrs=['placeholder','title','aria-label'];
  target.querySelectorAll('input,button,select,textarea,[title],[aria-label]').forEach(el=>{
    for(const attr of attrs){
      if(!el.hasAttribute(attr)) continue;
      el.setAttribute(attr,omidTranslateText(omidRememberAttr(el,attr),lang));
    }
  });
  document.documentElement.lang=lang;
  document.documentElement.dir=lang==='en'?'ltr':'rtl';
}

let isDark = localStorage.getItem('omid-theme') !== 'light';
function applyTheme(dark){
  isDark=!!dark;
  document.documentElement.setAttribute('data-theme',isDark?'dark':'light');
  document.body.classList.toggle('theme-dark',isDark);
  document.body.classList.toggle('theme-light',!isDark);
  const icon=document.getElementById('theme-icon');
  const mobIcon=document.getElementById('theme-mob-icon');
  const label=document.getElementById('theme-label');
  if(icon) icon.className='ti '+(isDark?'ti-sun':'ti-moon');
  if(mobIcon) mobIcon.className='ti '+(isDark?'ti-sun':'ti-moon');
  if(label) label.textContent=isDark?'Light Mode':'Dark Mode';
  localStorage.setItem('omid-theme',isDark?'dark':'light');
}
function toggleTheme(){
  applyTheme(!isDark);
  setTimeout(function(){
    try{if(typeof ch1!=='undefined'&&ch1)ch1.resize();if(typeof ch2!=='undefined'&&ch2)ch2.resize();if(typeof ch3!=='undefined'&&ch3)ch3.resize();}catch(e){}
  },100);
}
let uiLang=localStorage.getItem('omid-lang')||'en';
let __langApplying=false;
let langObserver=null;
function applyUiLang(){
  if(__langApplying)return;
  __langApplying=true;
  try{
    const b=document.body;
    b.dataset.uiLang=uiLang;
    b.classList.toggle('ui-en',uiLang==='en');
    b.classList.toggle('ui-fa',uiLang==='fa');
    b.setAttribute('dir',uiLang==='en'?'ltr':'rtl');
    const btn=document.getElementById('lang-btn');
    const side=document.getElementById('side-lang-label');
    const mb=document.getElementById('lang-mob-btn');
    if(btn)btn.textContent=uiLang==='en'?'FA':'EN';
    if(side)side.textContent='FA / EN · Bilingual';
    if(mb)mb.textContent=uiLang==='en'?'FA':'EN';
    const tl=document.getElementById('theme-label');
    if(tl)tl.textContent=isDark?'Light Mode':'Dark Mode';
    const ipBadge=document.getElementById('server-ip-badge');
    const ipFlag=document.getElementById('server-ip-flag');
    if(ipBadge)ipBadge.title='Server IP';
    if(ipFlag)ipFlag.title='Server IP';
    omidApplyLanguage(document.body,uiLang);
    applyTheme(isDark);
  }finally{__langApplying=false;}
  setTimeout(function(){
    try{if(typeof ch1!=='undefined'&&ch1)ch1.resize();if(typeof ch2!=='undefined'&&ch2)ch2.resize();if(typeof ch3!=='undefined'&&ch3)ch3.resize();}catch(e){}
    try{if(typeof loadServerInfo==='function')loadServerInfo();}catch(e){}
  },100);
}
function toggleUiLang(){
  uiLang=uiLang==='en'?'fa':'en';
  localStorage.setItem('omid-lang',uiLang);
  applyUiLang();
}
applyTheme(isDark);
applyUiLang();
langObserver=new MutationObserver(()=>{
  if(__langApplying)return;
  clearTimeout(window.__langTimer);
  window.__langTimer=setTimeout(()=>omidApplyLanguage(document.body,uiLang),0);
});
langObserver.observe(document.body,{subtree:true,childList:true,characterData:false});
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> Unlimited</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> Expired</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${d} days remaining</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${d} days remaining</span>`;
}
function protoBadge(p){
  const m={
    'vless-ws':['VLESS · WS','pc-ws'],
    'vless-xhttp-packet-up':['VLESS · XHTTP · packet-up','pc-xhttp'],
    'vless-xhttp-stream-up':['VLESS · XHTTP · stream-up','pc-xhttp'],
    'vmess-ws':['VMess · WS','pc-ws'],
    'vmess-xhttp-packet-up':['VMess · XHTTP · packet-up','pc-xhttp'],
    'vmess-xhttp-stream-up':['VMess · XHTTP · stream-up','pc-xhttp'],
    'trojan-ws':['Trojan · WS','pc-trojan'],
    'trojan-xhttp-packet-up':['Trojan · XHTTP · packet-up','pc-xhttp'],
    'trojan-xhttp-stream-up':['Trojan · XHTTP · stream-up','pc-xhttp']
  };
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
let __baseProtocol='vless';
let __transportMode='ws';
function syncProtocolSelection(){
  const combined = `${__baseProtocol}-${__transportMode}`;
  document.getElementById('nl-proto').value = combined;
  document.querySelectorAll('.proto-family-cards .proto-card').forEach(c=>c.classList.toggle('active', c.dataset.family===__baseProtocol));
  document.querySelectorAll('.proto-transport-cards .proto-card').forEach(c=>c.classList.toggle('active', c.dataset.transport===__transportMode));
}
function selectBaseProtocol(val){__baseProtocol=val;syncProtocolSelection();}
function selectTransport(val){__transportMode=val;syncProtocolSelection();}
function selectProto(val,el){
  const p=String(val||'vless-ws');
  __baseProtocol=p.startsWith('vmess-')?'vmess':p.startsWith('trojan-')?'trojan':'vless';
  __transportMode=(p.endsWith('-ws')?'ws':p.includes('packet-up')?'xhttp-packet-up':'xhttp-stream-up');
  syncProtocolSelection();
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={
  links:loadLinks,
  connections:loadConns,
  errors:loadErrs,
  subscriptions:loadSubsPage,
  subgroups:loadSubs,
  logs:loadActivity,
  settings:loadAccount,
  telegram:tgLoad
};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='of '+d.links_count+' configurations';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' errors';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='OMIDIRAN · '+d.uptime;
    document.getElementById('last-upd').textContent='Last update: '+new Date().toLocaleTimeString('en-US');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' Connect';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> No errors</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'Configurations',sub:'Group',auth:'Sign In',connection:'Connect',system:'SYSTEM'};
    const kindEn={link:'CONFIG',sub:'GROUP',auth:'AUTH',connection:'CONNECTION',system:'SYSTEM'};
    el.innerHTML=logs.map(l=>{
      /* ← اینجا لاگ رو ترجمه می‌کنیم */
      const msg = uiLang==='en'
        ? translateLogMessage(l.message, 'en')
        : l.message;
      const kindLabel = uiLang==='en'
        ? (kindEn[l.kind] || l.kind)
        : (kindFa[l.kind] || l.kind);
      const dt = new Date(l.time).toLocaleString(uiLang==='en' ? 'en-US' : 'fa-IR');
      return `
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(msg)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${dt} <span class="log-kind">${kindLabel}</span></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    // ✅ فقط وقتی dropdown رو rebuild کن که محتواش عوض شده باشه
    // وگرنه انتخاب فعلی کاربر هر ۵ seconds پریده می‌شه
    const oldVal = nlSub.value;
    const newOptionsHtml = '<option value="">— No group —</option>' +
      subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    if(nlSub.dataset.optionsHtml !== newOptionsHtml){
      nlSub.dataset.optionsHtml = newOptionsHtml;
      nlSub.innerHTML = newOptionsHtml;
      // اگه انتخاب قبلی هنوز معتبر بود، حفظش کن
      if(oldVal && Array.from(nlSub.options).some(o=>o.value===oldVal)){
        nlSub.value = oldVal;
      }
    }
    document.getElementById('links-pg-cnt').textContent=links.length+' configurations';
    document.getElementById('lsummary-badge').textContent=links.length;
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>No configuration exists</p></div>';return}
    empty.style.display='none';
    grid.innerHTML=links.map(l=>{
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return `<div class="cfg-card ${cardCls}">
    <div class="cfg-row">
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}</div>
        <div class="cfg-sub-meta">
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID copied','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          ${l.sub_token?`<span class="cfg-uuid-mini" style="background:var(--green-bg);color:var(--green-t)" onclick="navigator.clipboard.writeText('${esc(l.sub_token)}').then(()=>toast('Sub Token Copied','ok'))" title="Sub Token: ${esc(l.sub_token)}"><i class="ti ti-tag"></i> ${esc(l.sub_token)}</span>`:''}
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>of ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="Connection Port"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="Connected IPs / limit"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="Speed Limit"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'Unlimited'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="Enable/Disable"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('Link copied','ok'))" title="Copy link"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="window.open('${esc(l.sub_url)}','_blank','noopener')" title="Open Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="Edit"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="Reset usage"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="Delete"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'New Configuration';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  const sub_token=document.getElementById('nl-token').value.trim();
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit,sub_token})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn','nl-token'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    __baseProtocol='vless';__transportMode='ws';syncProtocolSelection();
    toast('Configuration created ✓','ok');loadLinks();
  }catch(e){toast('Creation failed','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  document.getElementById('el-token').value=l.sub_token||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const sub_token=document.getElementById('el-token').value.trim();
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit,sub_token};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('Configuration updated ✓','ok');loadLinks();
  }catch(e){toast('Update failed','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'Activated ✓':'Deactivated','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('Usage reset ✓','ok');loadLinks();}catch(e){toast('Error','err')}
}
async function deleteLink(uuid){
  if(!confirm('Delete this configuration?'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('Deleted ✓','ok');loadLinks();}catch(e){toast('Error','err')}
}
/* ══ OMID Styled QR Builder ══ */
function buildStyledQR(url, containerId, size){
  size = size || 280;
  const container = document.getElementById(containerId);
  if(!container) return null;
  container.innerHTML = "";
  const qr = new QRCodeStyling({
    width: size,
    height: size,
    type: "canvas",
    data: url,
    margin: 6,
    qrOptions: { errorCorrectionLevel: "M" },
    dotsOptions: {
      type: "extra-rounded",
      gradient: {
        type: "linear",
        rotation: Math.PI / 4,
        colorStops: [
          { offset: 0, color: "#4a90ff" },
          { offset: 1, color: "#b026ff" }
        ]
      }
    },
    backgroundOptions: { color: "#ffffff" },
    cornersSquareOptions: {
      type: "extra-rounded",
      gradient: {
        type: "linear",
        rotation: Math.PI / 4,
        colorStops: [
          { offset: 0, color: "#4a90ff" },
          { offset: 1, color: "#b026ff" }
        ]
      }
    },
    cornersDotOptions: {
      type: "dot",
      gradient: {
        type: "linear",
        rotation: Math.PI / 4,
        colorStops: [
          { offset: 0, color: "#4a90ff" },
          { offset: 1, color: "#b026ff" }
        ]
      }
    }
  });
  qr.append(container);
  return qr;
}

function showQR(link, title){
  // ساخت مودال QR مدرن (یک‌بار ساخته می‌شه)
  let modal = document.getElementById("qr-modal-panel");
  if(!modal){
    modal = document.createElement("div");
    modal.id = "qr-modal-panel";
    modal.style.cssText = "position:fixed;inset:0;z-index:999;background:rgba(0,0,0,.82);backdrop-filter:blur(10px);display:none;align-items:center;justify-content:center;padding:20px";
    modal.onclick = function(){ modal.classList.remove("show"); };
    modal.innerHTML = `
      <div onclick="event.stopPropagation()" style="background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px;text-align:center;max-width:380px;width:100%;box-shadow:0 24px 70px rgba(0,0,0,.6)">
        <div style="font-size:14px;font-weight:800;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;justify-content:center;gap:8px">
          <i class="ti ti-qrcode" style="color:var(--accent2)"></i>
          <span id="qr-modal-panel-title">QR</span>
        </div>
        <div style="background:#fff;border-radius:14px;padding:14px;display:inline-block;margin-bottom:16px;box-shadow:0 8px 24px rgba(0,0,0,.25)">
          <div id="qr-modal-panel-canvas" style="width:280px;height:280px"></div>
        </div>
        <button onclick="document.getElementById('qr-modal-panel').classList.remove('show')" style="width:100%;padding:11px;border-radius:12px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t1);font-weight:700;font-family:inherit;cursor:pointer;font-size:12.5px">
          Close
        </button>
      </div>
    `;
    document.body.appendChild(modal);
    const style = document.createElement("style");
    style.textContent = "#qr-modal-panel.show{display:flex!important}";
    document.head.appendChild(style);
  }
  document.getElementById("qr-modal-panel-title").textContent = title || "QR Code";
  buildStyledQR(link, "qr-modal-panel-canvas", 280);
  modal.classList.add("show");
}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-pg-cnt').textContent=subs.length+' groups';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">No groups yet</div><div class="subs-empty-v2-sub">Create a new group to organize configurations</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">No description</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'Protected':'Public'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${s.links_count}</div><div class="sub-card-stat-label">Configurations</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${s.active_count}</div><div class="sub-card-stat-label">Active</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">Usage</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Public link copied','ok'))" title="Copy"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="Open"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> Configurations</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('Subscription link copied','ok'))"><i class="ti ti-rss"></i> Subscription</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="Delete"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'New Group';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('Group created ✓','ok');loadSubs();
  }catch(e){toast('Group creation failed','err')}
}
async function deleteSub(sub_id){
  if(!confirm('Delete this group? Configurations will not be deleted.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('Group deleted ✓','ok');loadSubs();loadLinks();}catch(e){toast('Error','err')}
}
let currentSubId = null;
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('Load failed','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>No configurations yet</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info">
        <div class="lrow-v2-name">${esc(l.label)}</div>
        <div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
      </div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'Active':'Inactive'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=lmodalInSub.size+' selected';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('Group configurations saved ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('Save failed','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>No groups yet</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#A78BFA">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${s.links_count} Configurations · ${esc(s.total_used_fmt)} Usage ${s.has_password?'· 🔒 Protected':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-copy"></i> Subscription</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('Copied','ok'))"><i class="ti ti-globe"></i> Public</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('Copied ✓','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' connections';
    document.getElementById('ch-count').textContent=d.count;
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=uniqIps;
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' seconds':avgSec<3600?Math.floor(avgSec/60)+' minutes':Math.floor(avgSec/3600)+' hours';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' seconds':secs<3600?Math.floor(secs/60)+' minutes':Math.floor(secs/3600)+' hours';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP copied','ok'))" title="Copy IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> Live</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">Traffic</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">Connection duration</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'No configurations yet';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('Copied ✓','ok'))}
function qrFor(id){
  const el = document.getElementById(id);
  if(el) showQR(el.textContent, "Default Link");
}
function refreshAll(){fetchStats();fetchDefaultVless();loadServerInfo();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('Refreshed','ok')}
async function loadAccount(){
  try{
    const r=await authF('/api/account');
    if(!r.ok)return;
    const d=await r.json();
    const el=document.getElementById('cp-user');
    if(el)el.value=d.username||'';
  }catch(e){}
}
async function changeCredentials(){
  const user=document.getElementById('cp-user').value.trim();
  const cur=document.getElementById('cp-cur').value;
  const nw=document.getElementById('cp-new').value;
  const cf=document.getElementById('cp-cf').value;
  if(!user){toast('Enter username','err');return}
  if(user.length<3||user.length>32){toast('Username must be 3–32 characters','err');return}
  if(/\s/.test(user)){toast('Username cannot contain spaces','err');return}
  if(!cur){toast('Current password is required','err');return}
  if(nw&&nw.length<4){toast('New password must be at least 4 characters','err');return}
  if(nw!==cf){toast('New passwords do not match','err');return}
  if(!nw && !user){toast('No changes to save','err');return}
  try{
    const r=await authF('/api/change-credentials',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_username:user,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'Error');
    toast('Account updated successfully ✓','ok');
    document.getElementById('cp-user').value=d.username||user;
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
    checkPwStrength('');
  }catch(e){toast('✗ '+e.message,'err')}
}
async function changePw(){ return changeCredentials(); }
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['Very weak','Weak','Medium','Strong'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> Password strength';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,'rgba(59,130,246,.38)','rgba(59,130,246,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,
        titleColor:'#E8F4FF',bodyColor:'#7BAED4',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} MB`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},maxRotation:0}},
      y:{beginAtZero:true,suggestedMax:1,grace:'20%',grid:{color:'rgba(59,130,246,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},maxTicksLimit:6,callback:v=>{if(v>=1024)return (v/1024).toFixed(1)+' GB';if(v>=1)return v+' MB';return (v*1024).toFixed(0)+' KB'}}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#60A5FA',backgroundColor:grad1,fill:true,tension:.42,pointRadius:3,pointBackgroundColor:'#60A5FA',pointBorderColor:'#fff',pointBorderWidth:1.5,pointHoverRadius:6,pointHoverBackgroundColor:'#3B82F6',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:3};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(59,130,246,.45)','rgba(59,130,246,.08)','rgba(59,130,246,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'Usage',data:[],borderColor:'#60A5FA',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#3B82F6',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'Average',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,27,46,.97)',borderColor:'rgba(59,130,246,.35)',borderWidth:1,
          titleColor:'#E8F4FF',bodyColor:'#9DC3E8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{beginAtZero:true,suggestedMax:1,grace:'20%',grid:{color:'rgba(59,130,246,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxTicksLimit:6,callback:v=>{if(v>=1024)return (v/1024).toFixed(1)+' GB';if(v>=1)return v+' MB';return (v*1024).toFixed(0)+' KB'}}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS','XHTTP','HTTP'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#3B82F6','#10B981','#8B5CF6'],
      borderColor:'transparent',
      borderWidth:0,hoverOffset:8,borderRadius:4,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'68%',
      layout:{padding:{bottom:4}},
      plugins:{
        legend:{position:'bottom',labels:{color:getComputedStyle(document.documentElement).getPropertyValue('--t2').trim()||'#8DB8C7',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });

  /* ✅═══════════════ CHART RESIZE ENGINE v2 ═══════════════✅
     مشکل: Chart.js داخل CSS Grid عرض اشتباه می‌گرفت
     راه‌حل: ResizeObserver روی والد canvas (نه window)
     ═══════════════════════════════════════════════════════════ */
  (function bindChartResize(){
    function safeResize(){
      try{
        [ch1, ch2, ch3].forEach(function(c){ if(c && typeof c.resize === 'function') c.resize(); });
      }catch(e){}
    }

    /* ۱. اندازه‌گیری اولیه — بعد از اینکه layout نهایی شد */
    requestAnimationFrame(function(){
      setTimeout(safeResize, 100);
      setTimeout(safeResize, 350);   /* ← دوباره، برای اطمینان از فونت‌ها */
      setTimeout(safeResize, 800);   /* ← دوباره، برای اطمینان از CDN */
    });

    /* ۲. ResizeObserver روی والد هر canvas — این هسته‌ی راه‌حل */
    if(window.ResizeObserver){
      const containers = [
        document.getElementById('ch1')?.parentElement,
        document.getElementById('ch2')?.parentElement,
        document.getElementById('ch3')?.parentElement
      ].filter(Boolean);

      const ro = new ResizeObserver(function(){
        /* debounce برای جلوگیری از رندر مکرر */
        clearTimeout(window.__omidChartROTimer);
        window.__omidChartROTimer = setTimeout(safeResize, 80);
      });

      containers.forEach(function(el){ ro.observe(el); });
      window.__omidChartRO = ro;   /* نگه‌داشتن برای دیباگ */
    }

    /* ۳. fallback: window resize (برای مرورگرهای قدیمی) */
    if(!window.__omidChartWinResize){
      window.__omidChartWinResize = true;
      let __rt;
      window.addEventListener('resize', function(){
        clearTimeout(__rt);
        __rt = setTimeout(safeResize, 120);
      });
    }

    /* ۴. آپدیت نهایی وقتی تب دوباره Activated */
    if(!window.__omidChartVisBound){
      window.__omidChartVisBound = true;
      document.addEventListener('visibilitychange', function(){
        if(!document.hidden) setTimeout(safeResize, 200);
      });
    }
  })();
}
/* ══════ Telegram Bot Panel ══════ */
function tgToggleToken(){
  const inp=document.getElementById('tg-token');
  const icon=document.getElementById('tg-token-eye');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}

function tgShowResult(msg,type){
  const el=document.getElementById('tg-result');
  const icons={ok:'ti-circle-check',err:'ti-alert-circle',wait:'ti-loader-2'};
  el.className='tg-result '+type;
  el.innerHTML=`<i class="ti ${icons[type]||'ti-info-circle'}" ${type==='wait'?'style="animation:spin 1s linear infinite"':''}></i> ${msg}`;
  el.style.display='flex';
}

async function tgLoad(){
  try{
    const r=await authF('/api/telegram');
    const d=await r.json();
    document.getElementById('tg-token').value=d.bot_token||'';
    document.getElementById('tg-admins').value=d.admin_ids||'';
    const led=document.getElementById('tg-hero-led');
    const badge=document.getElementById('tg-status-badge');
    if(d.running){
      led.className='tg-hero-status on';
      badge.innerHTML='<span style="color:var(--green-t)">● Online & Running</span>';
    }else if(d.enabled){
      led.className='tg-hero-status off';
      badge.innerHTML='<span style="color:var(--amber-t)">● Stopped (token saved)</span>';
    }else{
      led.className='tg-hero-status off';
      badge.innerHTML='<span style="color:var(--t3)">● Inactive</span>';
    }
  }catch(e){console.error(e)}
}

async function tgTest(){
  const token=document.getElementById('tg-token').value.trim();
  if(!token){tgShowResult('Enter the token','err');return}
  tgShowResult('Testing...','wait');
  try{
    const r=await authF('/api/telegram/test',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({bot_token:token})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'Error');
    tgShowResult('✓ Token is valid · Bot: @'+d.bot_username,'ok');
  }catch(e){tgShowResult('✗ '+e.message,'err')}
}

async function tgSave(){
  const token=document.getElementById('tg-token').value.trim();
  const admins=document.getElementById('tg-admins').value.trim();
  if(!token){tgShowResult('Token is required','err');return}
  if(!admins){tgShowResult('Enter at least one Admin ID','err');return}
  tgShowResult('Saving and starting bot...','wait');
  try{
    const r=await authF('/api/telegram',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({bot_token:token,admin_ids:admins})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'Error');
    tgShowResult('✓ Bot started'+(d.bot_username?' · @'+d.bot_username:''),'ok');
    tgLoad();
  }catch(e){tgShowResult('✗ '+e.message,'err')}
}

async function tgStop(){
  if(!confirm('Stop the bot? (token will be saved)'))return;
  tgShowResult('Stopping...','wait');
  try{
    const r=await authF('/api/telegram/stop',{method:'POST'});
    if(!r.ok)throw new Error('Error');
    tgShowResult('✓ Bot stopped','ok');
    tgLoad();
  }catch(e){tgShowResult('✗ Failed to stop','err')}
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('en-US')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('Enter UUID','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','Connected: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ Connected - Valid UUID');ws.onerror=()=>wsLog('err','✗ Error - Invalid or inactive UUID');ws.onmessage=m=>wsLog('info','Received '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','Closed ('+e.code+')'+(e.code===1008?' - Access denied':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','Sent: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
/* ═════════ SERVER IP + LOCATION ═════════ */
let __serverInfo = null;
function serverFlagUrls(countryCode){
  const cc = String(countryCode || '').trim().toLowerCase();
  if(!cc || !/^[a-z]{2}$/.test(cc)) return [];
  // SVG برای بهترین وضوح؛ PNG بزرگ به‌Title fallback
  return [
    `https://flagcdn.com/${cc}.svg`,
    `https://flagcdn.com/w320/${cc}.png`,
    `https://flagcdn.com/w160/${cc}.png`
  ];
}
function setServerFlag(imgId, countryCode, fallbackEmoji='🌐'){
  const img = document.getElementById(imgId);
  if(!img) return;
  const urls = serverFlagUrls(countryCode);
  const wrap = img.parentElement;
  if(!urls.length){
    img.removeAttribute('src');
    img.style.display='none';
    if(wrap) wrap.textContent = fallbackEmoji;
    return;
  }
  let idx = 0;
  img.style.display='block';
  img.onload=()=>{img.style.display='block'};
  img.onerror=()=>{
    idx++;
    if(idx < urls.length){
      img.src = urls[idx];
      return;
    }
    img.removeAttribute('src');
    img.style.display='none';
    if(wrap) wrap.textContent = fallbackEmoji;
  };
  img.src = urls[0];
}
async function loadServerInfo(){
  try{
    const r = await authF('/api/server-info');
    const d = await r.json();
    if(d.error){ 
      const b = document.getElementById('server-ip-text');
      if(b) b.textContent = '—';
      return;
    }
    __serverInfo = d;
    const isEnNow = typeof uiLang !== 'undefined' && uiLang === 'en';
    const ipTitle = isEnNow ? 'Server IP' : 'Server IP';
    const ipBadge = document.getElementById('server-ip-badge');
    const ipFlag = document.getElementById('server-ip-flag');
    if(ipBadge) ipBadge.title = ipTitle;
    if(ipFlag) ipFlag.title = ipTitle;
    // Dashboard: فقط پرچم تصویری + IP
    const txt = document.getElementById('server-ip-text');
    if(txt) txt.textContent = d.ip || '—';
    setServerFlag('server-ip-flag', d.country_code, d.flag || '🌐');

    // Settings: اطلاعات کامل IP و لوکیشن — متن‌ها با زبان فعلی PANEL هماهنگ می‌شوند.
    const full = document.getElementById('srv-info-full');
    if(full){
      const isEn = typeof uiLang !== 'undefined' && uiLang === 'en';
      const ip = esc(d.ip || '—');

      // ترجمه‌ی جغرافیایی در حالت فارسی؛ نام ISP / Org / ASN دست‌نخورده می‌ماند.
      // نام کشورها از CLDR به‌صورت کامل نگه‌داری می‌شوند و نام شهرها از timezone
      // در صورت امکان به فارسی برمی‌گردند؛ در غیر این صورت مقدار اصلی حفظ می‌شود.
      const FA_COUNTRIES = {
        "AC": "جزایر آسنسیون",
        "AD": "آندورا",
        "AE": "امارات متحدهٔ عربی",
        "AF": "افغانستان",
        "AG": "آنتیگوا و باربودا",
        "AI": "آنگویلا",
        "AL": "آلبانی",
        "AM": "ارمنستان",
        "AO": "آنگولا",
        "AQ": "جنوبگان",
        "AR": "آرژانتین",
        "AS": "ساموآی امریکا",
        "AT": "اتریش",
        "AU": "استرالیا",
        "AW": "آروبا",
        "AX": "جزایر آلاند",
        "AZ": "جمهوری آذربایجان",
        "BA": "بوسنی و هرزگوین",
        "BB": "باربادوس",
        "BD": "بنگلادش",
        "BE": "بلژیک",
        "BF": "بورکینافاسو",
        "BG": "بلغارستان",
        "BH": "بحرین",
        "BI": "بوروندی",
        "BJ": "بنین",
        "BL": "سن بارتلمی",
        "BM": "برمودا",
        "BN": "برونئی",
        "BO": "بولیوی",
        "BQ": "جزایر کارائیب هلند",
        "BR": "برزیل",
        "BS": "باهاما",
        "BT": "بوتان",
        "BV": "جزیرهٔ بووه",
        "BW": "بوتسوانا",
        "BY": "بلاروس",
        "BZ": "بلیز",
        "CA": "کانادا",
        "CC": "جزایر کوکوس",
        "CD": "کنگو - کینشاسا",
        "CF": "جمهوری افریقای مرکزی",
        "CG": "کنگو - برازویل",
        "CH": "سوئیس",
        "CI": "ساحل عاج",
        "CK": "جزایر کوک",
        "CL": "شیلی",
        "CM": "کامرون",
        "CN": "چین",
        "CO": "کلمبیا",
        "CP": "جزایر کلیپرتون",
        "CR": "کاستاریکا",
        "CU": "کوبا",
        "CV": "کیپ\u200cورد",
        "CW": "کوراسائو",
        "CX": "جزیرهٔ کریسمس",
        "CY": "قبرس",
        "CZ": "چک",
        "DE": "آلمان",
        "DG": "دیه\u200cگو گارسیا",
        "DJ": "جیبوتی",
        "DK": "دانمارک",
        "DM": "دومینیکا",
        "DO": "جمهوری دومینیکن",
        "DZ": "الجزایر",
        "EA": "سبته و ملیله",
        "EC": "اکوادور",
        "EE": "استونی",
        "EG": "مصر",
        "EH": "صحرای غربی",
        "ER": "اریتره",
        "ES": "اسپانیا",
        "ET": "اتیوپی",
        "EU": "اتحادیهٔ اروپا",
        "EZ": "منطقهٔ یورو",
        "FI": "فنلاند",
        "FJ": "فیجی",
        "FK": "جزایر فالکلند",
        "FM": "میکرونزی",
        "FO": "جزایر فارو",
        "FR": "فرانسه",
        "GA": "گابن",
        "GB": "بریتانیا",
        "GD": "گرنادا",
        "GE": "گرجستان",
        "GF": "گویان فرانسه",
        "GG": "گرنزی",
        "GH": "غنا",
        "GI": "جبل\u200cالطارق",
        "GL": "گرینلند",
        "GM": "گامبیا",
        "GN": "گینه",
        "GP": "گوادلوپ",
        "GQ": "گینهٔ استوایی",
        "GR": "یونان",
        "GS": "جورجیای جنوبی و جزایر ساندویچ جنوبی",
        "GT": "گواتمالا",
        "GU": "گوام",
        "GW": "گینهٔ بیسائو",
        "GY": "گویان",
        "HK": "هنگ\u200cکنگ، منطقهٔ ویژهٔ اداری چین",
        "HM": "هرد و جزایر مک\u200cدونالد",
        "HN": "هندوراس",
        "HR": "کرواسی",
        "HT": "هائیتی",
        "HU": "مجارستان",
        "IC": "جزایر قناری",
        "ID": "اندونزی",
        "IE": "ایرلند",
        "IL": "اسرائیل",
        "IM": "جزیرهٔ من",
        "IN": "هند",
        "IO": "قلمرو بریتانیا در اقیانوس هند",
        "IQ": "عراق",
        "IR": "ایران",
        "IS": "ایسلند",
        "IT": "ایتالیا",
        "JE": "جرزی",
        "JM": "جامائیکا",
        "JO": "اردن",
        "JP": "ژاپن",
        "KE": "کنیا",
        "KG": "قرقیزستان",
        "KH": "کامبوج",
        "KI": "کیریباتی",
        "KM": "کومور",
        "KN": "سنت کیتس و نویس",
        "KP": "کرهٔ شمالی",
        "KR": "کرهٔ جنوبی",
        "KW": "کویت",
        "KY": "جزایر کِیمن",
        "KZ": "قزاقستان",
        "LA": "لائوس",
        "LB": "لبنان",
        "LC": "سنت لوسیا",
        "LI": "لیختن\u200cاشتاین",
        "LK": "سری\u200cلانکا",
        "LR": "لیبریا",
        "LS": "لسوتو",
        "LT": "لیتوانی",
        "LU": "لوکزامبورگ",
        "LV": "لتونی",
        "LY": "لیبی",
        "MA": "مراکش",
        "MC": "موناکو",
        "MD": "مولداوی",
        "ME": "مونته\u200cنگرو",
        "MF": "سنت مارتین",
        "MG": "ماداگاسکار",
        "MH": "جزایر مارشال",
        "MK": "مقدونیهٔ شمالی",
        "ML": "مالی",
        "MM": "میانمار (برمه)",
        "MN": "مغولستان",
        "MO": "ماکائو، منطقهٔ ویژهٔ اداری چین",
        "MP": "جزایر ماریانای شمالی",
        "MQ": "مارتینیک",
        "MR": "موریتانی",
        "MS": "مونت\u200cسرات",
        "MT": "مالت",
        "MU": "موریس",
        "MV": "مالدیو",
        "MW": "مالاوی",
        "MX": "مکزیک",
        "MY": "مالزی",
        "MZ": "موزامبیک",
        "NA": "نامیبیا",
        "NC": "کالدونیای جدید",
        "NE": "نیجر",
        "NF": "جزیرهٔ نورفولک",
        "NG": "نیجریه",
        "NI": "نیکاراگوئه",
        "NL": "هلند",
        "NO": "نروژ",
        "NP": "نپال",
        "NR": "نائورو",
        "NU": "نیوئه",
        "NZ": "نیوزیلند",
        "OM": "عمان",
        "PA": "پاناما",
        "PE": "پرو",
        "PF": "پلی\u200cنزی فرانسه",
        "PG": "پاپوا گینهٔ نو",
        "PH": "فیلیپین",
        "PK": "پاکستان",
        "PL": "لهستان",
        "PM": "سن پیر و میکلن",
        "PN": "جزایر پیت\u200cکرن",
        "PR": "پورتوریکو",
        "PS": "سرزمین\u200cهای فلسطینی",
        "PT": "پرتغال",
        "PW": "پالائو",
        "PY": "پاراگوئه",
        "QA": "قطر",
        "QO": "بخش\u200cهای دورافتادهٔ اقیانوسیه",
        "RE": "رئونیون",
        "RO": "رومانی",
        "RS": "صربستان",
        "RU": "روسیه",
        "RW": "رواندا",
        "SA": "عربستان سعودی",
        "SB": "جزایر سلیمان",
        "SC": "سیشل",
        "SD": "سودان",
        "SE": "سوئد",
        "SG": "سنگاپور",
        "SH": "سنت هلن",
        "SI": "اسلوونی",
        "SJ": "سوالبارد و یان ماین",
        "SK": "اسلواکی",
        "SL": "سیرالئون",
        "SM": "سان\u200cمارینو",
        "SN": "سنگال",
        "SO": "سومالی",
        "SR": "سورینام",
        "SS": "سودان جنوبی",
        "ST": "سائوتومه و پرینسیپ",
        "SV": "السالوادور",
        "SX": "سنت مارتن",
        "SY": "سوریه",
        "SZ": "اسواتینی",
        "TA": "تریستان دا کونا",
        "TC": "جزایر تورکس و کایکوس",
        "TD": "چاد",
        "TF": "سرزمین\u200cهای جنوبی فرانسه",
        "TG": "توگو",
        "TH": "تایلند",
        "TJ": "تاجیکستان",
        "TK": "توکلائو",
        "TL": "تیمور-لسته",
        "TM": "ترکمنستان",
        "TN": "تونس",
        "TO": "تونگا",
        "TR": "ترکیه",
        "TT": "ترینیداد و توباگو",
        "TV": "تووالو",
        "TW": "تایوان",
        "TZ": "تانزانیا",
        "UA": "اوکراین",
        "UG": "اوگاندا",
        "UM": "جزایر دورافتادهٔ ایالات متحده",
        "UN": "سازمان ملل متحد",
        "US": "ایالات متحده",
        "UY": "اروگوئه",
        "UZ": "ازبکستان",
        "VA": "واتیکان",
        "VC": "سنت وینسنت و گرنادین",
        "VE": "ونزوئلا",
        "VG": "جزایر ویرجین بریتانیا",
        "VI": "جزایر ویرجین ایالات متحده",
        "VN": "ویتنام",
        "VU": "وانواتو",
        "WF": "والیس و فوتونا",
        "WS": "ساموآ",
        "XA": "انگلیسی با لهجه خارجی",
        "XB": "مجازی - دوجهته",
        "XK": "کوزوو",
        "YE": "یمن",
        "YT": "مایوت",
        "ZA": "افریقای جنوبی",
        "ZM": "زامبیا",
        "ZW": "زیمبابوه",
        "ZZ": "ناحیهٔ نامشخص"
      };
      const FA_TZ_CITIES = {
        "Africa/Abidjan": "آبیجان",
        "Africa/Accra": "اکرا",
        "Africa/Addis_Ababa": "آدیس آبابا",
        "Africa/Algiers": "الجزیره",
        "Africa/Asmera": "اسمره",
        "Africa/Bamako": "باماکو",
        "Africa/Bangui": "بانگی",
        "Africa/Banjul": "بانجول",
        "Africa/Bissau": "بیسائو",
        "Africa/Blantyre": "بلانتیره",
        "Africa/Brazzaville": "برازویل",
        "Africa/Bujumbura": "بوجومبورا",
        "Africa/Cairo": "قاهره",
        "Africa/Casablanca": "کازابلانکا",
        "Africa/Ceuta": "سبته",
        "Africa/Conakry": "کوناکری",
        "Africa/Dakar": "داکار",
        "Africa/Dar_es_Salaam": "دارالسلام",
        "Africa/Djibouti": "جیبوتی",
        "Africa/Douala": "دوآلا",
        "Africa/El_Aaiun": "العیون",
        "Africa/Freetown": "فری‌تاون",
        "Africa/Gaborone": "گابورون",
        "Africa/Harare": "هراره",
        "Africa/Johannesburg": "ژوهانسبورگ",
        "Africa/Juba": "جوبا",
        "Africa/Kampala": "کامپالا",
        "Africa/Khartoum": "خارطوم",
        "Africa/Kigali": "کیگالی",
        "Africa/Kinshasa": "کینشاسا",
        "Africa/Lagos": "لاگوس",
        "Africa/Libreville": "لیبرویل",
        "Africa/Lome": "لومه",
        "Africa/Luanda": "لواندا",
        "Africa/Lubumbashi": "لوبومباشی",
        "Africa/Lusaka": "لوزاکا",
        "Africa/Malabo": "مالابو",
        "Africa/Maputo": "ماپوتو",
        "Africa/Maseru": "ماسرو",
        "Africa/Mbabane": "مبابانه",
        "Africa/Mogadishu": "موگادیشو",
        "Africa/Monrovia": "مونروویا",
        "Africa/Nairobi": "نایروبی",
        "Africa/Ndjamena": "انجامنا",
        "Africa/Niamey": "نیامی",
        "Africa/Nouakchott": "نوآکشوت",
        "Africa/Ouagadougou": "اوآگادوگو",
        "Africa/Porto-Novo": "پورتو نووو",
        "Africa/Sao_Tome": "سائوتومه",
        "Africa/Tripoli": "طرابلس",
        "Africa/Tunis": "تونس",
        "Africa/Windhoek": "ویندهوک",
        "America/Adak": "ایدک",
        "America/Anchorage": "انکوریج",
        "America/Anguilla": "آنگوئیلا",
        "America/Antigua": "آنتیگوا",
        "America/Araguaina": "آراگواینا",
        "America/Argentina/La_Rioja": "لاریوخا",
        "America/Argentina/Rio_Gallegos": "ریوگالگوس",
        "America/Argentina/Salta": "سالتا",
        "America/Argentina/San_Juan": "سن‌خوان",
        "America/Argentina/San_Luis": "سن‌لوئیس",
        "America/Argentina/Tucuman": "توکومن",
        "America/Argentina/Ushuaia": "اوشوایا",
        "America/Aruba": "اروبا",
        "America/Asuncion": "آسونسیون",
        "America/Bahia": "بایا",
        "America/Bahia_Banderas": "باهیا باندراس",
        "America/Barbados": "باربادوس",
        "America/Belem": "بلم",
        "America/Belize": "بلیز",
        "America/Blanc-Sablon": "بلان‐Subscriptionلون",
        "America/Boa_Vista": "بوئاویستا",
        "America/Bogota": "بوگوتا",
        "America/Boise": "بویسی",
        "America/Buenos_Aires": "بوئنوس‌آیرس",
        "America/Cambridge_Bay": "کمبریج‌بی",
        "America/Campo_Grande": "کمپو گرانده",
        "America/Cancun": "کانکون",
        "America/Caracas": "کاراکاس",
        "America/Catamarca": "کاتامارکا",
        "America/Cayenne": "کاین",
        "America/Cayman": "کیمن",
        "America/Chicago": "شیکاگو",
        "America/Chihuahua": "چیواوا",
        "America/Ciudad_Juarez": "سیوداد خوارز",
        "America/Coral_Harbour": "اتکوکان",
        "America/Cordoba": "کوردووا",
        "America/Costa_Rica": "کاستاریکا",
        "America/Creston": "کرستون",
        "America/Cuiaba": "کویاوا",
        "America/Curacao": "کوراسائو",
        "America/Danmarkshavn": "دانمارکس‌هاون",
        "America/Dawson": "داوسن",
        "America/Dawson_Creek": "داوسن کریک",
        "America/Denver": "دنور",
        "America/Detroit": "دیترویت",
        "America/Dominica": "دومینیکا",
        "America/Edmonton": "ادمونتون",
        "America/Eirunepe": "ایرونپه",
        "America/El_Salvador": "السالوادور",
        "America/Fort_Nelson": "فورت نلسون",
        "America/Fortaleza": "فورتالزا",
        "America/Glace_Bay": "گلیس‌بی",
        "America/Godthab": "نووک",
        "America/Goose_Bay": "گوس‌بی",
        "America/Grand_Turk": "گراند تورک",
        "America/Grenada": "گرنادا",
        "America/Guadeloupe": "گوادلوپ",
        "America/Guatemala": "گواتمالا",
        "America/Guayaquil": "گوایاکیل",
        "America/Guyana": "گویان",
        "America/Halifax": "هلیفکس",
        "America/Havana": "هاوانا",
        "America/Hermosillo": "ارموسیو",
        "America/Indiana/Knox": "ناکس، ایندیانا",
        "America/Indiana/Marengo": "مارنگو، ایندیانا",
        "America/Indiana/Petersburg": "پیترزبرگ، ایندیانا",
        "America/Indiana/Tell_City": "تل‌سیتی، ایندیانا",
        "America/Indiana/Vevay": "ویوی، ایندیانا",
        "America/Indiana/Vincennes": "وینسنس، اندیانا",
        "America/Indiana/Winamac": "ویناماک، ایندیانا",
        "America/Indianapolis": "ایندیاناپولیس",
        "America/Inuvik": "اینوویک",
        "America/Iqaluit": "ایکلوئت",
        "America/Jamaica": "جامائیکا",
        "America/Jujuy": "خوخوی",
        "America/Juneau": "جونو",
        "America/Kentucky/Monticello": "مانتیسلو، کنتاکی",
        "America/Kralendijk": "کرالندیک",
        "America/La_Paz": "لاپاز",
        "America/Lima": "لیما",
        "America/Los_Angeles": "لوس‌آنجلس",
        "America/Louisville": "لوئیزویل",
        "America/Lower_Princes": "بخش شاهزاده‌‌نشین پایین",
        "America/Maceio": "ماسیو",
        "America/Managua": "ماناگوا",
        "America/Manaus": "ماناوس",
        "America/Marigot": "ماریگات",
        "America/Martinique": "مارتینیک",
        "America/Matamoros": "ماتاموروس",
        "America/Mazatlan": "ماساتلان",
        "America/Mendoza": "مندوسا",
        "America/Menominee": "منامینی",
        "America/Merida": "مریدا",
        "America/Metlakatla": "متالاکاتلا",
        "America/Mexico_City": "مکزیکوسیتی",
        "America/Miquelon": "میکلون",
        "America/Moncton": "مانکتون",
        "America/Monterrey": "مونتری",
        "America/Montevideo": "مونته‌ویدئو",
        "America/Montserrat": "مونتسرات",
        "America/Nassau": "ناسائو",
        "America/New_York": "نیویورک",
        "America/Nome": "نوم",
        "America/Noronha": "نورونیا",
        "America/North_Dakota/Beulah": "بیولا، داکوتای شمالی",
        "America/North_Dakota/Center": "سنتر، داکوتای شمالی",
        "America/North_Dakota/New_Salem": "نیوسالم، داکوتای شمالی",
        "America/Ojinaga": "اوجیناگا",
        "America/Panama": "پاناما",
        "America/Paramaribo": "پاراماریبو",
        "America/Phoenix": "فینکس",
        "America/Port-au-Prince": "پورتوپرنس",
        "America/Port_of_Spain": "پورت‌آواسپین",
        "America/Porto_Velho": "پورتوولیو",
        "America/Puerto_Rico": "پورتوریکو",
        "America/Punta_Arenas": "پونتا آرناس",
        "America/Rankin_Inlet": "خلیجک رنکین",
        "America/Recife": "ریسیفی",
        "America/Regina": "رجاینا",
        "America/Resolute": "رزولوت",
        "America/Rio_Branco": "ریوبرانکو",
        "America/Santarem": "سنتارم",
        "America/Santiago": "سانتیاگو",
        "America/Santo_Domingo": "سانتو دومینگو",
        "America/Sao_Paulo": "سائوپائولو",
        "America/Scoresbysund": "اسکورسبیسوند",
        "America/Sitka": "سیتکا",
        "America/St_Barthelemy": "سنت بارتلمی",
        "America/St_Johns": "سنت جان",
        "America/St_Kitts": "سنت کیتس",
        "America/St_Lucia": "سنت لوسیا",
        "America/St_Thomas": "سنت توماس",
        "America/St_Vincent": "سنت وینسنت",
        "America/Swift_Current": "سویفت‌کارنت",
        "America/Tegucigalpa": "تگوسیگالپا",
        "America/Thule": "تول",
        "America/Tijuana": "تیخوانا",
        "America/Toronto": "تورنتو",
        "America/Tortola": "تورتولا",
        "America/Vancouver": "ونکوور",
        "America/Whitehorse": "وایت‌هورس",
        "America/Winnipeg": "وینیپگ",
        "America/Yakutat": "یاکوتات",
        "Antarctica/Casey": "کیسی",
        "Antarctica/Davis": "دیویس",
        "Antarctica/DumontDUrville": "دومون دورویل",
        "Antarctica/Macquarie": "مکواری",
        "Antarctica/Mawson": "ماوسون",
        "Antarctica/McMurdo": "مک‌موردو",
        "Antarctica/Palmer": "پالمر",
        "Antarctica/Rothera": "روترا",
        "Antarctica/Syowa": "شووا",
        "Antarctica/Troll": "ترول",
        "Antarctica/Vostok": "وستوک",
        "Arctic/Longyearbyen": "لانگ‌یربین",
        "Asia/Aden": "عدن",
        "Asia/Almaty": "آلماتی",
        "Asia/Amman": "عَمان",
        "Asia/Anadyr": "آنادیر",
        "Asia/Aqtau": "آقتاو",
        "Asia/Aqtobe": "آقتوبه",
        "Asia/Ashgabat": "عشق‌آباد",
        "Asia/Atyrau": "آتیراو",
        "Asia/Baghdad": "بغداد",
        "Asia/Bahrain": "بحرین",
        "Asia/Baku": "باکو",
        "Asia/Bangkok": "بانکوک",
        "Asia/Barnaul": "بارنائول",
        "Asia/Beirut": "بیروت",
        "Asia/Bishkek": "بیشکک",
        "Asia/Brunei": "برونئی",
        "Asia/Calcutta": "کلکته",
        "Asia/Chita": "چیتا",
        "Asia/Colombo": "کلمبو",
        "Asia/Damascus": "دمشق",
        "Asia/Dhaka": "داکا",
        "Asia/Dili": "دیلی",
        "Asia/Dubai": "دبی",
        "Asia/Dushanbe": "دوشنبه",
        "Asia/Famagusta": "فاماگوستا",
        "Asia/Gaza": "غزه",
        "Asia/Hebron": "الخلیل",
        "Asia/Hong_Kong": "هنگ‌کنگ",
        "Asia/Hovd": "خوود",
        "Asia/Irkutsk": "ایرکوتسک",
        "Asia/Jakarta": "جاکارتا",
        "Asia/Jayapura": "جایاپورا",
        "Asia/Jerusalem": "اورشلیم",
        "Asia/Kabul": "کابل",
        "Asia/Kamchatka": "کامچاتکا",
        "Asia/Karachi": "کراچی",
        "Asia/Katmandu": "کاتماندو",
        "Asia/Khandyga": "خاندیگا",
        "Asia/Krasnoyarsk": "کراسنویارسک",
        "Asia/Kuala_Lumpur": "کوالالامپور",
        "Asia/Kuching": "کوچینگ",
        "Asia/Kuwait": "کویت",
        "Asia/Macau": "ماکائو",
        "Asia/Magadan": "ماگادان",
        "Asia/Makassar": "ماکاسار",
        "Asia/Manila": "مانیل",
        "Asia/Muscat": "مسقط",
        "Asia/Nicosia": "نیکوزیا",
        "Asia/Novokuznetsk": "نوووکوزنتسک",
        "Asia/Novosibirsk": "نووسیبیریسک",
        "Asia/Omsk": "اومسک",
        "Asia/Oral": "اورال",
        "Asia/Phnom_Penh": "پنوم‌پن",
        "Asia/Pontianak": "پونتیاناک",
        "Asia/Pyongyang": "پیونگ‌یانگ",
        "Asia/Qatar": "قطر",
        "Asia/Qostanay": "قوستانای",
        "Asia/Qyzylorda": "قیزیل‌اوردا",
        "Asia/Rangoon": "یانگون",
        "Asia/Riyadh": "ریاض",
        "Asia/Saigon": "هوشی‌مین‌سیتی",
        "Asia/Sakhalin": "ساخالین",
        "Asia/Samarkand": "سمرقند",
        "Asia/Seoul": "سئول",
        "Asia/Shanghai": "شانگهای",
        "Asia/Singapore": "سنگاپور",
        "Asia/Srednekolymsk": "اسردنکولیمسک",
        "Asia/Taipei": "تایپه",
        "Asia/Tashkent": "تاشکند",
        "Asia/Tbilisi": "تفلیس",
        "Asia/Tehran": "تهران",
        "Asia/Thimphu": "تیمفو",
        "Asia/Tokyo": "توکیو",
        "Asia/Tomsk": "تومسک",
        "Asia/Ulaanbaatar": "اولان‌باتور",
        "Asia/Urumqi": "ارومچی",
        "Asia/Ust-Nera": "اوست نرا",
        "Asia/Vientiane": "وینتیان",
        "Asia/Vladivostok": "ولادی‌وستوک",
        "Asia/Yakutsk": "یاکوتسک",
        "Asia/Yekaterinburg": "یکاترینبرگ",
        "Asia/Yerevan": "ایروان",
        "Atlantic/Azores": "آزور",
        "Atlantic/Bermuda": "برمودا",
        "Atlantic/Canary": "قناری",
        "Atlantic/Cape_Verde": "کیپ‌ورد",
        "Atlantic/Faeroe": "فارو",
        "Atlantic/Madeira": "مادیرا",
        "Atlantic/Reykjavik": "ریکیاویک",
        "Atlantic/South_Georgia": "جورجیای جنوبی",
        "Atlantic/St_Helena": "سنت هلنا",
        "Atlantic/Stanley": "استانلی",
        "Australia/Adelaide": "آدلاید",
        "Australia/Brisbane": "بریسبین",
        "Australia/Broken_Hill": "بروکن‌هیل",
        "Australia/Darwin": "داروین",
        "Australia/Eucla": "اوکلا",
        "Australia/Hobart": "هوبارت",
        "Australia/Lindeman": "لیندمن",
        "Australia/Lord_Howe": "لردهاو",
        "Australia/Melbourne": "ملبورن",
        "Australia/Perth": "پرت",
        "Australia/Sydney": "سیدنی",
        "Etc/Unknown": "شهر نامشخص",
        "Europe/Amsterdam": "آمستردام",
        "Europe/Andorra": "آندورا",
        "Europe/Astrakhan": "آستراخان",
        "Europe/Athens": "آتن",
        "Europe/Belgrade": "بلگراد",
        "Europe/Berlin": "برلین",
        "Europe/Bratislava": "براتیسلاوا",
        "Europe/Brussels": "بروکسل",
        "Europe/Bucharest": "بخارست",
        "Europe/Budapest": "بوداپست",
        "Europe/Busingen": "بازنگن",
        "Europe/Chisinau": "کیشیناو",
        "Europe/Copenhagen": "کپنهاگ",
        "Europe/Dublin": "دوبلین",
        "Europe/Gibraltar": "جبل‌الطارق",
        "Europe/Guernsey": "گرنزی",
        "Europe/Helsinki": "هلسینکی",
        "Europe/Isle_of_Man": "جزیرهٔ من",
        "Europe/Istanbul": "استانبول",
        "Europe/Jersey": "جرزی",
        "Europe/Kaliningrad": "کالینینگراد",
        "Europe/Kiev": "کیف",
        "Europe/Kirov": "کیروف",
        "Europe/Lisbon": "لیسبون",
        "Europe/Ljubljana": "لیوبلیانا",
        "Europe/London": "لندن",
        "Europe/Luxembourg": "لوکزامبورگ",
        "Europe/Madrid": "مادرید",
        "Europe/Malta": "مالت",
        "Europe/Mariehamn": "ماریه‌هامن",
        "Europe/Minsk": "مینسک",
        "Europe/Monaco": "موناکو",
        "Europe/Moscow": "مسکو",
        "Europe/Oslo": "اسلو",
        "Europe/Paris": "پاریس",
        "Europe/Podgorica": "پادگاریتسا",
        "Europe/Prague": "پراگ",
        "Europe/Riga": "ریگا",
        "Europe/Rome": "رم",
        "Europe/Samara": "سامارا",
        "Europe/San_Marino": "سان‌مارینو",
        "Europe/Sarajevo": "سارایوو",
        "Europe/Saratov": "ساراتوف",
        "Europe/Simferopol": "سیمفروپل",
        "Europe/Skopje": "اسکوپیه",
        "Europe/Sofia": "صوفیه",
        "Europe/Stockholm": "استکهلم",
        "Europe/Tallinn": "تالین",
        "Europe/Tirane": "تیرانا",
        "Europe/Ulyanovsk": "اولیانوفسک",
        "Europe/Vaduz": "فادوتس",
        "Europe/Vatican": "واتیکان",
        "Europe/Vienna": "وین",
        "Europe/Vilnius": "ویلنیوس",
        "Europe/Volgograd": "ولگاگراد",
        "Europe/Warsaw": "ورشو",
        "Europe/Zagreb": "زاگرب",
        "Europe/Zurich": "زوریخ",
        "Indian/Antananarivo": "آنتاناناریوو",
        "Indian/Chagos": "شاگوس",
        "Indian/Christmas": "کریسمس",
        "Indian/Cocos": "کوکوس",
        "Indian/Comoro": "کومورو",
        "Indian/Kerguelen": "کرگولن",
        "Indian/Mahe": "ماهه",
        "Indian/Maldives": "مالدیو",
        "Indian/Mauritius": "موریس",
        "Indian/Mayotte": "مایوت",
        "Indian/Reunion": "رئونیون",
        "Pacific/Apia": "آپیا",
        "Pacific/Auckland": "اوکلند",
        "Pacific/Bougainville": "بوگنویل",
        "Pacific/Chatham": "چت‌هام",
        "Pacific/Easter": "ایستر",
        "Pacific/Efate": "افاته",
        "Pacific/Enderbury": "اندربری",
        "Pacific/Fakaofo": "فاکائوفو",
        "Pacific/Fiji": "فیجی",
        "Pacific/Funafuti": "فونافوتی",
        "Pacific/Galapagos": "گالاپاگوس",
        "Pacific/Gambier": "گامبیر",
        "Pacific/Guadalcanal": "گوادال‌کانال",
        "Pacific/Guam": "گوام",
        "Pacific/Honolulu": "هونولولو",
        "Pacific/Kanton": "کانتون",
        "Pacific/Kiritimati": "کریتیماتی",
        "Pacific/Kosrae": "کوسرای",
        "Pacific/Kwajalein": "کواجیلین",
        "Pacific/Majuro": "ماجورو",
        "Pacific/Marquesas": "مارکوزه",
        "Pacific/Midway": "میدوی",
        "Pacific/Nauru": "نائورو",
        "Pacific/Niue": "نیوئه",
        "Pacific/Norfolk": "نورفولک",
        "Pacific/Noumea": "نومئا",
        "Pacific/Pago_Pago": "پاگوپاگو",
        "Pacific/Palau": "پالائو",
        "Pacific/Pitcairn": "پیت‌کرن",
        "Pacific/Ponape": "پانپی",
        "Pacific/Port_Moresby": "پورت‌مورزبی",
        "Pacific/Rarotonga": "راروتونگا",
        "Pacific/Saipan": "سایپان",
        "Pacific/Tahiti": "تاهیتی",
        "Pacific/Tarawa": "تاراوا",
        "Pacific/Tongatapu": "تونگاتاپو",
        "Pacific/Truk": "چوک",
        "Pacific/Wake": "ویک",
        "Pacific/Wallis": "والیس"
      };
      const FA_CITY_ALIASES = {
        "Abidjan": "آبیجان",
        "Accra": "اکرا",
        "Adak": "ایدک",
        "Addis Ababa": "آدیس آبابا",
        "Adelaide": "آدلاید",
        "Aden": "عدن",
        "Algiers": "الجزیره",
        "Almaty": "آلماتی",
        "Amman": "عَمان",
        "Amsterdam": "آمستردام",
        "Anadyr": "آنادیر",
        "Anchorage": "انکوریج",
        "Andorra": "آندورا",
        "Anguilla": "آنگوئیلا",
        "Antananarivo": "آنتاناناریوو",
        "Antigua": "آنتیگوا",
        "Apia": "آپیا",
        "Aqtau": "آقتاو",
        "Aqtobe": "آقتوبه",
        "Araguaina": "آراگواینا",
        "Aruba": "اروبا",
        "Ashgabat": "عشق‌آباد",
        "Asmara": "اسمره",
        "Astrakhan": "آستراخان",
        "Asunción": "آسونسیون",
        "Athens": "آتن",
        "Atikokan": "اتکوکان",
        "Atyrau": "آتیراو",
        "Auckland": "اوکلند",
        "Azores": "آزور",
        "Baghdad": "بغداد",
        "Bahia": "بایا",
        "Bahrain": "بحرین",
        "Bahía de Banderas": "باهیا باندراس",
        "Baku": "باکو",
        "Bamako": "باماکو",
        "Bangkok": "بانکوک",
        "Bangui": "بانگی",
        "Banjul": "بانجول",
        "Barbados": "باربادوس",
        "Barnaul": "بارنائول",
        "Beirut": "بیروت",
        "Belem": "بلم",
        "Belgrade": "بلگراد",
        "Belize": "بلیز",
        "Berlin": "برلین",
        "Bermuda": "برمودا",
        "Beulah, North Dakota": "بیولا، داکوتای شمالی",
        "Bishkek": "بیشکک",
        "Bissau": "بیسائو",
        "Blanc-Sablon": "بلان‐Subscriptionلون",
        "Blantyre": "بلانتیره",
        "Boa Vista": "بوئاویستا",
        "Bogota": "بوگوتا",
        "Boise": "بویسی",
        "Bougainville": "بوگنویل",
        "Bratislava": "براتیسلاوا",
        "Brazzaville": "برازویل",
        "Brisbane": "بریسبین",
        "Broken Hill": "بروکن‌هیل",
        "Brunei": "برونئی",
        "Brussels": "بروکسل",
        "Bucharest": "بخارست",
        "Budapest": "بوداپست",
        "Buenos Aires": "بوئنوس‌آیرس",
        "Bujumbura": "بوجومبورا",
        "Busingen": "بازنگن",
        "Cairo": "قاهره",
        "Cambridge Bay": "کمبریج‌بی",
        "Campo Grande": "کمپو گرانده",
        "Canary": "قناری",
        "Cancún": "کانکون",
        "Cape Verde": "کیپ‌ورد",
        "Caracas": "کاراکاس",
        "Casablanca": "کازابلانکا",
        "Casey": "کیسی",
        "Catamarca": "کاتامارکا",
        "Cayenne": "کاین",
        "Cayman": "کیمن",
        "Center, North Dakota": "سنتر، داکوتای شمالی",
        "Ceuta": "سبته",
        "Chagos": "شاگوس",
        "Chatham": "چت‌هام",
        "Chicago": "شیکاگو",
        "Chihuahua": "چیواوا",
        "Chisinau": "کیشیناو",
        "Chita": "چیتا",
        "Christmas Island": "کریسمس",
        "Chuuk": "چوک",
        "Ciudad Juárez": "سیوداد خوارز",
        "Cocos Islands": "کوکوس",
        "Colombo": "کلمبو",
        "Comoro": "کومورو",
        "Conakry": "کوناکری",
        "Copenhagen": "کپنهاگ",
        "Cordoba": "کوردووا",
        "Costa Rica": "کاستاریکا",
        "Creston": "کرستون",
        "Cuiaba": "کویاوا",
        "Curaçao": "کوراسائو",
        "Dakar": "داکار",
        "Damascus": "دمشق",
        "Danmarkshavn": "دانمارکس‌هاون",
        "Dar es Salaam": "دارالسلام",
        "Darwin": "داروین",
        "Davis": "دیویس",
        "Dawson": "داوسن",
        "Dawson Creek": "داوسن کریک",
        "Denver": "دنور",
        "Detroit": "دیترویت",
        "Dhaka": "داکا",
        "Dili": "دیلی",
        "Djibouti": "جیبوتی",
        "Dominica": "دومینیکا",
        "Douala": "دوآلا",
        "Dubai": "دبی",
        "Dumont-d’Urville": "دومون دورویل",
        "Dushanbe": "دوشنبه",
        "Easter Island": "ایستر",
        "Edmonton": "ادمونتون",
        "Efate": "افاته",
        "Eirunepe": "ایرونپه",
        "El Aaiun": "العیون",
        "El Salvador": "السالوادور",
        "Enderbury": "اندربری",
        "Eucla": "اوکلا",
        "Fakaofo": "فاکائوفو",
        "Famagusta": "فاماگوستا",
        "Faroe": "فارو",
        "Fernando de Noronha": "نورونیا",
        "Fiji": "فیجی",
        "Fort Nelson": "فورت نلسون",
        "Fortaleza": "فورتالزا",
        "Freetown": "فری‌تاون",
        "Funafuti": "فونافوتی",
        "Gaborone": "گابورون",
        "Galapagos": "گالاپاگوس",
        "Gambier": "گامبیر",
        "Gaza": "غزه",
        "Gibraltar": "جبل‌الطارق",
        "Glace Bay": "گلیس‌بی",
        "Goose Bay": "گوس‌بی",
        "Grand Turk": "گراند تورک",
        "Grenada": "گرنادا",
        "Guadalcanal": "گوادال‌کانال",
        "Guadeloupe": "گوادلوپ",
        "Guam": "گوام",
        "Guatemala": "گواتمالا",
        "Guayaquil": "گوایاکیل",
        "Guernsey": "گرنزی",
        "Guyana": "گویان",
        "Halifax": "هلیفکس",
        "Harare": "هراره",
        "Havana": "هاوانا",
        "Hebron": "الخلیل",
        "Helsinki": "هلسینکی",
        "Hermosillo": "ارموسیو",
        "Ho Chi Minh City": "هوشی‌مین‌سیتی",
        "Hobart": "هوبارت",
        "Hong Kong": "هنگ‌کنگ",
        "Hovd": "خوود",
        "Indianapolis": "ایندیاناپولیس",
        "Inuvik": "اینوویک",
        "Iqaluit": "ایکلوئت",
        "Irkutsk": "ایرکوتسک",
        "Isle of Man": "جزیرهٔ من",
        "Istanbul": "استانبول",
        "Ittoqqortoormiit": "اسکورسبیسوند",
        "Jakarta": "جاکارتا",
        "Jamaica": "جامائیکا",
        "Jayapura": "جایاپورا",
        "Jersey": "جرزی",
        "Jerusalem": "اورشلیم",
        "Johannesburg": "ژوهانسبورگ",
        "Juba": "جوبا",
        "Jujuy": "خوخوی",
        "Juneau": "جونو",
        "Kabul": "کابل",
        "Kaliningrad": "کالینینگراد",
        "Kamchatka": "کامچاتکا",
        "Kampala": "کامپالا",
        "Kanton": "کانتون",
        "Karachi": "کراچی",
        "Kathmandu": "کاتماندو",
        "Kerguelen": "کرگولن",
        "Khandyga": "خاندیگا",
        "Khartoum": "خارطوم",
        "Kigali": "کیگالی",
        "Kinshasa": "کینشاسا",
        "Kiritimati": "کریتیماتی",
        "Kirov": "کیروف",
        "Knox, Indiana": "ناکس، ایندیانا",
        "Kolkata": "کلکته",
        "Kosrae": "کوسرای",
        "Kostanay": "قوستانای",
        "Kralendijk": "کرالندیک",
        "Krasnoyarsk": "کراسنویارسک",
        "Kuala Lumpur": "کوالالامپور",
        "Kuching": "کوچینگ",
        "Kuwait": "کویت",
        "Kwajalein": "کواجیلین",
        "Kyiv": "کیف",
        "La Paz": "لاپاز",
        "La Rioja": "لاریوخا",
        "Lagos": "لاگوس",
        "Libreville": "لیبرویل",
        "Lima": "لیما",
        "Lindeman": "لیندمن",
        "Lisbon": "لیسبون",
        "Ljubljana": "لیوبلیانا",
        "Lome": "لومه",
        "Longyearbyen": "لانگ‌یربین",
        "Lord Howe Island": "لردهاو",
        "Los Angeles": "لوس‌آنجلس",
        "Louisville": "لوئیزویل",
        "Lower Prince’s Quarter": "بخش شاهزاده‌‌نشین پایین",
        "Luanda": "لواندا",
        "Lubumbashi": "لوبومباشی",
        "Lusaka": "لوزاکا",
        "Luxembourg": "لوکزامبورگ",
        "Macao": "ماکائو",
        "Maceio": "ماسیو",
        "Macquarie Island": "مکواری",
        "Madeira": "مادیرا",
        "Madrid": "مادرید",
        "Magadan": "ماگادان",
        "Mahe": "ماهه",
        "Majuro": "ماجورو",
        "Makassar": "ماکاسار",
        "Malabo": "مالابو",
        "Maldives": "مالدیو",
        "Malta": "مالت",
        "Managua": "ماناگوا",
        "Manaus": "ماناوس",
        "Manila": "مانیل",
        "Maputo": "ماپوتو",
        "Marengo, Indiana": "مارنگو، ایندیانا",
        "Mariehamn": "ماریه‌هامن",
        "Marigot": "ماریگات",
        "Marquesas": "مارکوزه",
        "Martinique": "مارتینیک",
        "Maseru": "ماسرو",
        "Matamoros": "ماتاموروس",
        "Mauritius": "موریس",
        "Mawson": "ماوسون",
        "Mayotte": "مایوت",
        "Mazatlan": "ماساتلان",
        "Mbabane": "مبابانه",
        "McMurdo": "مک‌موردو",
        "Melbourne": "ملبورن",
        "Mendoza": "مندوسا",
        "Menominee": "منامینی",
        "Metlakatla": "متالاکاتلا",
        "Mexico City": "مکزیکوسیتی",
        "Midway": "میدوی",
        "Minsk": "مینسک",
        "Miquelon": "میکلون",
        "Mogadishu": "موگادیشو",
        "Monaco": "موناکو",
        "Moncton": "مانکتون",
        "Monrovia": "مونروویا",
        "Monterrey": "مونتری",
        "Montevideo": "مونته‌ویدئو",
        "Monticello, Kentucky": "مانتیسلو، کنتاکی",
        "Montserrat": "مونتسرات",
        "Moscow": "مسکو",
        "Muscat": "مسقط",
        "Mérida": "مریدا",
        "Nairobi": "نایروبی",
        "Nassau": "ناسائو",
        "Nauru": "نائورو",
        "Ndjamena": "انجامنا",
        "New Salem, North Dakota": "نیوسالم، داکوتای شمالی",
        "New York": "نیویورک",
        "Niamey": "نیامی",
        "Nicosia": "نیکوزیا",
        "Niue": "نیوئه",
        "Nome": "نوم",
        "Norfolk Island": "نورفولک",
        "Nouakchott": "نوآکشوت",
        "Noumea": "نومئا",
        "Novokuznetsk": "نوووکوزنتسک",
        "Novosibirsk": "نووسیبیریسک",
        "Nuuk": "نووک",
        "Ojinaga": "اوجیناگا",
        "Omsk": "اومسک",
        "Oral": "اورال",
        "Oslo": "اسلو",
        "Ouagadougou": "اوآگادوگو",
        "Pago Pago": "پاگوپاگو",
        "Palau": "پالائو",
        "Palmer": "پالمر",
        "Panama": "پاناما",
        "Paramaribo": "پاراماریبو",
        "Paris": "پاریس",
        "Perth": "پرت",
        "Petersburg, Indiana": "پیترزبرگ، ایندیانا",
        "Phnom Penh": "پنوم‌پن",
        "Phoenix": "فینکس",
        "Pitcairn": "پیت‌کرن",
        "Podgorica": "پادگاریتسا",
        "Pohnpei": "پانپی",
        "Pontianak": "پونتیاناک",
        "Port Moresby": "پورت‌مورزبی",
        "Port of Spain": "پورت‌آواسپین",
        "Port-au-Prince": "پورتوپرنس",
        "Porto Velho": "پورتوولیو",
        "Porto-Novo": "پورتو نووو",
        "Prague": "پراگ",
        "Puerto Rico": "پورتوریکو",
        "Punta Arenas": "پونتا آرناس",
        "Pyongyang": "پیونگ‌یانگ",
        "Qatar": "قطر",
        "Qyzylorda": "قیزیل‌اوردا",
        "Rankin Inlet": "خلیجک رنکین",
        "Rarotonga": "راروتونگا",
        "Recife": "ریسیفی",
        "Regina": "رجاینا",
        "Resolute": "رزولوت",
        "Reykjavik": "ریکیاویک",
        "Riga": "ریگا",
        "Rio Branco": "ریوبرانکو",
        "Rio Gallegos": "ریوگالگوس",
        "Riyadh": "ریاض",
        "Rome": "رم",
        "Rothera": "روترا",
        "Réunion": "رئونیون",
        "Saipan": "سایپان",
        "Sakhalin": "ساخالین",
        "Salta": "سالتا",
        "Samara": "سامارا",
        "Samarkand": "سمرقند",
        "San Juan": "سن‌خوان",
        "San Luis": "سن‌لوئیس",
        "San Marino": "سان‌مارینو",
        "Santarem": "سنتارم",
        "Santiago": "سانتیاگو",
        "Santo Domingo": "سانتو دومینگو",
        "Sao Paulo": "سائوپائولو",
        "Sarajevo": "سارایوو",
        "Saratov": "ساراتوف",
        "Seoul": "سئول",
        "Shanghai": "شانگهای",
        "Simferopol": "سیمفروپل",
        "Singapore": "سنگاپور",
        "Sitka": "سیتکا",
        "Skopje": "اسکوپیه",
        "Sofia": "صوفیه",
        "South Georgia": "جورجیای جنوبی",
        "Srednekolymsk": "اسردنکولیمسک",
        "St. Barthélemy": "سنت بارتلمی",
        "St. Helena": "سنت هلنا",
        "St. John’s": "سنت جان",
        "St. Kitts": "سنت کیتس",
        "St. Lucia": "سنت لوسیا",
        "St. Thomas": "سنت توماس",
        "St. Vincent": "سنت وینسنت",
        "Stanley": "استانلی",
        "Stockholm": "استکهلم",
        "Swift Current": "سویفت‌کارنت",
        "Sydney": "سیدنی",
        "Syowa": "شووا",
        "São Tomé": "سائوتومه",
        "Tahiti": "تاهیتی",
        "Taipei": "تایپه",
        "Tallinn": "تالین",
        "Tarawa": "تاراوا",
        "Tashkent": "تاشکند",
        "Tbilisi": "تفلیس",
        "Tegucigalpa": "تگوسیگالپا",
        "Tehran": "تهران",
        "Tell City, Indiana": "تل‌سیتی، ایندیانا",
        "Thimphu": "تیمفو",
        "Thule": "تول",
        "Tijuana": "تیخوانا",
        "Tirane": "تیرانا",
        "Tokyo": "توکیو",
        "Tomsk": "تومسک",
        "Tongatapu": "تونگاتاپو",
        "Toronto": "تورنتو",
        "Tortola": "تورتولا",
        "Tripoli": "طرابلس",
        "Troll": "ترول",
        "Tucuman": "توکومن",
        "Tunis": "تونس",
        "Ulaanbaatar": "اولان‌باتور",
        "Ulyanovsk": "اولیانوفسک",
        "Unknown City": "شهر نامشخص",
        "Urumqi": "ارومچی",
        "Ushuaia": "اوشوایا",
        "Ust-Nera": "اوست نرا",
        "Vaduz": "فادوتس",
        "Vancouver": "ونکوور",
        "Vatican": "واتیکان",
        "Vevay, Indiana": "ویوی، ایندیانا",
        "Vienna": "وین",
        "Vientiane": "وینتیان",
        "Vilnius": "ویلنیوس",
        "Vincennes, Indiana": "وینسنس، اندیانا",
        "Vladivostok": "ولادی‌وستوک",
        "Volgograd": "ولگاگراد",
        "Vostok": "وستوک",
        "Wake Island": "ویک",
        "Wallis": "والیس",
        "Warsaw": "ورشو",
        "Whitehorse": "وایت‌هورس",
        "Winamac, Indiana": "ویناماک، ایندیانا",
        "Windhoek": "ویندهوک",
        "Winnipeg": "وینیپگ",
        "Yakutat": "یاکوتات",
        "Yakutsk": "یاکوتسک",
        "Yangon": "یانگون",
        "Yekaterinburg": "یکاترینبرگ",
        "Yerevan": "ایروان",
        "Zagreb": "زاگرب",
        "Zurich": "زوریخ"
      };
      const FA_REGIONS = {
        'North Holland': 'هلند شمالی',
        'South Holland': 'هلند جنوبی',
        'Flevoland': 'فلِوولاند',
        'Utrecht': 'اوترخت',
        'Gelderland': 'خلدرلاند',
        'Overijssel': 'اوِریسل',
        'Zeeland': 'زیلاند',
        'Groningen': 'خرونینگن',
        'Friesland': 'فریسلاند',
        'Limburg': 'لیمبورخ',
        'Drenthe': 'درنته',
        'Bavaria': 'بایرن',
        'Berlin': 'برلین',
        'Hamburg': 'هامبورگ',
        'Hesse': 'هسن',
        'North Rhine-Westphalia': 'نوردراین-وستفالن',
        'California': 'کالیفرنیا',
        'New York': 'نیویورک',
        'Texas': 'تگزاس',
        'Florida': 'فلوریدا',
        'Washington': 'واشینگتن',
        'Ontario': 'انتاریو',
        'Quebec': 'کبک',
        'British Columbia': 'بریتیش کلمبیا',
        'Île-de-France': 'ایل-دو-فرانس',
        'England': 'انگلستان',
        'Scotland': 'اسکاتلند',
        'Wales': 'ولز',
        'Northern Ireland': 'ایرلند شمالی'
      };
      const trGeo = (type, value) => {
        const raw = String(value || '').trim();
        if(!raw) return '';
        if(isEn) return raw;
        if(type === 'country') {
          const code = String(d.country_code || '').trim().toUpperCase();
          return FA_COUNTRIES[code] || d.country_fa || raw;
        }
        if(type === 'timezone') {
          return FA_TZ_CITIES[raw] ? String(raw).split('/')[0] + '/' + FA_TZ_CITIES[raw] : raw;
        }
        if(type === 'city') {
          return FA_CITY_ALIASES[raw] || raw;
        }
        if(type === 'region') {
          return FA_REGIONS[raw] || raw;
        }
        return raw;
      };

      const country = esc(trGeo('country', d.country || d.country_fa || '—'));
      let cityValue = trGeo('city', d.city);
      if(!isEn && d.timezone && FA_TZ_CITIES[d.timezone]) {
        const tzCity = FA_TZ_CITIES[d.timezone];
        const rawCity = String(d.city || '').trim();
        const enTzCity = FA_CITY_ALIASES[rawCity];
        // اگر شهر با نام شهرِ timezone هم‌خوانی داشت، Version‌ی محلی‌شده‌ی CLDR را ترجیح بده.
        if(enTzCity || !rawCity) cityValue = tzCity;
      }
      const city = esc(cityValue);
      const region = (d.region && d.region !== d.city) ? esc(trGeo('region', d.region)) : '';
      const isp = esc(d.isp || d.org || '');
      const org = d.org && d.org !== d.isp ? esc(d.org) : '';
      const asn = d.asn ? esc(d.asn) : '';
      const timezone = d.timezone ? esc(trGeo('timezone', d.timezone)) : '';
      const parts = [country, city, region, isp, org, asn, timezone].filter(Boolean);
      const meta = parts.map((part, i) =>
        `${i ? '<span class="srv-info-sep">·</span>' : ''}<span class="srv-info-part" dir="auto">${part}</span>`
      ).join('');
      full.innerHTML = `
        <div class="srv-info-main">
          <span class="srv-info-flag-wrap"><img id="srv-info-flag" class="srv-info-flag" alt="" loading="lazy" decoding="async" referrerpolicy="no-referrer"></span>
          <div class="srv-info-copy">
            <div class="srv-info-ip" dir="ltr">${ip}</div>
            <div class="srv-info-meta">${meta}</div>
          </div>
        </div>`;
      setServerFlag('srv-info-flag', d.country_code, d.flag || '🌐');
    }
  }catch(e){ console.warn('server-info failed: ', e); }
}
document.addEventListener('DOMContentLoaded',async()=>{
  applyTheme(isDark);
  applyUiLang();
  await checkAuth();
  await loadServerInfo();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  document.getElementById('sub-all-url')&&(document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all');
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  tgLoad();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});
/* ═══════════════════════════════════════════════════════════════════════
   LOG MESSAGE TRANSLATOR
   ─────────────────────────────────────────────────────────────────────
   پیام‌های لاگ از سرور به فارسی میان و ZWNJ دارن.
   الگوها ابتدا به string نوشته می‌شن، بعد ZWNJ و کاراکترهای کنترلی از
   خودشون و از input پاک می‌شه و در نهایت به RegExp تبدیل می‌شن.
   ═══════════════════════════════════════════════════════════════════════ */

/* پاک‌سازی ZWNJ + کاراکترهای کنترلی RTL/LTR + فاصله‌های اضافی */
function cleanLogText(s){
  return String(s || '')
    .replace(/[\u200b\u200c\u200d\u200e\u200f\u202a-\u202e]/g, '')
    .trim();
}

/* الگوها — به‌صورت string، بدون توجه به ZWNJ (چون خودمان پاک می‌کنیم) */
const LOG_PATTERNS_RAW = [
  /* ── Auth ── */
  ['^ورود موفق به پنل از (.+)$',                     'Successfully signed in from $1'],
  ['^تلاش ورود ناموفق از (.+)$',                     'Failed login attempt from $1'],
  ['^اطلاعات ورود پنل تغییر کرد: (.+)$',             'Panel credentials changed: $1'],
  ['^رمز عبور پنل تغییر کرد$',                        'Panel password changed'],

  /* ── Config (link) ── */
  ['^کانفیگ «(.+?)» ساخته شد$',                       'Configuration "$1" created'],
  ['^کانفیگ «(.+?)» حذف شد$',                         'Configuration "$1" deleted'],
  ['^کانفیگ «(.+?)» فعال شد$',                        'Configuration "$1" enabled'],
  ['^کانفیگ «(.+?)» غیرفعال شد$',                     'Configuration "$1" disabled'],
  ['^کانفیگ «(.+?)» ویرایش شد: (.+)$',               'Configuration "$1" edited: $2'],
  ['^کانفیگ «(.+?)» ویرایش شد$',                      'Configuration "$1" edited'],
  ['^مصرف کانفیگ «(.+?)» ریست شد$',                   'Configuration "$1" usage reset'],
  ['^کانفیگ «(.+?)» به گروه اضافه شد$',              'Configuration "$1" added to group'],
  ['^کانفیگ «(.+?)» از گروه خارج شد$',               'Configuration "$1" removed from group'],
  ['^Sub Token کانفیگ «(.+?)» تنظیم شد: (.+)$',      'Configuration "$1" Sub Token set: $2'],

  /* ── Subscription Group ── */
  ['^گروه «(.+?)» ساخته شد$',                         'Group "$1" created'],
  ['^گروه «(.+?)» حذف شد$',                           'Group "$1" deleted'],

  /* ── System ── */
  ['^سرور راه‌اندازی شد$',                             'Server started'],
  ['^ربات تلگرام فعال شد \\(@(.+)\\)$',               'Telegram bot enabled (@$1)'],
  ['^ربات تلگرام غیرفعال شد \\(@(.+)\\)$',            'Telegram bot disabled (@$1)'],
  ['^ربات تلگرام فعال شد$',                            'Telegram bot enabled'],
  ['^ربات تلگرام غیرفعال شد$',                         'Telegram bot disabled'],
  ['^ربات تلگرام متوقف شد$',                            'Telegram bot stopped'],
];

/* تبدیل به RegExp با پاک‌سازی خود الگو */
const LOG_PATTERNS = LOG_PATTERNS_RAW.map(function(pair){
  const pattern = cleanLogText(pair[0]);
  const replacement = pair[1];
  return [new RegExp(pattern), replacement];
});

function translateLogMessage(msg, lang){
  if(!msg) return msg;
  const cleaned = cleanLogText(msg);
  if(lang !== 'en') return cleaned;
  for(let i = 0; i < LOG_PATTERNS.length; i++){
    const re = LOG_PATTERNS[i][0];
    const rep = LOG_PATTERNS[i][1];
    if(re.test(cleaned)) return cleaned.replace(re, rep);
  }
  return cleaned;
}
</script>
</body></html>"""


# جایگزینی نهایی لوگو در صفحات استاتیک (LOGIN_HTML / DASHBOARD_HTML)
LOGIN_HTML = (
    LOGIN_HTML
    .replace("__THEME_CSS__", _THEME_CSS)
    .replace("__LOGIN_CSS__", _LOGIN_CSS)
    .replace("__LOGO_B64__", LOGO_B64)
    .replace("__LANG_CENTER__", LANG_CENTER_JS)
)
DASHBOARD_HTML = (
    DASHBOARD_HTML
    .replace("__THEME_CSS__", _THEME_CSS)
    .replace("__DASHBOARD_CSS__", _DASHBOARD_CSS)
    .replace("__LOGO_B64__", LOGO_B64)
    .replace("__LANG_CENTER__", LANG_CENTER_JS)
)
