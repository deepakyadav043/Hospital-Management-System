import json
import os

import streamlit as st

st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

CREDENTIALS = {
    "admin":     {"password": "admin@234",   "role": "admin"},
    "doctor":    {"password": "doctor@459",  "role": "doctor"},
    "reception": {"password": "recep@389",   "role": "reception"},


}

DATA_FILE = "doctors.json"

def load_doctors():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_doctors():
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.doctor_list, f)


def save_patients():
    with open("patients.json", "w") as f:
        json.dump(st.session_state.patient_list, f)

def load_patients():
    if os.path.exists("patients.json"):
        with open("patients.json", "r") as f:
            return json.load(f)
    return []

def save_appointments():
    with open("appointments.json", "w") as f:
        json.dump(st.session_state.appointment_list, f)

def load_appointments():
    if os.path.exists("appointments.json"):
        with open("appointments.json", "r") as f:
            return json.load(f)
    return []

def save_bills():
    with open("bills.json", "w") as f:
        json.dump(st.session_state.bill_list, f)

def load_bills():
    if os.path.exists("bills.json"):
        with open("bills.json", "r") as f:
            return json.load(f)
    return []

def save_salaries():
    with open("salaries.json", "w") as f:
        json.dump(st.session_state.salary_list, f)

def load_salaries():
    if os.path.exists("salaries.json"):
        with open("salaries.json", "r") as f:
            return json.load(f)
    return []

defaults = {
    "logged_in": False, "role": None, "show_login": False,
    "doctor_list": load_doctors(), "patient_list": load_patients(), "appointment_list": load_appointments(),
    "bill_list": load_bills(), "salary_list": load_salaries(),
    "admin_page":     "🏠 Home",
    "doctor_page":    "🏠 Dashboard",
    "reception_page": "🏠 Dashboard",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --teal:#0d9488; --teal2:#14b8a6; --navy:#0f172a; --muted:#64748b; --text:#1e293b;
}
html,body,[class*="css"]{ font-family:'DM Sans',sans-serif; }
.stApp{ background:linear-gradient(to bottom right,#020617,#0f172a); }
#MainMenu,footer { visibility:hidden; }
.block-container{ padding-top:2rem !important; }

/* ── Sidebar ── */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#0f172a 0%,#134e4a 100%) !important;
  border-right:2px solid #14b8a6;
}
section[data-testid="stSidebar"] *{ color:white !important; }
section[data-testid="stSidebar"] [data-testid="stRadio"] { display:none !important; }
section[data-testid="stSidebar"] .stButton>button{
  background:transparent !important; border:none !important;
  border-radius:8px !important; color:#a7f3d0 !important;
  text-align:left !important; width:100% !important;
  padding:8px 12px !important; font-size:0.88rem !important;
  font-weight:500 !important; transition:all 0.2s !important;
  justify-content:flex-start !important; outline:none !important; box-shadow:none !important;
}
section[data-testid="stSidebar"] .stButton>button:hover{
  background:rgba(20,184,166,0.2) !important; color:#ffffff !important; transform:translateX(4px) !important;
}
section[data-testid="stSidebar"] .stButton>button[kind="primary"]{
  background:rgba(20,184,166,0.25) !important; border-left:3px solid #14b8a6 !important;
  color:#ffffff !important; font-weight:600 !important;
}
.logout-btn>button{
  background:rgba(239,68,68,0.15) !important; border:1px solid rgba(239,68,68,0.4) !important;
  color:#fca5a5 !important; border-radius:8px !important; width:100% !important;
  padding:8px 12px !important; font-weight:600 !important;
}
.logout-btn>button:hover{ background:rgba(239,68,68,0.3) !important; color:#fff !important; }
.sb-section-label{
  font-size:0.68rem; font-weight:700; letter-spacing:0.12em;
  color:#0d9488; text-transform:uppercase; padding:12px 12px 4px; display:block;
}

/* ── Top Nav ── */
.topnav{
  background:linear-gradient(90deg,#0f172a,#134e4a);
  border-radius:14px; padding:18px 28px; margin-top:15px;
  display:flex; align-items:center; justify-content:space-between;
  margin-bottom:1.5rem; color:white; border:1px solid rgba(20,184,166,0.3);
}
.topnav-title{ font-family:'Playfair Display',serif; font-size:1.4rem; color:#99f6e4; }
.topnav-info { font-size:.85rem; color:#a7f3d0; }

/* ══════════════════════════════════════
   LANDING PAGE — COLORFUL & INTERACTIVE
══════════════════════════════════════ */

/* Animated floating particles background */
.landing-bg {
  position:fixed; top:0; left:0; width:100%; height:100%;
  pointer-events:none; z-index:0; overflow:hidden;
}
.particle {
  position:absolute; border-radius:50%;
  animation: floatUp linear infinite;
  opacity:0;
}
@keyframes floatUp {
  0%   { transform:translateY(100vh) scale(0); opacity:0; }
  10%  { opacity:0.6; }
  90%  { opacity:0.3; }
  100% { transform:translateY(-10vh) scale(1); opacity:0; }
}

/* Glowing top nav for landing */
.landing-topnav {
  background: linear-gradient(90deg, #0f172a, #134e4a, #0f172a);
  background-size: 200% 100%;
  animation: navShimmer 4s ease infinite;
  border-radius:14px; padding:16px 28px;
  display:flex; align-items:center; justify-content:space-between;
  margin-bottom:1.5rem; color:white;
  border:1px solid rgba(20,184,166,0.5);
  box-shadow: 0 0 30px rgba(20,184,166,0.15), 0 4px 20px rgba(0,0,0,0.4);
  position:relative; z-index:10;
}
@keyframes navShimmer {
  0%,100% { background-position: 0% 50%; }
  50%      { background-position: 100% 50%; }
}
.landing-topnav-title {
  font-family:'Playfair Display',serif; font-size:1.4rem;
  background: linear-gradient(90deg, #99f6e4, #14b8a6, #99f6e4);
  background-size:200%;
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  animation: titleFlow 3s ease infinite;
}
@keyframes titleFlow {
  0%,100% { background-position:0%; }
  50%      { background-position:100%; }
}
.landing-topnav-info { font-size:.85rem; color:#a7f3d0; }

/* Hero */
.hero{
  border-radius:24px; overflow:hidden; position:relative;
  margin-bottom:2rem; min-height:380px; display:flex; align-items:flex-end;
  box-shadow: 0 25px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(20,184,166,0.2);
}
.hero-img{ position:absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; object-position:center; }
.hero-overlay{
  position:absolute; top:0; left:0; width:100%; height:100%;
  background:linear-gradient(135deg,rgba(15,23,42,0.92) 0%,rgba(19,78,74,0.7) 60%,rgba(13,148,136,0.3) 100%);
}
/* Animated scan line on hero */
.hero-scanline {
  position:absolute; top:0; left:0; width:100%; height:3px;
  background: linear-gradient(90deg, transparent, #14b8a6, transparent);
  animation: scanDown 3s ease-in-out infinite;
  z-index:3;
}
@keyframes scanDown {
  0%   { top:0%; opacity:1; }
  100% { top:100%; opacity:0; }
}
.hero-content{ position:relative; z-index:4; padding:56px 60px; width:100%; }
.hero h1{
  font-family:'Playfair Display',serif; font-size:3.4rem; font-weight:900;
  line-height:1.1; margin:0 0 0.5rem;
  background:linear-gradient(90deg,#ffffff 0%,#99f6e4 50%,#fbbf24 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  animation: heroTextShimmer 5s ease infinite;
  background-size: 200%;
}
@keyframes heroTextShimmer {
  0%,100% { background-position:0%; }
  50%      { background-position:100%; }
}
.hero-tagline{ font-size:1.15rem; color:#a7f3d0; margin-bottom:1.5rem; font-weight:300; }
.hero-badges { display:flex; gap:10px; flex-wrap:wrap; }
.badge{
  background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.25);
  border-radius:30px; padding:6px 16px; font-size:0.82rem; color:#ccfbf1;
  backdrop-filter:blur(8px); cursor:default;
  transition: all 0.3s ease;
  animation: badgePop 0.5s ease backwards;
}
.badge:hover {
  background:rgba(20,184,166,0.3) !important;
  border-color:#14b8a6 !important;
  transform:translateY(-3px) scale(1.05);
  box-shadow:0 8px 20px rgba(20,184,166,0.3);
}
.badge:nth-child(1){animation-delay:0.2s}
.badge:nth-child(2){animation-delay:0.4s}
.badge:nth-child(3){animation-delay:0.6s}
.badge:nth-child(4){animation-delay:0.8s}
@keyframes badgePop {
  from { opacity:0; transform:translateY(20px) scale(0.8); }
  to   { opacity:1; transform:translateY(0) scale(1); }
}

/* Stats row — colorful gradient cards */
.stats-row{ display:flex; gap:14px; margin-bottom:2rem; flex-wrap:wrap; }
.stat-card{
  flex:1; min-width:140px; border-radius:18px;
  padding:24px 18px; text-align:center;
  transition: all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  cursor:default; position:relative; overflow:hidden;
  border:1px solid rgba(255,255,255,0.1);
  animation: cardSlideUp 0.6s ease backwards;
}
.stat-card::before {
  content:''; position:absolute; top:-50%; left:-50%;
  width:200%; height:200%;
  background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 60%);
  opacity:0; transition:opacity 0.3s;
}
.stat-card:hover::before { opacity:1; }
.stat-card:hover{ transform:translateY(-8px) scale(1.03); box-shadow:0 20px 40px rgba(0,0,0,0.4); }
.stat-card:nth-child(1){ background:linear-gradient(135deg,#0f4c75,#1b6ca8); animation-delay:0.1s }
.stat-card:nth-child(2){ background:linear-gradient(135deg,#134e4a,#0d9488); animation-delay:0.2s }
.stat-card:nth-child(3){ background:linear-gradient(135deg,#4c1d95,#7c3aed); animation-delay:0.3s }
.stat-card:nth-child(4){ background:linear-gradient(135deg,#7c2d12,#ea580c); animation-delay:0.4s }
.stat-card:nth-child(5){ background:linear-gradient(135deg,#064e3b,#059669); animation-delay:0.5s }
@keyframes cardSlideUp {
  from { opacity:0; transform:translateY(40px); }
  to   { opacity:1; transform:translateY(0); }
}
.stat-number{
  font-family:'Playfair Display',serif; font-size:2.4rem; font-weight:900; color:white;
  text-shadow:0 2px 10px rgba(0,0,0,0.3);
}
.stat-label { font-size:.82rem; color:rgba(255,255,255,0.8); margin-top:6px; font-weight:500; }

/* Dashboard stat cards (dark) */
.dstat-row{ display:flex; gap:14px; margin-bottom:2rem; flex-wrap:wrap; }
.dstat-card{
  flex:1; min-width:140px; background:linear-gradient(135deg,#1e293b,#134e4a);
  border-radius:16px; padding:22px 18px; text-align:center;
  border:1px solid rgba(20,184,166,0.3); box-shadow:0 4px 20px rgba(0,0,0,0.3);
}
.dstat-number{ font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; color:#14b8a6; }
.dstat-label { font-size:.82rem; color:#a7f3d0; margin-top:4px; }

/* Section head */
.section-head{
  font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:white;
  border-left:5px solid var(--teal); padding-left:16px; margin:2rem 0 1.2rem;
}

/* About section — colorful */
.about-card {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  border-radius:20px; padding:28px;
  border:1px solid rgba(20,184,166,0.2);
  box-shadow:0 10px 40px rgba(0,0,0,0.3);
  position:relative; overflow:hidden;
}
.about-card::after {
  content:''; position:absolute; top:0; right:0;
  width:200px; height:200px;
  background:radial-gradient(circle, rgba(20,184,166,0.15) 0%, transparent 70%);
  pointer-events:none;
}
.about-card p { font-size:1rem; color:#cbd5e1; line-height:1.85; margin:0; }

/* Tags */
.tag{
  display:inline-block; border-radius:20px;
  padding:4px 14px; font-size:.78rem; font-weight:600; margin:3px;
  transition:all 0.3s ease; cursor:default;
}
.tag:hover { transform:scale(1.08) translateY(-2px); }
.tag:nth-child(1){ background:linear-gradient(90deg,#0d9488,#14b8a6); color:white; box-shadow:0 4px 12px rgba(13,148,136,0.4); }
.tag:nth-child(2){ background:linear-gradient(90deg,#7c3aed,#a855f7); color:white; box-shadow:0 4px 12px rgba(124,58,237,0.4); }
.tag:nth-child(3){ background:linear-gradient(90deg,#dc2626,#f87171); color:white; box-shadow:0 4px 12px rgba(220,38,38,0.4); }
.tag:nth-child(4){ background:linear-gradient(90deg,#059669,#34d399); color:white; box-shadow:0 4px 12px rgba(5,150,105,0.4); }

.mission-card {
  background:linear-gradient(135deg,#0f172a,#134e4a);
  border-radius:20px; padding:28px; color:white; height:100%;
  border:1px solid rgba(20,184,166,0.2);
  box-shadow:0 10px 40px rgba(0,0,0,0.3);
  position:relative; overflow:hidden;
}
.mission-card::before {
  content:''; position:absolute; bottom:-30px; left:-30px;
  width:150px; height:150px;
  background:radial-gradient(circle, rgba(20,184,166,0.12) 0%, transparent 70%);
}
.mission-card h3 { font-family:'Playfair Display',serif; color:#99f6e4; margin-top:0; }
.mission-card p { color:#a7f3d0; font-size:.92rem; line-height:1.7; }

/* Service cards — colorful */
.services-grid{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:2rem; }
.service-card{
  flex:1; min-width:160px; border-radius:18px;
  padding:28px 18px; text-align:center;
  transition:all 0.35s cubic-bezier(0.34,1.56,0.64,1);
  cursor:default; position:relative; overflow:hidden;
  border:1px solid rgba(255,255,255,0.06);
}
.service-card::before {
  content:''; position:absolute; inset:0;
  background:inherit; filter:brightness(1.15);
  opacity:0; transition:opacity 0.3s;
  border-radius:inherit;
}
.service-card:hover::before { opacity:1; }
.service-card:hover{ transform:translateY(-8px) scale(1.04); box-shadow:0 20px 40px rgba(0,0,0,0.4); }
.service-card:nth-child(1){ background:linear-gradient(135deg,#450a0a,#991b1b); }
.service-card:nth-child(2){ background:linear-gradient(135deg,#1e1b4b,#4338ca); }
.service-card:nth-child(3){ background:linear-gradient(135deg,#082f49,#0369a1); }
.service-card:nth-child(4){ background:linear-gradient(135deg,#052e16,#15803d); }
.service-card:nth-child(5){ background:linear-gradient(135deg,#2d1b69,#7c3aed); }
.service-card:nth-child(6){ background:linear-gradient(135deg,#0c1a2e,#1e40af); }
.service-card:nth-child(7){ background:linear-gradient(135deg,#431407,#c2410c); }
.service-card:nth-child(8){ background:linear-gradient(135deg,#4a044e,#a21caf); }
.service-icon { font-size:2.6rem; margin-bottom:12px; display:block; position:relative; z-index:1; filter:drop-shadow(0 4px 8px rgba(0,0,0,0.4)); }
.service-title{ font-weight:700; color:white; font-size:.95rem; position:relative; z-index:1; }
.service-desc { font-size:.78rem; color:rgba(255,255,255,0.7); margin-top:5px; position:relative; z-index:1; }

/* Info cards — colorful */
.info-row{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:2rem; }
.info-card{
  flex:1; min-width:190px; border-radius:16px; padding:22px;
  transition:all 0.3s ease; cursor:default;
  border:1px solid rgba(255,255,255,0.08);
  position:relative; overflow:hidden;
}
.info-card::after {
  content:''; position:absolute; top:-20px; right:-20px;
  width:80px; height:80px; border-radius:50%;
  background:rgba(255,255,255,0.05);
}
.info-card:hover { transform:translateY(-5px); box-shadow:0 15px 35px rgba(0,0,0,0.4); }
.info-card:nth-child(1){ background:linear-gradient(135deg,#0c4a6e,#075985); }
.info-card:nth-child(2){ background:linear-gradient(135deg,#14532d,#166534); }
.info-card:nth-child(3){ background:linear-gradient(135deg,#4c1d95,#5b21b6); }
.info-card:nth-child(4){ background:linear-gradient(135deg,#7c2d12,#9a3412); }
.info-card h4{ color:white; font-weight:700; margin:0 0 10px; font-size:1rem; }
.info-card p { color:rgba(255,255,255,0.82); margin:0; font-size:.88rem; line-height:1.7; }

/* Dash cards */
.dash-card{
  background:#1e293b; border-radius:14px; padding:22px; margin-bottom:16px;
  box-shadow:0 2px 12px rgba(0,0,0,.3); border-left:5px solid var(--teal);
}
.dash-card h4{ margin:0 0 6px; color:white; }
.dash-card p { margin:0; color:#94a3b8; font-size:.88rem; }

/* Table */
.data-table{ width:100%; border-collapse:collapse; font-size:.9rem; }
.data-table th{ background:#0d9488; color:white; padding:10px 14px; text-align:left; }
.data-table td{ padding:9px 14px; border-bottom:1px solid #334155; color:#e2e8f0; background:#1e293b; }
.data-table tr:hover td{ background:#134e4a; transition:0.2s; }

/* Slip */
.slip-box{
  background:linear-gradient(135deg,#134e4a,#1e293b);
  border-radius:14px; padding:28px; border:1px solid #14b8a6;
}
.slip-box h3{ font-family:'Playfair Display',serif; color:white; margin-top:0; }
.slip-box p { color:#a7f3d0; font-size:.95rem; line-height:2; }

/* Global buttons */
.stButton>button{
  border-radius:10px !important; font-weight:600 !important;
  transition:all .2s !important; outline:none !important; box-shadow:none !important;
}
.stButton>button:focus, .stButton>button:focus-visible { outline:none !important; box-shadow:none !important; }

/* Inputs */
.stTextInput input, .stNumberInput input, .stDateInput input, .stTimeInput input {
  border-radius:10px !important; border:1px solid #14b8a6 !important;
  outline:none !important; box-shadow:none !important;
}
.stTextInput input:focus, .stNumberInput input:focus,
.stDateInput input:focus, .stTimeInput input:focus {
  outline:none !important; box-shadow:none !important; border:1px solid #14b8a6 !important;
}
div[data-baseweb="select"] { outline:none !important; box-shadow:none !important; }
div[data-baseweb="select"] > div {
  border-radius:10px !important; border:1px solid #14b8a6 !important;
  outline:none !important; box-shadow:none !important;
}
div[data-baseweb="select"] > div:focus,
div[data-baseweb="select"] > div:focus-within,
div[data-baseweb="select"] > div:focus-visible {
  outline:none !important; box-shadow:none !important; border:1px solid #14b8a6 !important;
}
div[data-baseweb="select"] span { border:none !important; background:transparent !important; }
[data-baseweb="popover"] { outline:none !important; box-shadow:none !important; }
*, *:focus, *:focus-visible, *:focus-within { outline:none !important; box-shadow:none !important; }

/* Footer */
.landing-footer{
  border-radius:20px; padding:36px 40px; text-align:center;
  margin-top:3rem; font-size:.83rem; line-height:2.2;
  background: linear-gradient(135deg, #0f172a 0%, #134e4a 50%, #0f172a 100%);
  border:1px solid rgba(20,184,166,0.25);
  box-shadow:0 -10px 40px rgba(0,0,0,0.3);
  position:relative; overflow:hidden;
}
.landing-footer::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg, transparent, #14b8a6, #fbbf24, #14b8a6, transparent);
  animation:footerLine 3s ease infinite;
}
@keyframes footerLine {
  0%,100% { opacity:0.5; }
  50% { opacity:1; }
}
.landing-footer-title { font-size:1.1rem; color:#e2e8f0; font-weight:700; }
.landing-footer span{ color:#99f6e4; }
.landing-footer .ft-heart { color:#f87171; animation:heartbeat 1.5s ease infinite; display:inline-block; }
@keyframes heartbeat {
  0%,100% { transform:scale(1); }
  50% { transform:scale(1.3); }
}

[data-testid="stSidebar"] input[type="radio"]{ display:none !important; }
[data-testid="stSidebar"] .st-emotion-cache-j7qwjs{ display:none !important; }
</style>

<!-- Floating particles -->
<div class="landing-bg" id="particleBg"></div>
<script>
(function(){
  var bg = document.getElementById('particleBg');
  if(!bg) return;
  var colors = ['#14b8a6','#0d9488','#99f6e4','#fbbf24','#a855f7','#f87171','#34d399'];
  for(var i=0;i<25;i++){
    var p = document.createElement('div');
    p.className='particle';
    var size = Math.random()*8+4;
    p.style.cssText = [
      'width:'+size+'px','height:'+size+'px',
      'left:'+Math.random()*100+'%',
      'background:'+colors[Math.floor(Math.random()*colors.length)],
      'animation-duration:'+(Math.random()*15+10)+'s',
      'animation-delay:'+(Math.random()*10)+'s',
      'filter:blur('+(Math.random()*2)+'px)'
    ].join(';');
    bg.appendChild(p);
  }
})();
</script>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def logout():
    for k in ["logged_in","role","show_login","admin_page","doctor_page","reception_page"]:
        st.session_state[k] = defaults[k]

def next_id(lst): return len(lst)+1

def set_page(state_key, value):
    st.session_state[state_key] = value
    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def build_sidebar(role, page_key, sections):
    labels_map = {"admin":"🛡️ Admin","doctor":"👨‍⚕️ Doctor","reception":"🗂️ Receptionist"}
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align:center;padding:18px 8px 14px;">
          <div style="font-size:2.6rem;">🏥</div>
          <div style="font-family:'Playfair Display',serif;font-size:1.05rem;
               color:#99f6e4;font-weight:700;margin-top:4px;">Jan Kalyan Hospital</div>
          <div style="font-size:0.72rem;background:rgba(20,184,166,0.18);
               border:1px solid rgba(20,184,166,0.35);border-radius:20px;
               padding:2px 12px;display:inline-block;margin-top:6px;color:#99f6e4;">
               {labels_map[role]}</div>
        </div>
        <hr style="border-color:rgba(20,184,166,0.25);margin:0 0 8px;">
        """, unsafe_allow_html=True)

        current = st.session_state[page_key]
        for section_title, pages in sections:
            st.markdown(f'<span class="sb-section-label">{section_title}</span>', unsafe_allow_html=True)
            for page in pages:
                is_active = (current == page)
                clicked = st.button(
                    page,
                    key=f"nav__{page_key}__{page}",
                    type="primary" if is_active else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    st.session_state[page_key] = page
                    st.rerun()

        st.markdown('<hr style="border-color:rgba(239,68,68,0.25);margin:10px 0 6px;">', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
            if st.button("🚪 Logout", key=f"logout_{role}", use_container_width=True):
                logout(); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  LOGIN PAGE
# ══════════════════════════════════════════════════════════════════════════════
def show_login_page():
    st.markdown("""
    <div style='text-align:center;padding:24px 0 10px;'>
      <span style='font-size:3rem'>🏥</span>
      <h2 style='font-family:Playfair Display,serif;color:white;margin:6px 0 2px;'>Staff Portal Login</h2>
      <p style='color:#64748b;font-size:.92rem;'>Authorized personnel only</p>
    </div>
    """, unsafe_allow_html=True)
    _, col, _ = st.columns([1,2,1])
    with col:
        st.markdown("""
        <div style="
        background:rgba(15,23,42,0.9);
        border:1px solid rgba(20,184,166,0.3);
        border-radius:16px;
        padding:18px;
        margin-bottom:20px;
        color:white;
        ">

        <h3 style="color:#99f6e4;margin-top:0;">
        🔐 Demo Login Credentials
        </h3>

        <table style="width:100%;color:white;">
        <tr>
        <th align="left">Role</th>
        <th align="left">Username</th>
        <th align="left">Password</th>
        </tr>

        <tr>
        <td>🛡️ Admin</td>
        <td>admin</td>
        <td>admin@234</td>
        </tr>

        <tr>
        <td>👨‍⚕️ Doctor</td>
        <td>doctor</td>
        <td>doctor@459</td>
        </tr>

        <tr>
        <td>🗂️ Receptionist</td>
        <td>reception</td>
        <td>recep@389</td>
        </tr>

        </table>

        </div>
        """, unsafe_allow_html=True)



        role_label = st.selectbox("Login as", ["Admin","Doctor","Receptionist"])
        username   = st.text_input("Username", placeholder="Enter username")
        password   = st.text_input("Password", type="password", placeholder="Enter password")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔐 Login", use_container_width=True, type="primary"):
                rm = {"Admin":"admin","Doctor":"doctor","Receptionist":"reception"}
                rk = rm[role_label]
                cred = CREDENTIALS.get(rk)
                if cred and username==rk and password==cred["password"]:
                    st.session_state.logged_in = True
                    st.session_state.role = cred["role"]
                    st.session_state.show_login = False
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials.")
        with c2:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.show_login = False; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  LANDING PAGE
# ══════════════════════════════════════════════════════════════════════════════
def show_landing():
    st.markdown("""
    <div class="landing-topnav">
      <span class="landing-topnav-title">🏥 Jan Kalyan Hospital</span>
      <span class="landing-topnav-info">📍 Bihar &nbsp;|&nbsp; 📞 +91 8989651456 &nbsp;|&nbsp; ✉️ jankalyan@gmail.com</span>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn = st.columns([9,1])
    with col_btn:
        if st.button("🔐 Staff Login", type="primary", use_container_width=True):
            st.session_state.show_login = True; st.rerun()


    st.markdown("""
    <div class="hero">
      <img class="hero-img"
           src="https://imkarchitects.com/images/expertise-healthcare-banner.jpg"
           alt="Hospital" onerror="this.style.display='none'">
      <div class="hero-overlay"></div>
      <div class="hero-scanline"></div>
      <div class="hero-content">
        <h1>Healing With Heart,<br>Serving With Care</h1>
        <p class="hero-tagline">Your health is our mission — advanced care, compassionate touch.</p>
        <div class="hero-badges">
          <span class="badge">🏅 ISO Certified</span>
          <span class="badge">🕐 24/7 Emergency</span>
          <span class="badge">👨‍⚕️ 50+ Specialists</span>
          <span class="badge">🏥 300 Bed Capacity</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stats-row">
      <div class="stat-card"><div class="stat-number">15+</div><div class="stat-label">Years of Excellence</div></div>
      <div class="stat-card"><div class="stat-number">50K+</div><div class="stat-label">Patients Treated</div></div>
      <div class="stat-card"><div class="stat-number">50+</div><div class="stat-label">Specialist Doctors</div></div>
      <div class="stat-card"><div class="stat-number">300</div><div class="stat-label">Bed Capacity</div></div>
      <div class="stat-card"><div class="stat-number">24/7</div><div class="stat-label">Emergency Care</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">About Us</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("""
        <div class="about-card">
          <p>
          <b style="color:#99f6e4;">Jan Kalyan Hospital</b> has been a pillar of healthcare in Bihar for over 15 years.
          We combine cutting-edge technology with deeply compassionate service.<br><br>
          Our team of over 50 specialist doctors, 200+ nurses, and support staff work around the clock
          to ensure the best outcomes for every patient.
          </p>
          <div style="margin-top:16px;">
            <span class="tag">🎯 Patient-First</span>
            <span class="tag">🔬 Latest Technology</span>
            <span class="tag">❤️ Compassionate Care</span>
            <span class="tag">🌿 Holistic Wellness</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="mission-card">
          <h3>Our Mission</h3>
          <p>Affordable, world-class healthcare for every person in Bihar — through innovation, integrity, and compassion.</p>
          <h3>Our Vision</h3>
          <p>Bihar's most trusted hospital — where technology meets humanity.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">Our Services</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="services-grid">
      <div class="service-card"><span class="service-icon">🫀</span><div class="service-title">Cardiology</div><div class="service-desc">Heart care & surgery</div></div>
      <div class="service-card"><span class="service-icon">🧠</span><div class="service-title">Neurology</div><div class="service-desc">Brain & nerve disorders</div></div>
      <div class="service-card"><span class="service-icon">🦴</span><div class="service-title">Orthopedics</div><div class="service-desc">Bones, joints & spine</div></div>
      <div class="service-card"><span class="service-icon">👶</span><div class="service-title">Pediatrics</div><div class="service-desc">Child health & care</div></div>
      <div class="service-card"><span class="service-icon">🔬</span><div class="service-title">Pathology</div><div class="service-desc">Lab tests & diagnosis</div></div>
      <div class="service-card"><span class="service-icon">🩻</span><div class="service-title">Radiology</div><div class="service-desc">X-ray, MRI, CT scan</div></div>
      <div class="service-card"><span class="service-icon">🚑</span><div class="service-title">Emergency</div><div class="service-desc">24/7 trauma care</div></div>
      <div class="service-card"><span class="service-icon">🌸</span><div class="service-title">Gynecology</div><div class="service-desc">Women's health</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">Contact & Information</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-row">
      <div class="info-card"><h4>📍 Location</h4><p>Jan Kalyan Hospital<br>Main Road, Bihar — 800001<br>India</p></div>
      <div class="info-card"><h4>📞 Contact</h4><p>Phone: +91 8989651456<br>Emergency: +91 8989651400<br>Ambulance: 108</p></div>
      <div class="info-card"><h4>✉️ Email</h4><p>General: jankalyan@gmail.com<br>Appointments: appt@jankalyan.in<br>Admin: admin@jankalyan.in</p></div>
      <div class="info-card"><h4>🕐 Timings</h4><p>OPD: 8:00 AM – 8:00 PM<br>Emergency: 24 × 7<br>Lab: 7:00 AM – 9:00 PM</p></div>
    </div>
    <div class="landing-footer">
      <div class="landing-footer-title">🏥 Jan Kalyan Hospital</div>
      Bihar, India &nbsp;|&nbsp; <span>jankalyan@gmail.com</span> &nbsp;|&nbsp; <span>+91 8989651456</span><br><br>
      © 2025 Jan Kalyan Hospital. All rights reserved. &nbsp;|&nbsp; Built with <span class="ft-heart">❤️</span> for better healthcare in Bihar.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  TOP BAR
# ══════════════════════════════════════════════════════════════════════════════
def dashboard_header(role):
    icons  = {"admin":"🛡️","doctor":"👨‍⚕️","reception":"🗂️"}
    labels = {"admin":"Admin","doctor":"Doctor","reception":"Receptionist"}
    st.markdown(f"""
    <div class="topnav">
      <span class="topnav-title">🏥 Jan Kalyan Hospital — {labels[role]} Dashboard {icons[role]}</span>
      <span class="topnav-info">Bihar &nbsp;|&nbsp; jankalyan@gmail.com &nbsp;|&nbsp; +91 8989651456</span>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  FEATURE UIs
# ══════════════════════════════════════════════════════════════════════════════
def ui_add_doctor():
    st.subheader("➕ Add Doctor")
    with st.form("add_doc"):
        n=st.text_input("Doctor Name"); s=st.text_input("Specialization")
        e=st.number_input("Experience (years)",0,60,step=1)
        f=st.number_input("Consultation Fee (₹)",0,step=100)
        if st.form_submit_button("Add Doctor",type="primary"):
            if n and s:
                st.session_state.doctor_list.append({"id":next_id(st.session_state.doctor_list),"name":n,"spec":s,"exp":e,"fee":f})
                save_doctors()
                st.success(f"✅ Dr. {n} added!")
            else: st.warning("Fill all fields.")

def ui_view_doctors():
    st.subheader("👨‍⚕️ All Doctors")
    dl=st.session_state.doctor_list
    if not dl: st.info("No doctors added yet."); return
    rows="".join(f"<tr><td>{d['id']}</td><td>{d['name']}</td><td>{d['spec']}</td><td>{d['exp']} yrs</td><td>₹{d['fee']}</td></tr>" for d in dl)
    st.markdown(f'<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Experience</th><th>Fee</th></tr></thead><tbody>{rows}</tbody></table>',unsafe_allow_html=True)

def ui_search_doctor():
    st.subheader("🔍 Search Doctor")
    q=st.text_input("Enter doctor name")
    if q:
        found=[d for d in st.session_state.doctor_list if q.lower() in d['name'].lower()]
        if found:
            for d in found: st.markdown(f'<div class="dash-card"><h4>Dr. {d["name"]}</h4><p>Spec: {d["spec"]} | Exp: {d["exp"]} yrs | Fee: ₹{d["fee"]}</p></div>',unsafe_allow_html=True)
        else: st.error("No doctor found.")

def ui_delete_doctor():
    st.subheader("🗑️ Delete Doctor")
    if not st.session_state.doctor_list: st.info("No doctors to delete."); return
    opts={f"#{d['id']} — {d['name']}":d['id'] for d in st.session_state.doctor_list}
    sel=st.selectbox("Select Doctor",list(opts.keys()))
    if st.button("Delete Doctor",type="primary"):
        st.session_state.doctor_list=[d for d in st.session_state.doctor_list if d['id']!=opts[sel]]

        save_doctors()
        st.success("Doctor removed."); st.rerun()

def ui_add_patient():
    st.subheader("➕ Add Patient")
    with st.form("add_pat"):
        n=st.text_input("Patient Name"); a=st.number_input("Age",0,130,step=1)
        d=st.text_input("Disease / Condition"); r=st.text_input("Room Number")
        if st.form_submit_button("Add Patient",type="primary"):
            if n and d:
                st.session_state.patient_list.append({"id":next_id(st.session_state.patient_list),"name":n,"age":a,"disease":d,"room":r})
                save_patients()
                st.success(f"✅ {n} added!")
            else: st.warning("Fill required fields.")

def ui_view_patients():
    st.subheader("🧑‍⚕️ All Patients")
    pl=st.session_state.patient_list
    if not pl: st.info("No patients added yet."); return
    rows="".join(f"<tr><td>{p['id']}</td><td>{p['name']}</td><td>{p['age']}</td><td>{p['disease']}</td><td>{p['room']}</td></tr>" for p in pl)
    st.markdown(f'<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Age</th><th>Disease</th><th>Room</th></tr></thead><tbody>{rows}</tbody></table>',unsafe_allow_html=True)

def ui_search_patient():
    st.subheader("🔍 Search Patient")
    method=st.radio("Search by",["Name","ID"],horizontal=True)
    found=[]
    if method=="Name":
        q=st.text_input("Enter patient name")
        if q: found=[p for p in st.session_state.patient_list if q.lower() in p['name'].lower()]
    else:
        q=st.number_input("Enter patient ID",min_value=1,step=1)
        if st.button("Search"): found=[p for p in st.session_state.patient_list if p['id']==int(q)]
    for p in found:
        st.markdown(f'<div class="dash-card"><h4>{p["name"]}</h4><p>ID:{p["id"]} | Age:{p["age"]} | Disease:{p["disease"]} | Room:{p["room"]}</p></div>',unsafe_allow_html=True)
    if not found and method=="Name" and 'q' in dir() and q: st.error("Patient not found.")

def ui_book_appointment():
    st.subheader("📅 Book Appointment")
    with st.form("book_appt"):
        doc=st.text_input("Doctor Name"); pat=st.text_input("Patient Name")
        date=st.date_input("Date"); time=st.time_input("Time")
        if st.form_submit_button("Book Appointment",type="primary"):
            if doc and pat:
                st.session_state.appointment_list.append({"id":next_id(st.session_state.appointment_list),"doctor":doc,"patient":pat,"date":str(date),"time":str(time)})
                save_appointments()
                st.success("✅ Appointment booked!")
            else: st.warning("Fill all fields.")

def ui_view_appointments():
    st.subheader("📋 All Appointments")
    al=st.session_state.appointment_list
    if not al: st.info("No appointments yet."); return
    rows="".join(f"<tr><td>{a['id']}</td><td>{a['doctor']}</td><td>{a['patient']}</td><td>{a['date']}</td><td>{a['time']}</td></tr>" for a in al)
    st.markdown(f'<table class="data-table"><thead><tr><th>ID</th><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th></tr></thead><tbody>{rows}</tbody></table>',unsafe_allow_html=True)

def ui_search_appointment():
    st.subheader("🔍 Search Appointment by Date")
    date=st.date_input("Select Date")
    found=[a for a in st.session_state.appointment_list if a['date']==str(date)]
    if found:
        for a in found: st.markdown(f'<div class="dash-card"><h4>Appt #{a["id"]}</h4><p>Doctor:{a["doctor"]} | Patient:{a["patient"]} | Time:{a["time"]}</p></div>',unsafe_allow_html=True)
    else: st.info(f"No appointments on {date}.")

def ui_generate_bill():
    st.subheader("🧾 Generate Bill")
    with st.form("gen_bill"):
        name=st.text_input("Patient Name")
        doc_f=st.number_input("Doctor Fee (₹)",0,step=100)
        room=st.number_input("Room Charges (₹)",0,step=100)
        med=st.number_input("Medicine Charges (₹)",0,step=100)
        if st.form_submit_button("Generate Bill",type="primary"):
            if name:
                total=doc_f+room+med
                b={"id":next_id(st.session_state.bill_list),"name":name,"doc_fee":doc_f,"room":room,"med":med,"total":total}
                st.session_state.bill_list.append(b)
                save_bills()
                st.markdown(f'<div class="slip-box"><h3>🧾 Bill #{b["id"]}</h3><p>Patient: <b>{name}</b><br>Doctor Fee: ₹{doc_f} | Room: ₹{room} | Medicine: ₹{med}<br><span style="font-size:1.3rem;font-weight:700;color:#14b8a6;">Total: ₹{total:,}</span></p></div>',unsafe_allow_html=True)
            else: st.warning("Enter patient name.")

def ui_view_bills():
    st.subheader("💰 All Bills")
    bl=st.session_state.bill_list
    if not bl: st.info("No bills yet."); return
    rows="".join(f"<tr><td>{b['id']}</td><td>{b['name']}</td><td>₹{b['doc_fee']}</td><td>₹{b['room']}</td><td>₹{b['med']}</td><td><b>₹{b['total']:,}</b></td></tr>" for b in bl)
    st.markdown(f'<table class="data-table"><thead><tr><th>ID</th><th>Patient</th><th>Doctor Fee</th><th>Room</th><th>Medicine</th><th>Total</th></tr></thead><tbody>{rows}</tbody></table>',unsafe_allow_html=True)

def ui_add_salary():
    st.subheader("💵 Add Salary Record")
    with st.form("add_sal"):
        emp=st.text_input("Employee Name"); etype=st.selectbox("Type",["Doctor","Nurse","Staff"])
        basic=st.number_input("Basic Salary (₹)",0,step=1000)
        hra=st.number_input("HRA %",0.0,100.0,value=10.0,step=0.5)
        da=st.number_input("DA %",0.0,100.0,value=5.0,step=0.5)
        pf=st.number_input("PF %",0.0,100.0,value=12.0,step=0.5)
        month=st.selectbox("Month",["January","February","March","April","May","June","July","August","September","October","November","December"])
        year=st.text_input("Year","2025")
        if st.form_submit_button("Generate Salary Slip",type="primary"):
            if emp:
                hra_a=(hra/100)*basic; da_a=(da/100)*basic; pf_a=(pf/100)*basic
                gross=basic+hra_a+da_a; net=gross-pf_a
                s={"id":next_id(st.session_state.salary_list),"name":emp,"type":etype,"basic":basic,"hra":hra_a,"da":da_a,"pf":pf_a,"gross":gross,"net":net,"month":month,"year":year}
                st.session_state.salary_list.append(s)
                save_salaries()
                st.markdown(f'<div class="slip-box"><h3>💵 Salary Slip — {emp}</h3><p>Type:{etype} | Month:{month} {year}<br>Basic:₹{basic:,} | HRA:₹{hra_a:,.0f} | DA:₹{da_a:,.0f}<br>Gross:₹{gross:,.0f} | PF Deduction:₹{pf_a:,.0f}<br><span style="font-size:1.3rem;font-weight:700;color:#14b8a6;">Net Salary: ₹{net:,.0f}</span></p></div>',unsafe_allow_html=True)

def ui_view_salaries():
    st.subheader("📋 All Salary Records")
    sl=st.session_state.salary_list
    if not sl: st.info("No records yet."); return
    rows="".join(f"<tr><td>{s['id']}</td><td>{s['name']}</td><td>{s['type']}</td><td>₹{s['basic']:,}</td><td>₹{s['gross']:,.0f}</td><td><b>₹{s['net']:,.0f}</b></td><td>{s['month']} {s['year']}</td></tr>" for s in sl)
    st.markdown(f'<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Type</th><th>Basic</th><th>Gross</th><th>Net</th><th>Month</th></tr></thead><tbody>{rows}</tbody></table>',unsafe_allow_html=True)

def ui_search_salary():
    st.subheader("🔍 Search Salary")
    q=st.text_input("Employee name")
    if q:
        found=[s for s in st.session_state.salary_list if q.lower() in s['name'].lower()]
        if found:
            for s in found: st.markdown(f'<div class="dash-card"><h4>{s["name"]} ({s["type"]})</h4><p>Month:{s["month"]} {s["year"]} | Net:₹{s["net"]:,.0f}</p></div>',unsafe_allow_html=True)
        else: st.error("No record found.")

def ui_salary_calculator():
    st.subheader("🧮 Salary Calculator")
    with st.form("sal_calc"):
        basic=st.number_input("Basic Salary (₹)",0,step=1000)
        hra=st.number_input("HRA %",0.0,100.0,value=10.0)
        da=st.number_input("DA %",0.0,100.0,value=5.0)
        pf=st.number_input("PF %",0.0,100.0,value=12.0)
        if st.form_submit_button("Calculate",type="primary"):
            hra_a=(hra/100)*basic; da_a=(da/100)*basic; pf_a=(pf/100)*basic
            gross=basic+hra_a+da_a; net=gross-pf_a
            c1,c2,c3,c4=st.columns(4)
            c1.metric("Gross",f"₹{gross:,.0f}"); c2.metric("HRA",f"₹{hra_a:,.0f}")
            c3.metric("DA",f"₹{da_a:,.0f}");     c4.metric("Net",f"₹{net:,.0f}")

def ui_delete_salary():
    st.subheader("🗑️ Delete Salary Record")
    if not st.session_state.salary_list: st.info("No records."); return
    opts={f"#{s['id']} — {s['name']} ({s['month']} {s['year']})":s['id'] for s in st.session_state.salary_list}
    sel=st.selectbox("Select Record",list(opts.keys()))
    if st.button("Delete Record",type="primary"):
        st.session_state.salary_list=[s for s in st.session_state.salary_list if s['id']!=opts[sel]]
        save_salaries()
        st.success("Deleted."); st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  DASHBOARDS
# ══════════════════════════════════════════════════════════════════════════════
ADMIN_SECTIONS = [
    ("Overview",      ["🏠 Home"]),
    ("Doctors",       ["➕ Add Doctor","👁️ View Doctors","🔍 Search Doctor","🗑️ Delete Doctor"]),
    ("Patients",      ["➕ Add Patient","👁️ View Patients","🔍 Search Patient"]),
    ("Appointments",  ["📅 Book Appointment","📋 View Appointments","📆 Search by Date"]),
    ("Billing",       ["🧾 Generate Bill","💰 View Bills"]),
    ("Salary",        ["💵 Add Salary","📑 View Salaries","🔎 Search Salary","🧮 Salary Calculator","🗑️ Delete Salary"]),
]
ADMIN_DISPATCH = {
    "➕ Add Doctor":ui_add_doctor,"👁️ View Doctors":ui_view_doctors,
    "🔍 Search Doctor":ui_search_doctor,"🗑️ Delete Doctor":ui_delete_doctor,
    "➕ Add Patient":ui_add_patient,"👁️ View Patients":ui_view_patients,
    "🔍 Search Patient":ui_search_patient,
    "📅 Book Appointment":ui_book_appointment,"📋 View Appointments":ui_view_appointments,
    "📆 Search by Date":ui_search_appointment,
    "🧾 Generate Bill":ui_generate_bill,"💰 View Bills":ui_view_bills,
    "💵 Add Salary":ui_add_salary,"📑 View Salaries":ui_view_salaries,
    "🔎 Search Salary":ui_search_salary,"🧮 Salary Calculator":ui_salary_calculator,
    "🗑️ Delete Salary":ui_delete_salary,
}
DOCTOR_SECTIONS = [
    ("Overview",     ["🏠 Dashboard"]),
    ("Patients",     ["👁️ View Patients","🔍 Search Patient"]),
    ("Appointments", ["📅 View Appointments","📆 Search by Date"]),
    ("Doctors",      ["👨‍⚕️ View All Doctors"]),
]
DOCTOR_DISPATCH = {
    "👁️ View Patients":ui_view_patients,"🔍 Search Patient":ui_search_patient,
    "📅 View Appointments":ui_view_appointments,"📆 Search by Date":ui_search_appointment,
    "👨‍⚕️ View All Doctors":ui_view_doctors,
}
RECEPTION_SECTIONS = [
    ("Overview",     ["🏠 Dashboard"]),
    ("Patients",     ["➕ Add Patient","👁️ View Patients","🔍 Search Patient"]),
    ("Appointments", ["📅 Book Appointment","📋 View Appointments"]),
    ("Billing",      ["🧾 Generate Bill","💰 View Bills"]),
]
RECEPTION_DISPATCH = {
    "➕ Add Patient":ui_add_patient,"👁️ View Patients":ui_view_patients,
    "🔍 Search Patient":ui_search_patient,
    "📅 Book Appointment":ui_book_appointment,"📋 View Appointments":ui_view_appointments,
    "🧾 Generate Bill":ui_generate_bill,"💰 View Bills":ui_view_bills,
}

def render_dashboard(role, page_key, sections, dispatch, stats_html, welcome_msg):
    build_sidebar(role, page_key, sections)
    dashboard_header(role)
    st.markdown(stats_html, unsafe_allow_html=True)
    menu = st.session_state[page_key]
    if menu in ("🏠 Home","🏠 Dashboard"):
        st.markdown(f'<div class="dash-card"><h4>{welcome_msg["title"]}</h4><p>{welcome_msg["body"]}</p></div>', unsafe_allow_html=True)
    elif menu in dispatch:
        dispatch[menu]()

def admin_dashboard():
    stats = f"""
    <div class="dstat-row">
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.doctor_list)}</div><div class="dstat-label">👨‍⚕️ Doctors</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.patient_list)}</div><div class="dstat-label">🧑 Patients</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.appointment_list)}</div><div class="dstat-label">📅 Appointments</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.bill_list)}</div><div class="dstat-label">🧾 Bills</div></div>
    </div>"""
    render_dashboard("admin","admin_page",ADMIN_SECTIONS,ADMIN_DISPATCH,stats,
        {"title":"Welcome, Admin 🛡️","body":"Use the sidebar to manage doctors, patients, appointments, billing, and salary records."})

def doctor_dashboard():
    stats = f"""
    <div class="dstat-row">
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.patient_list)}</div><div class="dstat-label">🧑 Patients</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.appointment_list)}</div><div class="dstat-label">📅 Appointments</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.doctor_list)}</div><div class="dstat-label">👨‍⚕️ Doctors</div></div>
    </div>"""
    render_dashboard("doctor","doctor_page",DOCTOR_SECTIONS,DOCTOR_DISPATCH,stats,
        {"title":"Welcome, Doctor 👨‍⚕️","body":"Use the sidebar to view patients and check appointment schedules."})

def reception_dashboard():
    stats = f"""
    <div class="dstat-row">
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.patient_list)}</div><div class="dstat-label">🧑 Patients</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.appointment_list)}</div><div class="dstat-label">📅 Appointments</div></div>
      <div class="dstat-card"><div class="dstat-number">{len(st.session_state.bill_list)}</div><div class="dstat-label">🧾 Bills</div></div>
    </div>"""
    render_dashboard("reception","reception_page",RECEPTION_SECTIONS,RECEPTION_DISPATCH,stats,
        {"title":"Welcome, Receptionist 🗂️","body":"Use the sidebar to register patients, book appointments, and generate bills."})

# ══════════════════════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.logged_in:
    role = st.session_state.role
    if role=="admin":       admin_dashboard()
    elif role=="doctor":    doctor_dashboard()
    elif role=="reception": reception_dashboard()
elif st.session_state.show_login:
    show_login_page()
else:
    show_landing()
