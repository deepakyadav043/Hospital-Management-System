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

defaults = {
    "logged_in": False, "role": None, "show_login": False,
    "doctor_list": [], "patient_list": [], "appointment_list": [],
    "bill_list": [], "salary_list": [],
    "admin_page":     "🏠 Home",
    "doctor_page":    "🏠 Dashboard",
    "reception_page": "🏠 Dashboard",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Outfit:wght@300;400;500;600;700&display=swap');

:root {
  --teal:#0d9488; --teal2:#14b8a6; --teal3:#5eead4;
  --navy:#020617; --navy2:#0f172a; --navy3:#1e293b;
  --accent:#f59e0b; --accent2:#fbbf24;
  --red:#ef4444; --green:#22c55e;
  --muted:#64748b; --text:#e2e8f0; --subtext:#94a3b8;
  --border:rgba(20,184,166,0.18);
  --glass:rgba(15,23,42,0.65);
  --radius:16px;
}

*, *::before, *::after {
  box-sizing: border-box;
  outline: none !important;
  box-shadow: none !important;
}
*:focus, *:focus-visible, *:focus-within { outline: none !important; box-shadow: none !important; }

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
.stApp {
  background: var(--navy);
  background-image:
    radial-gradient(ellipse 80% 60% at 10% 0%, rgba(13,148,136,0.12) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 90% 100%, rgba(245,158,11,0.06) 0%, transparent 60%);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 2rem !important; max-width: 100% !important; }

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--navy2); }
::-webkit-scrollbar-thumb { background: var(--teal); border-radius: 10px; }

/* ══════════════════════════════════════════
   SIDEBAR
══════════════════════════════════════════ */
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #020617 0%, #0a1628 40%, #0d2a28 100%) !important;
  border-right: 1px solid var(--border) !important;
  width: 260px !important;
}
section[data-testid="stSidebar"] * { color: white !important; }
section[data-testid="stSidebar"] [data-testid="stRadio"] { display: none !important; }

/* Sidebar nav buttons */
section[data-testid="stSidebar"] .stButton > button {
  background: transparent !important;
  border: none !important;
  border-radius: 10px !important;
  color: #94a3b8 !important;
  text-align: left !important;
  width: 100% !important;
  padding: 9px 14px !important;
  font-size: 0.85rem !important;
  font-weight: 500 !important;
  font-family: 'Outfit', sans-serif !important;
  letter-spacing: 0.01em !important;
  transition: all 0.2s ease !important;
  justify-content: flex-start !important;
  outline: none !important;
  box-shadow: none !important;
  position: relative !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
  background: rgba(20,184,166,0.1) !important;
  color: #e2e8f0 !important;
  transform: translateX(3px) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
  background: linear-gradient(135deg, rgba(13,148,136,0.25), rgba(20,184,166,0.15)) !important;
  color: #5eead4 !important;
  font-weight: 600 !important;
  border-left: 2px solid #14b8a6 !important;
}
.logout-btn > button {
  background: rgba(239,68,68,0.1) !important;
  border: 1px solid rgba(239,68,68,0.3) !important;
  color: #fca5a5 !important;
  border-radius: 10px !important;
  width: 100% !important;
  padding: 9px 14px !important;
  font-weight: 600 !important;
  font-family: 'Outfit', sans-serif !important;
}
.logout-btn > button:hover {
  background: rgba(239,68,68,0.2) !important;
  color: #fff !important;
}
.sb-label {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: rgba(20,184,166,0.55);
  text-transform: uppercase;
  padding: 14px 14px 4px;
  display: block;
}
.sb-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(20,184,166,0.2), transparent);
  margin: 6px 12px;
}

/* ══════════════════════════════════════════
   TOP HEADER BAR
══════════════════════════════════════════ */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 28px;
  background: linear-gradient(135deg, rgba(15,23,42,0.9), rgba(13,78,74,0.4));
  border: 1px solid var(--border);
  border-radius: 18px;
  margin-bottom: 1.8rem;
  backdrop-filter: blur(12px);
  animation: slideDown 0.5s ease;
}
.topbar-left { display: flex; align-items: center; gap: 14px; }
.topbar-icon {
  width: 44px; height: 44px;
  background: linear-gradient(135deg, var(--teal), var(--teal2));
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.4rem;
  box-shadow: 0 4px 15px rgba(13,148,136,0.35);
}
.topbar-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.2rem; font-weight: 700;
  color: white;
}
.topbar-subtitle { font-size: 0.78rem; color: var(--subtext); margin-top: 1px; }
.topbar-right { display: flex; align-items: center; gap: 16px; }
.topbar-badge {
  background: rgba(20,184,166,0.12);
  border: 1px solid rgba(20,184,166,0.25);
  border-radius: 20px;
  padding: 5px 14px;
  font-size: 0.78rem;
  color: var(--teal3);
  font-weight: 500;
}
.status-dot {
  display: inline-block;
  width: 7px; height: 7px;
  background: var(--green);
  border-radius: 50%;
  margin-right: 6px;
  animation: pulse 2s infinite;
}

/* ══════════════════════════════════════════
   STAT CARDS — ANIMATED
══════════════════════════════════════════ */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 14px;
  margin-bottom: 2rem;
}
.stat-card {
  background: linear-gradient(145deg, rgba(30,41,59,0.8), rgba(15,23,42,0.9));
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px 20px;
  position: relative;
  overflow: hidden;
  cursor: default;
  animation: fadeUp 0.5s ease both;
  transition: transform 0.25s ease, border-color 0.25s ease;
}
.stat-card:hover {
  transform: translateY(-5px);
  border-color: rgba(20,184,166,0.4);
}
.stat-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--teal), var(--teal2), transparent);
  border-radius: 18px 18px 0 0;
}
.stat-card::after {
  content: '';
  position: absolute;
  bottom: -30px; right: -20px;
  width: 80px; height: 80px;
  border-radius: 50%;
  background: rgba(20,184,166,0.05);
}
.stat-icon {
  font-size: 1.6rem;
  margin-bottom: 10px;
  display: block;
}
.stat-number {
  font-family: 'Syne', sans-serif;
  font-size: 2.4rem;
  font-weight: 800;
  color: white;
  line-height: 1;
  letter-spacing: -0.02em;
}
.stat-label {
  font-size: 0.78rem;
  color: var(--subtext);
  margin-top: 5px;
  font-weight: 500;
  letter-spacing: 0.03em;
}
.stat-trend {
  position: absolute;
  top: 18px; right: 18px;
  font-size: 0.7rem;
  color: var(--green);
  background: rgba(34,197,94,0.1);
  border-radius: 8px;
  padding: 2px 8px;
}
.stat-card:nth-child(1) { animation-delay: 0.05s; }
.stat-card:nth-child(2) { animation-delay: 0.1s; }
.stat-card:nth-child(3) { animation-delay: 0.15s; }
.stat-card:nth-child(4) { animation-delay: 0.2s; }

/* ══════════════════════════════════════════
   SECTION TITLE
══════════════════════════════════════════ */
.section-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: white;
  margin: 2rem 0 1.2rem;
  display: flex;
  align-items: center;
  gap: 10px;
}
.section-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, var(--border), transparent);
}

/* ══════════════════════════════════════════
   CONTENT CARD (for forms / sections)
══════════════════════════════════════════ */
.content-card {
  background: linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.8));
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px;
  backdrop-filter: blur(8px);
  animation: fadeUp 0.4s ease;
  margin-bottom: 1rem;
}

/* ══════════════════════════════════════════
   WELCOME CARD (home screen)
══════════════════════════════════════════ */
.welcome-card {
  background: linear-gradient(135deg, rgba(13,148,136,0.15), rgba(20,184,166,0.08), rgba(15,23,42,0.9));
  border: 1px solid rgba(20,184,166,0.25);
  border-radius: 20px;
  padding: 36px 40px;
  position: relative;
  overflow: hidden;
  animation: fadeUp 0.4s ease;
  margin-bottom: 1.5rem;
}
.welcome-card::before {
  content: '';
  position: absolute;
  top: -50px; right: -50px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(20,184,166,0.12) 0%, transparent 70%);
  border-radius: 50%;
}
.welcome-card::after {
  content: '';
  position: absolute;
  bottom: -30px; left: -30px;
  width: 150px; height: 150px;
  background: radial-gradient(circle, rgba(245,158,11,0.06) 0%, transparent 70%);
  border-radius: 50%;
}
.welcome-role {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--teal2);
  margin-bottom: 8px;
}
.welcome-title {
  font-family: 'Syne', sans-serif;
  font-size: 2rem;
  font-weight: 800;
  color: white;
  margin: 0 0 10px;
  line-height: 1.15;
}
.welcome-sub {
  color: var(--subtext);
  font-size: 0.92rem;
  line-height: 1.65;
  max-width: 520px;
}
.quick-actions {
  display: flex;
  gap: 10px;
  margin-top: 20px;
  flex-wrap: wrap;
}
.qa-chip {
  background: rgba(20,184,166,0.12);
  border: 1px solid rgba(20,184,166,0.22);
  border-radius: 30px;
  padding: 7px 16px;
  font-size: 0.8rem;
  color: var(--teal3);
  font-weight: 500;
  cursor: default;
  transition: all 0.2s;
}
.qa-chip:hover {
  background: rgba(20,184,166,0.22);
  color: white;
}

/* ══════════════════════════════════════════
   INFO ROW (quick info blocks)
══════════════════════════════════════════ */
.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-bottom: 1.5rem;
}
.info-tile {
  background: rgba(30,41,59,0.5);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 18px;
  transition: all 0.2s;
}
.info-tile:hover {
  background: rgba(30,41,59,0.8);
  border-color: rgba(20,184,166,0.3);
}
.info-tile-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--teal2);
  margin-bottom: 6px;
}
.info-tile-value {
  font-size: 0.9rem;
  color: var(--text);
  line-height: 1.6;
}

/* ══════════════════════════════════════════
   DATA TABLE
══════════════════════════════════════════ */
.data-table-wrap {
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--border);
  animation: fadeUp 0.4s ease;
}
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
}
.data-table thead tr {
  background: linear-gradient(135deg, rgba(13,148,136,0.35), rgba(20,184,166,0.2));
}
.data-table th {
  padding: 13px 18px;
  text-align: left;
  font-weight: 600;
  color: var(--teal3);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.data-table td {
  padding: 12px 18px;
  border-bottom: 1px solid rgba(20,184,166,0.07);
  color: var(--text);
  background: rgba(15,23,42,0.6);
}
.data-table tr:last-child td { border-bottom: none; }
.data-table tbody tr:hover td {
  background: rgba(20,184,166,0.07);
  transition: 0.15s;
}
.table-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 20px;
  font-size: 0.72rem;
  font-weight: 600;
  background: rgba(20,184,166,0.15);
  color: var(--teal3);
}

/* ══════════════════════════════════════════
   SLIP / RECEIPT
══════════════════════════════════════════ */
.slip-card {
  background: linear-gradient(135deg, rgba(13,148,136,0.12), rgba(15,23,42,0.95));
  border: 1px solid rgba(20,184,166,0.3);
  border-radius: 18px;
  padding: 28px;
  animation: fadeUp 0.4s ease;
  position: relative;
  overflow: hidden;
}
.slip-card::after {
  content: '🏥';
  position: absolute;
  bottom: 10px; right: 20px;
  font-size: 3rem;
  opacity: 0.07;
}
.slip-header {
  font-family: 'Syne', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  color: white;
  margin-bottom: 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}
.slip-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid rgba(20,184,166,0.06);
  font-size: 0.9rem;
}
.slip-row:last-child { border-bottom: none; }
.slip-key { color: var(--subtext); }
.slip-val { color: white; font-weight: 500; }
.slip-total {
  margin-top: 14px;
  padding: 14px;
  background: rgba(20,184,166,0.1);
  border: 1px solid rgba(20,184,166,0.2);
  border-radius: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.slip-total-label { font-size: 0.85rem; color: var(--subtext); font-weight: 600; }
.slip-total-val {
  font-family: 'Syne', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--teal2);
}

/* ══════════════════════════════════════════
   DASH INLINE CARD
══════════════════════════════════════════ */
.dash-card {
  background: rgba(30,41,59,0.5);
  border: 1px solid var(--border);
  border-left: 3px solid var(--teal2);
  border-radius: 12px;
  padding: 18px 20px;
  margin-bottom: 12px;
  transition: all 0.2s;
  animation: fadeUp 0.3s ease;
}
.dash-card:hover {
  background: rgba(30,41,59,0.8);
  border-color: rgba(20,184,166,0.35);
  transform: translateX(3px);
}
.dash-card h4 { color: white; margin: 0 0 5px; font-size: 0.95rem; font-weight: 600; }
.dash-card p  { color: var(--subtext); margin: 0; font-size: 0.85rem; line-height: 1.6; }

/* ══════════════════════════════════════════
   FORM INPUTS
══════════════════════════════════════════ */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTimeInput input {
  border-radius: 10px !important;
  border: 1px solid rgba(20,184,166,0.3) !important;
  background: rgba(15,23,42,0.6) !important;
  color: white !important;
  transition: border-color 0.2s !important;
}
.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus,
.stTimeInput input:focus {
  border-color: var(--teal2) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(20,184,166,0.12) !important;
}
div[data-baseweb="select"] > div {
  border-radius: 10px !important;
  border: 1px solid rgba(20,184,166,0.3) !important;
  background: rgba(15,23,42,0.6) !important;
}
div[data-baseweb="select"] > div:focus-within {
  border-color: var(--teal2) !important;
  box-shadow: 0 0 0 3px rgba(20,184,166,0.12) !important;
}

/* ── Global submit buttons ── */
.stButton > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  font-family: 'Outfit', sans-serif !important;
  transition: all 0.2s !important;
}
.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, var(--teal), var(--teal2)) !important;
  color: white !important;
  border: none !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(20,184,166,0.35) !important;
}
.stFormSubmitButton > button {
  background: linear-gradient(135deg, var(--teal), var(--teal2)) !important;
  color: white !important;
  border: none !important;
  border-radius: 10px !important;
  font-weight: 600 !important;
}
.stFormSubmitButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(20,184,166,0.35) !important;
}

/* ══════════════════════════════════════════
   LANDING STYLES
══════════════════════════════════════════ */
.landing-nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 28px;
  background: rgba(15,23,42,0.8);
  border: 1px solid var(--border);
  border-radius: 18px;
  margin-bottom: 2rem;
  backdrop-filter: blur(12px);
}
.landing-nav-brand {
  font-family: 'Syne', sans-serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: white;
  display: flex; align-items: center; gap: 10px;
}
.landing-nav-info { font-size: 0.78rem; color: var(--subtext); }
.hero {
  border-radius: 22px; overflow: hidden;
  position: relative; min-height: 380px;
  display: flex; align-items: flex-end;
  margin-bottom: 2rem;
}
.hero-img { position: absolute; top:0; left:0; width:100%; height:100%; object-fit:cover; }
.hero-overlay {
  position: absolute; top:0; left:0; width:100%; height:100%;
  background: linear-gradient(100deg, rgba(2,6,23,0.92) 0%, rgba(13,78,74,0.7) 55%, rgba(13,148,136,0.35) 100%);
}
.hero-content { position: relative; z-index:2; padding: 56px 60px; width: 100%; }
.hero h1 {
  font-family: 'Syne', sans-serif;
  font-size: 3.2rem; font-weight: 800;
  line-height: 1.1; margin: 0 0 10px;
  color: white;
}
.hero h1 span { color: var(--teal2); }
.hero-tagline { font-size: 1.05rem; color: #a7f3d0; margin-bottom: 1.6rem; font-weight: 300; }
.hero-badges { display:flex; gap:10px; flex-wrap:wrap; }
.badge {
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 30px; padding: 5px 15px;
  font-size: 0.8rem; color: #ccfbf1;
  backdrop-filter: blur(4px);
}
.landing-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 14px; margin-bottom: 2rem;
}
.landing-stat {
  background: rgba(30,41,59,0.6);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 22px 16px;
  text-align: center;
  border-top: 3px solid var(--teal);
  transition: 0.25s;
}
.landing-stat:hover { transform: translateY(-4px); border-color: var(--teal2); }
.landing-stat-num {
  font-family: 'Syne', sans-serif;
  font-size: 2rem; font-weight: 800; color: var(--teal2);
}
.landing-stat-label { font-size: 0.77rem; color: var(--subtext); margin-top: 4px; }
.section-head {
  font-family: 'Syne', sans-serif;
  font-size: 1.7rem; font-weight: 700; color: white;
  display: flex; align-items: center; gap: 12px;
  margin: 2rem 0 1.2rem;
}
.section-head::before {
  content: '';
  width: 5px; height: 26px;
  background: linear-gradient(180deg, var(--teal), var(--teal2));
  border-radius: 3px;
  display: inline-block;
}
.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 14px; margin-bottom: 2rem;
}
.service-card {
  background: rgba(30,41,59,0.6);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 26px 18px;
  text-align: center;
  transition: all 0.25s;
  cursor: default;
}
.service-card:hover {
  transform: translateY(-5px);
  border-color: rgba(20,184,166,0.35);
  background: rgba(13,148,136,0.12);
}
.service-icon { font-size: 2.2rem; margin-bottom: 10px; }
.service-title { font-weight: 600; color: white; font-size: 0.9rem; }
.service-desc  { font-size: 0.75rem; color: var(--subtext); margin-top: 4px; }
.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 12px; margin-bottom: 2rem;
}
.contact-card {
  background: rgba(20,184,166,0.06);
  border: 1px solid rgba(20,184,166,0.15);
  border-radius: 14px; padding: 20px;
}
.contact-card h4 { color: var(--teal2); font-size: 0.88rem; font-weight: 700; margin: 0 0 8px; }
.contact-card p  { color: var(--subtext); font-size: 0.84rem; line-height: 1.7; margin: 0; }
.footer-bar {
  background: rgba(15,23,42,0.8);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 26px 36px;
  text-align: center;
  margin-top: 3rem;
  font-size: 0.82rem;
  color: var(--subtext);
  line-height: 2;
}
.footer-bar strong { color: white; font-size: 1rem; font-family: 'Syne', sans-serif; }
.footer-bar a { color: var(--teal2); text-decoration: none; }

/* ══════════════════════════════════════════
   LOGIN
══════════════════════════════════════════ */
.login-wrap {
  background: linear-gradient(145deg, rgba(30,41,59,0.85), rgba(15,23,42,0.95));
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 40px;
  backdrop-filter: blur(12px);
  animation: fadeUp 0.4s ease;
}
.login-logo {
  text-align: center;
  margin-bottom: 24px;
}
.login-icon {
  font-size: 3rem;
  display: block;
  margin-bottom: 8px;
}
.login-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: white;
  margin: 0 0 4px;
}
.login-sub { color: var(--subtext); font-size: 0.85rem; }
.stSelectbox label, .stTextInput label { color: var(--subtext) !important; font-size: 0.82rem !important; }

/* ══════════════════════════════════════════
   ANIMATIONS
══════════════════════════════════════════ */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-12px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

/* ── Metric style ── */
[data-testid="stMetric"] {
  background: rgba(30,41,59,0.6) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  padding: 16px 18px !important;
}
[data-testid="stMetricLabel"] { color: var(--subtext) !important; font-size: 0.78rem !important; }
[data-testid="stMetricValue"] { color: var(--teal2) !important; font-family: 'Syne', sans-serif !important; }

[data-testid="stSidebar"] input[type="radio"] { display: none !important; }
[data-testid="stSidebar"] .st-emotion-cache-j7qwjs { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def logout():
    for k in ["logged_in","role","show_login","admin_page","doctor_page","reception_page"]:
        st.session_state[k] = defaults[k]

def next_id(lst): return len(lst) + 1

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def build_sidebar(role, page_key, sections):
    role_meta = {
        "admin":     ("🛡️", "Administrator", "#f59e0b"),
        "doctor":    ("👨‍⚕️", "Doctor", "#14b8a6"),
        "reception": ("🗂️", "Receptionist", "#8b5cf6"),
    }
    icon, label, color = role_meta[role]
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:20px 12px 16px; text-align:center;">
          <div style="font-size:2.2rem; margin-bottom:6px;">🏥</div>
          <div style="font-family:'Syne',sans-serif; font-size:1rem; color:white; font-weight:700;">
            Jan Kalyan Hospital
          </div>
          <div style="margin-top:10px; display:inline-flex; align-items:center; gap:7px;
               background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1);
               border-radius:20px; padding:5px 14px;">
            <span style="font-size:1rem;">{icon}</span>
            <span style="font-size:0.78rem; color:#94a3b8; font-weight:500;">{label}</span>
          </div>
        </div>
        <div style="height:1px; background:linear-gradient(90deg,transparent,rgba(20,184,166,0.25),transparent); margin:0 8px 6px;"></div>
        """, unsafe_allow_html=True)

        current = st.session_state[page_key]
        for section_title, pages in sections:
            st.markdown(f'<span class="sb-label">{section_title}</span>', unsafe_allow_html=True)
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

        st.markdown('<div style="height:1px; background:rgba(239,68,68,0.2); margin:10px 8px 8px;"></div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="logout-btn">', unsafe_allow_html=True)
            if st.button("🚪 Logout", key=f"logout_{role}", use_container_width=True):
                logout(); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  TOP BAR
# ══════════════════════════════════════════════════════════════════════════════
def dashboard_header(role):
    from datetime import datetime
    now = datetime.now()
    hour = now.hour
    greeting = "Good morning" if hour < 12 else ("Good afternoon" if hour < 17 else "Good evening")

    labels = {"admin": ("Administrator", "🛡️"), "doctor": ("Doctor", "👨‍⚕️"), "reception": ("Receptionist", "🗂️")}
    label, icon = labels[role]

    st.markdown(f"""
    <div class="topbar">
      <div class="topbar-left">
        <div class="topbar-icon">🏥</div>
        <div>
          <div class="topbar-title">Jan Kalyan Hospital</div>
          <div class="topbar-subtitle">{greeting}, {label} {icon}</div>
        </div>
      </div>
      <div class="topbar-right">
        <div class="topbar-badge"><span class="status-dot"></span>System Online</div>
        <div class="topbar-badge">📅 {now.strftime('%d %b %Y')}</div>
        <div class="topbar-badge">🕐 {now.strftime('%I:%M %p')}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  FEATURE UIs
# ══════════════════════════════════════════════════════════════════════════════
def ui_add_doctor():
    st.markdown('<div class="section-title">➕ Add New Doctor</div>', unsafe_allow_html=True)
    with st.form("add_doc"):
        c1, c2 = st.columns(2)
        with c1:
            n = st.text_input("Doctor Name", placeholder="Dr. Full Name")
            s = st.text_input("Specialization", placeholder="e.g. Cardiology")
        with c2:
            e = st.number_input("Experience (years)", 0, 60, step=1)
            f = st.number_input("Consultation Fee (₹)", 0, step=100)
        if st.form_submit_button("➕ Add Doctor", type="primary", use_container_width=True):
            if n and s:
                st.session_state.doctor_list.append({
                    "id": next_id(st.session_state.doctor_list),
                    "name": n, "spec": s, "exp": e, "fee": f
                })
                st.success(f"✅ Dr. {n} has been added successfully!")
            else:
                st.warning("⚠️ Please fill in all required fields.")

def ui_view_doctors():
    st.markdown('<div class="section-title">👨‍⚕️ All Doctors</div>', unsafe_allow_html=True)
    dl = st.session_state.doctor_list
    if not dl:
        st.info("📋 No doctors added yet. Use 'Add Doctor' to get started.")
        return
    rows = "".join(
        f"""<tr>
          <td><span class="table-badge">#{d['id']}</span></td>
          <td><strong style="color:white">Dr. {d['name']}</strong></td>
          <td>{d['spec']}</td>
          <td>{d['exp']} yrs</td>
          <td style="color:#14b8a6;font-weight:600;">₹{d['fee']:,}</td>
        </tr>""" for d in dl
    )
    st.markdown(f"""
    <div class="data-table-wrap">
      <table class="data-table">
        <thead><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Experience</th><th>Fee</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    """, unsafe_allow_html=True)
    st.caption(f"Showing {len(dl)} doctor(s)")

def ui_search_doctor():
    st.markdown('<div class="section-title">🔍 Search Doctor</div>', unsafe_allow_html=True)
    q = st.text_input("Search by doctor name", placeholder="Type to search...")
    if q:
        found = [d for d in st.session_state.doctor_list if q.lower() in d['name'].lower()]
        if found:
            for d in found:
                st.markdown(f"""
                <div class="dash-card">
                  <h4>👨‍⚕️ Dr. {d['name']}</h4>
                  <p>🏥 <b>Specialization:</b> {d['spec']} &nbsp;&nbsp; ⏳ <b>Experience:</b> {d['exp']} years &nbsp;&nbsp; 💰 <b>Fee:</b> ₹{d['fee']:,}</p>
                </div>""", unsafe_allow_html=True)
        else:
            st.error(f"❌ No doctor found matching '{q}'")

def ui_delete_doctor():
    st.markdown('<div class="section-title">🗑️ Delete Doctor</div>', unsafe_allow_html=True)
    if not st.session_state.doctor_list:
        st.info("No doctors to delete."); return
    opts = {f"#{d['id']} — Dr. {d['name']} ({d['spec']})": d['id'] for d in st.session_state.doctor_list}
    sel = st.selectbox("Select Doctor to Remove", list(opts.keys()))
    st.warning("⚠️ This action cannot be undone.")
    if st.button("🗑️ Confirm Delete", type="primary"):
        st.session_state.doctor_list = [d for d in st.session_state.doctor_list if d['id'] != opts[sel]]
        st.success("✅ Doctor removed successfully."); st.rerun()

def ui_add_patient():
    st.markdown('<div class="section-title">➕ Register New Patient</div>', unsafe_allow_html=True)
    with st.form("add_pat"):
        c1, c2 = st.columns(2)
        with c1:
            n = st.text_input("Patient Name", placeholder="Full name")
            a = st.number_input("Age", 0, 130, step=1)
        with c2:
            d = st.text_input("Disease / Condition", placeholder="Primary diagnosis")
            r = st.text_input("Room Number", placeholder="e.g. 201-A")
        if st.form_submit_button("➕ Register Patient", type="primary", use_container_width=True):
            if n and d:
                st.session_state.patient_list.append({
                    "id": next_id(st.session_state.patient_list),
                    "name": n, "age": a, "disease": d, "room": r
                })
                st.success(f"✅ {n} registered successfully!")
            else:
                st.warning("⚠️ Please fill all required fields.")

def ui_view_patients():
    st.markdown('<div class="section-title">🧑‍⚕️ All Patients</div>', unsafe_allow_html=True)
    pl = st.session_state.patient_list
    if not pl:
        st.info("📋 No patients registered yet."); return
    rows = "".join(
        f"""<tr>
          <td><span class="table-badge">#{p['id']}</span></td>
          <td><strong style="color:white">{p['name']}</strong></td>
          <td>{p['age']}</td>
          <td>{p['disease']}</td>
          <td><span class="table-badge">🚪 {p['room']}</span></td>
        </tr>""" for p in pl
    )
    st.markdown(f"""
    <div class="data-table-wrap">
      <table class="data-table">
        <thead><tr><th>ID</th><th>Name</th><th>Age</th><th>Condition</th><th>Room</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>""", unsafe_allow_html=True)
    st.caption(f"Showing {len(pl)} patient(s)")

def ui_search_patient():
    st.markdown('<div class="section-title">🔍 Search Patient</div>', unsafe_allow_html=True)
    method = st.radio("Search by", ["Name", "ID"], horizontal=True)
    found = []
    if method == "Name":
        q = st.text_input("Enter patient name", placeholder="Type to search...")
        if q:
            found = [p for p in st.session_state.patient_list if q.lower() in p['name'].lower()]
    else:
        q = st.number_input("Enter patient ID", min_value=1, step=1)
        if st.button("🔍 Search", type="primary"):
            found = [p for p in st.session_state.patient_list if p['id'] == int(q)]
    for p in found:
        st.markdown(f"""
        <div class="dash-card">
          <h4>🧑 {p['name']}</h4>
          <p>🆔 <b>ID:</b> {p['id']} &nbsp; 🎂 <b>Age:</b> {p['age']} &nbsp; 🏥 <b>Condition:</b> {p['disease']} &nbsp; 🚪 <b>Room:</b> {p['room']}</p>
        </div>""", unsafe_allow_html=True)
    if method == "Name" and not found and 'q' in dir() and q:
        st.error("❌ No patient found.")

def ui_book_appointment():
    st.markdown('<div class="section-title">📅 Book Appointment</div>', unsafe_allow_html=True)
    with st.form("book_appt"):
        c1, c2 = st.columns(2)
        with c1:
            doc = st.text_input("Doctor Name", placeholder="Attending doctor")
            pat = st.text_input("Patient Name", placeholder="Patient full name")
        with c2:
            date = st.date_input("Appointment Date")
            time = st.time_input("Appointment Time")
        if st.form_submit_button("📅 Confirm Booking", type="primary", use_container_width=True):
            if doc and pat:
                st.session_state.appointment_list.append({
                    "id": next_id(st.session_state.appointment_list),
                    "doctor": doc, "patient": pat,
                    "date": str(date), "time": str(time)
                })
                st.success("✅ Appointment booked successfully!")
            else:
                st.warning("⚠️ Please fill all fields.")

def ui_view_appointments():
    st.markdown('<div class="section-title">📋 All Appointments</div>', unsafe_allow_html=True)
    al = st.session_state.appointment_list
    if not al:
        st.info("📋 No appointments scheduled yet."); return
    rows = "".join(
        f"""<tr>
          <td><span class="table-badge">#{a['id']}</span></td>
          <td><strong style="color:white">{a['doctor']}</strong></td>
          <td>{a['patient']}</td>
          <td>📅 {a['date']}</td>
          <td>🕐 {a['time']}</td>
        </tr>""" for a in al
    )
    st.markdown(f"""
    <div class="data-table-wrap">
      <table class="data-table">
        <thead><tr><th>ID</th><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>""", unsafe_allow_html=True)
    st.caption(f"Showing {len(al)} appointment(s)")

def ui_search_appointment():
    st.markdown('<div class="section-title">📆 Search by Date</div>', unsafe_allow_html=True)
    date = st.date_input("Select Date")
    found = [a for a in st.session_state.appointment_list if a['date'] == str(date)]
    if found:
        st.success(f"Found {len(found)} appointment(s) on {date}")
        for a in found:
            st.markdown(f"""
            <div class="dash-card">
              <h4>📅 Appointment #{a['id']}</h4>
              <p>👨‍⚕️ <b>Doctor:</b> {a['doctor']} &nbsp; 🧑 <b>Patient:</b> {a['patient']} &nbsp; 🕐 <b>Time:</b> {a['time']}</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.info(f"No appointments found on {date}.")

def ui_generate_bill():
    st.markdown('<div class="section-title">🧾 Generate Bill</div>', unsafe_allow_html=True)
    with st.form("gen_bill"):
        name = st.text_input("Patient Name", placeholder="Full name")
        c1, c2, c3 = st.columns(3)
        with c1: doc_f = st.number_input("Doctor Fee (₹)", 0, step=100)
        with c2: room  = st.number_input("Room Charges (₹)", 0, step=100)
        with c3: med   = st.number_input("Medicine Charges (₹)", 0, step=100)
        if st.form_submit_button("🧾 Generate Bill", type="primary", use_container_width=True):
            if name:
                total = doc_f + room + med
                b = {"id": next_id(st.session_state.bill_list), "name": name,
                     "doc_fee": doc_f, "room": room, "med": med, "total": total}
                st.session_state.bill_list.append(b)
                st.markdown(f"""
                <div class="slip-card">
                  <div class="slip-header">🧾 Bill Receipt #{b['id']}</div>
                  <div class="slip-row"><span class="slip-key">Patient Name</span><span class="slip-val">{name}</span></div>
                  <div class="slip-row"><span class="slip-key">Doctor Consultation</span><span class="slip-val">₹{doc_f:,}</span></div>
                  <div class="slip-row"><span class="slip-key">Room Charges</span><span class="slip-val">₹{room:,}</span></div>
                  <div class="slip-row"><span class="slip-key">Medicine & Supplies</span><span class="slip-val">₹{med:,}</span></div>
                  <div class="slip-total">
                    <span class="slip-total-label">💰 Total Amount Due</span>
                    <span class="slip-total-val">₹{total:,}</span>
                  </div>
                </div>""", unsafe_allow_html=True)
            else:
                st.warning("⚠️ Enter patient name.")

def ui_view_bills():
    st.markdown('<div class="section-title">💰 All Bills</div>', unsafe_allow_html=True)
    bl = st.session_state.bill_list
    if not bl:
        st.info("No bills generated yet."); return
    rows = "".join(
        f"""<tr>
          <td><span class="table-badge">#{b['id']}</span></td>
          <td><strong style="color:white">{b['name']}</strong></td>
          <td>₹{b['doc_fee']:,}</td>
          <td>₹{b['room']:,}</td>
          <td>₹{b['med']:,}</td>
          <td style="color:#14b8a6;font-weight:700;">₹{b['total']:,}</td>
        </tr>""" for b in bl
    )
    st.markdown(f"""
    <div class="data-table-wrap">
      <table class="data-table">
        <thead><tr><th>ID</th><th>Patient</th><th>Doctor Fee</th><th>Room</th><th>Medicine</th><th>Total</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>""", unsafe_allow_html=True)
    total_rev = sum(b['total'] for b in bl)
    st.markdown(f"""
    <div style="margin-top:14px; background:rgba(20,184,166,0.08); border:1px solid rgba(20,184,166,0.2);
         border-radius:12px; padding:14px 20px; display:flex; justify-content:space-between; align-items:center;">
      <span style="color:#94a3b8; font-size:0.85rem;">Total Revenue from {len(bl)} bill(s)</span>
      <span style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800; color:#14b8a6;">₹{total_rev:,}</span>
    </div>""", unsafe_allow_html=True)

def ui_add_salary():
    st.markdown('<div class="section-title">💵 Generate Salary Slip</div>', unsafe_allow_html=True)
    with st.form("add_sal"):
        c1, c2 = st.columns(2)
        with c1:
            emp   = st.text_input("Employee Name", placeholder="Full name")
            etype = st.selectbox("Employee Type", ["Doctor", "Nurse", "Staff"])
            basic = st.number_input("Basic Salary (₹)", 0, step=1000)
        with c2:
            hra   = st.number_input("HRA %", 0.0, 100.0, value=10.0, step=0.5)
            da    = st.number_input("DA %", 0.0, 100.0, value=5.0, step=0.5)
            pf    = st.number_input("PF Deduction %", 0.0, 100.0, value=12.0, step=0.5)
        c3, c4 = st.columns(2)
        with c3: month = st.selectbox("Month", ["January","February","March","April","May","June","July","August","September","October","November","December"])
        with c4: year  = st.text_input("Year", "2025")
        if st.form_submit_button("💵 Generate Salary Slip", type="primary", use_container_width=True):
            if emp:
                hra_a = (hra/100)*basic; da_a = (da/100)*basic; pf_a = (pf/100)*basic
                gross = basic + hra_a + da_a; net = gross - pf_a
                s = {"id": next_id(st.session_state.salary_list), "name": emp, "type": etype,
                     "basic": basic, "hra": hra_a, "da": da_a, "pf": pf_a,
                     "gross": gross, "net": net, "month": month, "year": year}
                st.session_state.salary_list.append(s)
                st.markdown(f"""
                <div class="slip-card">
                  <div class="slip-header">💵 Salary Slip — {emp}</div>
                  <div class="slip-row"><span class="slip-key">Employee Type</span><span class="slip-val">{etype}</span></div>
                  <div class="slip-row"><span class="slip-key">Period</span><span class="slip-val">{month} {year}</span></div>
                  <div class="slip-row"><span class="slip-key">Basic Salary</span><span class="slip-val">₹{basic:,.0f}</span></div>
                  <div class="slip-row"><span class="slip-key">HRA ({hra}%)</span><span class="slip-val">₹{hra_a:,.0f}</span></div>
                  <div class="slip-row"><span class="slip-key">DA ({da}%)</span><span class="slip-val">₹{da_a:,.0f}</span></div>
                  <div class="slip-row"><span class="slip-key">Gross Salary</span><span class="slip-val">₹{gross:,.0f}</span></div>
                  <div class="slip-row"><span class="slip-key">PF Deduction ({pf}%)</span><span class="slip-val" style="color:#f87171;">− ₹{pf_a:,.0f}</span></div>
                  <div class="slip-total">
                    <span class="slip-total-label">🏦 Net Take-Home</span>
                    <span class="slip-total-val">₹{net:,.0f}</span>
                  </div>
                </div>""", unsafe_allow_html=True)

def ui_view_salaries():
    st.markdown('<div class="section-title">📑 All Salary Records</div>', unsafe_allow_html=True)
    sl = st.session_state.salary_list
    if not sl:
        st.info("No salary records yet."); return
    rows = "".join(
        f"""<tr>
          <td><span class="table-badge">#{s['id']}</span></td>
          <td><strong style="color:white">{s['name']}</strong></td>
          <td>{s['type']}</td>
          <td>₹{s['basic']:,}</td>
          <td>₹{s['gross']:,.0f}</td>
          <td style="color:#14b8a6;font-weight:700;">₹{s['net']:,.0f}</td>
          <td>{s['month']} {s['year']}</td>
        </tr>""" for s in sl
    )
    st.markdown(f"""
    <div class="data-table-wrap">
      <table class="data-table">
        <thead><tr><th>ID</th><th>Name</th><th>Type</th><th>Basic</th><th>Gross</th><th>Net</th><th>Month</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>""", unsafe_allow_html=True)

def ui_search_salary():
    st.markdown('<div class="section-title">🔎 Search Salary Record</div>', unsafe_allow_html=True)
    q = st.text_input("Employee name", placeholder="Type to search...")
    if q:
        found = [s for s in st.session_state.salary_list if q.lower() in s['name'].lower()]
        if found:
            for s in found:
                st.markdown(f"""
                <div class="dash-card">
                  <h4>💵 {s['name']} <span style="font-size:0.78rem;color:#94a3b8;font-weight:400;">({s['type']})</span></h4>
                  <p>📅 {s['month']} {s['year']} &nbsp; | &nbsp; Basic: ₹{s['basic']:,} &nbsp; | &nbsp;
                  <span style="color:#14b8a6;font-weight:600;">Net: ₹{s['net']:,.0f}</span></p>
                </div>""", unsafe_allow_html=True)
        else:
            st.error("❌ No record found.")

def ui_salary_calculator():
    st.markdown('<div class="section-title">🧮 Salary Calculator</div>', unsafe_allow_html=True)
    with st.form("sal_calc"):
        basic = st.number_input("Basic Salary (₹)", 0, step=1000)
        c1, c2, c3 = st.columns(3)
        with c1: hra = st.number_input("HRA %", 0.0, 100.0, value=10.0)
        with c2: da  = st.number_input("DA %",  0.0, 100.0, value=5.0)
        with c3: pf  = st.number_input("PF %",  0.0, 100.0, value=12.0)
        if st.form_submit_button("🧮 Calculate", type="primary", use_container_width=True):
            hra_a = (hra/100)*basic; da_a = (da/100)*basic; pf_a = (pf/100)*basic
            gross = basic + hra_a + da_a; net = gross - pf_a
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("💰 Gross", f"₹{gross:,.0f}")
            c2.metric("🏠 HRA",   f"₹{hra_a:,.0f}")
            c3.metric("📈 DA",    f"₹{da_a:,.0f}")
            c4.metric("🏦 Net",   f"₹{net:,.0f}")

def ui_delete_salary():
    st.markdown('<div class="section-title">🗑️ Delete Salary Record</div>', unsafe_allow_html=True)
    if not st.session_state.salary_list:
        st.info("No records."); return
    opts = {f"#{s['id']} — {s['name']} ({s['month']} {s['year']})": s['id'] for s in st.session_state.salary_list}
    sel = st.selectbox("Select Record", list(opts.keys()))
    st.warning("⚠️ This action cannot be undone.")
    if st.button("🗑️ Confirm Delete", type="primary"):
        st.session_state.salary_list = [s for s in st.session_state.salary_list if s['id'] != opts[sel]]
        st.success("✅ Record deleted."); st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  DASHBOARD SECTIONS
# ══════════════════════════════════════════════════════════════════════════════
ADMIN_SECTIONS = [
    ("Overview",     ["🏠 Home"]),
    ("Doctors",      ["➕ Add Doctor","👁️ View Doctors","🔍 Search Doctor","🗑️ Delete Doctor"]),
    ("Patients",     ["➕ Add Patient","👁️ View Patients","🔍 Search Patient"]),
    ("Appointments", ["📅 Book Appointment","📋 View Appointments","📆 Search by Date"]),
    ("Billing",      ["🧾 Generate Bill","💰 View Bills"]),
    ("Salary",       ["💵 Add Salary","📑 View Salaries","🔎 Search Salary","🧮 Salary Calculator","🗑️ Delete Salary"]),
]
ADMIN_DISPATCH = {
    "➕ Add Doctor": ui_add_doctor,"👁️ View Doctors": ui_view_doctors,
    "🔍 Search Doctor": ui_search_doctor,"🗑️ Delete Doctor": ui_delete_doctor,
    "➕ Add Patient": ui_add_patient,"👁️ View Patients": ui_view_patients,
    "🔍 Search Patient": ui_search_patient,
    "📅 Book Appointment": ui_book_appointment,"📋 View Appointments": ui_view_appointments,
    "📆 Search by Date": ui_search_appointment,
    "🧾 Generate Bill": ui_generate_bill,"💰 View Bills": ui_view_bills,
    "💵 Add Salary": ui_add_salary,"📑 View Salaries": ui_view_salaries,
    "🔎 Search Salary": ui_search_salary,"🧮 Salary Calculator": ui_salary_calculator,
    "🗑️ Delete Salary": ui_delete_salary,
}

DOCTOR_SECTIONS = [
    ("Overview",     ["🏠 Dashboard"]),
    ("Patients",     ["👁️ View Patients","🔍 Search Patient"]),
    ("Appointments", ["📅 View Appointments","📆 Search by Date"]),
    ("Doctors",      ["👨‍⚕️ View All Doctors"]),
]
DOCTOR_DISPATCH = {
    "👁️ View Patients": ui_view_patients,"🔍 Search Patient": ui_search_patient,
    "📅 View Appointments": ui_view_appointments,"📆 Search by Date": ui_search_appointment,
    "👨‍⚕️ View All Doctors": ui_view_doctors,
}

RECEPTION_SECTIONS = [
    ("Overview",     ["🏠 Dashboard"]),
    ("Patients",     ["➕ Add Patient","👁️ View Patients","🔍 Search Patient"]),
    ("Appointments", ["📅 Book Appointment","📋 View Appointments"]),
    ("Billing",      ["🧾 Generate Bill","💰 View Bills"]),
]
RECEPTION_DISPATCH = {
    "➕ Add Patient": ui_add_patient,"👁️ View Patients": ui_view_patients,
    "🔍 Search Patient": ui_search_patient,
    "📅 Book Appointment": ui_book_appointment,"📋 View Appointments": ui_view_appointments,
    "🧾 Generate Bill": ui_generate_bill,"💰 View Bills": ui_view_bills,
}

# ══════════════════════════════════════════════════════════════════════════════
#  HOME SCREENS
# ══════════════════════════════════════════════════════════════════════════════
def admin_home():
    dl = st.session_state.doctor_list
    pl = st.session_state.patient_list
    al = st.session_state.appointment_list
    bl = st.session_state.bill_list
    sl = st.session_state.salary_list
    total_rev = sum(b['total'] for b in bl)

    st.markdown(f"""
    <div class="welcome-card">
      <div class="welcome-role">🛡️ Administrator Panel</div>
      <div class="welcome-title">Welcome back, Admin</div>
      <div class="welcome-sub">
        Full access to all hospital operations — manage doctors, patients, appointments,
        billing, and payroll from this central command center.
      </div>
      <div class="quick-actions">
        <span class="qa-chip">👨‍⚕️ {len(dl)} Doctors</span>
        <span class="qa-chip">🧑 {len(pl)} Patients</span>
        <span class="qa-chip">📅 {len(al)} Appointments</span>
        <span class="qa-chip">💰 ₹{total_rev:,} Revenue</span>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-icon">👨‍⚕️</span>
        <div class="stat-number">{len(dl)}</div>
        <div class="stat-label">Registered Doctors</div>
        <div class="stat-trend">Active</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">🧑</span>
        <div class="stat-number">{len(pl)}</div>
        <div class="stat-label">Total Patients</div>
        <div class="stat-trend">In system</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">📅</span>
        <div class="stat-number">{len(al)}</div>
        <div class="stat-label">Appointments</div>
        <div class="stat-trend">Scheduled</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">🧾</span>
        <div class="stat-number">{len(bl)}</div>
        <div class="stat-label">Bills Generated</div>
        <div class="stat-trend">₹{total_rev:,}</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">💵</span>
        <div class="stat-number">{len(sl)}</div>
        <div class="stat-label">Salary Records</div>
        <div class="stat-trend">Payroll</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🏥 Hospital Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-grid">
      <div class="info-tile">
        <div class="info-tile-label">📍 Location</div>
        <div class="info-tile-value">Main Road, Bihar — 800001<br>India</div>
      </div>
      <div class="info-tile">
        <div class="info-tile-label">📞 Emergency</div>
        <div class="info-tile-value">+91 8989651400<br>Ambulance: 108</div>
      </div>
      <div class="info-tile">
        <div class="info-tile-label">🕐 OPD Hours</div>
        <div class="info-tile-value">8:00 AM – 8:00 PM<br>Emergency: 24 × 7</div>
      </div>
      <div class="info-tile">
        <div class="info-tile-label">🏅 Certifications</div>
        <div class="info-tile-value">ISO Certified<br>NABH Accredited</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

def doctor_home():
    pl = st.session_state.patient_list
    al = st.session_state.appointment_list
    dl = st.session_state.doctor_list
    st.markdown(f"""
    <div class="welcome-card">
      <div class="welcome-role">👨‍⚕️ Doctor Panel</div>
      <div class="welcome-title">Welcome, Doctor</div>
      <div class="welcome-sub">
        Access patient records, review your appointment schedule, and view the full doctor directory from here.
      </div>
      <div class="quick-actions">
        <span class="qa-chip">🧑 {len(pl)} Patients</span>
        <span class="qa-chip">📅 {len(al)} Appointments</span>
        <span class="qa-chip">👨‍⚕️ {len(dl)} Doctors on Staff</span>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-icon">🧑</span>
        <div class="stat-number">{len(pl)}</div>
        <div class="stat-label">Total Patients</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">📅</span>
        <div class="stat-number">{len(al)}</div>
        <div class="stat-label">Appointments</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">👨‍⚕️</span>
        <div class="stat-number">{len(dl)}</div>
        <div class="stat-label">Doctors on Staff</div>
      </div>
    </div>""", unsafe_allow_html=True)

def reception_home():
    pl = st.session_state.patient_list
    al = st.session_state.appointment_list
    bl = st.session_state.bill_list
    total_rev = sum(b['total'] for b in bl)
    st.markdown(f"""
    <div class="welcome-card">
      <div class="welcome-role">🗂️ Receptionist Panel</div>
      <div class="welcome-title">Welcome, Receptionist</div>
      <div class="welcome-sub">
        Register new patients, book appointments, and generate bills — all from this front-desk hub.
      </div>
      <div class="quick-actions">
        <span class="qa-chip">🧑 {len(pl)} Patients registered</span>
        <span class="qa-chip">📅 {len(al)} Appointments today</span>
        <span class="qa-chip">💰 ₹{total_rev:,} billed</span>
      </div>
    </div>
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-icon">🧑</span>
        <div class="stat-number">{len(pl)}</div>
        <div class="stat-label">Registered Patients</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">📅</span>
        <div class="stat-number">{len(al)}</div>
        <div class="stat-label">Appointments</div>
      </div>
      <div class="stat-card">
        <span class="stat-icon">🧾</span>
        <div class="stat-number">{len(bl)}</div>
        <div class="stat-label">Bills Generated</div>
        <div class="stat-trend">₹{total_rev:,}</div>
      </div>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  RENDER DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
def render_dashboard(role, page_key, sections, dispatch, home_fn):
    build_sidebar(role, page_key, sections)
    dashboard_header(role)
    menu = st.session_state[page_key]
    if menu in ("🏠 Home", "🏠 Dashboard"):
        home_fn()
    elif menu in dispatch:
        dispatch[menu]()

def admin_dashboard():
    render_dashboard("admin","admin_page",ADMIN_SECTIONS,ADMIN_DISPATCH,admin_home)

def doctor_dashboard():
    render_dashboard("doctor","doctor_page",DOCTOR_SECTIONS,DOCTOR_DISPATCH,doctor_home)

def reception_dashboard():
    render_dashboard("reception","reception_page",RECEPTION_SECTIONS,RECEPTION_DISPATCH,reception_home)

# ══════════════════════════════════════════════════════════════════════════════
#  LOGIN PAGE
# ══════════════════════════════════════════════════════════════════════════════
def show_login_page():
    _, col, _ = st.columns([1, 1.4, 1])
    with col:
        st.markdown("""
        <div class="login-wrap">
          <div class="login-logo">
            <span class="login-icon">🏥</span>
            <div class="login-title">Staff Portal</div>
            <div class="login-sub">Jan Kalyan Hospital — Authorized personnel only</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
        role_label = st.selectbox("Login as", ["Admin", "Doctor", "Receptionist"])
        username   = st.text_input("Username", placeholder="Enter your username")
        password   = st.text_input("Password", type="password", placeholder="Enter your password")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔐 Sign In", use_container_width=True, type="primary"):
                rm = {"Admin": "admin", "Doctor": "doctor", "Receptionist": "reception"}
                rk = rm[role_label]
                cred = CREDENTIALS.get(rk)
                if cred and username == rk and password == cred["password"]:
                    st.session_state.logged_in = True
                    st.session_state.role = cred["role"]
                    st.session_state.show_login = False
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Please try again.")
        with c2:
            if st.button("← Back", use_container_width=True):
                st.session_state.show_login = False; st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  LANDING PAGE
# ══════════════════════════════════════════════════════════════════════════════
def show_landing():
    st.markdown("""
    <div class="landing-nav">
      <div class="landing-nav-brand">🏥 Jan Kalyan Hospital</div>
      <div class="landing-nav-info">📍 Bihar &nbsp;|&nbsp; 📞 +91 8989651456 &nbsp;|&nbsp; ✉️ jankalyan@gmail.com</div>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn = st.columns([9, 1])
    with col_btn:
        if st.button("🔐 Staff Login", type="primary", use_container_width=True):
            st.session_state.show_login = True; st.rerun()

    st.markdown("""
    <div class="hero">
      <img class="hero-img" src="https://imkarchitects.com/images/expertise-healthcare-banner.jpg"
           alt="Hospital" onerror="this.style.display='none'">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <h1>Healing With <span>Heart</span>,<br>Serving With Care</h1>
        <p class="hero-tagline">Your health is our mission — advanced care, compassionate touch.</p>
        <div class="hero-badges">
          <span class="badge">🏅 ISO Certified</span>
          <span class="badge">🕐 24/7 Emergency</span>
          <span class="badge">👨‍⚕️ 50+ Specialists</span>
          <span class="badge">🏥 300 Bed Capacity</span>
        </div>
      </div>
    </div>
    <div class="landing-stats">
      <div class="landing-stat"><div class="landing-stat-num">15+</div><div class="landing-stat-label">Years of Excellence</div></div>
      <div class="landing-stat"><div class="landing-stat-num">50K+</div><div class="landing-stat-label">Patients Treated</div></div>
      <div class="landing-stat"><div class="landing-stat-num">50+</div><div class="landing-stat-label">Specialist Doctors</div></div>
      <div class="landing-stat"><div class="landing-stat-num">300</div><div class="landing-stat-label">Bed Capacity</div></div>
      <div class="landing-stat"><div class="landing-stat-num">24/7</div><div class="landing-stat-label">Emergency Care</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">Our Services</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="services-grid">
      <div class="service-card"><div class="service-icon">🫀</div><div class="service-title">Cardiology</div><div class="service-desc">Heart care & surgery</div></div>
      <div class="service-card"><div class="service-icon">🧠</div><div class="service-title">Neurology</div><div class="service-desc">Brain & nerve disorders</div></div>
      <div class="service-card"><div class="service-icon">🦴</div><div class="service-title">Orthopedics</div><div class="service-desc">Bones, joints & spine</div></div>
      <div class="service-card"><div class="service-icon">👶</div><div class="service-title">Pediatrics</div><div class="service-desc">Child health & care</div></div>
      <div class="service-card"><div class="service-icon">🔬</div><div class="service-title">Pathology</div><div class="service-desc">Lab tests & diagnosis</div></div>
      <div class="service-card"><div class="service-icon">🩻</div><div class="service-title">Radiology</div><div class="service-desc">X-ray, MRI, CT scan</div></div>
      <div class="service-card"><div class="service-icon">🚑</div><div class="service-title">Emergency</div><div class="service-desc">24/7 trauma care</div></div>
      <div class="service-card"><div class="service-icon">🌸</div><div class="service-title">Gynecology</div><div class="service-desc">Women's health</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-head">Contact & Information</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-grid">
      <div class="contact-card"><h4>📍 Location</h4><p>Jan Kalyan Hospital<br>Main Road, Bihar — 800001<br>India</p></div>
      <div class="contact-card"><h4>📞 Contact</h4><p>Phone: +91 8989651456<br>Emergency: +91 8989651400<br>Ambulance: 108</p></div>
      <div class="contact-card"><h4>✉️ Email</h4><p>General: jankalyan@gmail.com<br>Appointments: appt@jankalyan.in<br>Admin: admin@jankalyan.in</p></div>
      <div class="contact-card"><h4>🕐 Timings</h4><p>OPD: 8:00 AM – 8:00 PM<br>Emergency: 24 × 7<br>Lab: 7:00 AM – 9:00 PM</p></div>
    </div>
    <div class="footer-bar">
      <strong>🏥 Jan Kalyan Hospital</strong><br>
      Bihar, India &nbsp;|&nbsp; <a href="mailto:jankalyan@gmail.com">jankalyan@gmail.com</a> &nbsp;|&nbsp; +91 8989651456<br><br>
      © 2025 Jan Kalyan Hospital. All rights reserved. Built with ❤️ for better healthcare in Bihar.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.logged_in:
    role = st.session_state.role
    if role == "admin":       admin_dashboard()
    elif role == "doctor":    doctor_dashboard()
    elif role == "reception": reception_dashboard()
elif st.session_state.show_login:
    show_login_page()
else:
    show_landing()
