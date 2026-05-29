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

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --teal:#0d9488; --teal2:#14b8a6; --navy:#0f172a; --muted:#64748b; --text:#1e293b;
}
html,body,[class*="css"]{ font-family:'DM Sans',sans-serif; }
.stApp{ background:linear-gradient(to bottom right,#020617,#0f172a); }
#MainMenu,footer {
#  visibility:hidden;
#  }
.block-container{ 
    padding-top:2rem !important; 
}

/* ── Sidebar ── */
section[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#0f172a 0%,#134e4a 100%) !important;
  border-right:2px solid #14b8a6;
}
section[data-testid="stSidebar"] *{ color:white !important; }

/* Remove ALL radio circles */
section[data-testid="stSidebar"] [data-testid="stRadio"] { display:none !important; }

/* Sidebar nav buttons */
section[data-testid="stSidebar"] .stButton>button{
  background:transparent !important;
  border:none !important;
  border-radius:8px !important;
  color:#a7f3d0 !important;
  text-align:left !important;
  width:100% !important;
  padding:8px 12px !important;
  font-size:0.88rem !important;
  font-weight:500 !important;
  transition:all 0.2s !important;
  justify-content:flex-start !important;
}
section[data-testid="stSidebar"] .stButton>button:hover{
  background:rgba(20,184,166,0.2) !important;
  color:#ffffff !important;
  transform:translateX(4px) !important;
}
/* Active page button */
section[data-testid="stSidebar"] .stButton>button[kind="primary"]{
  background:rgba(20,184,166,0.25) !important;
  border-left:3px solid #14b8a6 !important;
  color:#ffffff !important;
  font-weight:600 !important;
}
/* Logout button */
.logout-btn>button{
  background:rgba(239,68,68,0.15) !important;
  border:1px solid rgba(239,68,68,0.4) !important;
  color:#fca5a5 !important;
  border-radius:8px !important;
  width:100% !important;
  padding:8px 12px !important;
  font-weight:600 !important;
}
.logout-btn>button:hover{
  background:rgba(239,68,68,0.3) !important;
  color:#fff !important;
}
.sb-section-label{
  font-size:0.68rem; font-weight:700; letter-spacing:0.12em;
  color:#0d9488; text-transform:uppercase; padding:12px 12px 4px;
  display:block;
}

/* ── Top Nav ── */
.topnav{
  background:linear-gradient(90deg,#0f172a,#134e4a);
  border-radius:14px; 
  padding:18px 28px;
  margin-top:15px;
  display:flex; align-items:center; justify-content:space-between;
  margin-bottom:1.5rem; color:white;
  border:1px solid rgba(20,184,166,0.3);
}
.topnav-title{ font-family:'Playfair Display',serif; font-size:1.4rem; color:#99f6e4; }
.topnav-info { font-size:.85rem; color:#a7f3d0; }

/* ── Hero ── */
.hero{
  border-radius:20px; overflow:hidden; position:relative;
  margin-bottom:2rem; min-height:340px;
  display:flex; align-items:flex-end;
}
.hero-img{
  position:absolute; top:0; left:0; width:100%; height:100%;
  object-fit:cover; object-position:center;
}
.hero-overlay{
  position:absolute; top:0; left:0; width:100%; height:100%;
  background:linear-gradient(90deg,rgba(15,23,42,0.88) 0%,rgba(19,78,74,0.75) 50%,rgba(13,148,136,0.4) 100%);
}
.hero-content{
  position:relative; z-index:2; padding:56px 60px; width:100%;
}
.hero h1{
  font-family:'Playfair Display',serif; font-size:3.2rem; font-weight:900;
  line-height:1.1; margin:0 0 0.5rem;
  background:linear-gradient(90deg,#ffffff,#99f6e4);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero-tagline{ font-size:1.15rem; color:#a7f3d0; margin-bottom:1.5rem; font-weight:300; }
.hero-badges { display:flex; gap:10px; flex-wrap:wrap; }
.badge{
  background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22);
  border-radius:30px; padding:5px 14px; font-size:0.82rem; color:#ccfbf1;
  backdrop-filter:blur(4px);
}

/* ── Stats row ── */
.stats-row{ display:flex; gap:14px; margin-bottom:2rem; flex-wrap:wrap; }
.stat-card{
  flex:1; min-width:140px; background:white; border-radius:16px;
  padding:22px 18px; text-align:center;
  box-shadow:0 4px 20px rgba(0,0,0,0.08); border-top:4px solid var(--teal);
  transition:0.25s;
}
.stat-card:hover{ transform:translateY(-5px); box-shadow:0 10px 25px rgba(20,184,166,0.2); }
.stat-number{ font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; color:var(--teal); }
.stat-label { font-size:.82rem; color:var(--muted); margin-top:4px; }

/* ── Dashboard stat cards (dark) ── */
.dstat-row{ display:flex; gap:14px; margin-bottom:2rem; flex-wrap:wrap; }
.dstat-card{
  flex:1; min-width:140px;
  background:linear-gradient(135deg,#1e293b,#134e4a);
  border-radius:16px; padding:22px 18px; text-align:center;
  border:1px solid rgba(20,184,166,0.3);
  box-shadow:0 4px 20px rgba(0,0,0,0.3);
}
.dstat-number{ font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:700; color:#14b8a6; }
.dstat-label { font-size:.82rem; color:#a7f3d0; margin-top:4px; }

/* ── Section head ── */
.section-head{
  font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:white;
  border-left:5px solid var(--teal); padding-left:16px; margin:2rem 0 1.2rem;
}

/* ── Service cards ── */
.services-grid{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:2rem; }
.service-card{
  flex:1; min-width:160px; background:white; border-radius:14px;
  padding:26px 18px; text-align:center;
  box-shadow:0 2px 16px rgba(0,0,0,0.06); transition:transform .2s,box-shadow .2s;
}
.service-card:hover{ transform:translateY(-4px); box-shadow:0 8px 28px rgba(13,148,136,.15); }
.service-icon { font-size:2.4rem; margin-bottom:10px; }
.service-title{ font-weight:600; color:var(--navy); font-size:.92rem; }
.service-desc { font-size:.78rem; color:var(--muted); margin-top:4px; }

/* ── Info cards ── */
.info-row{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:2rem; }
.info-card{
  flex:1; min-width:190px;
  background:linear-gradient(135deg,#f0fdf4,#ccfbf1);
  border-radius:14px; padding:22px; border:1px solid #a7f3d0;
}
.info-card h4{ color:var(--teal); font-weight:600; margin:0 0 8px; font-size:.95rem; }
.info-card p { color:var(--text); margin:0; font-size:.88rem; line-height:1.6; }

/* ── Dash cards ── */
.dash-card{
  background:#1e293b; border-radius:14px; padding:22px; margin-bottom:16px;
  box-shadow:0 2px 12px rgba(0,0,0,.3); border-left:5px solid var(--teal);
}
.dash-card h4{ margin:0 0 6px; color:white; }
.dash-card p { margin:0; color:#94a3b8; font-size:.88rem; }

/* ── Table ── */
.data-table{ width:100%; border-collapse:collapse; font-size:.9rem; }
.data-table th{ background:#0d9488; color:white; padding:10px 14px; text-align:left; }
.data-table td{ padding:9px 14px; border-bottom:1px solid #334155; color:#e2e8f0; background:#1e293b; }
.data-table tr:hover td{ background:#134e4a; transition:0.2s; }

/* ── Slip ── */
.slip-box{
  background:linear-gradient(135deg,#134e4a,#1e293b);
  border-radius:14px; padding:28px; border:1px solid #14b8a6;
}
.slip-box h3{ font-family:'Playfair Display',serif; color:white; margin-top:0; }
.slip-box p { color:#a7f3d0; font-size:.95rem; line-height:2; }

/* ── Tags ── */
.tag{
  display:inline-block; background:#ccfbf1; color:#0f766e;
  border-radius:20px; padding:3px 12px; font-size:.78rem; font-weight:500; margin:2px;
}

/* ── Global buttons ── */
.stButton>button{
  border-radius:10px !important; font-weight:600 !important; transition:all .2s !important;
}
.stTextInput input,
.stNumberInput input,
.stSelectbox div,
.stDateInput input,
.stTimeInput input{
  border-radius:10px !important; 
  border:1px solid #14b8a6 !important;
}
div[data-baseweb="select"] span{
    border:none !important;
    background:transparent !important;
}

/* ── Remove focus outline/ring ── */
*:focus { 
  outline: none !important; 
  box-shadow: none !important; 
}
[data-baseweb="select"]:focus-within,
[data-baseweb="select"] *:focus {
  outline: none !important;
  box-shadow: none !important;
  border-color: #14b8a6 !important;
}
            
}
/* ── Footer ── */
.footer{
  background:var(--navy); color:#94a3b8; border-radius:14px;
  padding:28px 40px; text-align:center; margin-top:3rem; font-size:.83rem; line-height:2;
}
.footer span{ color:#99f6e4; }

/* Remove radio circles globally in sidebar */
[data-testid="stSidebar"] input[type="radio"]{ display:none !important; }
[data-testid="stSidebar"] .st-emotion-cache-j7qwjs{ display:none !important; }
</style>
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
#  SIDEBAR BUILDER  — uses buttons only, no radio, no selectbox
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
    <div class="topnav">
      <span class="topnav-title">🏥 Jan Kalyan Hospital</span>
      <span class="topnav-info">📍 Bihar &nbsp;|&nbsp; 📞 +91 8989651456 &nbsp;|&nbsp; ✉️ jankalyan@gmail.com</span>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn = st.columns([9,1])
    with col_btn:
        if st.button("🔐 Staff Login", type="primary", use_container_width=True):
            st.session_state.show_login = True; st.rerun()

    # Hero with real hospital image
    st.markdown("""
    <div class="hero">
      <img class="hero-img"
           src="https://imkarchitects.com/images/expertise-healthcare-banner.jpg"
           alt="Hospital" onerror="this.style.display='none'">
      <div class="hero-overlay"></div>
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
        <div class="dash-card">
          <p style="font-size:1rem;color:#cbd5e1;line-height:1.85;">
          <b>Jan Kalyan Hospital</b> has been a pillar of healthcare in Bihar for over 15 years.
          We combine cutting-edge technology with deeply compassionate service.<br><br>
          Our team of over 50 specialist doctors, 200+ nurses, and support staff work around the clock
          to ensure the best outcomes for every patient.
          </p>
          <div style="margin-top:12px;">
            <span class="tag">🎯 Patient-First</span>
            <span class="tag">🔬 Latest Technology</span>
            <span class="tag">❤️ Compassionate Care</span>
            <span class="tag">🌿 Holistic Wellness</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#0f172a,#134e4a);border-radius:14px;padding:28px;color:white;height:100%;">
          <h3 style="font-family:'Playfair Display',serif;color:#99f6e4;margin-top:0;">Our Mission</h3>
          <p style="color:#a7f3d0;font-size:.92rem;line-height:1.7;">
          Affordable, world-class healthcare for every person in Bihar — through innovation, integrity, and compassion.
          </p>
          <h3 style="font-family:'Playfair Display',serif;color:#99f6e4;">Our Vision</h3>
          <p style="color:#a7f3d0;font-size:.92rem;line-height:1.7;">
          Bihar's most trusted hospital — where technology meets humanity.
          </p>
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
    <div class="info-row">
      <div class="info-card"><h4>📍 Location</h4><p>Jan Kalyan Hospital<br>Main Road, Bihar — 800001<br>India</p></div>
      <div class="info-card"><h4>📞 Contact</h4><p>Phone: +91 8989651456<br>Emergency: +91 8989651400<br>Ambulance: 108</p></div>
      <div class="info-card"><h4>✉️ Email</h4><p>General: jankalyan@gmail.com<br>Appointments: appt@jankalyan.in<br>Admin: admin@jankalyan.in</p></div>
      <div class="info-card"><h4>🕐 Timings</h4><p>OPD: 8:00 AM – 8:00 PM<br>Emergency: 24 × 7<br>Lab: 7:00 AM – 9:00 PM</p></div>
    </div>
    <div class="footer">
      <b style="font-size:1.05rem;color:#e2e8f0;">🏥 Jan Kalyan Hospital</b><br>
      Bihar, India &nbsp;|&nbsp; <span>jankalyan@gmail.com</span> &nbsp;|&nbsp; <span>+91 8989651456</span><br><br>
      © 2025 Jan Kalyan Hospital. All rights reserved. &nbsp;|&nbsp; Built with ❤️ for better healthcare in Bihar.
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
        st.success("Doctor removed."); st.rerun()

def ui_add_patient():
    st.subheader("➕ Add Patient")
    with st.form("add_pat"):
        n=st.text_input("Patient Name"); a=st.number_input("Age",0,130,step=1)
        d=st.text_input("Disease / Condition"); r=st.text_input("Room Number")
        if st.form_submit_button("Add Patient",type="primary"):
            if n and d:
                st.session_state.patient_list.append({"id":next_id(st.session_state.patient_list),"name":n,"age":a,"disease":d,"room":r})
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
