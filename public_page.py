# public_page.py
# صفحه‌ی پابلیک ساب — UI مدرن اپ‌مانند
# از pages.py جدا شده برای نگهداری بهتر

from pages import LOGO_B64

# ═══════════════════════════════════════════════════════════════════════
# Public subscription page — Modern App-like UI v4
# Features: bottom nav, theme switcher, smart import, offline cache
# ═══════════════════════════════════════════════════════════════════════
PUBLIC_PAGE_HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark" data-lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="theme-color" content="#060a14" id="meta-theme">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>OMID Network · Subscription</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
/* ═══════════════════════════════════════════════════════════════════════
   DESIGN TOKENS
   ═══════════════════════════════════════════════════════════════════════ */
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#060a14;
  --bg2:#0a1020;
  --card:rgba(12,19,38,.85);
  --card-solid:#0c1326;
  --card-b:rgba(96,148,246,.14);
  --card-bh:rgba(96,148,246,.32);
  --accent:#3B7CF6;
  --accent2:#6EA3FF;
  --accent-d:rgba(59,124,246,.12);
  --green:#22C55E;
  --green-bg:rgba(34,197,94,.12);
  --green-t:#4ADE80;
  --red:#EF4444;
  --red-bg:rgba(239,68,68,.12);
  --red-t:#F87171;
  --amber:#F59E0B;
  --amber-bg:rgba(245,158,11,.12);
  --amber-t:#FBBF24;
  --purple:#A78BFA;
  --purple-bg:rgba(167,139,250,.12);
  --t1:#EFF4FF;
  --t2:#8AA0C4;
  --t3:#4D5F84;
  --glass:rgba(12,19,38,.7);
  --header-h:60px;
  --nav-h:64px;
  --radius:20px;
  --radius-sm:14px;
  --shadow:0 8px 32px rgba(0,0,0,.4);
  --safe-top:env(safe-area-inset-top,0px);
  --safe-bottom:env(safe-area-inset-bottom,0px);
}
html[data-theme="light"]{
  --bg:#EFF3FA;
  --bg2:#E5ECF8;
  --card:rgba(255,255,255,.9);
  --card-solid:#FFFFFF;
  --card-b:rgba(59,124,246,.16);
  --card-bh:rgba(59,124,246,.36);
  --accent:#2E63D6;
  --accent2:#1E4CB8;
  --accent-d:rgba(46,99,214,.08);
  --green:#059669;
  --green-bg:rgba(5,150,105,.1);
  --green-t:#047857;
  --red:#DC2626;
  --red-bg:rgba(220,38,38,.08);
  --red-t:#B42333;
  --amber:#D97706;
  --amber-bg:rgba(217,119,6,.1);
  --amber-t:#A15C00;
  --purple:#7C3AED;
  --purple-bg:rgba(124,58,237,.08);
  --t1:#0F172A;
  --t2:#3E5170;
  --t3:#7A8AA8;
  --glass:rgba(255,255,255,.85);
  --shadow:0 8px 32px rgba(20,40,90,.12);
}
html,body{height:100%;overflow-x:hidden}
body{
  font-family:'Vazirmatn',sans-serif;
  background:var(--bg);
  color:var(--t1);
  font-size:14px;
  line-height:1.5;
  transition:background .3s,color .3s;
  overscroll-behavior-y:none;
  -webkit-font-smoothing:antialiased;
}
body::before{
  content:"";
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 50% at 50% -10%,rgba(59,124,246,.18),transparent 60%),
    radial-gradient(ellipse 60% 40% at 90% 110%,rgba(167,139,250,.1),transparent 60%);
}
html[data-theme="light"] body::before{
  background:
    radial-gradient(ellipse 80% 50% at 50% -10%,rgba(46,99,214,.08),transparent 60%),
    radial-gradient(ellipse 60% 40% at 90% 110%,rgba(124,58,237,.06),transparent 60%);
}
::-webkit-scrollbar{width:0;height:0}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input{font-family:inherit}

/* ═══════════════════════════════════════════════════════════════════════
   HEADER
   ═══════════════════════════════════════════════════════════════════════ */
.app-header{
  position:fixed;top:0;left:0;right:0;z-index:100;
  padding-top:var(--safe-top);
  height:calc(var(--header-h) + var(--safe-top));
  background:var(--glass);
  backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--card-b);
  display:flex;align-items:center;justify-content:space-between;
  padding-left:16px;padding-right:16px;
  transition:background .3s,border-color .3s;
}
.brand{display:flex;align-items:center;gap:10px;min-width:0}
.brand-logo{
  width:36px;height:36px;border-radius:10px;overflow:hidden;
  flex-shrink:0;
  box-shadow:0 0 18px rgba(59,124,246,.25);
  border:1px solid var(--card-b);
}
.brand-logo img{width:100%;height:100%;object-fit:cover}
.brand-text{min-width:0}
.brand-name{font-size:13.5px;font-weight:800;letter-spacing:-.01em;color:var(--t1);white-space:nowrap}
.brand-sub{font-size:9.5px;color:var(--t3);margin-top:1px;white-space:nowrap}
.header-actions{display:flex;align-items:center;gap:6px}
.icon-btn{
  width:36px;height:36px;border-radius:11px;
  background:var(--card);border:1px solid var(--card-b);
  color:var(--t2);display:flex;align-items:center;justify-content:center;
  font-size:16px;transition:.18s;
}
.icon-btn:active{transform:scale(.92);background:var(--accent-d);color:var(--accent2)}
.status-pill{
  display:inline-flex;align-items:center;gap:5px;
  font-size:9.5px;font-weight:700;color:var(--green-t);
  background:var(--green-bg);padding:4px 9px;border-radius:20px;
  border:1px solid rgba(34,197,94,.2);
}
.status-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 2s infinite}

/* ═══════════════════════════════════════════════════════════════════════
   MAIN CONTENT AREA
   ═══════════════════════════════════════════════════════════════════════ */
.app-main{
  position:relative;z-index:1;
  padding-top:calc(var(--header-h) + var(--safe-top) + 12px);
  padding-bottom:calc(var(--nav-h) + var(--safe-bottom) + 20px);
  padding-left:14px;padding-right:14px;
  min-height:100vh;
  max-width:640px;margin:0 auto;
}
.tab-panel{display:none;animation:fadeUp .3s ease}
.tab-panel.active{display:block}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* ═══════════════════════════════════════════════════════════════════════
   HERO CARD
   ═══════════════════════════════════════════════════════════════════════ */
.hero{
  position:relative;overflow:hidden;
  background:linear-gradient(155deg,rgba(59,124,246,.14) 0%,var(--card) 55%);
  border:1px solid var(--card-b);
  border-radius:24px;padding:22px 20px;
  margin-bottom:14px;
  box-shadow:var(--shadow);
}
.hero::before{
  content:"";position:absolute;top:-80px;right:-80px;width:220px;height:220px;
  background:radial-gradient(circle,rgba(59,124,246,.25),transparent 70%);
  pointer-events:none;
}
.hero::after{
  content:"";position:absolute;bottom:-60px;left:-60px;width:180px;height:180px;
  background:radial-gradient(circle,rgba(167,139,250,.15),transparent 70%);
  pointer-events:none;
}
.hero-head{display:flex;align-items:flex-start;justify-content:space-between;gap:10px;position:relative;z-index:1}
.hero-title{font-size:22px;font-weight:800;letter-spacing:-.02em;margin-bottom:4px;word-break:break-word}
.hero-desc{font-size:12px;color:var(--t2);line-height:1.7;margin-bottom:14px}
.hero-badge{
  display:inline-flex;align-items:center;gap:5px;
  padding:5px 11px;border-radius:20px;font-size:10.5px;font-weight:700;
  background:var(--green-bg);color:var(--green-t);
}
.hero-stats{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px;position:relative;z-index:1}
.hero-stat{
  background:rgba(0,0,0,.15);
  border:1px solid var(--card-b);border-radius:14px;
  padding:12px 14px;
}
html[data-theme="light"] .hero-stat{background:rgba(59,124,246,.04)}
.hero-stat-label{
  font-size:9.5px;color:var(--t3);font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px;
  display:flex;align-items:center;gap:5px;
}
.hero-stat-label i{font-size:12px;color:var(--accent)}
.hero-stat-val{font-size:18px;font-weight:800;letter-spacing:-.02em}
.hero-stat-sub{font-size:10px;color:var(--t3);margin-top:2px}

/* Usage progress bar */
.usage-bar{
  margin-top:16px;position:relative;z-index:1;
}
.usage-track{
  height:8px;border-radius:6px;background:rgba(0,0,0,.2);
  overflow:hidden;margin-bottom:8px;
}
html[data-theme="light"] .usage-track{background:rgba(59,124,246,.08)}
.usage-fill{
  height:100%;border-radius:6px;
  background:linear-gradient(90deg,var(--green) 0%,var(--accent) 100%);
  transition:width .6s cubic-bezier(.34,1.56,.64,1);
  position:relative;overflow:hidden;
}
.usage-fill::after{
  content:"";position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.3),transparent);
  animation:shimmer 2.2s linear infinite;
}
@keyframes shimmer{0%{transform:translateX(-100%)}100%{transform:translateX(220%)}}
.usage-labels{display:flex;justify-content:space-between;font-size:10.5px;color:var(--t3)}

/* ═══════════════════════════════════════════════════════════════════════
   QUICK ACTIONS
   ═══════════════════════════════════════════════════════════════════════ */
.quick-actions{
  display:grid;grid-template-columns:repeat(2,1fr);gap:10px;
  margin-bottom:14px;
}
.action-btn{
  display:flex;align-items:center;gap:10px;
  background:var(--card);border:1px solid var(--card-b);
  border-radius:16px;padding:14px 16px;
  color:var(--t1);font-size:12.5px;font-weight:700;
  transition:.18s;
  text-align:right;
}
.action-btn:active{transform:scale(.97);background:var(--accent-d)}
.action-btn i{
  width:34px;height:34px;border-radius:10px;
  background:var(--accent-d);color:var(--accent2);
  display:flex;align-items:center;justify-content:center;
  font-size:17px;flex-shrink:0;
}
.action-btn.primary{
  background:linear-gradient(135deg,var(--accent) 0%,var(--purple) 100%);
  border:none;color:#fff;
}
.action-btn.primary i{background:rgba(255,255,255,.2);color:#fff}
.action-btn.primary:active{transform:scale(.97);filter:brightness(1.1)}

/* ═══════════════════════════════════════════════════════════════════════
   SECTION
   ═══════════════════════════════════════════════════════════════════════ */
.section-title{
  display:flex;align-items:center;gap:8px;
  font-size:12px;font-weight:800;color:var(--t2);
  text-transform:uppercase;letter-spacing:.08em;
  margin:20px 4px 12px;
}
.section-title i{font-size:15px;color:var(--accent)}
.section-count{
  margin-inline-start:auto;font-size:10.5px;font-weight:700;
  color:var(--accent2);background:var(--accent-d);
  padding:3px 9px;border-radius:20px;
}

/* ═══════════════════════════════════════════════════════════════════════
   CONFIG CARDS
   ═══════════════════════════════════════════════════════════════════════ */
.cfg-list{display:flex;flex-direction:column;gap:11px}
.cfg-card{
  background:var(--card);border:1px solid var(--card-b);
  border-radius:18px;overflow:hidden;
  transition:.2s;position:relative;
}
.cfg-card.off{opacity:.55}
.cfg-card.exp{border-color:rgba(245,158,11,.3)}
.cfg-card:active{transform:scale(.995)}
.cfg-top{
  padding:15px 17px 13px;
  display:flex;align-items:flex-start;gap:12px;
  position:relative;
}
.cfg-top::before{
  content:"";position:absolute;top:14px;bottom:14px;inset-inline-start:0;
  width:3px;border-radius:3px;background:var(--green);
}
.cfg-card.off .cfg-top::before{background:var(--red)}
.cfg-card.exp .cfg-top::before{background:var(--amber)}
.cfg-icon{
  width:40px;height:40px;border-radius:12px;
  background:var(--accent-d);color:var(--accent2);
  display:flex;align-items:center;justify-content:center;
  font-size:19px;flex-shrink:0;
}
.cfg-info{flex:1;min-width:0}
.cfg-label{font-size:14px;font-weight:800;color:var(--t1);margin-bottom:5px;word-break:break-word}
.cfg-badges{display:flex;flex-wrap:wrap;gap:5px}
.chip{
  font-size:9.5px;font-weight:700;padding:3px 8px;
  border-radius:7px;letter-spacing:.02em;white-space:nowrap;
}
.chip.ws{background:var(--accent-d);color:var(--accent2)}
.chip.xhttp{background:var(--purple-bg);color:var(--purple)}
.chip.green{background:var(--green-bg);color:var(--green-t)}
.chip.red{background:var(--red-bg);color:var(--red-t)}
.chip.amber{background:var(--amber-bg);color:var(--amber-t)}
.cfg-usage{margin-top:11px}
.cfg-usage .usage-track{height:5px;margin-bottom:5px}
.cfg-usage .usage-fill{background:linear-gradient(90deg,var(--accent),var(--accent2))}
.cfg-usage-labels{display:flex;justify-content:space-between;font-size:10px;color:var(--t3)}
.cfg-actions{
  display:flex;gap:6px;padding:10px 12px 12px;
  border-top:1px solid var(--card-b);
  background:rgba(0,0,0,.1);
}
html[data-theme="light"] .cfg-actions{background:rgba(59,124,246,.02)}
.cfg-btn{
  flex:1;display:flex;align-items:center;justify-content:center;gap:6px;
  padding:10px 8px;border-radius:12px;
  font-size:11.5px;font-weight:700;
  background:var(--accent-d);color:var(--accent2);
  border:1px solid var(--card-b);transition:.15s;
}
.cfg-btn:active{transform:scale(.96);background:rgba(59,124,246,.22)}
.cfg-btn i{font-size:14px}
.cfg-btn.primary{
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff;border:none;
}

/* ═══════════════════════════════════════════════════════════════════════
   BOTTOM NAV
   ═══════════════════════════════════════════════════════════════════════ */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;z-index:100;
  height:calc(var(--nav-h) + var(--safe-bottom));
  padding-bottom:var(--safe-bottom);
  background:var(--glass);
  backdrop-filter:blur(24px);
  -webkit-backdrop-filter:blur(24px);
  border-top:1px solid var(--card-b);
  display:flex;align-items:stretch;
  max-width:640px;margin:0 auto;
  transition:background .3s,border-color .3s;
}
.nav-item{
  flex:1;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:3px;
  color:var(--t3);font-size:9.5px;font-weight:700;
  transition:.2s;position:relative;
}
.nav-item i{font-size:22px;transition:.2s}
.nav-item:active{transform:scale(.92)}
.nav-item.active{color:var(--accent2)}
.nav-item.active i{
  filter:drop-shadow(0 0 8px var(--accent2));
  transform:translateY(-1px);
}
.nav-item.active::before{
  content:"";position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:36px;height:3px;border-radius:0 0 3px 3px;
  background:linear-gradient(90deg,var(--accent),var(--purple));
  box-shadow:0 0 12px var(--accent);
}

/* ═══════════════════════════════════════════════════════════════════════
   LOCK SCREEN
   ═══════════════════════════════════════════════════════════════════════ */
.lock-screen{
  position:fixed;inset:0;z-index:200;
  background:var(--bg);
  display:none;align-items:center;justify-content:center;
  padding:20px;
}
.lock-screen.show{display:flex}
.lock-card{
  width:100%;max-width:360px;
  background:var(--card);
  border:1px solid var(--card-b);border-radius:26px;
  overflow:hidden;box-shadow:var(--shadow);
  animation:fadeUp .4s ease;
}
.lock-banner{
  padding:36px 24px 26px;text-align:center;
  background:linear-gradient(150deg,var(--accent-d) 0%,transparent 70%);
}
.lock-icon{
  width:70px;height:70px;border-radius:20px;
  background:var(--accent-d);color:var(--accent2);
  border:1px solid var(--card-bh);
  display:flex;align-items:center;justify-content:center;
  font-size:32px;margin:0 auto 18px;
  position:relative;
}
.lock-icon::after{
  content:"";position:absolute;inset:-8px;
  border-radius:26px;border:1.5px solid var(--card-b);
  animation:breathe 2.8s ease-in-out infinite;
}
@keyframes breathe{
  0%,100%{transform:scale(1);opacity:.5}
  50%{transform:scale(1.06);opacity:0}
}
.lock-title{font-size:17px;font-weight:800;color:var(--t1);margin-bottom:5px}
.lock-sub{font-size:12px;color:var(--t3);line-height:1.7}
.lock-form{padding:22px 24px 26px}
.lock-input-wrap{position:relative;margin-bottom:12px}
.lock-input{
  width:100%;padding:14px 46px 14px 14px;
  background:rgba(0,0,0,.2);border:1px solid var(--card-b);
  border-radius:14px;color:var(--t1);font-size:15px;
  text-align:center;letter-spacing:.2em;outline:none;
  transition:.18s;
}
html[data-theme="light"] .lock-input{background:rgba(59,124,246,.04)}
.lock-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.lock-eye{
  position:absolute;inset-inline-end:12px;top:50%;
  transform:translateY(-50%);
  color:var(--t3);font-size:18px;padding:4px;
}
.lock-error{
  color:var(--red-t);font-size:11.5px;text-align:center;
  margin-bottom:10px;min-height:16px;font-weight:600;
}
.btn-primary{
  width:100%;padding:14px;border-radius:14px;
  background:linear-gradient(135deg,var(--accent),var(--accent2));
  color:#fff;font-size:14px;font-weight:800;
  display:flex;align-items:center;justify-content:center;gap:8px;
  box-shadow:0 8px 24px rgba(59,124,246,.3);
  transition:.18s;
}
.btn-primary:active{transform:scale(.98)}

/* ═══════════════════════════════════════════════════════════════════════
   MODALS
   ═══════════════════════════════════════════════════════════════════════ */
.modal-bg{
  position:fixed;inset:0;z-index:300;
  background:rgba(0,0,0,.7);
  backdrop-filter:blur(8px);
  -webkit-backdrop-filter:blur(8px);
  display:none;align-items:flex-end;justify-content:center;
  padding:0;
}
html[data-theme="light"] .modal-bg{background:rgba(20,40,80,.35)}
.modal-bg.show{display:flex;animation:fadeIn .2s ease}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.sheet{
  width:100%;max-width:640px;
  background:var(--card-solid);
  border-top-left-radius:24px;border-top-right-radius:24px;
  padding:20px 20px calc(20px + var(--safe-bottom));
  border-top:1px solid var(--card-b);
  animation:slideUp .3s cubic-bezier(.34,1.56,.64,1);
  max-height:85vh;overflow-y:auto;
}
@keyframes slideUp{from{transform:translateY(100%)}to{transform:translateY(0)}}
.sheet-handle{
  width:40px;height:4px;border-radius:4px;
  background:var(--t3);opacity:.3;
  margin:0 auto 16px;
}
.sheet-title{
  font-size:16px;font-weight:800;color:var(--t1);
  margin-bottom:16px;display:flex;align-items:center;gap:8px;
}
.sheet-title i{color:var(--accent)}

/* Client picker */
.client-grid{
  display:grid;grid-template-columns:repeat(3,1fr);gap:10px;
  margin-bottom:16px;
}
.client-btn{
  display:flex;flex-direction:column;align-items:center;gap:6px;
  padding:14px 8px;border-radius:14px;
  background:var(--card);border:1px solid var(--card-b);
  transition:.15s;
}
.client-btn:active{transform:scale(.95);background:var(--accent-d)}
.client-btn i{font-size:24px;color:var(--accent2)}
.client-btn span{font-size:10.5px;font-weight:700;color:var(--t1);text-align:center;line-height:1.3}

/* QR modal */
.qr-box{
  text-align:center;
}
.qr-img{
  background:#fff;border-radius:16px;padding:14px;
  display:inline-block;margin-bottom:14px;
  max-width:260px;
}
.qr-img img{width:100%;display:block;border-radius:8px}

/* Copy field */
.copy-field{
  display:flex;gap:8px;margin-bottom:10px;
}
.copy-field input{
  flex:1;padding:11px 13px;
  background:rgba(0,0,0,.15);
  border:1px solid var(--card-b);border-radius:11px;
  color:var(--t2);font-family:ui-monospace,monospace;
  font-size:10.5px;outline:none;
  min-width:0;
}
html[data-theme="light"] .copy-field input{background:rgba(59,124,246,.04)}
.copy-field button{
  padding:11px 14px;border-radius:11px;
  background:var(--accent);color:#fff;font-weight:700;
  font-size:11.5px;display:flex;align-items:center;gap:5px;
  transition:.15s;white-space:nowrap;
}
.copy-field button:active{transform:scale(.95)}

/* ═══════════════════════════════════════════════════════════════════════
   TOAST
   ═══════════════════════════════════════════════════════════════════════ */
.toast{
  position:fixed;bottom:calc(var(--nav-h) + var(--safe-bottom) + 16px);
  left:50%;transform:translateX(-50%) translateY(60px);
  z-index:400;padding:11px 20px;
  background:var(--card-solid);border:1px solid var(--card-b);
  border-radius:14px;color:var(--t1);
  font-size:12.5px;font-weight:700;
  box-shadow:var(--shadow);
  display:flex;align-items:center;gap:8px;
  opacity:0;transition:all .3s cubic-bezier(.34,1.56,.64,1);
  pointer-events:none;white-space:nowrap;
}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(34,197,94,.4);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.4);background:var(--red-bg);color:var(--red-t)}
.toast i{font-size:16px}

/* ═══════════════════════════════════════════════════════════════════════
   SETTINGS TAB
   ═══════════════════════════════════════════════════════════════════════ */
.settings-card{
  background:var(--card);border:1px solid var(--card-b);
  border-radius:18px;padding:6px;margin-bottom:12px;
}
.settings-row{
  display:flex;align-items:center;gap:12px;
  padding:14px 14px;border-radius:14px;
  transition:.15s;
}
.settings-row + .settings-row{border-top:1px solid var(--card-b)}
.settings-row:active{background:var(--accent-d)}
.settings-icon{
  width:38px;height:38px;border-radius:11px;
  background:var(--accent-d);color:var(--accent2);
  display:flex;align-items:center;justify-content:center;
  font-size:18px;flex-shrink:0;
}
.settings-text{flex:1;min-width:0}
.settings-label{font-size:13px;font-weight:700;color:var(--t1)}
.settings-sub{font-size:10.5px;color:var(--t3);margin-top:2px}
.settings-value{
  font-size:11.5px;font-weight:700;color:var(--accent2);
  display:flex;align-items:center;gap:5px;
}
/* Segmented control */
.segment{
  display:flex;gap:3px;background:rgba(0,0,0,.15);
  padding:3px;border-radius:10px;border:1px solid var(--card-b);
}
html[data-theme="light"] .segment{background:rgba(59,124,246,.05)}
.segment button{
  padding:6px 11px;border-radius:8px;
  font-size:10.5px;font-weight:700;color:var(--t3);
  transition:.15s;
}
.segment button.active{
  background:var(--accent);color:#fff;
  box-shadow:0 2px 8px rgba(59,124,246,.4);
}

/* ═══════════════════════════════════════════════════════════════════════
   SKELETON
   ═══════════════════════════════════════════════════════════════════════ */
.skeleton{
  background:linear-gradient(90deg,var(--card) 0%,var(--card-b) 50%,var(--card) 100%);
  background-size:200% 100%;
  animation:skeleton 1.5s ease-in-out infinite;
  border-radius:14px;
}
@keyframes skeleton{0%{background-position:200% 0}100%{background-position:-200% 0}}
.skel-card{height:130px;margin-bottom:12px}
.skel-line{height:14px;margin-bottom:8px}
.skel-line.short{width:60%}

/* ═══════════════════════════════════════════════════════════════════════
   EMPTY
   ═══════════════════════════════════════════════════════════════════════ */
.empty{
  text-align:center;padding:60px 20px;color:var(--t3);
}
.empty i{font-size:44px;opacity:.35;display:block;margin-bottom:14px}
.empty-title{font-size:14px;font-weight:700;color:var(--t2);margin-bottom:4px}
.empty-sub{font-size:11.5px}

/* ═══════════════════════════════════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════════════════════════════════ */
@media(min-width:641px){
  .app-header{padding-left:24px;padding-right:24px}
  .app-main{padding-left:20px;padding-right:20px}
}
</style>
</head>
<body>

<!-- ═══ LOCK SCREEN ═══ -->
<div class="lock-screen" id="lockScreen">
  <div class="lock-card">
    <div class="lock-banner">
      <div class="lock-icon"><i class="ti ti-shield-lock"></i></div>
      <div class="lock-title" id="lockName">—</div>
      <div class="lock-sub" data-i18n="lock_sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز را وارد کنید.</div>
    </div>
    <div class="lock-form">
      <div class="lock-error" id="lockError"></div>
      <div class="lock-input-wrap">
        <input class="lock-input" type="password" id="lockPw" placeholder="••••••••" autocomplete="off">
        <button class="lock-eye" onclick="togglePwVis()"><i class="ti ti-eye" id="lockEye"></i></button>
      </div>
      <button class="btn-primary" onclick="submitLock()">
        <i class="ti ti-lock-open"></i>
        <span data-i18n="enter">ورود به گروه</span>
      </button>
    </div>
  </div>
</div>

<!-- ═══ HEADER ═══ -->
<header class="app-header">
  <div class="brand">
    <div class="brand-logo"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div>
    <div class="brand-text">
      <div class="brand-name">OMID Network</div>
      <div class="brand-sub" id="subName">—</div>
    </div>
  </div>
  <div class="header-actions">
    <span class="status-pill" id="statusPill" style="display:none"><span class="status-dot"></span> LIVE</span>
    <button class="icon-btn" onclick="toggleLang()" id="langBtn">EN</button>
    <button class="icon-btn" onclick="cycleTheme()" id="themeBtn"><i class="ti ti-sun"></i></button>
  </div>
</header>

<!-- ═══ MAIN ═══ -->
<main class="app-main" id="appMain">
  <!-- Loading skeleton -->
  <div id="loading">
    <div class="skeleton skel-card"></div>
    <div class="skeleton skel-line"></div>
    <div class="skeleton skel-line short"></div>
  </div>

  <!-- TAB: HOME -->
  <section class="tab-panel active" id="tab-home" style="display:none">
    <div class="hero" id="hero">
      <div class="hero-head">
        <div style="flex:1;min-width:0">
          <div class="hero-title" id="heroTitle">—</div>
          <div class="hero-desc" id="heroDesc"></div>
        </div>
        <span class="hero-badge" id="heroBadge"><span class="status-dot"></span> <span data-i18n="online">آنلاین</span></span>
      </div>
      <div class="hero-stats">
        <div class="hero-stat">
          <div class="hero-stat-label"><i class="ti ti-plug-connected"></i> <span data-i18n="live_conns">اتصالات زنده</span></div>
          <div class="hero-stat-val" id="statConns">—</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-label"><i class="ti ti-chart-pie"></i> <span data-i18n="active_cfgs">کانفیگ فعال</span></div>
          <div class="hero-stat-val" id="statActive">—</div>
          <div class="hero-stat-sub" id="statActiveSub">—</div>
        </div>
      </div>
      <div class="usage-bar">
        <div class="usage-track"><div class="usage-fill" id="usageFill" style="width:0%"></div></div>
        <div class="usage-labels">
          <span id="usageUsed">—</span>
          <span id="usageTotal">—</span>
        </div>
      </div>
    </div>

    <div class="quick-actions">
      <button class="action-btn primary" onclick="openImportSheet()">
        <i class="ti ti-rocket"></i>
        <span data-i18n="import">افزودن به کلاینت</span>
      </button>
      <button class="action-btn" onclick="copySubUrl()">
        <i class="ti ti-copy"></i>
        <span data-i18n="copy_sub">کپی لینک ساب</span>
      </button>
      <button class="action-btn" onclick="showSubQR()">
        <i class="ti ti-qrcode"></i>
        <span data-i18n="qr_sub">QR ساب</span>
      </button>
      <button class="action-btn" onclick="refreshData()">
        <i class="ti ti-refresh"></i>
        <span data-i18n="refresh">بروزرسانی</span>
      </button>
    </div>

    <div class="section-title">
      <i class="ti ti-bolt"></i>
      <span data-i18n="quick_preview">پیش‌نمایش کانفیگ‌ها</span>
      <span class="section-count" id="quickCount">0</span>
    </div>
    <div class="cfg-list" id="quickList"></div>
  </section>

  <!-- TAB: CONFIGS -->
  <section class="tab-panel" id="tab-configs">
    <div class="section-title">
      <i class="ti ti-list"></i>
      <span data-i18n="all_configs">همه کانفیگ‌ها</span>
      <span class="section-count" id="cfgCount">0</span>
    </div>
    <div class="cfg-list" id="cfgList"></div>
  </section>

  <!-- TAB: STATS -->
  <section class="tab-panel" id="tab-stats">
    <div class="hero" style="padding:24px">
      <div class="hero-stat-label"><i class="ti ti-database"></i> <span data-i18n="total_usage">کل مصرف</span></div>
      <div style="font-size:34px;font-weight:900;letter-spacing:-.03em;margin-top:6px" id="statsTotal">—</div>
      <div style="font-size:11px;color:var(--t3);margin-top:4px" data-i18n="all_configs">همه کانفیگ‌ها</div>
    </div>
    <div class="section-title">
      <i class="ti ti-chart-bar"></i>
      <span data-i18n="per_config">مصرف هر کانفیگ</span>
    </div>
    <div class="cfg-list" id="statsList"></div>
  </section>

  <!-- TAB: SETTINGS -->
  <section class="tab-panel" id="tab-settings">
    <div class="section-title">
      <i class="ti ti-palette"></i>
      <span data-i18n="theme">پوسته</span>
    </div>
    <div class="settings-card">
      <div class="settings-row">
        <div class="settings-icon"><i class="ti ti-brightness"></i></div>
        <div class="settings-text">
          <div class="settings-label" data-i18n="theme_mode">حالت نمایش</div>
          <div class="settings-sub" data-i18n="theme_sub">تاریک، روشن یا خودکار</div>
        </div>
        <div class="segment" id="themeSegment">
          <button data-theme-opt="dark"><i class="ti ti-moon"></i></button>
          <button data-theme-opt="light"><i class="ti ti-sun"></i></button>
          <button data-theme-opt="auto"><i class="ti ti-device-desktop"></i></button>
        </div>
      </div>
    </div>

    <div class="section-title">
      <i class="ti ti-language"></i>
      <span data-i18n="language">زبان</span>
    </div>
    <div class="settings-card">
      <div class="settings-row">
        <div class="settings-icon"><i class="ti ti-world"></i></div>
        <div class="settings-text">
          <div class="settings-label" data-i18n="interface_lang">زبان رابط کاربری</div>
          <div class="settings-sub">Persian / English</div>
        </div>
        <div class="segment" id="langSegment">
          <button data-lang-opt="fa">FA</button>
          <button data-lang-opt="en">EN</button>
        </div>
      </div>
    </div>

    <div class="section-title">
      <i class="ti ti-apps"></i>
      <span data-i18n="client">کلاینت پیش‌فرض</span>
    </div>
    <div class="settings-card">
      <div class="settings-row" onclick="openImportSheet()">
        <div class="settings-icon"><i class="ti ti-device-mobile"></i></div>
        <div class="settings-text">
          <div class="settings-label" id="defaultClientName" data-i18n="client_default">انتخاب کلاینت پیش‌فرض</div>
          <div class="settings-sub" data-i18n="client_sub">برای دکمه‌ی افزودن سریع</div>
        </div>
        <i class="ti ti-chevron-left" style="color:var(--t3);font-size:18px"></i>
      </div>
    </div>

    <div class="section-title">
      <i class="ti ti-info-circle"></i>
      <span data-i18n="about">درباره</span>
    </div>
    <div class="settings-card">
      <div class="settings-row">
        <div class="settings-icon"><i class="ti ti-shield-check"></i></div>
        <div class="settings-text">
          <div class="settings-label" data-i18n="secure">اتصال رمزنگاری‌شده</div>
          <div class="settings-sub">TLS 1.3 · AES-256</div>
        </div>
      </div>
      <div class="settings-row">
        <div class="settings-icon"><i class="ti ti-versions"></i></div>
        <div class="settings-text">
          <div class="settings-label">OMID Network</div>
          <div class="settings-sub" data-i18n="version">نسخه</div>
        </div>
        <div class="settings-value">v1.0</div>
      </div>
    </div>
  </section>
</main>

<!-- ═══ BOTTOM NAV ═══ -->
<nav class="bottom-nav">
  <button class="nav-item active" data-tab="home" onclick="switchTab('home')">
    <i class="ti ti-home"></i>
    <span data-i18n="tab_home">خانه</span>
  </button>
  <button class="nav-item" data-tab="configs" onclick="switchTab('configs')">
    <i class="ti ti-list"></i>
    <span data-i18n="tab_configs">کانفیگ‌ها</span>
  </button>
  <button class="nav-item" data-tab="stats" onclick="switchTab('stats')">
    <i class="ti ti-chart-bar"></i>
    <span data-i18n="tab_stats">آمار</span>
  </button>
  <button class="nav-item" data-tab="settings" onclick="switchTab('settings')">
    <i class="ti ti-settings"></i>
    <span data-i18n="tab_settings">تنظیمات</span>
  </button>
</nav>

<!-- ═══ IMPORT SHEET ═══ -->
<div class="modal-bg" id="importModal" onclick="closeSheet('importModal')">
  <div class="sheet" onclick="event.stopPropagation()">
    <div class="sheet-handle"></div>
    <div class="sheet-title"><i class="ti ti-rocket"></i> <span data-i18n="choose_client">انتخاب کلاینت</span></div>
    <div class="client-grid" id="clientGrid"></div>
    <div class="copy-field">
      <input id="importUrl" readonly>
      <button onclick="copyImportUrl()"><i class="ti ti-copy"></i></button>
    </div>
    <div style="font-size:10.5px;color:var(--t3);text-align:center;line-height:1.7">
      <span data-i18n="import_hint">اگه کلاینت به‌طور خودکار باز نشد، لینک را کپی و دستی در کلاینت وارد کنید.</span>
    </div>
  </div>
</div>

<!-- ═══ QR SHEET ═══ -->
<div class="modal-bg" id="qrModal" onclick="closeSheet('qrModal')">
  <div class="sheet" onclick="event.stopPropagation()">
    <div class="sheet-handle"></div>
    <div class="sheet-title"><i class="ti ti-qrcode"></i> <span id="qrTitle">QR Code</span></div>
    <div class="qr-box">
      <div class="qr-img"><img id="qrImage" src="" alt="QR"></div>
    </div>
  </div>
</div>

<!-- ═══ TOAST ═══ -->
<div class="toast" id="toast"></div>

<script>
/* ═══════════════════════════════════════════════════════════════════════
   I18N DICTIONARY
   ═══════════════════════════════════════════════════════════════════════ */
const I18N = {
  fa: {
    lock_sub:"این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز را وارد کنید.",
    enter:"ورود به گروه",
    online:"آنلاین",
    live_conns:"اتصالات زنده",
    active_cfgs:"کانفیگ فعال",
    import:"افزودن به کلاینت",
    copy_sub:"کپی لینک ساب",
    qr_sub:"QR ساب",
    refresh:"بروزرسانی",
    quick_preview:"پیش‌نمایش کانفیگ‌ها",
    all_configs:"همه کانفیگ‌ها",
    total_usage:"کل مصرف",
    per_config:"مصرف هر کانفیگ",
    theme:"پوسته",
    theme_mode:"حالت نمایش",
    theme_sub:"تاریک، روشن یا خودکار",
    language:"زبان",
    interface_lang:"زبان رابط کاربری",
    client:"کلاینت پیش‌فرض",
    client_default:"انتخاب کلاینت پیش‌فرض",
    client_sub:"برای دکمه‌ی افزودن سریع",
    about:"درباره",
    secure:"اتصال رمزنگاری‌شده",
    version:"نسخه",
    tab_home:"خانه",
    tab_configs:"کانفیگ‌ها",
    tab_stats:"آمار",
    tab_settings:"تنظیمات",
    choose_client:"انتخاب کلاینت",
    import_hint:"اگه کلاینت به‌طور خودکار باز نشد، لینک را کپی و دستی در کلاینت وارد کنید.",
    copy_all:"کپی همه",
    copy:"کپی",
    copied:"کپی شد ✓",
    error_load:"خطا در بارگذاری",
    wrong_pw:"رمز اشتباه است",
    link:"لینک",
    qr:"QR",
    usage:"مصرف",
    no_configs:"هنوز کانفیگی وجود ندارد",
    unlimited:"نامحدود",
    empty_title:"کانفیگی برای نمایش نیست",
    empty_sub:"هنوز هیچ کانفیگی در این گروه نیست"
  },
  en: {
    lock_sub:"This group is password protected. Enter the password to view configurations.",
    enter:"Enter Group",
    online:"Online",
    live_conns:"Live Connections",
    active_cfgs:"Active Configs",
    import:"Import to Client",
    copy_sub:"Copy Sub URL",
    qr_sub:"Sub QR",
    refresh:"Refresh",
    quick_preview:"Configuration Preview",
    all_configs:"All Configurations",
    total_usage:"Total Usage",
    per_config:"Usage per Config",
    theme:"Theme",
    theme_mode:"Display Mode",
    theme_sub:"Dark, Light or Auto",
    language:"Language",
    interface_lang:"Interface Language",
    client:"Default Client",
    client_default:"Choose Default Client",
    client_sub:"For quick import button",
    about:"About",
    secure:"Encrypted Connection",
    version:"Version",
    tab_home:"Home",
    tab_configs:"Configs",
    tab_stats:"Stats",
    tab_settings:"Settings",
    choose_client:"Choose Client",
    import_hint:"If the client didn't open automatically, copy the link and paste it manually.",
    copy_all:"Copy All",
    copy:"Copy",
    copied:"Copied ✓",
    error_load:"Failed to load",
    wrong_pw:"Wrong password",
    link:"Link",
    qr:"QR",
    usage:"Usage",
    no_configs:"No configurations yet",
    unlimited:"Unlimited",
    empty_title:"No configurations to show",
    empty_sub:"There are no configurations in this group yet"
  }
};

/* ═══════════════════════════════════════════════════════════════════════
   CLIENT DEFINITIONS
   ═══════════════════════════════════════════════════════════════════════ */
const CLIENTS = [
  { id:"v2rayng",     name:"v2rayNG",     icon:"ti-brand-android",  scheme:(u)=>u },
  { id:"nekobox",     name:"NekoBox",     icon:"ti-cat",            scheme:(u)=>u },
  { id:"singbox",     name:"Sing-Box",    icon:"ti-box",            scheme:(u)=>"sing-box://import-remote-profile?url="+encodeURIComponent(u)+"#OMID" },
  { id:"streisand",   name:"Streisand",   icon:"ti-apple",          scheme:(u)=>"streisand://import/"+encodeURIComponent(u) },
  { id:"shadowrocket",name:"Shadowrocket",icon:"ti-rocket",         scheme:(u)=>"sub://"+btoa(u) },
  { id:"clash",       name:"Clash",       icon:"ti-sword",          scheme:(u)=>"clash://install-config?url="+encodeURIComponent(u) },
  { id:"hiddify",     name:"Hiddify",     icon:"ti-shield-check",   scheme:(u)=>"hiddify://import/"+encodeURIComponent(u) },
  { id:"foxray",      name:"FoXray",      icon:"ti-brand-firefox",  scheme:(u)=>"foxray://install-config?url="+encodeURIComponent(u) },
  { id:"v2rayn",      name:"v2rayN",      icon:"ti-brand-windows",  scheme:(u)=>u }
];

/* ═══════════════════════════════════════════════════════════════════════
   GLOBAL STATE
   ═══════════════════════════════════════════════════════════════════════ */
const UUID_KEY = "__UUID_KEY__";
const STORAGE_PREFIX = "omid_pub_";
let state = {
  data: null,
  savedPw: "",
  lang: localStorage.getItem(STORAGE_PREFIX+"lang") || "fa",
  theme: localStorage.getItem(STORAGE_PREFIX+"theme") || "dark",
  defaultClient: localStorage.getItem(STORAGE_PREFIX+"client") || "v2rayng"
};

/* ═══════════════════════════════════════════════════════════════════════
   HELPERS
   ═══════════════════════════════════════════════════════════════════════ */
function esc(s){return String(s||"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function t(key){return (I18N[state.lang] && I18N[state.lang][key]) || I18N.fa[key] || key}

function applyTranslations(){
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const k = el.dataset.i18n;
    if(k) el.textContent = t(k);
  });
  document.documentElement.setAttribute("data-lang", state.lang);
  document.documentElement.setAttribute("dir", state.lang==="fa" ? "rtl" : "ltr");
  document.getElementById("langBtn").textContent = state.lang==="fa" ? "EN" : "FA";
  document.querySelectorAll("#langSegment button").forEach(b=>b.classList.toggle("active", b.dataset.langOpt===state.lang));
}

function applyTheme(){
  let theme = state.theme;
  if(theme === "auto"){
    theme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  document.documentElement.setAttribute("data-theme", theme);
  const icon = document.querySelector("#themeBtn i");
  if(icon) icon.className = "ti " + (theme==="dark" ? "ti-sun" : "ti-moon");
  const meta = document.getElementById("meta-theme");
  if(meta) meta.setAttribute("content", theme==="dark" ? "#060a14" : "#EFF3FA");
  document.querySelectorAll("#themeSegment button").forEach(b=>b.classList.toggle("active", b.dataset.themeOpt===state.theme));
}

function cycleTheme(){
  const order = ["dark","light","auto"];
  const next = order[(order.indexOf(state.theme)+1) % order.length];
  state.theme = next;
  localStorage.setItem(STORAGE_PREFIX+"theme", next);
  applyTheme();
}

function toast(msg, type){
  const el = document.getElementById("toast");
  el.className = "toast show" + (type ? " "+type : "");
  el.innerHTML = '<i class="ti '+(type==="ok"?"ti-circle-check":type==="err"?"ti-alert-circle":"ti-info-circle")+'"></i> '+esc(msg);
  clearTimeout(window.__toastT);
  window.__toastT = setTimeout(()=>el.classList.remove("show"), 2400);
}

async function copyText(text){
  try{
    await navigator.clipboard.writeText(text);
    toast(t("copied"), "ok");
  }catch(e){
    // fallback
    const ta = document.createElement("textarea");
    ta.value = text; ta.style.position="fixed"; ta.style.opacity="0";
    document.body.appendChild(ta); ta.select();
    try{document.execCommand("copy");toast(t("copied"),"ok")}catch(_){toast("Copy failed","err")}
    document.body.removeChild(ta);
  }
}

/* ═══════════════════════════════════════════════════════════════════════
   TAB SWITCHING
   ═══════════════════════════════════════════════════════════════════════ */
function switchTab(name){
  document.querySelectorAll(".tab-panel").forEach(p=>p.classList.remove("active"));
  const target = document.getElementById("tab-"+name);
  if(target) target.classList.add("active");
  document.querySelectorAll(".nav-item").forEach(n=>n.classList.toggle("active", n.dataset.tab===name));
  window.scrollTo({top:0,behavior:"smooth"});
}

/* ═══════════════════════════════════════════════════════════════════════
   SHEETS & MODALS
   ═══════════════════════════════════════════════════════════════════════ */
function openSheet(id){document.getElementById(id).classList.add("show")}
function closeSheet(id){document.getElementById(id).classList.remove("show")}

function openImportSheet(){
  if(!state.data) return;
  const url = getSubUrl();
  document.getElementById("importUrl").value = url;
  renderClients();
  openSheet("importModal");
}

function renderClients(){
  const grid = document.getElementById("clientGrid");
  const url = getSubUrl();
  grid.innerHTML = CLIENTS.map(c=>`
    <button class="client-btn" onclick="launchClient('${c.id}')">
      <i class="ti ${c.icon}"></i>
      <span>${esc(c.name)}</span>
    </button>
  `).join("");
}

function launchClient(id){
  const c = CLIENTS.find(x=>x.id===id);
  if(!c) return;
  const url = getSubUrl();
  const deep = typeof c.scheme==="function" ? c.scheme(url) : url;
  // save as default
  state.defaultClient = id;
  localStorage.setItem(STORAGE_PREFIX+"client", id);
  updateDefaultClientLabel();
  // try to open
  if(deep === url){
    copyText(url);
  }else{
    try{
      window.location.href = deep;
      setTimeout(()=>copyText(url), 500);
    }catch(e){copyText(url)}
  }
  closeSheet("importModal");
}

function updateDefaultClientLabel(){
  const c = CLIENTS.find(x=>x.id===state.defaultClient);
  const el = document.getElementById("defaultClientName");
  if(el && c) el.textContent = c.name;
}

function copyImportUrl(){
  const url = document.getElementById("importUrl").value;
  if(url) copyText(url);
}

function showQR(title, link){
  document.getElementById("qrTitle").textContent = title;
  document.getElementById("qrImage").src = "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data="+encodeURIComponent(link)+"&bgcolor=ffffff&color=0F172A";
  openSheet("qrModal");
}

function showSubQR(){
  if(!state.data) return;
  showQR(t("qr_sub"), getSubUrl());
}

function getSubUrl(){
  const base = state.data?.sub_url || (location.protocol+"//"+location.host+"/sub-group/"+UUID_KEY);
  return state.savedPw ? base + "?pw=" + encodeURIComponent(state.savedPw) : base;
}

function copySubUrl(){
  copyText(getSubUrl());
}

/* ═══════════════════════════════════════════════════════════════════════
   DATA LOADING
   ═══════════════════════════════════════════════════════════════════════ */
async function loadData(pw){
  const url = "/api/public/sub/"+UUID_KEY+(pw?"?pw="+encodeURIComponent(pw):"");
  const r = await fetch(url, {cache:"no-store"});
  if(!r.ok) throw new Error("HTTP "+r.status);
  return r.json();
}

async function refreshData(){
  try{
    const data = await loadData(state.savedPw);
    if(data.locked){
      showLock(data.name);
      return;
    }
    state.data = data;
    localStorage.setItem(STORAGE_PREFIX+"cache_"+UUID_KEY, JSON.stringify(data));
    renderAll();
    toast(t("refresh")+" ✓", "ok");
  }catch(e){
    toast(t("error_load"), "err");
  }
}

function showLock(name){
  document.getElementById("lockScreen").classList.add("show");
  document.getElementById("lockName").textContent = name;
  setTimeout(()=>document.getElementById("lockPw").focus(), 200);
}

function hideLock(){
  document.getElementById("lockScreen").classList.remove("show");
}

function togglePwVis(){
  const inp = document.getElementById("lockPw");
  const icon = document.getElementById("lockEye");
  const toText = inp.type === "password";
  inp.type = toText ? "text" : "password";
  icon.className = "ti " + (toText ? "ti-eye-off" : "ti-eye");
}

async function submitLock(){
  const pw = document.getElementById("lockPw").value;
  const errEl = document.getElementById("lockError");
  errEl.textContent = "";
  try{
    const data = await loadData(pw);
    if(data.locked){
      errEl.textContent = t("wrong_pw");
      return;
    }
    state.savedPw = pw;
    state.data = data;
    localStorage.setItem(STORAGE_PREFIX+"cache_"+UUID_KEY, JSON.stringify(data));
    hideLock();
    renderAll();
  }catch(e){
    errEl.textContent = t("error_load");
  }
}

/* ═══════════════════════════════════════════════════════════════════════
   RENDERING
   ═══════════════════════════════════════════════════════════════════════ */
function fmtBytes(b){
  if(!b||b===0) return "0 B";
  if(b<1024) return b+" B";
  if(b<1048576) return (b/1024).toFixed(1)+" KB";
  if(b<1073741824) return (b/1048576).toFixed(2)+" MB";
  return (b/1073741824).toFixed(2)+" GB";
}

function protoClass(p){
  if(!p) return "ws";
  if(p.startsWith("xhttp")) return "xhttp";
  return "ws";
}

function protoName(p){
  if(!p||p==="vless-ws") return "VLESS · WS";
  if(p==="xhttp-packet-up") return "XHTTP · packet-up";
  if(p==="xhttp-stream-up") return "XHTTP · stream-up";
  if(p==="xhttp-stream-one") return "XHTTP ULTRA";
  return p;
}

function renderConfigCard(l, idx){
  const pct = l.limit_bytes===0 ? 0 : Math.min(100, (l.used_bytes/l.limit_bytes)*100);
  const limitTxt = l.limit_bytes===0 ? t("unlimited") : fmtBytes(l.limit_bytes);
  const usedTxt = fmtBytes(l.used_bytes);
  const cls = !l.active ? "off" : "";
  const conns = l.connections || 0;
  return `
    <div class="cfg-card ${cls}">
      <div class="cfg-top">
        <div class="cfg-icon"><i class="ti ti-key"></i></div>
        <div class="cfg-info">
          <div class="cfg-label">${esc(l.label)}</div>
          <div class="cfg-badges">
            <span class="chip ${protoClass(l.protocol)}">${esc(protoName(l.protocol))}</span>
            ${l.active
              ? '<span class="chip green"><i class="ti ti-circle-check"></i> '+t("online")+'</span>'
              : '<span class="chip red"><i class="ti ti-circle-x"></i> Off</span>'}
            ${conns>0 ? '<span class="chip amber"><i class="ti ti-plug-connected"></i> '+conns+'</span>' : ''}
          </div>
          <div class="cfg-usage">
            <div class="usage-track"><div class="usage-fill" style="width:${pct}%"></div></div>
            <div class="cfg-usage-labels">
              <span>${esc(usedTxt)}</span>
              <span>${esc(limitTxt)}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="cfg-actions">
        <button class="cfg-btn primary" onclick="quickImport(${idx})">
          <i class="ti ti-rocket"></i> ${t("import")}
        </button>
        <button class="cfg-btn" onclick="copyCfgLink(${idx})">
          <i class="ti ti-copy"></i> ${t("link")}
        </button>
        <button class="cfg-btn" onclick="qrCfg(${idx})">
          <i class="ti ti-qrcode"></i> ${t("qr")}
        </button>
      </div>
    </div>
  `;
}

function renderAll(){
  const d = state.data;
  if(!d) return;
  // Header subtitle
  document.getElementById("subName").textContent = d.name || "—";
  // Hero
  document.getElementById("heroTitle").textContent = d.name || "—";
  document.getElementById("heroDesc").textContent = d.desc || "";
  document.getElementById("statConns").textContent = d.active_connections || 0;
  const activeCount = (d.links||[]).filter(l=>l.active).length;
  document.getElementById("statActive").textContent = activeCount;
  document.getElementById("statActiveSub").textContent = (d.links||[]).length + " total";
  // Total usage
  const total = (d.links||[]).reduce((s,l)=>s+(l.used_bytes||0),0);
  const totalLimit = (d.links||[]).reduce((s,l)=>s+(l.limit_bytes||0),0);
  const pct = totalLimit>0 ? Math.min(100, (total/totalLimit)*100) : (total>0 ? 25 : 0);
  document.getElementById("usageFill").style.width = pct+"%";
  document.getElementById("usageUsed").textContent = fmtBytes(total);
  document.getElementById("usageTotal").textContent = totalLimit>0 ? fmtBytes(totalLimit) : "∞";
  document.getElementById("statsTotal").textContent = fmtBytes(total);
  document.getElementById("statusPill").style.display = "inline-flex";
  // Lists
  const links = d.links || [];
  document.getElementById("quickCount").textContent = links.length;
  document.getElementById("cfgCount").textContent = links.length;
  const quickList = document.getElementById("quickList");
  const cfgList = document.getElementById("cfgList");
  const statsList = document.getElementById("statsList");
  if(!links.length){
    const empty = '<div class="empty"><i class="ti ti-inbox"></i><div class="empty-title">'+t("empty_title")+'</div><div class="empty-sub">'+t("empty_sub")+'</div></div>';
    quickList.innerHTML = empty;
    cfgList.innerHTML = empty;
    statsList.innerHTML = empty;
  }else{
    quickList.innerHTML = links.slice(0,3).map((l,i)=>renderConfigCard(l,i)).join("");
    cfgList.innerHTML = links.map((l,i)=>renderConfigCard(l,i)).join("");
    statsList.innerHTML = links.map((l,i)=>`
      <div class="cfg-card">
        <div class="cfg-top">
          <div class="cfg-icon"><i class="ti ti-chart-line"></i></div>
          <div class="cfg-info">
            <div class="cfg-label">${esc(l.label)}</div>
            <div class="cfg-usage">
              <div class="usage-track"><div class="usage-fill" style="width:${l.limit_bytes===0?0:Math.min(100,(l.used_bytes/l.limit_bytes)*100)}%"></div></div>
              <div class="cfg-usage-labels">
                <span>${fmtBytes(l.used_bytes)}</span>
                <span>${l.limit_bytes===0?t("unlimited"):fmtBytes(l.limit_bytes)}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `).join("");
  }
  // Hide loading, show tabs
  document.getElementById("loading").style.display = "none";
  ["home","configs","stats","settings"].forEach(t=>{
    const el = document.getElementById("tab-"+t);
    if(el) el.style.display = "";
  });
}

function quickImport(idx){
  const l = state.data?.links?.[idx];
  if(!l) return;
  const c = CLIENTS.find(x=>x.id===state.defaultClient);
  if(!c){openImportSheet();return}
  const deep = typeof c.scheme==="function" ? c.scheme(l.vless_link) : l.vless_link;
  if(deep===l.vless_link){
    copyText(l.vless_link);
  }else{
    try{
      window.location.href = deep;
      setTimeout(()=>copyText(l.vless_link), 500);
    }catch(e){copyText(l.vless_link)}
  }
}

function copyCfgLink(idx){
  const l = state.data?.links?.[idx];
  if(l) copyText(l.vless_link);
}

function qrCfg(idx){
  const l = state.data?.links?.[idx];
  if(l) showQR(l.label, l.vless_link);
}

/* ═══════════════════════════════════════════════════════════════════════
   INIT
   ═══════════════════════════════════════════════════════════════════════ */
function toggleLang(){
  state.lang = state.lang==="fa" ? "en" : "fa";
  localStorage.setItem(STORAGE_PREFIX+"lang", state.lang);
  applyTranslations();
}

document.getElementById("themeSegment").addEventListener("click", e=>{
  const btn = e.target.closest("button");
  if(!btn) return;
  state.theme = btn.dataset.themeOpt;
  localStorage.setItem(STORAGE_PREFIX+"theme", state.theme);
  applyTheme();
});

document.getElementById("langSegment").addEventListener("click", e=>{
  const btn = e.target.closest("button");
  if(!btn) return;
  state.lang = btn.dataset.langOpt;
  localStorage.setItem(STORAGE_PREFIX+"lang", state.lang);
  applyTranslations();
});

document.getElementById("lockPw").addEventListener("keydown", e=>{
  if(e.key==="Enter") submitLock();
});

window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", ()=>{
  if(state.theme==="auto") applyTheme();
});

/* boot */
(async function init(){
  applyTranslations();
  applyTheme();
  updateDefaultClientLabel();
  // Show cached data immediately if available
  const cached = localStorage.getItem(STORAGE_PREFIX+"cache_"+UUID_KEY);
  if(cached){
    try{
      state.data = JSON.parse(cached);
      renderAll();
    }catch(e){}
  }
  // Then fetch fresh
  try{
    const data = await loadData();
    if(data.locked){
      document.getElementById("loading").style.display="none";
      showLock(data.name);
      return;
    }
    state.data = data;
    localStorage.setItem(STORAGE_PREFIX+"cache_"+UUID_KEY, JSON.stringify(data));
    renderAll();
  }catch(e){
    if(!state.data){
      document.getElementById("loading").style.display="none";
      document.getElementById("tab-home").style.display = "";
      document.getElementById("quickList").innerHTML = '<div class="empty"><i class="ti ti-alert-circle"></i><div class="empty-title">'+t("error_load")+'</div></div>';
    }
  }
})();
</script>
</body></html>'''

PUBLIC_PAGE_HTML_TEMPLATE = PUBLIC_PAGE_HTML_TEMPLATE.replace("__LOGO_B64__", LOGO_B64)


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v4 — UI مدرن اپ‌مانند
    از یک template جدا استفاده می‌کنه تا مشکل f-string brace نداشته باشیم."""
    return PUBLIC_PAGE_HTML_TEMPLATE.replace("__UUID_KEY__", uuid_key)

# ═══════════════════════════════════════════════════════════════════════
# Single-config page — Subscription Info UI (Marzban-style)
# ═══════════════════════════════════════════════════════════════════════
SINGLE_CONFIG_HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#0a0a14" id="meta-theme">
<title>Subscription info · OMID</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#0a0a14;
  --bg-grad:radial-gradient(ellipse 900px 600px at 20% -10%,rgba(168,85,247,.12),transparent 60%),
            radial-gradient(ellipse 700px 500px at 90% 110%,rgba(0,212,255,.08),transparent 60%),
            #0a0a14;
  --card:#13131f;
  --card-2:#17172a;
  --card-border:rgba(255,255,255,.06);
  --card-border-h:rgba(255,255,255,.12);
  --accent:#00d4ff;
  --accent-2:#a855f7;
  --green:#22c55e;
  --green-bg:rgba(34,197,94,.12);
  --red:#ef4444;
  --red-bg:rgba(239,68,68,.12);
  --amber:#f59e0b;
  --amber-bg:rgba(245,158,11,.12);
  --t1:#e8e8f0;
  --t2:#8a8aa8;
  --t3:#5a5a7a;
  --radius:20px;
  --radius-sm:12px;
  --shadow:0 20px 60px rgba(0,0,0,.5);
  --font:'Inter','Vazirmatn',system-ui,sans-serif;
}
html[data-theme="light"]{
  --bg:#f0f0f7;
  --bg-grad:radial-gradient(ellipse 900px 600px at 20% -10%,rgba(168,85,247,.10),transparent 60%),
            radial-gradient(ellipse 700px 500px at 90% 110%,rgba(0,180,220,.08),transparent 60%),
            #f0f0f7;
  --card:#ffffff;
  --card-2:#f8f8fc;
  --card-border:rgba(0,0,0,.06);
  --card-border-h:rgba(0,0,0,.12);
  --accent:#0088cc;
  --accent-2:#7c3aed;
  --green:#16a34a;
  --green-bg:rgba(22,163,74,.10);
  --red:#dc2626;
  --red-bg:rgba(220,38,38,.10);
  --amber:#d97706;
  --amber-bg:rgba(217,119,6,.10);
  --t1:#1a1a2e;
  --t2:#5a5a7a;
  --t3:#9a9ab0;
  --shadow:0 20px 60px rgba(50,50,100,.12);
}
html,body{min-height:100%}
body{
  font-family:var(--font);
  background:var(--bg-grad);
  color:var(--t1);
  font-size:14px;
  line-height:1.5;
  transition:background .3s,color .3s;
  -webkit-font-smoothing:antialiased;
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:24px 16px;
}
html[dir="rtl"] body{font-family:'Vazirmatn','Inter',system-ui,sans-serif}

::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.1);border-radius:3px}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
a{color:inherit;text-decoration:none}
input{font-family:inherit}

/* ═══════════════════════════════════════════════════════════════════════
   MAIN CARD
   ═══════════════════════════════════════════════════════════════════════ */
.sub-card{
  width:100%;
  max-width:720px;
  background:var(--card);
  border:1px solid var(--card-border);
  border-radius:24px;
  padding:28px;
  box-shadow:var(--shadow);
  position:relative;
  overflow:hidden;
}
.sub-card::before{
  content:"";position:absolute;top:-100px;right:-100px;width:300px;height:300px;
  background:radial-gradient(circle,rgba(168,85,247,.06),transparent 70%);
  pointer-events:none;
}

/* ══ Header ══ */
.sub-header{
  display:flex;align-items:center;justify-content:space-between;
  gap:14px;margin-bottom:24px;position:relative;z-index:1;
}
.sub-brand{display:flex;align-items:center;gap:12px;min-width:0}
.sub-logo{
  width:44px;height:44px;border-radius:12px;overflow:hidden;flex-shrink:0;
  background:linear-gradient(135deg,var(--accent) 0%,var(--accent-2) 100%);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 6px 20px rgba(0,212,255,.18);
}
.sub-logo img{width:100%;height:100%;object-fit:cover}
.sub-logo i{color:#fff;font-size:22px}
.sub-title{font-size:16px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.sub-subtitle{font-size:11.5px;color:var(--t3);margin-top:1px}
.sub-actions{display:flex;gap:8px;flex-shrink:0}
.icon-btn{
  width:36px;height:36px;border-radius:10px;
  background:rgba(255,255,255,.03);
  border:1px solid var(--card-border);
  color:var(--t2);
  display:flex;align-items:center;justify-content:center;
  font-size:16px;transition:.15s;
}
html[data-theme="light"] .icon-btn{background:rgba(0,0,0,.02)}
.icon-btn:hover{background:rgba(255,255,255,.06);color:var(--t1);border-color:var(--card-border-h)}
html[data-theme="light"] .icon-btn:hover{background:rgba(0,0,0,.04)}

/* ══ Usage Hero ══ */
.usage-hero{
  display:grid;
  grid-template-columns:180px 1fr;
  gap:24px;
  align-items:center;
  padding-bottom:24px;
  border-bottom:1px solid var(--card-border);
  margin-bottom:24px;
  position:relative;z-index:1;
}
.usage-left{display:flex;flex-direction:column;align-items:center}
.usage-remaining-label{font-size:11px;color:var(--t3);font-weight:600;letter-spacing:.05em;text-transform:uppercase;margin-bottom:6px}
.usage-remaining-val{
  font-size:42px;font-weight:900;color:var(--accent);
  letter-spacing:-.03em;line-height:1;
  display:flex;align-items:baseline;gap:6px;
  margin-bottom:6px;
}
.usage-remaining-val span{font-size:16px;font-weight:600;color:var(--t2)}
.usage-of{font-size:11.5px;color:var(--t3)}

/* Circular progress */
.circle-wrap{position:relative;width:150px;height:150px;margin-top:20px}
.circle-wrap svg{width:100%;height:100%;transform:rotate(-90deg)}
.circle-bg{fill:none;stroke:rgba(255,255,255,.06);stroke-width:8}
html[data-theme="light"] .circle-bg{stroke:rgba(0,0,0,.05)}
.circle-fg{fill:none;stroke:url(#grad);stroke-width:8;stroke-linecap:round;transition:stroke-dashoffset 1s cubic-bezier(.4,0,.2,1)}
.circle-center{
  position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
}
.circle-pct{font-size:24px;font-weight:900;color:var(--t1);letter-spacing:-.02em}
.circle-label{font-size:10px;color:var(--t3);font-weight:600;text-transform:uppercase;letter-spacing:.08em;margin-top:2px}

/* Info grid */
.usage-right{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.info-tile{
  background:var(--card-2);
  border:1px solid var(--card-border);
  border-radius:12px;
  padding:12px 14px;
  transition:.15s;
}
.info-tile:hover{border-color:var(--card-border-h);transform:translateY(-1px)}
.info-label{
  font-size:10px;color:var(--t3);font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;
  margin-bottom:5px;
}
.info-val{font-size:14px;font-weight:700;color:var(--t1);word-break:break-word}
.info-val.accent{color:var(--accent)}
.info-val.green{color:var(--green)}
.info-val.red{color:var(--red)}
.status-pill{
  display:inline-flex;align-items:center;gap:5px;
  font-size:11px;font-weight:700;
  padding:3px 9px;border-radius:6px;
  background:var(--green-bg);color:var(--green);
}
.status-pill.off{background:var(--red-bg);color:var(--red)}
.status-dot{width:5px;height:5px;border-radius:50%;background:currentColor}

/* ══ Tabs ══ */
.tabs{
  display:flex;gap:4px;
  border-bottom:1px solid var(--card-border);
  margin-bottom:20px;
  position:relative;z-index:1;
}
.tab{
  display:flex;align-items:center;gap:6px;
  padding:10px 14px 12px;
  font-size:12.5px;font-weight:700;
  color:var(--t3);
  cursor:pointer;
  position:relative;
  transition:.15s;
  border-bottom:2px solid transparent;
  margin-bottom:-1px;
  white-space:nowrap;
}
.tab i{font-size:15px}
.tab:hover{color:var(--t2)}
.tab.active{color:var(--accent);border-bottom-color:var(--accent)}
.tab-count{
  font-size:9.5px;font-weight:700;
  background:rgba(255,255,255,.06);
  padding:1px 6px;border-radius:10px;
  color:var(--t2);
}
html[data-theme="light"] .tab-count{background:rgba(0,0,0,.05)}
.tab.active .tab-count{background:rgba(0,212,255,.12);color:var(--accent)}

.tab-content{display:none;position:relative;z-index:1}
.tab-content.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

/* ══ Subscription URL row ══ */
.sub-url-row{
  display:flex;align-items:center;gap:12px;
  background:var(--card-2);
  border:1px solid var(--card-border);
  border-radius:14px;
  padding:14px 16px;
  margin-bottom:14px;
}
.sub-url-badge{
  font-size:9px;font-weight:800;letter-spacing:.08em;
  background:var(--green-bg);color:var(--green);
  padding:4px 8px;border-radius:6px;
  flex-shrink:0;
}
.sub-url-text{
  flex:1;min-width:0;
  font-family:ui-monospace,monospace;
  font-size:12px;
  color:var(--t2);
  overflow:hidden;text-overflow:ellipsis;
  white-space:nowrap;
}
.sub-url-copy{
  width:34px;height:34px;border-radius:9px;
  background:rgba(255,255,255,.04);
  border:1px solid var(--card-border);
  color:var(--t2);
  display:flex;align-items:center;justify-content:center;
  font-size:15px;
  flex-shrink:0;
  transition:.15s;
}
html[data-theme="light"] .sub-url-copy{background:rgba(0,0,0,.02)}
.sub-url-copy:hover{background:rgba(0,212,255,.1);color:var(--accent);border-color:rgba(0,212,255,.3)}

/* ══ QR section ══ */
.qr-section{
  display:flex;align-items:center;gap:22px;
  background:var(--card-2);
  border:1px dashed var(--card-border-h);
  border-radius:16px;
  padding:20px;
}
.qr-img{
  width:140px;height:140px;
  background:#fff;
  border-radius:12px;
  padding:10px;
  flex-shrink:0;
  box-shadow:0 8px 24px rgba(0,0,0,.15);
}
.qr-img img{width:100%;height:100%;display:block;border-radius:6px}
.qr-text h4{font-size:15px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.01em}
.qr-text p{font-size:12px;color:var(--t3);line-height:1.7}

/* ══ Apps tab ══ */
.apps-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.app-btn{
  display:flex;flex-direction:column;align-items:center;gap:8px;
  padding:16px 10px;
  background:var(--card-2);
  border:1px solid var(--card-border);
  border-radius:14px;
  transition:.18s;
}
.app-btn:hover{transform:translateY(-2px);border-color:var(--card-border-h);background:var(--card)}
.app-btn:active{transform:translateY(0) scale(.97)}
.app-btn i{font-size:26px;color:var(--accent)}
.app-btn span{font-size:11.5px;font-weight:700;color:var(--t1);text-align:center;line-height:1.3}

/* ══ Configs tab ══ */
.cfg-row{
  display:flex;align-items:center;gap:12px;
  padding:14px;
  background:var(--card-2);
  border:1px solid var(--card-border);
  border-radius:12px;
  margin-bottom:8px;
  transition:.15s;
}
.cfg-row:hover{border-color:var(--card-border-h)}
.cfg-row-icon{
  width:38px;height:38px;border-radius:10px;
  background:rgba(0,212,255,.1);color:var(--accent);
  display:flex;align-items:center;justify-content:center;
  font-size:17px;flex-shrink:0;
}
.cfg-row-info{flex:1;min-width:0}
.cfg-row-label{font-size:13px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cfg-row-meta{font-size:10.5px;color:var(--t3);margin-top:2px}
.cfg-row-actions{display:flex;gap:6px;flex-shrink:0}
.cfg-mini-btn{
  width:32px;height:32px;border-radius:8px;
  background:rgba(255,255,255,.03);
  border:1px solid var(--card-border);
  color:var(--t2);
  display:flex;align-items:center;justify-content:center;
  font-size:14px;transition:.15s;
}
html[data-theme="light"] .cfg-mini-btn{background:rgba(0,0,0,.02)}
.cfg-mini-btn:hover{background:rgba(0,212,255,.1);color:var(--accent);border-color:rgba(0,212,255,.3)}

/* ══ Footer ══ */
.sub-footer{
  display:flex;align-items:center;gap:8px;
  padding-top:18px;
  margin-top:20px;
  border-top:1px solid var(--card-border);
  font-size:11px;color:var(--t3);
  position:relative;z-index:1;
}
.sub-footer i{font-size:14px}

/* ══ Toast ══ */
.toast{
  position:fixed;bottom:28px;left:50%;
  transform:translateX(-50%) translateY(80px);
  z-index:400;padding:12px 20px;
  background:var(--card);border:1px solid var(--card-border-h);
  border-radius:12px;color:var(--t1);
  font-size:12.5px;font-weight:700;
  box-shadow:var(--shadow);
  display:flex;align-items:center;gap:8px;
  opacity:0;transition:all .3s cubic-bezier(.34,1.56,.64,1);
  pointer-events:none;white-space:nowrap;
}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(34,197,94,.4);background:var(--green-bg);color:var(--green)}
.toast.err{border-color:rgba(239,68,68,.4);background:var(--red-bg);color:var(--red)}

/* ══ Loading skeleton ══ */
.skel{
  background:linear-gradient(90deg,var(--card-2) 0%,var(--card-border) 50%,var(--card-2) 100%);
  background-size:200% 100%;animation:skel 1.5s ease-in-out infinite;border-radius:14px;
}
@keyframes skel{0%{background-position:200% 0}100%{background-position:-200% 0}}

/* ══ Responsive ══ */
@media(max-width:640px){
  body{padding:16px 10px;align-items:flex-start}
  .sub-card{padding:20px;border-radius:20px}
  .usage-hero{grid-template-columns:1fr;gap:20px;justify-items:center}
  .usage-left{width:100%}
  .usage-right{width:100%;grid-template-columns:1fr 1fr}
  .circle-wrap{width:130px;height:130px}
  .usage-remaining-val{font-size:36px}
  .tabs{gap:0;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .tab{padding:10px 12px 12px;font-size:12px}
  .qr-section{flex-direction:column;text-align:center;gap:16px}
  .apps-grid{grid-template-columns:repeat(3,1fr);gap:8px}
  .app-btn{padding:12px 6px}
  .app-btn i{font-size:22px}
  .app-btn span{font-size:10.5px}
  .sub-url-row{flex-wrap:wrap}
  .sub-url-text{font-size:11px;flex-basis:100%}
}
</style>
</head>
<body>

<div class="sub-card" id="root">
  <div class="skel" style="height:80px;margin-bottom:20px"></div>
  <div class="skel" style="height:200px;margin-bottom:20px"></div>
  <div class="skel" style="height:120px"></div>
</div>

<div class="toast" id="toast"></div>

<svg width="0" height="0" style="position:absolute">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7"/>
      <stop offset="100%" stop-color="#00d4ff"/>
    </linearGradient>
  </defs>
</svg>

<script>
const UUID = "__UUID_KEY__";
const SP = "omid_one_";
let LANG = localStorage.getItem(SP+"lang") || "en";
let THEME = localStorage.getItem(SP+"theme") || "dark";
let DATA = null;
let DEFAULT_CLIENT = localStorage.getItem(SP+"client") || "v2rayng";

const T = {
  en: {
    title:"Subscription info",
    remaining:"Remaining", of:"of", usage:"Usage",
    days_left:"Days left", expiry:"Expiry", status:"Status",
    downloaded:"Downloaded", uploaded:"Uploaded", total_quota:"Total quota",
    last_online:"Last Online",
    active:"Active", expired:"Expired", disabled:"Disabled",
    tab_sub:"Subscription", tab_apps:"Apps", tab_configs:"Configs",
    scan_phone:"Scan with your phone",
    scan_desc:"Scan this code in your VPN app to add the subscription without copying the link.",
    auto_update:"Auto-updates every 12 hours",
    copied:"Copied ✓", copy_failed:"Copy failed",
    unlimited:"Unlimited", never:"Never",
    no_configs:"No configurations",
    import_hint:"Open with:",
    share_text:"OMID Subscription"
  },
  fa: {
    title:"اطلاعات اشتراک",
    remaining:"باقی‌مانده", of:"از", usage:"مصرف",
    days_left:"روز باقی‌مانده", expiry:"انقضا", status:"وضعیت",
    downloaded:"دانلود", uploaded:"آپلود", total_quota:"سهمیه کل",
    last_online:"آخرین اتصال",
    active:"فعال", expired:"منقضی", disabled:"غیرفعال",
    tab_sub:"اشتراک", tab_apps:"اپلیکیشن", tab_configs:"کانفیگ‌ها",
    scan_phone:"با گوشی اسکن کنید",
    scan_desc:"این کد را در اپ VPN اسکن کنید تا اشتراک بدون کپی لینک اضافه شود.",
    auto_update:"بروزرسانی خودکار هر ۱۲ ساعت",
    copied:"کپی شد ✓", copy_failed:"کپی نشد",
    unlimited:"نامحدود", never:"هیچ‌وقت",
    no_configs:"کانفیگی وجود ندارد",
    import_hint:"باز کن با:",
    share_text:"اشتراک OMID"
  }
};

const CLIENTS = [
  { id:"v2rayng",   name:"v2rayNG",   icon:"ti-brand-android", scheme:u=>u },
  { id:"nekobox",   name:"NekoBox",   icon:"ti-cat",           scheme:u=>u },
  { id:"singbox",   name:"Sing-Box",  icon:"ti-box",           scheme:u=>"sing-box://import-remote-profile?url="+encodeURIComponent(u)+"#OMID" },
  { id:"streisand", name:"Streisand", icon:"ti-apple",         scheme:u=>"streisand://import/"+encodeURIComponent(u) },
  { id:"shadowrocket",name:"Shadowrocket",icon:"ti-rocket",    scheme:u=>"sub://"+btoa(u) },
  { id:"clash",     name:"Clash",     icon:"ti-sword",         scheme:u=>"clash://install-config?url="+encodeURIComponent(u) },
  { id:"hiddify",   name:"Hiddify",   icon:"ti-shield-check",  scheme:u=>"hiddify://import/"+encodeURIComponent(u) },
  { id:"foxray",    name:"FoXray",    icon:"ti-brand-firefox", scheme:u=>"foxray://install-config?url="+encodeURIComponent(u) },
  { id:"v2rayn",    name:"v2rayN",    icon:"ti-brand-windows", scheme:u=>u }
];

function t(k){return (T[LANG] && T[LANG][k]) || T.en[k] || k}

function esc(s){return String(s||"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}

function fmtDate(iso){
  if(!iso) return t("never");
  try{
    const d = new Date(iso);
    const loc = LANG==="fa" ? "fa-IR" : "en-US";
    return d.toLocaleString(loc, {year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit"});
  }catch(e){return iso}
}

function daysLeft(iso){
  if(!iso) return null;
  try{
    const d = Math.ceil((new Date(iso) - Date.now()) / 864e5);
    return d > 0 ? d : 0;
  }catch(e){return null}
}

function applyTheme(){
  // فقط dark/light — auto حذف شد
  const th = THEME === "light" ? "light" : "dark";
  THEME = th;
  document.documentElement.setAttribute("data-theme", th);
  const btn = document.getElementById("theme-btn");
  if(btn) btn.innerHTML = '<i class="ti '+(th==="dark"?"ti-moon":"ti-sun")+'"></i>';
  const meta = document.getElementById("meta-theme");
  if(meta) meta.setAttribute("content", th==="dark"?"#0a0a14":"#f0f0f7");
}

function toggleTheme(){
  // فقط ۲ حالت: dark ↔ light
  THEME = THEME === "dark" ? "light" : "dark";
  localStorage.setItem(SP+"theme", THEME);
  applyTheme();
}

function toggleLang(){
  LANG = LANG==="fa" ? "en" : "fa";
  localStorage.setItem(SP+"lang", LANG);
  applyLang();
  if(DATA) render(DATA);
}

function applyLang(){
  document.documentElement.lang = LANG;
  document.documentElement.dir = LANG==="fa" ? "rtl" : "ltr";
  const btn = document.getElementById("lang-btn");
  if(btn) btn.textContent = LANG==="fa" ? "EN" : "FA";
}

function toast(msg, type){
  const el = document.getElementById("toast");
  el.className = "toast show" + (type ? " "+type : "");
  el.innerHTML = '<i class="ti '+(type==="ok"?"ti-circle-check":type==="err"?"ti-alert-circle":"ti-info-circle")+'"></i> '+esc(msg);
  clearTimeout(window.__t);
  window.__t = setTimeout(()=>el.classList.remove("show"), 2200);
}

async function copyText(text){
  try{ await navigator.clipboard.writeText(text); toast(t("copied"),"ok"); }
  catch(e){
    const ta = document.createElement("textarea"); ta.value = text;
    ta.style.position="fixed"; ta.style.opacity="0";
    document.body.appendChild(ta); ta.select();
    try{document.execCommand("copy");toast(t("copied"),"ok")}catch(_){toast(t("copy_failed"),"err")}
    document.body.removeChild(ta);
  }
}

function switchTab(name){
  document.querySelectorAll(".tab").forEach(x=>x.classList.toggle("active", x.dataset.tab===name));
  document.querySelectorAll(".tab-content").forEach(x=>x.classList.toggle("active", x.id==="tab-"+name));
}

function protoName(p){
  if(!p||p==="vless-ws") return "VLESS · WebSocket";
  if(p==="xhttp-packet-up") return "XHTTP · packet-up";
  if(p==="xhttp-stream-up") return "XHTTP · stream-up";
  if(p==="xhttp-stream-one") return "XHTTP Ultra";
  return p;
}

function launchClient(id){
  const c = CLIENTS.find(x=>x.id===id);
  if(!c || !DATA) return;
  const url = DATA.sub_url;
  const deep = typeof c.scheme==="function" ? c.scheme(url) : url;
  DEFAULT_CLIENT = id;
  localStorage.setItem(SP+"client", id);
  if(deep === url){
    copyText(url);
  }else{
    try{
      window.location.href = deep;
      setTimeout(()=>copyText(url), 600);
    }catch(e){copyText(url)}
  }
}

function showQR(){
  document.getElementById("qr-modal").classList.add("show");
}
function closeQR(){
  document.getElementById("qr-modal").classList.remove("show");
}

function render(d){
  DATA = d;

  const isFa = LANG==="fa";
  const used = d.used_bytes || 0;
  const limit = d.limit_bytes || 0;
  const remaining = d.remaining_bytes || 0;
  const pct = limit === 0 ? 0 : Math.min(100, (used / limit) * 100);
  const dLeft = daysLeft(d.expires_at);
  const isExpired = d.expired || (dLeft !== null && dLeft === 0);
  const isActive = d.active && !isExpired;
  const statusKey = isActive ? "active" : (isExpired ? "expired" : "disabled");
  const statusClass = isActive ? "" : "off";

  // Circle math
  const R = 66;
  const C = 2 * Math.PI * R;
  const offset = C * (1 - (100 - pct)/100); // 0% = empty, 100% = full
  // در واقع: با pct=0 → offset=C (خالی)، pct=100 → offset=0 (پر)
  const dashOffset = C * (1 - pct / 100);

  const apps = CLIENTS.map(c=>`
    <button class="app-btn" onclick="launchClient('${c.id}')" title="${esc(c.name)}">
      <i class="ti ${c.icon}"></i>
      <span>${esc(c.name)}</span>
    </button>
  `).join("");

  const html = `
    <div class="sub-header">
      <div class="sub-brand">
        <div class="sub-logo">
          <img src="data:image/png;base64,__LOGO_B64__" alt="OMID" onerror="this.style.display='none';this.parentNode.innerHTML='<i class=\\'ti ti-rocket\\'></i>'">
        </div>
        <div>
          <div class="sub-title">${t("title")}</div>
          <div class="sub-subtitle">${esc(d.label)}${d.note ? " · "+esc(d.note) : ""}</div>
        </div>
      </div>
      <div class="sub-actions">
        <button class="icon-btn" onclick="toggleTheme()" id="theme-btn" title="Theme">
          <i class="ti ti-moon"></i>
        </button>
        <button class="icon-btn" onclick="toggleLang()" id="lang-btn" title="Language">
          ${LANG==="fa" ? "EN" : "FA"}
        </button>
      </div>
    </div>

    <div class="usage-hero">
      <div class="usage-left">
        <div class="usage-remaining-label">${t("remaining")}</div>
        <div class="usage-remaining-val">${esc(d.remaining_fmt || "0 B").split(" ")[0]}<span>${esc((d.remaining_fmt || "0 B").split(" ")[1] || "")}</span></div>
        <div class="usage-of">${t("of")} ${esc(d.limit_fmt || "∞")}</div>

        <div class="circle-wrap">
          <svg viewBox="0 0 150 150">
            <circle class="circle-bg" cx="75" cy="75" r="${R}"/>
            <circle class="circle-fg" cx="75" cy="75" r="${R}"
              stroke-dasharray="${C.toFixed(2)}"
              stroke-dashoffset="${dashOffset.toFixed(2)}"/>
          </svg>
          <div class="circle-center">
            <div class="circle-pct">${pct.toFixed(1)}%</div>
            <div class="circle-label">${t("usage")}</div>
          </div>
        </div>
      </div>

      <div class="usage-right">
        <div class="info-tile">
          <div class="info-label">${t("days_left")}</div>
          <div class="info-val accent">${dLeft === null ? t("unlimited") : dLeft}</div>
        </div>
        <div class="info-tile">
          <div class="info-label">${t("expiry")}</div>
          <div class="info-val">${esc(fmtDate(d.expires_at))}</div>
        </div>
        <div class="info-tile">
          <div class="info-label">${t("status")}</div>
          <div class="info-val"><span class="status-pill ${statusClass}"><span class="status-dot"></span>${t(statusKey)}</span></div>
        </div>
        <div class="info-tile">
          <div class="info-label">${t("downloaded")}</div>
          <div class="info-val green">${esc(d.down_fmt || "0 B")}</div>
        </div>
        <div class="info-tile">
          <div class="info-label">${t("uploaded")}</div>
          <div class="info-val green">${esc(d.up_fmt || "0 B")}</div>
        </div>
        <div class="info-tile">
          <div class="info-label">${t("total_quota")}</div>
          <div class="info-val accent">${esc(d.limit_fmt || "∞")}</div>
        </div>
        <div class="info-tile" style="grid-column:1/-1">
          <div class="info-label">${t("last_online")}</div>
          <div class="info-val">${esc(fmtDate(d.last_online))}</div>
        </div>
      </div>
    </div>

    <div class="tabs">
      <div class="tab active" data-tab="sub" onclick="switchTab('sub')">
        <i class="ti ti-link"></i> ${t("tab_sub")}
      </div>
      <div class="tab" data-tab="apps" onclick="switchTab('apps')">
        <i class="ti ti-apps"></i> ${t("tab_apps")}
      </div>
      <div class="tab" data-tab="configs" onclick="switchTab('configs')">
        <i class="ti ti-list"></i> ${t("tab_configs")} <span class="tab-count">1</span>
      </div>
    </div>

    <div class="tab-content active" id="tab-sub">
      <div class="sub-url-row">
        <span class="sub-url-badge">SUB</span>
        <span class="sub-url-text" id="sub-url-text">${esc(d.sub_url)}</span>
        <button class="sub-url-copy" onclick="copyText('${esc(d.sub_url)}')" title="Copy">
          <i class="ti ti-copy"></i>
        </button>
        <button class="sub-url-copy" onclick="showQR()" title="QR">
          <i class="ti ti-qrcode"></i>
        </button>
      </div>

      <div class="qr-section">
        <div class="qr-img">
          <img src="https://api.qrserver.com/v1/create-qr-code/?size=280x280&data=${encodeURIComponent(d.sub_url)}&bgcolor=ffffff&color=000000&margin=0" alt="QR">
        </div>
        <div class="qr-text">
          <h4>${t("scan_phone")}</h4>
          <p>${t("scan_desc")}</p>
        </div>
      </div>
    </div>

    <div class="tab-content" id="tab-apps">
      <div class="apps-grid">${apps}</div>
    </div>

    <div class="tab-content" id="tab-configs">
      <div class="cfg-row">
        <div class="cfg-row-icon"><i class="ti ti-key"></i></div>
        <div class="cfg-row-info">
          <div class="cfg-row-label">${esc(d.label)}</div>
          <div class="cfg-row-meta">${esc(protoName(d.protocol))}</div>
        </div>
        <div class="cfg-row-actions">
          <button class="cfg-mini-btn" onclick="copyText('${esc(d.vless_link)}')" title="Copy">
            <i class="ti ti-copy"></i>
          </button>
          <button class="cfg-mini-btn" onclick="showQR()" title="QR">
            <i class="ti ti-qrcode"></i>
          </button>
        </div>
      </div>
    </div>

    <div class="sub-footer">
      <i class="ti ti-refresh"></i> ${t("auto_update")}
    </div>
  `;

  document.getElementById("root").innerHTML = html;
  applyTheme();
  applyLang();
}

// QR Modal
function injectQrModal(){
  if(document.getElementById("qr-modal")) return;
  const modal = document.createElement("div");
  modal.id = "qr-modal";
  modal.style.cssText = "position:fixed;inset:0;z-index:500;background:rgba(0,0,0,.85);backdrop-filter:blur(10px);display:none;align-items:center;justify-content:center;padding:20px";
  modal.onclick = closeQR;
  modal.innerHTML = `
    <div onclick="event.stopPropagation()" style="background:var(--card);border:1px solid var(--card-border);border-radius:20px;padding:24px;text-align:center;max-width:380px;width:100%">
      <div style="font-size:14px;font-weight:800;color:var(--t1);margin-bottom:16px">
        <i class="ti ti-qrcode"></i> QR
      </div>
      <div style="background:#fff;border-radius:14px;padding:14px;display:inline-block;margin-bottom:16px">
        <img id="qr-modal-img" src="" style="width:280px;height:280px;display:block;border-radius:8px">
      </div>
      <button onclick="closeQR()" style="width:100%;padding:11px;border-radius:11px;background:var(--card-2);border:1px solid var(--card-border);color:var(--t1);font-weight:700;font-family:inherit">
        ${LANG==="fa"?"بستن":"Close"}
      </button>
    </div>
  `;
  document.body.appendChild(modal);
  const style = document.createElement("style");
  style.textContent = "#qr-modal.show{display:flex!important}";
  document.head.appendChild(style);
}

async function load(){
  try{
    const r = await fetch("/api/public/one/"+UUID, {cache:"no-store"});
    if(!r.ok) throw new Error("HTTP "+r.status);
    const d = await r.json();
    render(d);
  }catch(e){
    document.getElementById("root").innerHTML = `
      <div style="text-align:center;padding:60px 20px;color:var(--red)">
        <i class="ti ti-alert-circle" style="font-size:48px;opacity:.5;display:block;margin-bottom:14px"></i>
        <div style="font-size:15px;font-weight:700">${t("copy_failed")}</div>
      </div>`;
  }
}

(async function init(){
  applyTheme();
  applyLang();
  injectQrModal();
  await load();
  // Auto refresh هر 30 ثانیه
  setInterval(load, 30000);
})();
</script>
</body></html>'''

SINGLE_CONFIG_HTML_TEMPLATE = SINGLE_CONFIG_HTML_TEMPLATE.replace("__LOGO_B64__", LOGO_B64)


def get_single_config_page_html(uuid: str) -> str:
    """صفحه‌ی UI برای یه کانفیگ تکی — طراحی Subscription Info مثل Marzban."""
    return SINGLE_CONFIG_HTML_TEMPLATE.replace("__UUID_KEY__", uuid)

# ═══════════════════════════════════════════════════════════════════════
# Admin page — همه‌ی کانفیگ‌ها (Marzban-style dashboard)
# ═══════════════════════════════════════════════════════════════════════
ADMIN_ALL_HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#0a0a14" id="meta-theme">
<title>Admin · All Configs · OMID</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#0a0a14;
  --bg-grad:radial-gradient(ellipse 900px 600px at 20% -10%,rgba(168,85,247,.12),transparent 60%),
            radial-gradient(ellipse 700px 500px at 90% 110%,rgba(0,212,255,.08),transparent 60%),
            #0a0a14;
  --card:#13131f;--card-2:#17172a;
  --card-border:rgba(255,255,255,.06);
  --card-border-h:rgba(255,255,255,.12);
  --accent:#00d4ff;--accent-2:#a855f7;
  --green:#22c55e;--green-bg:rgba(34,197,94,.12);
  --red:#ef4444;--red-bg:rgba(239,68,68,.12);
  --amber:#f59e0b;--amber-bg:rgba(245,158,11,.12);
  --purple:#a78bfa;--purple-bg:rgba(167,139,250,.12);
  --t1:#e8e8f0;--t2:#8a8aa8;--t3:#5a5a7a;
  --shadow:0 20px 60px rgba(0,0,0,.5);
  --font:'Vazirmatn','Inter',system-ui,sans-serif;
}
html[data-theme="light"]{
  --bg:#f0f0f7;
  --bg-grad:radial-gradient(ellipse 900px 600px at 20% -10%,rgba(168,85,247,.10),transparent 60%),
            radial-gradient(ellipse 700px 500px at 90% 110%,rgba(0,180,220,.08),transparent 60%),
            #f0f0f7;
  --card:#ffffff;--card-2:#f8f8fc;
  --card-border:rgba(0,0,0,.06);
  --card-border-h:rgba(0,0,0,.12);
  --accent:#0088cc;--accent-2:#7c3aed;
  --green:#16a34a;--green-bg:rgba(22,163,74,.10);
  --red:#dc2626;--red-bg:rgba(220,38,38,.10);
  --amber:#d97706;--amber-bg:rgba(217,119,6,.10);
  --purple:#7c3aed;--purple-bg:rgba(124,58,237,.08);
  --t1:#1a1a2e;--t2:#5a5a7a;--t3:#9a9ab0;
  --shadow:0 20px 60px rgba(50,50,100,.12);
}
html[dir="ltr"] body{font-family:'Inter','Vazirmatn',system-ui,sans-serif}
html,body{min-height:100%}
body{font-family:var(--font);background:var(--bg-grad);color:var(--t1);font-size:14px;
  line-height:1.5;transition:background .3s,color .3s;-webkit-font-smoothing:antialiased}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.1);border-radius:3px}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input{font-family:inherit}
a{color:inherit;text-decoration:none}

.wrap{max-width:960px;margin:0 auto;padding:20px 16px 40px}

/* HEADER */
.hd{display:flex;align-items:center;gap:14px;padding:16px 18px;
  background:var(--card);border:1px solid var(--card-border);border-radius:18px;
  margin-bottom:18px;position:relative;overflow:hidden}
.hd::before{content:"";position:absolute;top:-60px;right:-60px;width:200px;height:200px;
  background:radial-gradient(circle,rgba(168,85,247,.15),transparent 70%);pointer-events:none}
.hd-logo{width:44px;height:44px;border-radius:12px;overflow:hidden;flex-shrink:0;
  background:linear-gradient(135deg,var(--accent),var(--accent-2));
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 6px 20px rgba(0,212,255,.18)}
.hd-logo img{width:100%;height:100%;object-fit:cover}
.hd-info{flex:1;min-width:0;position:relative;z-index:1}
.hd-title{font-size:16px;font-weight:800;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.hd-title small{font-size:9px;font-weight:800;letter-spacing:.1em;padding:3px 8px;border-radius:6px;
  background:linear-gradient(135deg,var(--accent),var(--accent-2));color:#fff}
.hd-sub{font-size:11.5px;color:var(--t3);margin-top:2px}
.hd-actions{display:flex;gap:8px;position:relative;z-index:1}
.icon-btn{width:36px;height:36px;border-radius:10px;background:rgba(255,255,255,.03);
  border:1px solid var(--card-border);color:var(--t2);
  display:flex;align-items:center;justify-content:center;font-size:16px;transition:.15s}
html[data-theme="light"] .icon-btn{background:rgba(0,0,0,.02)}
.icon-btn:hover{background:rgba(255,255,255,.06);color:var(--t1);border-color:var(--card-border-h)}

/* TABS */
.tabs{display:flex;gap:4px;background:var(--card);border:1px solid var(--card-border);
  border-radius:14px;padding:5px;margin-bottom:18px;overflow-x:auto}
.tab{flex:1;display:flex;align-items:center;justify-content:center;gap:6px;
  padding:10px 14px;border-radius:10px;font-size:12.5px;font-weight:700;
  color:var(--t3);transition:.15s;white-space:nowrap;cursor:pointer}
.tab i{font-size:15px}
.tab:hover{color:var(--t2);background:rgba(255,255,255,.03)}
.tab.active{background:linear-gradient(135deg,var(--accent),var(--accent-2));color:#fff;
  box-shadow:0 4px 14px rgba(0,212,255,.25)}
.tab.active i{filter:drop-shadow(0 0 4px rgba(255,255,255,.5))}

.tab-panel{display:none;animation:fadeIn .25s ease}
.tab-panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}

/* HERO */
.hero{background:linear-gradient(155deg,rgba(168,85,247,.12) 0%,var(--card) 55%);
  border:1px solid var(--card-border);border-radius:22px;padding:24px;
  margin-bottom:16px;position:relative;overflow:hidden}
.hero::before{content:"";position:absolute;top:-80px;right:-80px;width:260px;height:260px;
  background:radial-gradient(circle,rgba(168,85,247,.18),transparent 70%);pointer-events:none}
.hero-main{display:flex;align-items:center;gap:24px;position:relative;z-index:1;flex-wrap:wrap}
.hero-num{font-size:42px;font-weight:900;letter-spacing:-.03em;line-height:1;
  color:var(--accent);text-shadow:0 0 24px rgba(0,212,255,.25)}
.hero-lbl{font-size:11px;color:var(--t3);font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.hero-desc{font-size:12px;color:var(--t2);margin-top:6px}

.hero-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;
  margin-top:20px;position:relative;z-index:1}
.stat{background:var(--card-2);border:1px solid var(--card-border);
  border-radius:14px;padding:12px 14px;transition:.15s}
.stat:hover{border-color:var(--card-border-h);transform:translateY(-2px)}
.stat-l{font-size:9.5px;color:var(--t3);font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:5px;
  display:flex;align-items:center;gap:4px}
.stat-l i{font-size:11px}
.stat-v{font-size:20px;font-weight:800;letter-spacing:-.02em}
.stat.green .stat-v{color:var(--green)}
.stat.red .stat-v{color:var(--red)}
.stat.amber .stat-v{color:var(--amber)}
.stat.purple .stat-v{color:var(--purple)}

/* URL ROW */
.url-row{display:flex;align-items:center;gap:12px;background:var(--card);
  border:1px solid var(--card-border);border-radius:14px;padding:14px 16px;
  margin-bottom:16px;flex-wrap:wrap}
.url-badge{font-size:9px;font-weight:800;letter-spacing:.08em;
  background:var(--green-bg);color:var(--green);padding:4px 8px;border-radius:6px;flex-shrink:0}
.url-text{flex:1;min-width:200px;font-family:ui-monospace,monospace;font-size:12px;
  color:var(--t2);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.url-btn{width:34px;height:34px;border-radius:9px;background:rgba(255,255,255,.04);
  border:1px solid var(--card-border);color:var(--t2);
  display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;transition:.15s}
.url-btn:hover{background:rgba(0,212,255,.1);color:var(--accent);border-color:rgba(0,212,255,.3)}

/* FILTER */
.toolbar{display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap}
.search{flex:1;min-width:200px;position:relative}
.search input{width:100%;padding:11px 40px 11px 14px;border-radius:12px;
  border:1px solid var(--card-border);background:var(--card);color:var(--t1);
  font-size:12.5px;outline:none;transition:.15s}
.search input:focus{border-color:rgba(0,212,255,.4);box-shadow:0 0 0 3px rgba(0,212,255,.08)}
.search i{position:absolute;top:50%;transform:translateY(-50%);
  left:14px;color:var(--t3);font-size:15px;pointer-events:none}
html[dir="ltr"] .search i{left:auto;right:14px}
html[dir="ltr"] .search input{padding:11px 14px 11px 40px}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip-f{font-size:11.5px;font-weight:700;padding:8px 14px;border-radius:10px;
  background:var(--card);border:1px solid var(--card-border);color:var(--t2);
  cursor:pointer;transition:.15s;white-space:nowrap}
.chip-f:hover{border-color:var(--card-border-h);color:var(--t1)}
.chip-f.active{background:linear-gradient(135deg,var(--accent),var(--accent-2));color:#fff;
  border-color:transparent;box-shadow:0 4px 12px rgba(0,212,255,.2)}

/* SECTION */
.section{margin-bottom:18px}
.section-head{display:flex;align-items:center;gap:10px;margin-bottom:10px;padding:0 4px}
.section-ic{width:34px;height:34px;border-radius:10px;
  background:var(--purple-bg);color:var(--purple);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.section-title{font-size:14px;font-weight:800;color:var(--t1)}
.section-sub{font-size:10.5px;color:var(--t3);margin-top:2px}
.section-count{margin-inline-start:auto;font-size:10.5px;font-weight:700;
  color:var(--accent);background:rgba(0,212,255,.1);padding:4px 10px;border-radius:20px}

/* CFG CARD */
.cfg-card{background:var(--card);border:1px solid var(--card-border);
  border-radius:14px;padding:14px 16px;margin-bottom:8px;transition:.15s;
  position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-border-h)}
.cfg-card::before{content:"";position:absolute;top:14px;bottom:14px;
  inset-inline-start:0;width:3px;border-radius:3px;background:var(--green)}
.cfg-card.off::before{background:var(--red)}
.cfg-card.exp::before{background:var(--amber)}
.cfg-top{display:flex;align-items:flex-start;gap:12px}
.cfg-ic{width:38px;height:38px;border-radius:10px;
  background:rgba(0,212,255,.1);color:var(--accent);
  display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.cfg-info{flex:1;min-width:0}
.cfg-label{font-size:13.5px;font-weight:800;margin-bottom:5px;word-break:break-word}
.cfg-badges{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px}
.chip{font-size:9.5px;font-weight:700;padding:3px 8px;border-radius:7px;white-space:nowrap;
  display:inline-flex;align-items:center;gap:3px}
.chip.ws{background:rgba(0,212,255,.12);color:var(--accent)}
.chip.xhttp{background:var(--purple-bg);color:var(--purple)}
.chip.green{background:var(--green-bg);color:var(--green)}
.chip.red{background:var(--red-bg);color:var(--red)}
.chip.amber{background:var(--amber-bg);color:var(--amber)}
.cfg-usage-track{height:5px;border-radius:3px;background:rgba(0,0,0,.2);
  overflow:hidden;margin-bottom:5px}
.cfg-usage-fill{height:100%;border-radius:3px;
  background:linear-gradient(90deg,var(--accent),var(--accent-2));transition:width .4s}
.cfg-usage-lbl{display:flex;justify-content:space-between;font-size:10px;color:var(--t3)}
.cfg-actions{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px;
  padding-top:12px;border-top:1px solid var(--card-border)}
.cfg-btn{display:flex;align-items:center;gap:5px;padding:8px 12px;border-radius:9px;
  font-size:11px;font-weight:700;background:rgba(255,255,255,.03);
  border:1px solid var(--card-border);color:var(--t2);transition:.15s;cursor:pointer}
.cfg-btn:hover{background:rgba(0,212,255,.1);color:var(--accent);border-color:rgba(0,212,255,.3)}
.cfg-btn.primary{background:linear-gradient(135deg,var(--accent),var(--accent-2));
  color:#fff;border-color:transparent}
.cfg-btn.primary:hover{filter:brightness(1.08);color:#fff}

.group-block{background:var(--card);border:1px solid var(--card-border);
  border-radius:18px;margin-bottom:14px;overflow:hidden}
.group-head{display:flex;align-items:center;gap:12px;padding:16px 18px;
  background:linear-gradient(155deg,rgba(168,85,247,.1) 0%,transparent 60%);
  cursor:pointer;transition:.15s}
.group-head:hover{background:linear-gradient(155deg,rgba(168,85,247,.16) 0%,transparent 60%)}
.group-ic{width:40px;height:40px;border-radius:11px;
  background:linear-gradient(135deg,var(--purple),var(--accent-2));
  display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0}
.group-info{flex:1;min-width:0}
.group-name{font-size:14px;font-weight:800;display:flex;align-items:center;gap:6px}
.group-name .lock{font-size:11px;color:var(--amber)}
.group-meta{font-size:10.5px;color:var(--t3);margin-top:2px}
.group-toggle{color:var(--t3);font-size:18px;transition:.25s}
.group-body{padding:0 14px 14px;display:none}
.group-block.open .group-body{display:block}
.group-block.open .group-toggle{transform:rotate(180deg)}
.group-actions{display:flex;gap:6px;margin-bottom:10px;padding-top:2px;flex-wrap:wrap}

/* EMPTY */
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:42px;opacity:.3;display:block;margin-bottom:12px}
.empty-title{font-size:13.5px;font-weight:700;color:var(--t2)}
.empty-sub{font-size:11px;margin-top:4px}

/* TOAST */
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(80px);
  z-index:500;padding:12px 22px;background:var(--card);
  border:1px solid var(--card-border-h);border-radius:12px;color:var(--t1);
  font-size:12.5px;font-weight:700;box-shadow:var(--shadow);
  display:flex;align-items:center;gap:8px;
  opacity:0;transition:all .3s cubic-bezier(.34,1.56,.64,1);
  pointer-events:none;white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{background:var(--green-bg);border-color:rgba(34,197,94,.4);color:var(--green)}
.toast.err{background:var(--red-bg);border-color:rgba(239,68,68,.4);color:var(--red)}

/* SKELETON */
.skel{background:linear-gradient(90deg,var(--card-2) 0%,var(--card-border) 50%,var(--card-2) 100%);
  background-size:200% 100%;animation:skel 1.5s infinite;border-radius:14px;height:120px;margin-bottom:10px}
@keyframes skel{0%{background-position:200% 0}100%{background-position:-200% 0}}

@media(max-width:640px){
  .hero-stats{grid-template-columns:repeat(2,1fr)}
  .hero-num{font-size:36px}
  .tabs{flex-wrap:nowrap;overflow-x:auto}
  .tab{padding:10px 12px;font-size:11.5px;flex:0 0 auto}
}
</style>
</head>
<body>

<div class="wrap">

  <!-- HEADER -->
  <div class="hd">
    <div class="hd-logo"><img src="data:image/png;base64,__LOGO_B64__" alt="OMID"></div>
    <div class="hd-info">
      <div class="hd-title">OMID Network <small>ADMIN</small></div>
      <div class="hd-sub" id="hdSub">همه‌ی کانفیگ‌ها · پنل مدیریتی</div>
    </div>
    <div class="hd-actions">
      <button class="icon-btn" onclick="toggleTheme()" id="themeBtn" title="Theme"><i class="ti ti-moon"></i></button>
      <button class="icon-btn" onclick="toggleLang()" id="langBtn" title="Language">EN</button>
    </div>
  </div>

  <!-- TABS -->
  <div class="tabs">
    <div class="tab active" data-tab="overview" onclick="switchTab('overview')">
      <i class="ti ti-layout-dashboard"></i><span data-i18n="tab_overview">Overview</span>
    </div>
    <div class="tab" data-tab="configs" onclick="switchTab('configs')">
      <i class="ti ti-list"></i><span data-i18n="tab_configs">Configs</span>
    </div>
    <div class="tab" data-tab="groups" onclick="switchTab('groups')">
      <i class="ti ti-folders"></i><span data-i18n="tab_groups">Groups</span>
    </div>
  </div>

  <!-- LOADING -->
  <div id="loading">
    <div class="skel"></div>
    <div class="skel" style="height:180px"></div>
    <div class="skel" style="height:80px"></div>
  </div>

  <!-- TAB: OVERVIEW -->
  <div class="tab-panel active" id="tab-overview" style="display:none">
    <div class="hero">
      <div class="hero-main">
        <div>
          <div class="hero-lbl" data-i18n="total_usage">کل مصرف</div>
          <div class="hero-num" id="heroTotal">—</div>
          <div class="hero-desc" id="heroSub">—</div>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat"><div class="stat-l"><i class="ti ti-keys"></i> <span data-i18n="total">کل کانفیگ</span></div><div class="stat-v" id="sTotal">—</div></div>
        <div class="stat green"><div class="stat-l"><i class="ti ti-circle-check"></i> <span data-i18n="active">فعال</span></div><div class="stat-v" id="sActive">—</div></div>
        <div class="stat amber"><div class="stat-l"><i class="ti ti-calendar-x"></i> <span data-i18n="expired">منقضی</span></div><div class="stat-v" id="sExpired">—</div></div>
        <div class="stat red"><div class="stat-l"><i class="ti ti-circle-x"></i> <span data-i18n="disabled">غیرفعال</span></div><div class="stat-v" id="sDisabled">—</div></div>
      </div>
    </div>

    <div class="url-row">
      <span class="url-badge">SUB-ALL</span>
      <span class="url-text" id="subAllUrl">—</span>
      <button class="url-btn" onclick="copySubAll()" title="Copy"><i class="ti ti-copy"></i></button>
      <button class="url-btn" onclick="showQR('Sub-All', document.getElementById('subAllUrl').textContent)" title="QR"><i class="ti ti-qrcode"></i></button>
    </div>

    <div class="section">
      <div class="section-head">
        <div class="section-ic"><i class="ti ti-bolt"></i></div>
        <div>
          <div class="section-title" data-i18n="quick_preview">پیش‌نمایش سریع</div>
          <div class="section-sub" data-i18n="quick_sub">آخرین کانفیگ‌های ساخته‌شده</div>
        </div>
        <span class="section-count" id="quickCount">0</span>
      </div>
      <div id="quickList"></div>
    </div>
  </div>

  <!-- TAB: CONFIGS -->
  <div class="tab-panel" id="tab-configs">
    <div class="toolbar">
      <div class="search">
        <i class="ti ti-search"></i>
        <input type="text" id="searchInp" placeholder="جستجو..." oninput="renderConfigs()">
      </div>
    </div>
    <div class="toolbar" style="margin-bottom:14px">
      <div class="chips" id="filterChips">
        <button class="chip-f active" data-filter="all" onclick="setFilter('all',this)">All</button>
        <button class="chip-f" data-filter="active" onclick="setFilter('active',this)">Active</button>
        <button class="chip-f" data-filter="expired" onclick="setFilter('expired',this)">Expired</button>
        <button class="chip-f" data-filter="disabled" onclick="setFilter('disabled',this)">Disabled</button>
      </div>
    </div>
    <div id="cfgListWrap"></div>
  </div>

  <!-- TAB: GROUPS -->
  <div class="tab-panel" id="tab-groups">
    <div class="toolbar">
      <div class="search">
        <i class="ti ti-search"></i>
        <input type="text" id="searchGrp" placeholder="جستجو در گروه‌ها..." oninput="renderGroups()">
      </div>
    </div>
    <div id="grpListWrap"></div>
  </div>

</div>

<div class="toast" id="toast"></div>

<script>
const SP = "omid_admin_";
let LANG = localStorage.getItem(SP+"lang") || "fa";
let THEME = localStorage.getItem(SP+"theme") || "dark";
let DATA = null;
let FILTER = "all";
let TAB = "overview";

const T = {
  fa: {
    tab_overview:"نمای کلی", tab_configs:"کانفیگ‌ها", tab_groups:"گروه‌ها",
    total_usage:"کل مصرف", total:"کل کانفیگ", active:"فعال", expired:"منقضی", disabled:"غیرفعال",
    quick_preview:"پیش‌نمایش سریع", quick_sub:"آخرین کانفیگ‌های ساخته‌شده",
    ungrouped:"بدون گروه", groups:"گروه‌های ساب",
    copied:"کپی شد ✓", copy_failed:"کپی نشد", link:"لینک", sub:"ساب", qr:"QR",
    import:"افزودن به کلاینت", unlimited:"نامحدود", connections:"اتصال",
    empty_title:"هیچ کانفیگی نیست", empty_sub:"هنوز کانفیگی ساخته نشده",
    empty_filter:"موردی با این فیلتر پیدا نشد",
    loading:"در حال بارگذاری..."
  },
  en: {
    tab_overview:"Overview", tab_configs:"Configs", tab_groups:"Groups",
    total_usage:"Total Usage", total:"Total", active:"Active", expired:"Expired", disabled:"Disabled",
    quick_preview:"Quick Preview", quick_sub:"Latest configurations",
    ungrouped:"Ungrouped", groups:"Subscription Groups",
    copied:"Copied ✓", copy_failed:"Copy failed", link:"Link", sub:"Sub", qr:"QR",
    import:"Import", unlimited:"Unlimited", connections:"conn",
    empty_title:"No configurations", empty_sub:"No configs created yet",
    empty_filter:"No matches for this filter",
    loading:"Loading..."
  }
};
function t(k){return (T[LANG] && T[LANG][k]) || T.fa[k] || k}

function esc(s){return String(s||"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}

function fmtBytes(b){
  if(!b||b===0) return "0 B";
  if(b<1024) return b+" B";
  if(b<1048576) return (b/1024).toFixed(1)+" KB";
  if(b<1073741824) return (b/1048576).toFixed(2)+" MB";
  return (b/1073741824).toFixed(2)+" GB";
}

function fmtDate(iso){
  if(!iso) return "—";
  try{
    const d = new Date(iso);
    const loc = LANG==="fa" ? "fa-IR" : "en-US";
    return d.toLocaleDateString(loc,{year:"numeric",month:"2-digit",day:"2-digit"});
  }catch(e){return iso}
}

function daysLeft(iso){
  if(!iso) return null;
  try{
    const d = Math.ceil((new Date(iso) - Date.now()) / 864e5);
    return d > 0 ? d : 0;
  }catch(e){return null}
}

function protoName(p){
  if(!p||p==="vless-ws") return "VLESS · WS";
  if(p==="xhttp-packet-up") return "XHTTP · packet-up";
  if(p==="xhttp-stream-up") return "XHTTP · stream-up";
  if(p==="xhttp-stream-one") return "XHTTP Ultra";
  return p;
}
function protoClass(p){
  if(!p) return "ws";
  if(p.startsWith("xhttp")) return "xhttp";
  return "ws";
}

function applyTheme(){
  const th = THEME === "light" ? "light" : "dark";
  THEME = th;
  document.documentElement.setAttribute("data-theme", th);
  const btn = document.getElementById("themeBtn");
  if(btn) btn.innerHTML = '<i class="ti '+(th==="dark"?"ti-moon":"ti-sun")+'"></i>';
  const meta = document.getElementById("meta-theme");
  if(meta) meta.setAttribute("content", th==="dark"?"#0a0a14":"#f0f0f7");
}
function toggleTheme(){
  THEME = THEME === "dark" ? "light" : "dark";
  localStorage.setItem(SP+"theme", THEME);
  applyTheme();
}
function toggleLang(){
  LANG = LANG==="fa" ? "en" : "fa";
  localStorage.setItem(SP+"lang", LANG);
  applyLang();
  if(DATA) renderAll();
}
function applyLang(){
  document.documentElement.lang = LANG;
  document.documentElement.dir = LANG==="fa" ? "rtl" : "ltr";
  document.querySelectorAll("[data-i18n]").forEach(el=>el.textContent = t(el.dataset.i18n));
  const btn = document.getElementById("langBtn");
  if(btn) btn.textContent = LANG==="fa" ? "EN" : "FA";
}

function toast(msg, type){
  const el = document.getElementById("toast");
  el.className = "toast show" + (type ? " "+type : "");
  el.innerHTML = '<i class="ti '+(type==="ok"?"ti-circle-check":type==="err"?"ti-alert-circle":"ti-info-circle")+'"></i> '+esc(msg);
  clearTimeout(window.__t);
  window.__t = setTimeout(()=>el.classList.remove("show"), 2200);
}
async function copyText(text){
  try{ await navigator.clipboard.writeText(text); toast(t("copied"),"ok"); }
  catch(e){
    const ta = document.createElement("textarea"); ta.value = text;
    ta.style.position="fixed"; ta.style.opacity="0";
    document.body.appendChild(ta); ta.select();
    try{document.execCommand("copy");toast(t("copied"),"ok")}catch(_){toast(t("copy_failed"),"err")}
    document.body.removeChild(ta);
  }
}
function showQR(title, link){
  window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank');
}
function copySubAll(){
  if(DATA) copyText(DATA.sub_all_url);
}

function switchTab(name){
  TAB = name;
  document.querySelectorAll(".tab-panel").forEach(p=>p.classList.remove("active"));
  const el = document.getElementById("tab-"+name);
  if(el) el.classList.add("active");
  document.querySelectorAll(".tab").forEach(b=>b.classList.toggle("active", b.dataset.tab===name));
}
function setFilter(f, btn){
  FILTER = f;
  document.querySelectorAll("#filterChips .chip-f").forEach(b=>b.classList.toggle("active", b.dataset.filter===f));
  renderConfigs();
}
function toggleGroup(id){
  const el = document.getElementById("grp-"+id);
  if(el) el.classList.toggle("open");
}

function renderCard(l, idx){
  const pct = l.limit_bytes===0 ? 0 : Math.min(100, (l.used_bytes/l.limit_bytes)*100);
  const cls = !l.allowed ? (l.expired?"exp":(l.active?"":"off")) : "";
  const dLeft = daysLeft(l.expires_at);
  const expTxt = !l.expires_at ? t("unlimited") : (dLeft===0 ? t("expired") : (dLeft+"d"));
  return `
    <div class="cfg-card ${cls}">
      <div class="cfg-top">
        <div class="cfg-ic"><i class="ti ti-key"></i></div>
        <div class="cfg-info">
          <div class="cfg-label">${esc(l.label)}</div>
          <div class="cfg-badges">
            <span class="chip ${protoClass(l.protocol)}">${esc(protoName(l.protocol))}</span>
            ${l.allowed
              ? '<span class="chip green"><i class="ti ti-circle-check"></i> '+t("active")+'</span>'
              : (l.expired ? '<span class="chip amber"><i class="ti ti-calendar-x"></i> '+t("expired")+'</span>'
                           : '<span class="chip red"><i class="ti ti-circle-x"></i> '+t("disabled")+'</span>')}
            <span class="chip">:${l.port}</span>
            <span class="chip">${esc(l.fingerprint)}</span>
            ${l.connections>0 ? '<span class="chip amber"><i class="ti ti-plug-connected"></i> '+l.connections+'</span>' : ''}
            <span class="chip">${expTxt}</span>
          </div>
          <div class="cfg-usage-track"><div class="cfg-usage-fill" style="width:${pct}%"></div></div>
          <div class="cfg-usage-lbl">
            <span>${esc(l.used_fmt)}</span>
            <span>${esc(l.limit_fmt)}</span>
          </div>
        </div>
      </div>
      <div class="cfg-actions">
        <button class="cfg-btn" onclick="copyText('${esc(l.vless_link)}')"><i class="ti ti-copy"></i> ${t("link")}</button>
        <button class="cfg-btn" onclick="copyText('${esc(l.sub_url)}')"><i class="ti ti-rss"></i> ${t("sub")}</button>
        <button class="cfg-btn" onclick="showQR('${esc(l.label)}','${esc(l.sub_url)}')"><i class="ti ti-qrcode"></i> ${t("qr")}</button>
      </div>
    </div>
  `;
}

function renderAll(){
  if(!DATA) return;
  document.getElementById("loading").style.display = "none";
  ["overview","configs","groups"].forEach(id=>{
    const el = document.getElementById("tab-"+id);
    if(el) el.style.display = "";
  });

  // Hero
  document.getElementById("heroTotal").textContent = DATA.total_used_fmt;
  document.getElementById("heroSub").textContent = DATA.total + " configs · " + DATA.active_connections + " live";
  document.getElementById("sTotal").textContent = DATA.total;
  document.getElementById("sActive").textContent = DATA.active;
  document.getElementById("sExpired").textContent = DATA.expired;
  document.getElementById("sDisabled").textContent = DATA.disabled;
  document.getElementById("subAllUrl").textContent = DATA.sub_all_url;
  document.getElementById("hdSub").textContent = DATA.total + " configs · " + DATA.groups_count + " groups";

  // Quick list (latest 3 across groups+ungrouped)
  const all = [];
  (DATA.groups||[]).forEach(g=>g.links.forEach(l=>all.push(l)));
  (DATA.ungrouped||[]).forEach(l=>all.push(l));
  all.sort((a,b)=> (b.expires_at||"").localeCompare(a.expires_at||""));
  document.getElementById("quickCount").textContent = Math.min(3, all.length);
  document.getElementById("quickList").innerHTML = all.slice(0,3).map(renderCard).join("") ||
    '<div class="empty"><i class="ti ti-inbox"></i><div class="empty-title">'+t("empty_title")+'</div></div>';

  renderConfigs();
  renderGroups();
}

function renderConfigs(){
  const wrap = document.getElementById("cfgListWrap");
  if(!DATA) return;
  const q = (document.getElementById("searchInp").value || "").trim().toLowerCase();
  const all = [];
  (DATA.groups||[]).forEach(g=>g.links.forEach(l=>all.push(l)));
  (DATA.ungrouped||[]).forEach(l=>all.push(l));

  let filtered = all;
  if(FILTER === "active") filtered = all.filter(l=>l.allowed);
  else if(FILTER === "expired") filtered = all.filter(l=>l.expired);
  else if(FILTER === "disabled") filtered = all.filter(l=>!l.active && !l.expired);
  if(q) filtered = filtered.filter(l=> (l.label||"").toLowerCase().includes(q) || (l.note||"").toLowerCase().includes(q));

  if(!filtered.length){
    wrap.innerHTML = '<div class="empty"><i class="ti ti-filter-off"></i><div class="empty-title">'+t("empty_filter")+'</div></div>';
    return;
  }
  wrap.innerHTML = filtered.map(renderCard).join("");
}

function renderGroups(){
  const wrap = document.getElementById("grpListWrap");
  if(!DATA) return;
  const q = (document.getElementById("searchGrp").value || "").trim().toLowerCase();
  let groups = DATA.groups || [];
  if(q) groups = groups.filter(g=> (g.name||"").toLowerCase().includes(q) || (g.desc||"").toLowerCase().includes(q));

  let html = "";

  // Groups
  html += groups.map(g=>`
    <div class="group-block" id="grp-${esc(g.sub_id)}">
      <div class="group-head" onclick="toggleGroup('${esc(g.sub_id)}')">
        <div class="group-ic"><i class="ti ti-folder"></i></div>
        <div class="group-info">
          <div class="group-name">
            ${esc(g.name)}
            ${g.has_password ? '<span class="lock"><i class="ti ti-lock"></i></span>' : ''}
          </div>
          <div class="group-meta">${g.links.length} ${LANG==="fa"?"کانفیگ":"configs"}${g.desc?" · "+esc(g.desc):""}</div>
        </div>
        <i class="ti ti-chevron-down group-toggle"></i>
      </div>
      <div class="group-body">
        <div class="group-actions">
          <button class="cfg-btn primary" onclick="event.stopPropagation();copyText('${esc(g.public_url)}')"><i class="ti ti-world"></i> Public</button>
          <button class="cfg-btn" onclick="event.stopPropagation();copyText('${esc(g.sub_url)}')"><i class="ti ti-rss"></i> Sub</button>
          <button class="cfg-btn" onclick="event.stopPropagation();showQR('${esc(g.name)}','${esc(g.sub_url)}')"><i class="ti ti-qrcode"></i> QR</button>
        </div>
        ${g.links.length ? g.links.map(renderCard).join("") : '<div class="empty" style="padding:20px"><div class="empty-sub">'+(LANG==="fa"?"کانفیگی داخل این گروه نیست":"No configs in this group")+'</div></div>'}
      </div>
    </div>
  `).join("");

  // Ungrouped
  if((DATA.ungrouped||[]).length){
    html += `
      <div class="group-block open" id="grp-ungrouped">
        <div class="group-head" onclick="toggleGroup('ungrouped')">
          <div class="group-ic" style="background:linear-gradient(135deg,var(--amber),var(--red))"><i class="ti ti-inbox"></i></div>
          <div class="group-info">
            <div class="group-name">${t("ungrouped")}</div>
            <div class="group-meta">${DATA.ungrouped.length} ${LANG==="fa"?"کانفیگ":"configs"}</div>
          </div>
          <i class="ti ti-chevron-down group-toggle"></i>
        </div>
        <div class="group-body">
          ${DATA.ungrouped.map(renderCard).join("")}
        </div>
      </div>
    `;
  }

  if(!html){
    html = '<div class="empty"><i class="ti ti-folders"></i><div class="empty-title">'+(LANG==="fa"?"گروهی پیدا نشد":"No groups found")+'</div></div>';
  }
  wrap.innerHTML = html;
}

async function load(){
  try{
    const r = await fetch("/api/admin/all", {cache:"no-store", credentials:"same-origin"});
    if(!r.ok){
      if(r.status === 401){ location.href = "/"; return; }
      throw new Error("HTTP "+r.status);
    }
    DATA = await r.json();
    renderAll();
  }catch(e){
    document.getElementById("loading").innerHTML = '<div class="empty"><i class="ti ti-alert-circle"></i><div class="empty-title">'+t("copy_failed")+'</div></div>';
  }
}

(async function init(){
  applyTheme();
  applyLang();
  await load();
  setInterval(load, 15000);
})();
</script>
</body></html>'''

ADMIN_ALL_HTML_TEMPLATE = ADMIN_ALL_HTML_TEMPLATE.replace("__LOGO_B64__", LOGO_B64)


def get_admin_all_page_html() -> str:
    """صفحه‌ی ادمین — نمایش همه‌ی کانفیگ‌ها با سبک Marzban."""
    return ADMIN_ALL_HTML_TEMPLATE