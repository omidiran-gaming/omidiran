# pages.py - OMID-IRAN PANEL v1.0
# شامل: LOGIN_HTML, DASHBOARD_HTML, get_public_page_html()

# لوگوی OMID (به‌صورت base64 داخلی)
LOGO_B64 = "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"

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OMID-IRAN PANEL · Login</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{box-sizing:border-box;margin:0;padding:0}html,body{min-height:100%;font-family:'Vazirmatn',sans-serif;background:#02070c;color:#E7FBFF}body{display:grid;place-items:center;overflow:hidden;position:relative}
body::before{content:"";position:fixed;inset:0;background:radial-gradient(circle at 16% 12%,rgba(17,173,201,.16),transparent 28%),radial-gradient(circle at 85% 80%,rgba(103,55,166,.13),transparent 25%),linear-gradient(rgba(74,225,247,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(74,225,247,.022) 1px,transparent 1px);background-size:auto,auto,40px 40px,40px 40px;pointer-events:none}
.scan{position:fixed;left:0;right:0;top:0;height:1px;background:linear-gradient(90deg,transparent,#58E9FF,transparent);box-shadow:0 0 22px #58E9FF;animation:scan 5.5s linear infinite;opacity:.6}@keyframes scan{0%{transform:translateY(0)}100%{transform:translateY(100vh)}}
.shell{width:min(460px,calc(100% - 28px));position:relative;z-index:2}.hud{display:flex;justify-content:space-between;align-items:center;margin-bottom:13px}.kicker{font-size:9px;letter-spacing:.18em;color:#4D7B88;font-weight:800}.lang{border:1px solid rgba(78,223,244,.18);background:rgba(9,44,56,.34);color:#82E7F6;border-radius:10px;padding:8px 10px;font:700 10px Vazirmatn,sans-serif;cursor:pointer}
.card{background:linear-gradient(145deg,rgba(6,27,39,.86),rgba(2,12,18,.76));border:1px solid rgba(74,220,239,.17);border-radius:28px;padding:28px;box-shadow:0 35px 110px rgba(0,0,0,.56),inset 0 1px 0 rgba(255,255,255,.03);backdrop-filter:blur(24px);position:relative;overflow:hidden}.card::before{content:"";position:absolute;inset:0;background:linear-gradient(120deg,transparent 0 38%,rgba(85,230,248,.04) 46%,transparent 56%);pointer-events:none}
.brand{display:flex;align-items:center;gap:13px;margin-bottom:25px}.brand-img{width:56px;height:56px;border-radius:16px;overflow:hidden;border:1px solid rgba(84,228,247,.22);box-shadow:0 0 30px rgba(11,167,196,.20)}.brand-img img{width:100%;height:100%;object-fit:cover}.brand-name{font-size:15px;font-weight:900;letter-spacing:.04em}.brand-sub{font-size:9px;color:#5993A2;margin-top:3px;text-transform:uppercase;letter-spacing:.13em}
h1{font-size:24px;line-height:1.35;font-weight:900;letter-spacing:-.03em;margin-bottom:8px}p.sub{font-size:11px;color:#6D98A5;line-height:1.9;margin-bottom:20px}.accent{color:#5CEBFF;text-shadow:0 0 18px rgba(92,235,255,.16)}
.err{display:none;align-items:center;gap:8px;background:rgba(255,93,112,.08);border:1px solid rgba(255,93,112,.22);color:#FF9AA8;border-radius:12px;padding:10px 12px;font-size:11px;margin-bottom:14px}.err.show{display:flex}.field{margin-bottom:14px}.field label{display:block;font-size:10px;color:#5D8794;margin-bottom:6px;font-weight:700}.input-shell{position:relative}.input-shell input{width:100%;height:48px;background:rgba(0,8,13,.52);border:1px solid rgba(72,219,240,.12);border-radius:13px;color:#E7FBFF;padding:0 44px 0 14px;outline:none;font:500 13px Vazirmatn,sans-serif;transition:.18s}.input-shell input:focus{border-color:rgba(87,229,250,.45);box-shadow:0 0 0 3px rgba(11,167,196,.08),0 0 30px rgba(11,167,196,.06)}.ic{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:#4C8290;font-size:17px}
.btn{width:100%;height:50px;border:none;border-radius:13px;background:linear-gradient(135deg,#07677C,#0BA4BE 58%,#1D638D);color:#fff;font:800 13px Vazirmatn,sans-serif;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 10px 32px rgba(0,125,153,.22);transition:.18s}.btn:hover{transform:translateY(-2px);filter:brightness(1.08)}.btn:disabled{opacity:.6;transform:none}
.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:16px}.meta{padding:10px 11px;border-radius:12px;border:1px solid rgba(74,220,239,.08);background:rgba(8,30,39,.28)}.meta span{display:block;font-size:7px;color:#3F6875;letter-spacing:.12em;margin-bottom:3px}.meta b{font-size:9px;color:#8FC8D4}.foot{display:flex;justify-content:space-between;gap:10px;margin-top:14px;color:#3F6875;font-size:8.5px}.ok{color:#56DDB0}@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:520px){.card{padding:22px;border-radius:23px}h1{font-size:21px}}
</style></head>
<body>
<div class="scan"></div><div class="shell">
  <div class="hud"><span class="kicker">OMID-01 / SECURE ACCESS GATE</span><button class="lang" id="lang-login" type="button">FA / EN</button></div>
  <div class="card">
    <div class="brand"><div class="brand-img"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div><div><div class="brand-name">OMID-IRAN PANEL</div><div class="brand-sub">Free For All · v1.0</div></div></div>
    <h1>ورود به <span class="accent">OMID-IRAN PANEL</span></h1>
    <p class="sub">Enter your access key to open the command dashboard · برای ورود به پنل کلید دسترسی را وارد کنید</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field"><label>رمز عبور · PASSWORD</label><div class="input-shell"><input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required><i class="ti ti-lock ic"></i></div></div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-terminal-2"></i> ورود به مرکز کنترل / Sign in</button>
    </form>
    <div class="meta-grid"><div class="meta"><span>NETWORK</span><b>OMID Network</b></div><div class="meta"><span>STATUS</span><b class="ok">● SYSTEM ONLINE</b></div></div>
    <div class="foot"><span>Free For All</span><span>OMID-IRAN PANEL · v1.0</span></div>
  </div>
</div>
<script>
const lb=document.getElementById('lang-login');let l=localStorage.getItem('omid-lang')||'both';
lb.addEventListener('click',()=>{l=l==='both'?'en':l==='en'?'fa':'both';localStorage.setItem('omid-lang',l);lb.textContent=l==='both'?'FA / EN':l==='en'?'EN':'FA';});
document.getElementById('form').addEventListener('submit',async e=>{e.preventDefault();const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');err.classList.remove('show');btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';try{const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}location.href='/dashboard';}catch(e){et.textContent=e.message;err.classList.add('show');btn.disabled=false;btn.innerHTML='<i class="ti ti-terminal-2"></i> ورود به مرکز کنترل / Sign in';}});
</script></body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OMID-IRAN PANEL · OMID</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#060f1d;--bg2:#0a1628;--bg3:#0e1e35;
  --card:#0d1b2e;--card-b:rgba(59,130,246,0.13);--card-bh:rgba(59,130,246,0.28);
  --accent:#3B82F6;--accent2:#60A5FA;--accent-d:rgba(59,130,246,0.12);
  --green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FCD34D;
  --purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.1);
  --t1:#E8F4FF;--t2:#7BAED4;--t3:#3D6B8E;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.35);
}
[data-theme="light"]{
  --bg:#F0F4FA;--bg2:#E4EDF9;--bg3:#D5E3F5;
  --card:#FFFFFF;--card-b:rgba(59,130,246,0.15);--card-bh:rgba(59,130,246,0.35);
  --accent:#2563EB;--accent2:#1D4ED8;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --shadow:0 4px 20px rgba(0,0,0,0.1);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(139,92,246,.3),0 0 8px rgba(59,130,246,.25);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1)}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(59,130,246,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.15s}
.tg-btn:hover{filter:brightness(1.1)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;box-shadow:0 0 8px rgba(139,92,246,.35)}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#A78BFA}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ صفحه ترافیک - ریدیزاین ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(59,130,246,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.04)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{background:linear-gradient(135deg,#2F8FFF,#8B5CF6);color:#fff;box-shadow:0 2px 14px rgba(139,92,246,.35)}
.btn-p:hover{background:#2563EB;box-shadow:0 4px 18px rgba(59,130,246,.4)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);border-color:rgba(59,130,246,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(59,130,246,.15)}
.btn-g:hover{background:rgba(59,130,246,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,.2)}
.btn-pur:hover{background:rgba(139,92,246,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(59,130,246,0.05);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(59,130,246,.45);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px rgba(59,130,246,.08)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(59,130,246,.15);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.2);color:var(--amber-t)}
/* ══════ پنل ساخت کانفیگ - طراحی جدید ══════ */
.create-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(59,130,246,.35)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(37,99,235,.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(59,130,246,.5);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(59,130,246,.18);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(59,130,246,.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(59,130,246,.35);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(59,130,246,.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
/* ══════ پنل اطلاعات سرور ══════ */
.srv-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(59,130,246,.35)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme="light"] .srv-tile{background:rgba(37,99,235,.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ══════ پنل تغییر رمز ══════ */
.pw-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(139,92,246,.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(139,92,246,.5);box-shadow:0 0 0 3px rgba(139,92,246,.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(139,92,246,.32);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(139,92,246,.42)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* ══════ اتصالات فعال - نسخه پیشرفته ══════ */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}

.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(139,92,246,.07);border:1px solid rgba(139,92,246,.2);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:#A78BFA;word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
/* ══════ گروه‌های ساب - ریدیزاین کامل ══════ */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:rgba(139,92,246,.5);box-shadow:0 0 0 3px rgba(139,92,246,.1)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(139,92,246,.14),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(139,92,246,.35)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(124,58,237,.03)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(139,92,246,.08);border:1px dashed rgba(139,92,246,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#A78BFA;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:#A78BFA;transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ══════ مودال ساخت گروه - نسخه فشرده ══════ */
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:linear-gradient(155deg,rgba(139,92,246,.14) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(139,92,246,.2),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(139,92,246,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .modal-v2-input{background:rgba(124,58,237,.04)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(139,92,246,.55);box-shadow:0 0 0 3px rgba(139,92,246,.12);background:rgba(0,0,0,.28)}
[data-theme="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(139,92,246,.4);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(139,92,246,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* ══════ مودال انتخاب کانفیگ - نسخه پیشرفته ══════ */
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(59,130,246,.35)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(59,130,246,.5);box-shadow:0 0 0 3px rgba(59,130,246,.1)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(59,130,246,.2)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}

.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(59,130,246,.1);border-color:rgba(59,130,246,.25)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(59,130,246,.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

/* ══════ کانفیگ‌ها - طراحی ردیفی حرفه‌ای ══════ */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(59,130,246,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(59,130,246,0.1);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#A78BFA}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}

@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}

/* ── زیر ۷۶۸px: تبدیل کامل به کارت موبایل ── */
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}

/* ══════ اتصالات فعال با IP ══════ */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}

/* ══════ لاگ فعالیت‌ها ══════ */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(59,130,246,.05);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(59,130,246,.05)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}

/* ═════ OMID-IRAN PANEL v1.0 — glassmorphism theme override ═════ */
:root{
 --bg:#040A12;--bg2:rgba(7,18,29,.82);--bg3:#0A2430;
 --card:rgba(8,25,38,.60);--card-b:rgba(69,199,232,.13);--card-bh:rgba(69,199,232,.30);
 --accent:#0B738D;--accent2:#49CFEF;--accent-d:rgba(11,115,141,.13);
 --green:#20C997;--green-bg:rgba(32,201,151,.10);--green-t:#5BE0B2;
 --red:#EF5B6B;--red-bg:rgba(239,91,107,.10);--red-t:#FF8D9A;
 --amber:#F5B84B;--amber-bg:rgba(245,184,75,.10);--amber-t:#FFD58A;
 --purple:#A36AF4;--purple-bg:rgba(163,106,244,.10);
 --t1:#ECF9FF;--t2:#95B6C6;--t3:#507183;
 --sidebar-w:264px;--radius:20px;--shadow:0 12px 40px rgba(0,0,0,.38)
}
body{background:radial-gradient(circle at 7% 8%,rgba(8,111,134,.13),transparent 26%),radial-gradient(circle at 95% 90%,rgba(30,74,95,.14),transparent 28%),#040A12}
body::before{content:"";position:fixed;inset:0;pointer-events:none;background:linear-gradient(120deg,transparent 0 38%,rgba(70,217,241,.025) 46%,transparent 58%),linear-gradient(rgba(71,206,235,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(71,206,235,.018) 1px,transparent 1px);background-size:auto,42px 42px,42px 42px;z-index:0}
.sidebar{background:linear-gradient(180deg,rgba(6,20,32,.90),rgba(4,12,21,.86));backdrop-filter:blur(22px);border-left-color:rgba(69,199,232,.18);box-shadow:-18px 0 55px rgba(0,0,0,.14)}
.logo{padding:22px 17px 18px;border-bottom-color:rgba(69,199,232,.14)}
.logo-img,.mob-logo{border-radius:13px;box-shadow:0 0 22px rgba(0,174,206,.24),0 0 12px rgba(255,0,177,.12)}
.logo-name{font-size:13px;letter-spacing:.03em}.logo-sub{color:#6E95A7}
.nav-sec{letter-spacing:.08em;color:#557B8D}
.nav-it{border-radius:12px;transition:all .18s ease;position:relative}
.nav-it:hover{background:rgba(49,171,198,.08);transform:translateX(-2px)}
.nav-it.on{background:linear-gradient(90deg,rgba(9,105,129,.23),rgba(9,105,129,.07));border-color:rgba(69,199,232,.20);box-shadow:inset 0 0 25px rgba(8,108,130,.06)}
.nav-it.on::before{background:linear-gradient(180deg,#45D2EE,#087991);box-shadow:0 0 12px rgba(69,210,238,.45)}
.theme-btn{background:rgba(10,89,109,.12);border-color:rgba(69,199,232,.14);color:#A8D4E1}.theme-btn:hover{background:rgba(10,110,133,.18)}
.main{position:relative;z-index:1}
.metric,.card,.create-panel,.vless-box,.modal,.modal-v2,.traf-chart-card,.traf-main-stat,.traf-mini{background:linear-gradient(145deg,rgba(10,29,43,.62),rgba(5,16,27,.56));backdrop-filter:blur(16px);border-color:rgba(69,199,232,.13);box-shadow:0 12px 30px rgba(0,0,0,.18)}
.metric:hover,.traf-mini:hover,.card:hover{border-color:rgba(69,199,232,.28);box-shadow:0 16px 38px rgba(0,0,0,.24)}
.tb-title i,.card-title i,.traf-chart-title i,.vl-title i{color:#43CDEB}
.btn-p{background:linear-gradient(135deg,#075F73,#0B97B5);box-shadow:0 8px 22px rgba(0,117,145,.22)}
.btn-p:hover{background:linear-gradient(135deg,#087A92,#11A7C1)}
.btn-g{background:rgba(8,105,128,.11);color:#63D8EF;border-color:rgba(69,199,232,.15)}
.btn-o{background:rgba(255,255,255,.015);border-color:rgba(69,199,232,.12)}
.btn-pur{background:rgba(139,86,223,.11);border-color:rgba(163,106,244,.18)}
.vless-box::before{background:radial-gradient(circle,rgba(11,115,141,.19),transparent 70%)}
.vl-code{color:#73DAF0;background:rgba(0,0,0,.25);border-color:rgba(69,199,232,.12)}
.badge.bg-blue{background:rgba(11,115,141,.15);color:#63D7EE}.bg-purple{background:rgba(163,106,244,.11);color:#BD91FF}
.cp-head-icon,.m-icon{box-shadow:0 0 20px rgba(11,115,141,.14)}
.modal-bg{backdrop-filter:blur(8px)}
/* medium motion */
.metric,.card,.btn,.nav-it,.traf-mini{transition-duration:.22s}
.lang-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:rgba(11,115,141,.12);border:1px solid rgba(69,199,232,.14);color:#8FE4F3;border-radius:10px;padding:8px 10px;font:600 11px Vazirmatn,sans-serif;cursor:pointer;transition:.18s;width:100%;margin-bottom:7px}.lang-btn:hover{background:rgba(11,115,141,.20);border-color:rgba(69,199,232,.25);transform:translateY(-1px)}.lang-wide{letter-spacing:.02em}.mob-right .lang-btn{width:auto;height:34px;margin:0;padding:0 9px;font-size:9.5px}body.ui-en .nav-it{font-size:0} body.ui-en .nav-it::after{font-size:12px} body.ui-en .nav-it[data-pg="overview"]::after{content:"Dashboard"} body.ui-en .nav-it[data-pg="links"]::after{content:"Configurations"} body.ui-en .nav-it[data-pg="subgroups"]::after{content:"Subscription Groups"} body.ui-en .nav-it[data-pg="subscriptions"]::after{content:"Subscriptions"} body.ui-en .nav-it[data-pg="traffic"]::after{content:"Traffic"} body.ui-en .nav-it[data-pg="connections"]::after{content:"Connections"} body.ui-en .nav-it[data-pg="security"]::after{content:"Security"} body.ui-en .nav-it[data-pg="logs"]::after{content:"Activity Logs"} body.ui-en .nav-it[data-pg="errors"]::after{content:"Errors"} body.ui-en .nav-it[data-pg="testws"]::after{content:"WebSocket Test"} body.ui-en .nav-it[data-pg="settings"]::after{content:"Settings"} body.ui-en .nav-it[data-pg="support"]::after{content:"Support"} body.ui-en .nav-sec{font-size:0} body.ui-en .nav-sec:first-child::after{content:"PANEL";font-size:10px} body.ui-en .nav-sec:nth-of-type(2)::after{content:"SYSTEM";font-size:10px}

/* ═══════════════════════════════════════════════════════════════════════
   OMID-IRAN PANEL · GAMING ENGINEERING HUD
   Glass surfaces + cockpit layout + teal/cyan telemetry
   ═══════════════════════════════════════════════════════════════════════ */
:root{
  --bg:#02070c;--bg2:rgba(4,13,20,.86);--bg3:#071722;
  --card:rgba(6,20,30,.68);--card-b:rgba(56,211,229,.14);--card-bh:rgba(56,211,229,.34);
  --accent:#0BA7C4;--accent2:#56E7FF;--accent-d:rgba(11,167,196,.13);
  --green:#26E6A3;--green-bg:rgba(38,230,163,.10);--green-t:#6DFFC3;
  --red:#FF5D70;--red-bg:rgba(255,93,112,.10);--red-t:#FF9AA8;
  --amber:#FFB84D;--amber-bg:rgba(255,184,77,.10);--amber-t:#FFD892;
  --purple:#B277FF;--purple-bg:rgba(178,119,255,.10);
  --t1:#E8FBFF;--t2:#8DB8C7;--t3:#4C7381;
  --sidebar-w:286px;--radius:22px;--shadow:0 18px 60px rgba(0,0,0,.38);
}
html,body{background:#02070c;overflow-x:hidden}
body{background:
 radial-gradient(900px 520px at 8% 0%,rgba(0,174,204,.11),transparent 62%),
 radial-gradient(700px 500px at 92% 88%,rgba(25,76,100,.13),transparent 64%),
 #02070c;letter-spacing:.01em}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.48;background-image:linear-gradient(rgba(84,227,246,.033) 1px,transparent 1px),linear-gradient(90deg,rgba(84,227,246,.025) 1px,transparent 1px);background-size:38px 38px;mask-image:linear-gradient(to bottom,black,transparent 85%)}
body::before{content:"";position:fixed;left:0;right:0;top:82px;height:1px;background:linear-gradient(90deg,transparent,rgba(83,228,249,.35),transparent);box-shadow:0 0 18px rgba(83,228,249,.18);z-index:0;pointer-events:none}
.sidebar{left:0;right:auto;width:var(--sidebar-w);border-left:0;border-right:1px solid rgba(67,211,231,.16);background:linear-gradient(180deg,rgba(4,17,25,.93),rgba(2,9,15,.94));backdrop-filter:blur(28px);box-shadow:18px 0 60px rgba(0,0,0,.26)}
.logo{padding:21px 18px 17px;border-bottom:1px solid rgba(71,209,232,.12);gap:13px}
.logo-img,.mob-logo{border-radius:16px;border:1px solid rgba(86,231,255,.20);box-shadow:0 0 26px rgba(11,167,196,.24),0 0 8px rgba(178,119,255,.10);background:#031017}
.logo-name{font-size:13px;font-weight:900;letter-spacing:.035em;color:#E9FCFF}.logo-sub{color:#67ACBE;font-size:10px}.logo-meta{font-size:8px;color:#3E6775;margin-top:4px;letter-spacing:.12em;font-weight:700}
.nav-wrap{padding:10px 8px 12px}.nav-sec{padding:15px 12px 7px;color:#3E6978;letter-spacing:.18em;font-size:9px}.nav-it{border-left:2px solid transparent;border-right:0;border-radius:13px;margin:3px 4px;padding:10px 12px;color:#607F8C;position:relative;overflow:hidden;transition:.18s}.nav-it::after{transition:.18s}.nav-it:hover{background:linear-gradient(90deg,rgba(13,147,174,.12),rgba(13,147,174,.03));color:#B9E8F1;transform:translateX(3px)}.nav-it.on{background:linear-gradient(90deg,rgba(9,154,182,.20),rgba(9,154,182,.035));color:#E6FBFF;border-left-color:#4DE5FB;box-shadow:inset 0 0 30px rgba(11,167,196,.06),0 0 24px rgba(11,167,196,.05)}.nav-it.on::before{content:"";position:absolute;left:0;top:7px;bottom:7px;width:3px;background:linear-gradient(180deg,#73F1FF,#0787A4);border-radius:0 6px 6px 0;box-shadow:0 0 14px rgba(86,231,255,.60)}.nav-it i{color:#4C8290}.nav-it.on i{color:#62E9FF}.nav-badge{margin-right:auto;background:rgba(77,229,251,.09);border:1px solid rgba(77,229,251,.09);color:#64DCEC;padding:2px 7px}
.side-telemetry{margin:13px 12px 2px;padding:12px;border:1px solid rgba(67,211,231,.11);border-radius:15px;background:linear-gradient(135deg,rgba(9,43,55,.50),rgba(3,16,24,.34));box-shadow:inset 0 0 25px rgba(11,167,196,.035)}.telemetry-head{display:flex;justify-content:space-between;align-items:center;font-size:8px;color:#3F7786;letter-spacing:.16em;font-weight:800;margin-bottom:9px}.telemetry-led{width:6px;height:6px;border-radius:50%;background:#35E5AA;box-shadow:0 0 10px #35E5AA}.telemetry-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}.telemetry-grid div{display:flex;flex-direction:column;gap:2px}.telemetry-grid span{font-size:7px;color:#426A77;letter-spacing:.11em}.telemetry-grid b{font-size:9px;color:#9FD0DC;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sb-foot{padding:13px 14px;border-top:1px solid rgba(67,211,231,.10);background:linear-gradient(180deg,transparent,rgba(4,18,26,.38))}.side-lang,.theme-btn,.logout-btn{border-radius:12px}.side-lang{display:flex;align-items:center;justify-content:center;gap:7px;background:rgba(11,167,196,.07);border:1px solid rgba(76,216,235,.13);color:#79D8E8;padding:9px;font:700 11px Vazirmatn,sans-serif;cursor:pointer;width:100%;margin-bottom:7px;transition:.18s}.side-lang:hover{background:rgba(11,167,196,.13);transform:translateY(-1px)}
.theme-btn{background:rgba(10,84,102,.10);border-color:rgba(67,211,231,.10);color:#8DB8C7}.logout-btn{background:rgba(255,93,112,.07);border-color:rgba(255,93,112,.14);color:#FF9BAA}
.mob-top{display:flex;position:fixed;top:0;left:0;right:0;height:68px;background:linear-gradient(180deg,rgba(3,11,17,.92),rgba(3,11,17,.75));border-bottom:1px solid rgba(67,211,231,.11);backdrop-filter:blur(24px);z-index:150;align-items:center;justify-content:space-between;padding:0 18px 0 calc(var(--sidebar-w) + 18px);box-shadow:0 10px 35px rgba(0,0,0,.14)}
.mob-top .ml{display:flex;align-items:center;gap:11px}.mob-logo{width:34px;height:34px}.mob-brand-copy{display:flex;flex-direction:column;gap:1px}.mob-title{color:#E9FCFF;font-size:13px;font-weight:900;letter-spacing:.04em}.mob-subtitle{color:#4C8190;font-size:8.5px;letter-spacing:.10em;text-transform:uppercase;font-weight:700}.mob-right{display:flex;align-items:center;gap:8px}.top-status{display:inline-flex;align-items:center;gap:6px;color:#64C4D4;font-size:8px;font-weight:800;letter-spacing:.10em;padding:7px 10px;border:1px solid rgba(39,230,163,.11);background:rgba(39,230,163,.05);border-radius:999px}.mob-right .lang-btn{width:auto;height:36px;margin:0;padding:0 12px;border-radius:10px;background:rgba(11,167,196,.08);border-color:rgba(77,229,251,.16);color:#7CE6F4}.theme-mob{border-radius:10px;border-color:rgba(77,229,251,.12);background:rgba(11,167,196,.07);color:#75D8E8}.menu-btn{display:none}
.main{margin-right:0;margin-left:var(--sidebar-w);padding:98px 28px 60px;position:relative;z-index:1}
.topbar{margin-bottom:24px}.tb-title{font-size:20px;font-weight:850;letter-spacing:-.025em}.tb-sub{color:#4D7B88}.tb-title i{color:#51E2F8;text-shadow:0 0 14px rgba(81,226,248,.35)}
.metric,.card,.create-panel,.vless-box,.modal,.modal-v2,.traf-chart-card,.traf-main-stat,.traf-mini{background:linear-gradient(145deg,rgba(7,29,40,.69),rgba(3,15,23,.56));border:1px solid rgba(75,213,234,.13);backdrop-filter:blur(20px);box-shadow:0 16px 42px rgba(0,0,0,.18),inset 0 1px 0 rgba(255,255,255,.025)}
.metric{border-radius:20px;padding:18px;min-height:145px}.metric:hover{transform:translateY(-4px);border-color:rgba(87,227,247,.28);box-shadow:0 18px 48px rgba(0,0,0,.28),0 0 28px rgba(11,167,196,.06)}.metric::after{width:2px;background:linear-gradient(180deg,#62E9FF,#08768E);opacity:1;height:45%;top:18px;border-radius:2px}
.m-icon{border-radius:11px;background:rgba(11,167,196,.08);color:#58DDEF;box-shadow:0 0 24px rgba(11,167,196,.10)}.m-label{color:#557D89}.m-val{font-size:30px;font-weight:900}.m-sub{color:#466C79}
.vless-box{border-radius:22px;padding:22px 24px}.vl-code{background:rgba(0,5,9,.38);border-color:rgba(83,222,242,.14);color:#72E9FF;box-shadow:inset 0 0 30px rgba(0,0,0,.18)}.vl-title{color:#9ECFD9}.btn-p{background:linear-gradient(135deg,#07667B,#0A9FB8 58%,#116F99);border:1px solid rgba(95,232,251,.18);box-shadow:0 10px 26px rgba(0,127,154,.18)}.btn-p:hover{filter:brightness(1.08);transform:translateY(-1px)}.btn-g{background:rgba(12,145,169,.10);border-color:rgba(83,222,242,.14);color:#72DDEB}.btn-o{background:rgba(255,255,255,.018);border-color:rgba(83,222,242,.10)}.btn-pur{background:rgba(167,105,241,.10);border-color:rgba(178,119,255,.17)}
.cfg-card,.conn-card{background:linear-gradient(145deg,rgba(6,23,33,.74),rgba(3,12,19,.64));border-color:rgba(75,213,234,.12);border-radius:18px}.cfg-card:hover,.conn-card:hover{border-color:rgba(80,227,247,.27);transform:translateY(-2px);box-shadow:0 15px 35px rgba(0,0,0,.20)}
.modal-bg{background:rgba(0,5,9,.72);backdrop-filter:blur(14px)}.modal,.modal-v2{border-color:rgba(83,222,242,.16);box-shadow:0 30px 90px rgba(0,0,0,.50),0 0 60px rgba(11,167,196,.07)}
.toast{backdrop-filter:blur(20px);border-color:rgba(83,222,242,.16);box-shadow:0 16px 50px rgba(0,0,0,.36)}
/* responsive cockpit */
@media(max-width:1050px){.sidebar{right:auto;left:0;transform:translateX(-105%)}.sidebar.open{transform:translateX(0);box-shadow:18px 0 55px rgba(0,0,0,.55)}.sb-close{display:flex;right:12px;left:auto}.main{margin-left:0;padding-top:86px}.mob-top{padding:0 14px}.menu-btn{display:flex}}
@media(max-width:560px){.top-status{display:none}.mob-top{height:62px}.main{padding:78px 12px 44px}.tb-title{font-size:17px}.metrics{grid-template-columns:1fr 1fr!important;gap:9px}.metric{min-height:125px;padding:14px}.m-val{font-size:24px}}
@media(max-width:390px){.metrics{grid-template-columns:1fr!important}}
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
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">Close / بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> Save / ذخیره</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت New Group / گروه جدید</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">Cancel / انصراف</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> ساخت گروه</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> Edit Configuration / ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
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
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">Cancel / انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> Save Changes / ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div>
    <div class="mob-brand-copy"><span class="mob-title">OMID-IRAN PANEL</span><span class="mob-subtitle">Free For All · v1.0</span></div>
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
    <div><div class="logo-name">OMID-IRAN PANEL</div><div class="logo-sub">Free For All · v1.0</div><div class="logo-meta">OMID NETWORK NODE</div></div>
  </div>
  <div class="side-telemetry">
    <div class="telemetry-head"><span>CORE TELEMETRY</span><span class="telemetry-led"></span></div>
    <div class="telemetry-grid">
      <div><span>NODE</span><b>OMID-01</b></div>
      <div><span>ENGINE</span><b>VLESS / XHTTP</b></div>
    </div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">PANEL / پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">SYSTEM / سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</div>
  </div>
  <div class="sb-foot">
    <button class="side-lang" onclick="toggleUiLang()"><i class="ti ti-language"></i><span id="side-lang-label">FA / EN · دو زبانه</span></button>
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>
    
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> Logout / خروج</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> Dashboard / داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh / رفرش</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> Copy / کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · 3 mode</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">OMID-IRAN PANEL v1.0 · OMID Network · Railway</span>
    
    
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">Create Configuration / ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
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
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> پورت اتصال</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر هم‌زمان</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> New Group / گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک New Group / گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی (هر کانفیگ)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون <i class="ti ti-rss"></i> کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">شامل تمام کانفیگ‌های فعال.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک سابسکریپشن گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh / رفرش</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> Refresh / رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">Live Connections / اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth سخت‌گیرانه</span><span class="sr-v" style="color:var(--green-t)">● فعال v9</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کانفیگ</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک ساب</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت پیش‌فرض</div><div class="srv-tile-val">443 (TLS) · قابل تغییر در هر کانفیگ</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v1.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>
<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div></div></div>
  <div class="srv-panel">
    <div class="srv-hero">
      <div class="srv-hero-icon"><i class="ti ti-headset"></i></div>
      <div class="srv-hero-text">
        <div class="srv-hero-domain">Support / پشتیبانی</div>
        <div class="srv-hero-sub"><span class="dot dg pulse"></span> راه‌های ارتباطی</div>
      </div>
    </div>
    <div class="srv-tiles">
      <a class="srv-tile" href="https://t.me/omid_gamingORG" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-speakerphone"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">کانال تلگرام</div><div class="srv-tile-val">t.me/omid_gamingORG</div></div>
      </a>
      <a class="srv-tile" href="https://github.com/omidseifi88/omidiran" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-brand-github"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">گیت‌هاب</div><div class="srv-tile-val">github.com/omidseifi88/omidiran</div></div>
      </a>
    </div>
  </div>
</section>
</main>
<script>
let uiLang=localStorage.getItem('omid-lang')||'both';
function toggleUiLang(){uiLang=uiLang==='both'?'en':uiLang==='en'?'fa':'both';localStorage.setItem('omid-lang',uiLang);applyUiLang();}
function applyUiLang(){
  const b=document.body; b.dataset.uiLang=uiLang;
  const btn=document.getElementById('lang-btn'), mb=document.getElementById('lang-mob-btn');
  const label=uiLang==='both'?'FA / EN · دو زبانه':uiLang==='en'?'EN · English':'FA · فارسی';
  if(btn)btn.textContent=label; if(mb)mb.textContent=uiLang==='both'?'FA / EN':uiLang==='en'?'EN':'FA'; const side=document.getElementById('side-lang-label'); if(side) side.textContent=label;
  b.classList.toggle('ui-en',uiLang==='en'); b.classList.toggle('ui-fa',uiLang==='fa');
}
let isDark=localStorage.getItem('gateway-theme')!=='light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';
  document.getElementById('theme-icon').className='ti '+icon;
  document.getElementById('theme-label').textContent=label;
  const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('gateway-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
applyUiLang();
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-ultra']};
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
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
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
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
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
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
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
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
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
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
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
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
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
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
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
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
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
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک New Group / گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'رمزدار':'پابلیک'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','ok'))" title="کپی"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button>
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
  const name=document.getElementById('ns-name').value.trim()||'New Group / گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
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
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
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
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
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
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
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
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#A78BFA">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'· 🔒 رمزدار':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-globe"></i> پابلیک</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}
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
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
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
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">Traffic / ترافیک</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">مدت اتصال</div>
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
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}
async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}
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
  const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
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
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(59,130,246,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#3B82F6',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#3B82F6',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
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
      {label:'مصرف',data:[],borderColor:'#3B82F6',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#3B82F6',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
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
        y:{grid:{color:'rgba(59,130,246,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#3B82F6','#10B981','#8B5CF6'],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#0d1b2e',
      borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'72%',
      plugins:{
        legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  document.getElementById('sub-all-url')&&(document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all');
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});
</script>
</body></html>"""


# جایگزینی نهایی لوگو در صفحات استاتیک (LOGIN_HTML / DASHBOARD_HTML)
LOGIN_HTML = LOGIN_HTML.replace("__LOGO_B64__", LOGO_B64)
DASHBOARD_HTML = DASHBOARD_HTML.replace("__LOGO_B64__", LOGO_B64)

def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v3 — طراحی حرفه‌ای‌تر: لینک کانفیگ پنهان با دکمه نمایش، صفحه‌ی رمز با طراحی ویژه"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>OMID Network · Subscription</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#060a14;--bg2:#0a1020;--bg3:#0d1428;
  --card:#0c1326;--card-b:rgba(96,148,246,0.12);--card-bh:rgba(96,148,246,0.28);
  --accent:#3B7CF6;--accent2:#6EA3FF;--accent-d:rgba(59,124,246,0.1);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.1);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.1);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.1);--purple-t:#BCA4F7;
  --t1:#EFF4FF;--t2:#8AA0C4;--t3:#48577A;
  --radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="light"]{{
  --bg:#F0F3FA;--bg2:#E5ECF8;--bg3:#D9E3F4;
  --card:#FFFFFF;--card-b:rgba(59,124,246,0.14);--card-bh:rgba(59,124,246,0.32);
  --accent:#2E63D6;--accent2:#1E4CB8;--accent-d:rgba(46,99,214,0.08);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.08);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.08);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.08);--purple-t:#5A3CAD;
  --t1:#101A30;--t2:#48577A;--t3:#8694B0;
  --shadow:0 12px 36px rgba(20,40,90,0.12);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(59,124,246,0.13),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(96,148,246,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(96,148,246,0.025) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(139,92,246,.3),0 0 8px rgba(59,130,246,.25);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,124,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,var(--accent) 0%,#2952C8 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(59,124,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#1D4ED8;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}

.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}

/* ── کارت کانفیگ به‌شکل بلیط دسترسی (signature element) ── */
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(96,148,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}

/* خط جداکننده‌ی بلیطی با دندانه‌های گرد، شبیه پاره‌خط بُرد بلیط */
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}

.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(46,99,214,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#2F8FFF,#8B5CF6);color:#fff;box-shadow:0 3px 14px rgba(139,92,246,.35)}}
.btn-p:hover{{background:var(--accent2)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(96,148,246,.16)}}
.btn-g:hover{{background:rgba(96,148,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

/* ── صفحه‌ی قفل / رمز ── */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,124,246,.16),rgba(59,124,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(46,99,214,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}

@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:19px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:32px 22px 22px}}
  .lock-form{{padding:20px 22px 26px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* OMID Network public subscription branding */
:root{{--accent:#0B7289;--accent2:#52D6EF;--accent-d:rgba(11,114,137,.12);--card-b:rgba(82,214,239,.14);--card-bh:rgba(82,214,239,.30)}}
body{{background:radial-gradient(circle at 18% 7%,rgba(11,114,137,.15),transparent 30%),radial-gradient(circle at 85% 90%,rgba(30,70,92,.18),transparent 32%),var(--bg)}}
.brand-img{{border-radius:13px;box-shadow:0 0 22px rgba(0,174,206,.24),0 0 10px rgba(255,0,177,.12)}}
.sub-info,.stat-card,.cfg-card,.lock-card,.qr-box{{background:linear-gradient(145deg,rgba(10,28,43,.68),rgba(6,15,25,.60));backdrop-filter:blur(16px);border-color:rgba(82,214,239,.14)}}
.copy-all-bar{{background:linear-gradient(120deg,#075E73 0%,#0B879F 55%,#1D5A83 100%);box-shadow:0 10px 30px rgba(6,124,147,.24)}}
.btn-p{{background:linear-gradient(135deg,#075E73,#0C9BB7);box-shadow:0 5px 18px rgba(6,124,147,.22)}}
.btn-g{{background:rgba(8,110,134,.12);color:#6BDCF2;border-color:rgba(82,214,239,.16)}}
.footer{{letter-spacing:.02em}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> Close / بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><img src="data:image/png;base64,{LOGO_B64}" alt="OMID"></div>
      <div><div class="brand-name">OMID-IRAN PANEL</div><div class="brand-sub">OMID · v1.0</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="pub-lang" onclick="togglePubLang()" title="Language / زبان">FA / EN</button>
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="Theme / تم"><i class="ti ti-sun" id="theme-icon"></i></button>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">OMID Network · OMID-IRAN PANEL v1.0 · Free For All</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let pubLang=localStorage.getItem('omid-pub-lang')||'both';
function togglePubLang(){{pubLang=pubLang==='both'?'en':pubLang==='en'?'fa':'both';localStorage.setItem('omid-pub-lang',pubLang);document.getElementById('pub-lang').textContent=pubLang==='both'?'FA / EN':pubLang==='en'?'EN':'FA';document.body.dataset.uiLang=pubLang;}}
let isDark=localStorage.getItem('gateway-pub-theme')!=='light';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('gateway-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);
togglePubLang();

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._subUrl  = subUrl;
  window._subName = d.name;
  window._links   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._subUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._subName + ' — کل گروه', window._subUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> Copy all configurations / کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Live Connections / اتصالات زنده</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Total Usage / کل مصرف</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-sub">همه کانفیگ‌ها</div>
      </div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> Configurations / کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._links[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._links[${{i}}].label, window._links[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._links||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
