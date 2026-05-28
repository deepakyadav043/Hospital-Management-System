import streamlit as st

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Credentials (hidden in code, not shown in UI) ────────────────────────────
CREDENTIALS = {
    "admin":     {"password": "admin@234",   "role": "admin"},
    "doctor":    {"password": "doctor@459",  "role": "doctor"},
    "reception": {"password": "recep@389",   "role": "reception"},
}

# ─── Session State Init ───────────────────────────────────────────────────────
for key, val in {
    "logged_in": False, "role": None, "show_login": False,
    "doctor_list": [], "patient_list": [], "appointment_list": [],
    "bill_list": [], "salary_list": []
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
          /* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #134e4a 100%);
    border-right: 2px solid #14b8a6;
}

section[data-testid="stSidebar"] .css-1d391kg {
    padding-top: 20px;
}

section[data-testid="stSidebar"] .stSelectbox label {
    color: white !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stSelectbox div {
    color: white;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p {
    color: white !important;
}
              
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --teal:    #0d9488;
  --teal2:   #14b8a6;
  --navy:    #0f172a;
  --cream:   #f0fdf4;
  --gold:    #f59e0b;
  --red:     #ef4444;
  --card-bg: #ffffff;
  --text:    #1e293b;
  --muted:   #64748b;
}

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
            .stApp {
    background: linear-gradient(to bottom right, #020617, #0f172a);
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; }

/* Hero */
.hero {
  background: linear-gradient(135deg, #0f172a 0%, #134e4a 60%, #0d9488 100%);
  border-radius: 20px;
  padding: 70px 60px;
  color: white;
  position: relative;
  overflow: hidden;
  margin-bottom: 2rem;
}
.hero::before {
  content: '';
  position: absolute; top: -60px; right: -60px;
  width: 350px; height: 350px;
  background: radial-gradient(circle, rgba(20,184,166,0.25) 0%, transparent 70%);
  border-radius: 50%;
}
.hero::after {
  content: '';
  position: absolute; bottom: -80px; left: 30%;
  width: 250px; height: 250px;
  background: radial-gradient(circle, rgba(245,158,11,0.15) 0%, transparent 70%);
  border-radius: 50%;
}
.hero h1 {
  font-family: 'Playfair Display', serif;
  font-size: 3.6rem; font-weight: 900;
  line-height: 1.1; margin: 0 0 0.5rem;
  background: linear-gradient(90deg, #ffffff, #99f6e4);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-tagline { font-size: 1.2rem; color: #a7f3d0; margin-bottom: 1.5rem; font-weight: 300; }
.hero-badges { display: flex; gap: 12px; flex-wrap: wrap; }
.badge {
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 30px;
  padding: 6px 16px; font-size: 0.85rem; color: #ccfbf1;
}

/* Stat cards */
.stats-row { display: flex; gap: 16px; margin-bottom: 2rem; flex-wrap: wrap; }
.stat-card {
  flex: 1; 
  min-width: 150px;
  background: white;
  border-radius: 16px;
  padding: 24px 20px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.07);
  border-top: 4px solid var(--teal);
  transition: 0.3s;
}
            
.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(20,184,166,0.2);
}
            
.stat-number { font-family:'Playfair Display',serif; font-size:2.4rem; font-weight:700; color:var(--teal); }
.stat-label  { font-size:.85rem; color:var(--muted); margin-top:4px; }

/* Section headers */
.section-head {
  font-family:'Playfair Display',serif;
  font-size:2rem; font-weight:700; color:var(--navy);
  border-left:5px solid var(--teal); padding-left:16px;
  margin:2rem 0 1.2rem;
}

/* Service cards */
.services-grid { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 2rem; }
.service-card {
  flex: 1; min-width: 170px;
  background: white;
  border-radius: 14px;
  padding: 28px 20px;
  text-align: center;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  transition: transform .2s, box-shadow .2s;
  cursor: default;
}
.service-card:hover { transform: translateY(-4px); box-shadow: 0 8px 28px rgba(13,148,136,.15); }
.service-icon { font-size: 2.6rem; margin-bottom: 10px; }
.service-title { font-weight: 600; color: var(--navy); font-size: .95rem; }
.service-desc  { font-size:.8rem; color:var(--muted); margin-top:4px; }

/* Info cards */
.info-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 2rem; }
.info-card {
  flex: 1; min-width: 200px;
  background: linear-gradient(135deg, #f0fdf4, #ccfbf1);
  border-radius: 14px; padding: 24px;
  border: 1px solid #a7f3d0;
}
.info-card h4 { color: var(--teal); font-weight:600; margin:0 0 8px; font-size:1rem; }
.info-card p  { color: var(--text); margin:0; font-size:.9rem; line-height:1.6; }

/* Login modal */
.login-box {
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 20px 60px rgba(0,0,0,.15);
  max-width: 440px; margin: 0 auto;
  border-top: 6px solid var(--teal);
}
.login-box h2 {
  font-family:'Playfair Display',serif;
  color: var(--navy); margin-bottom: .3rem;
}
.login-box p { color: var(--muted); margin-bottom: 1.5rem; font-size:.9rem; }

/* Dashboard cards */
.dash-card {
  background: white; border-radius: 14px;
  padding: 22px; margin-bottom: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,.06);
  border-left: 5px solid var(--teal);
}
.dash-card h4 { margin:0 0 6px; color:var(--navy); }
.dash-card p  { margin:0; color:var(--muted); font-size:.88rem; }

/* Nav bar */
.topnav {
  background: linear-gradient(90deg, #0f172a, #134e4a);
  border-radius: 14px;
  padding: 14px 28px;
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 1.5rem; color: white;
}
.topnav-title { font-family:'Playfair Display',serif; font-size:1.4rem; color:#99f6e4; }
.topnav-info  { font-size:.85rem; color:#a7f3d0; }

/* Buttons */
.stButton > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  transition: all .2s !important;
}
            
/* Better Form Inputs */
.stTextInput input,
.stNumberInput input,
.stSelectbox div,
.stDateInput input,
.stTimeInput input {
    border-radius: 10px !important;
    border: 1px solid #14b8a6 !important;
}

/* Tags */
.tag {
  display:inline-block;
  background: #ccfbf1; color: #0f766e;
  border-radius: 20px; padding: 3px 12px;
  font-size:.8rem; font-weight:500; margin:2px;
}

/* Table */
.data-table { width:100%; border-collapse:collapse; font-size:.9rem; }
.data-table th { background:#0d9488; color:white; padding:10px 14px; text-align:left; }
.data-table td { padding:9px 14px; border-bottom:1px solid #e2e8f0; }
.data-table tr:hover td {
    background:#ccfbf1;
    transition: 0.3s;
}

/* Footer */
.footer {
  background: var(--navy); color: #94a3b8;
  border-radius: 14px; padding: 30px 40px;
  text-align: center; margin-top: 3rem;
  font-size: .85rem; line-height: 2;
}
.footer span { color: #99f6e4; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.show_login = False

def next_id(lst): return len(lst) + 1

# ══════════════════════════════════════════════════════════════════════════════
#  LOGIN PAGE
# ══════════════════════════════════════════════════════════════════════════════

def show_login_page():
    st.markdown("""
    <div style='text-align:center; padding: 10px 0 6px;'>
      <span style='font-size:3rem'>🏥</span>
      <h2 style='font-family:Playfair Display,serif; color:#0f172a; margin:0;'>Staff Portal Login</h2>
      <p style='color:#64748b; font-size:.95rem;'>Authorized personnel only</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        role_label = st.selectbox("Login as", ["Admin", "Doctor", "Receptionist"])
        username   = st.text_input("Username", placeholder="Enter username")
        password   = st.text_input("Password", type="password", placeholder="Enter password")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔐 Login", use_container_width=True, type="primary"):
                role_map = {"Admin": "admin", "Doctor": "doctor", "Receptionist": "reception"}
                role_key = role_map[role_label]
                cred = CREDENTIALS.get(role_key)
                if cred and username == role_key and password == cred["password"]:
                    st.session_state.logged_in = True
                    st.session_state.role = cred["role"]
                    st.session_state.show_login = False
                    st.success(f"✅ Welcome, {role_label}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Please try again.")
        with c2:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.show_login = False
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
#  LANDING PAGE
# ══════════════════════════════════════════════════════════════════════════════

def show_landing():
    # Top Nav
    st.markdown("""
    <div class="topnav">
      <span class="topnav-title">🏥 Jan Kalyan Hospital</span>
      <span class="topnav-info">📍 Bihar &nbsp;|&nbsp; 📞 +91 8989651456 &nbsp;|&nbsp; ✉️ jankalyan@gmail.com</span>
    </div>
    """, unsafe_allow_html=True)

    # Login button top-right
    col_nav, col_btn = st.columns([8, 1])
    with col_btn:
        if st.button("🔐 Staff Login", type="primary", use_container_width=True):
            st.session_state.show_login = True
            st.rerun()

    # Hero
    st.markdown("""
    <div class="hero">
      <h1>Healing With Heart,<br>Serving With Care</h1>
      <p class="hero-tagline">Your health is our mission — advanced care, compassionate touch.</p>
      <div class="hero-badges">
        <span class="badge">🏅 ISO Certified</span>
        <span class="badge">🕐 24/7 Emergency</span>
        <span class="badge">👨‍⚕️ 50+ Specialists</span>
        <span class="badge">🏥 300 Bed Capacity</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stats-row">
      <div class="stat-card"><div class="stat-number">15+</div><div class="stat-label">Years of Excellence</div></div>
      <div class="stat-card"><div class="stat-number">50K+</div><div class="stat-label">Patients Treated</div></div>
      <div class="stat-card"><div class="stat-number">50+</div><div class="stat-label">Specialist Doctors</div></div>
      <div class="stat-card"><div class="stat-number">300</div><div class="stat-label">Bed Capacity</div></div>
      <div class="stat-card"><div class="stat-number">24/7</div><div class="stat-label">Emergency Care</div></div>
    </div>
    """, unsafe_allow_html=True)

    # About
    st.markdown('<div class="section-head">About Us</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div class="dash-card">
          <p style="font-size:1rem; color:#334155; line-height:1.8;">
          <b>Jan Kalyan Hospital</b> has been a pillar of healthcare in Bihar for over 15 years.
          Founded with the goal of providing <em>quality medical care to every individual</em>,
          we combine cutting-edge technology with deeply compassionate service.<br><br>
          Our team of over 50 specialist doctors, 200+ nurses, and support staff work around the clock
          to ensure the best outcomes for every patient. From routine check-ups to complex surgeries,
          we are equipped to handle all your medical needs under one roof.
          </p>
          <div style="margin-top:12px;">
            <span class="tag">🎯 Patient-First Philosophy</span>
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
          <p style="color:#a7f3d0;font-size:.95rem;line-height:1.7;">
          To deliver affordable, world-class healthcare to every person in Bihar — regardless of background —
          through innovation, integrity, and unwavering compassion.
          </p>
          <h3 style="font-family:'Playfair Display',serif;color:#99f6e4;">Our Vision</h3>
          <p style="color:#a7f3d0;font-size:.95rem;line-height:1.7;">
          To be Bihar's most trusted hospital — a centre of healing where technology meets humanity.
          </p>
        </div>
        """, unsafe_allow_html=True)

    # Services
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

    # Contact & Info
    st.markdown('<div class="section-head">Contact & Information</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-row">
      <div class="info-card">
        <h4>📍 Location</h4>
        <p>Jan Kalyan Hospital<br>Main Road, Bihar — 800001<br>India</p>
      </div>
      <div class="info-card">
        <h4>📞 Contact</h4>
        <p>Phone: +91 8989651456<br>Emergency: +91 8989651400<br>Ambulance: 108</p>
      </div>
      <div class="info-card">
        <h4>✉️ Email</h4>
        <p>General: jankalyan@gmail.com<br>Appointments: appt@jankalyan.in<br>Admin: admin@jankalyan.in</p>
      </div>
      <div class="info-card">
        <h4>🕐 Timings</h4>
        <p>OPD: 8:00 AM – 8:00 PM<br>Emergency: 24 × 7<br>Lab: 7:00 AM – 9:00 PM</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
      <b style="font-size:1.1rem; color:#e2e8f0;">🏥 Jan Kalyan Hospital</b><br>
      Bihar, India &nbsp;|&nbsp; <span>jankalyan@gmail.com</span> &nbsp;|&nbsp; <span>+91 8989651456</span><br><br>
      © 2025 Jan Kalyan Hospital. All rights reserved. &nbsp;|&nbsp;
      Built with ❤️ for better healthcare in Bihar.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  DASHBOARD HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def dashboard_header(role):
    icons = {"admin": "🛡️", "doctor": "👨‍⚕️", "reception": "🗂️"}
    labels = {"admin": "Admin", "doctor": "Doctor", "reception": "Receptionist"}
    st.markdown(f"""
    <div class="topnav">
      <span class="topnav-title">🏥 Jan Kalyan Hospital — {labels[role]} Dashboard {icons[role]}</span>
      <span class="topnav-info">Bihar &nbsp;|&nbsp; jankalyan@gmail.com &nbsp;|&nbsp; +91 8989651456</span>
    </div>
    """, unsafe_allow_html=True)
    if st.sidebar.button("🚪 Logout", use_container_width=True):
        logout()
        st.rerun()

# ── Doctor helpers ─────────────────────────────────────────────────────────────
def ui_add_doctor():
    st.subheader("➕ Add Doctor")
    with st.form("add_doc"):
        n = st.text_input("Doctor Name")
        s = st.text_input("Specialization")
        e = st.number_input("Experience (years)", 0, 60, step=1)
        f = st.number_input("Consultation Fee (₹)", 0, step=100)
        if st.form_submit_button("Add Doctor", type="primary"):
            if n and s:
                st.session_state.doctor_list.append({
                    "id": next_id(st.session_state.doctor_list),
                    "name": n, "spec": s, "exp": e, "fee": f
                })
                st.success(f"✅ Dr. {n} added!")
            else:
                st.warning("Fill all fields.")

def ui_view_doctors():
    st.subheader("👨‍⚕️ All Doctors")
    dl = st.session_state.doctor_list
    if not dl:
        st.info("No doctors added yet.")
        return
    rows = "".join(f"<tr><td>{d['id']}</td><td>{d['name']}</td><td>{d['spec']}</td><td>{d['exp']} yrs</td><td>₹{d['fee']}</td></tr>" for d in dl)
    st.markdown(f"""<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Experience</th><th>Fee</th></tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

def ui_search_doctor():
    st.subheader("🔍 Search Doctor")
    q = st.text_input("Enter doctor name")
    if q:
        found = [d for d in st.session_state.doctor_list if q.lower() in d['name'].lower()]
        if found:
            for d in found:
                st.markdown(f"""<div class="dash-card"><h4>Dr. {d['name']}</h4><p>Specialization: {d['spec']} &nbsp;|&nbsp; Experience: {d['exp']} yrs &nbsp;|&nbsp; Fee: ₹{d['fee']}</p></div>""", unsafe_allow_html=True)
        else:
            st.error("No doctor found.")

def ui_delete_doctor():
    st.subheader("🗑️ Delete Doctor")
    ids = [d['id'] for d in st.session_state.doctor_list]
    if not ids:
        st.info("No doctors to delete."); return
    sel = st.selectbox("Select Doctor ID", ids)
    if st.button("Delete", type="primary"):
        st.session_state.doctor_list = [d for d in st.session_state.doctor_list if d['id'] != sel]
        st.success("Doctor removed.")

# ── Patient helpers ────────────────────────────────────────────────────────────
def ui_add_patient():
    st.subheader("➕ Add Patient")
    with st.form("add_pat"):
        n = st.text_input("Patient Name")
        a = st.number_input("Age", 0, 130, step=1)
        d = st.text_input("Disease / Condition")
        r = st.text_input("Room Number")
        if st.form_submit_button("Add Patient", type="primary"):
            if n and d:
                st.session_state.patient_list.append({
                    "id": next_id(st.session_state.patient_list),
                    "name": n, "age": a, "disease": d, "room": r
                })
                st.success(f"✅ {n} added!")
            else:
                st.warning("Fill required fields.")

def ui_view_patients():
    st.subheader("🧑‍⚕️ All Patients")
    pl = st.session_state.patient_list
    if not pl:
        st.info("No patients added yet."); return
    rows = "".join(f"<tr><td>{p['id']}</td><td>{p['name']}</td><td>{p['age']}</td><td>{p['disease']}</td><td>{p['room']}</td></tr>" for p in pl)
    st.markdown(f"""<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Age</th><th>Disease</th><th>Room</th></tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

def ui_search_patient():
    st.subheader("🔍 Search Patient")
    method = st.radio("Search by", ["Name", "ID"], horizontal=True)
    if method == "Name":
        q = st.text_input("Enter patient name")
        if q:
            found = [p for p in st.session_state.patient_list if q.lower() in p['name'].lower()]
    else:
        q = st.number_input("Enter patient ID", min_value=1, step=1)
        found = [p for p in st.session_state.patient_list if p['id'] == q]
    if 'found' in dir() and found:
        for p in found:
            st.markdown(f"""<div class="dash-card"><h4>{p['name']}</h4><p>ID: {p['id']} &nbsp;|&nbsp; Age: {p['age']} &nbsp;|&nbsp; Disease: {p['disease']} &nbsp;|&nbsp; Room: {p['room']}</p></div>""", unsafe_allow_html=True)
    elif 'found' in dir():
        st.error("Patient not found.")

# ── Appointment helpers ────────────────────────────────────────────────────────
def ui_book_appointment():
    st.subheader("📅 Book Appointment")
    with st.form("book_appt"):
        doc  = st.text_input("Doctor Name")
        pat  = st.text_input("Patient Name")
        date = st.date_input("Date")
        time = st.time_input("Time")
        if st.form_submit_button("Book Appointment", type="primary"):
            if doc and pat:
                st.session_state.appointment_list.append({
                    "id": next_id(st.session_state.appointment_list),
                    "doctor": doc, "patient": pat,
                    "date": str(date), "time": str(time)
                })
                st.success("✅ Appointment booked!")
            else:
                st.warning("Fill all fields.")

def ui_view_appointments():
    st.subheader("📋 All Appointments")
    al = st.session_state.appointment_list
    if not al:
        st.info("No appointments yet."); return
    rows = "".join(f"<tr><td>{a['id']}</td><td>{a['doctor']}</td><td>{a['patient']}</td><td>{a['date']}</td><td>{a['time']}</td></tr>" for a in al)
    st.markdown(f"""<table class="data-table"><thead><tr><th>ID</th><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th></tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

def ui_search_appointment():
    st.subheader("🔍 Search Appointment")
    date = st.date_input("Select Date")
    found = [a for a in st.session_state.appointment_list if a['date'] == str(date)]
    if found:
        for a in found:
            st.markdown(f"""<div class="dash-card"><h4>Appointment #{a['id']}</h4><p>Doctor: {a['doctor']} &nbsp;|&nbsp; Patient: {a['patient']} &nbsp;|&nbsp; Time: {a['time']}</p></div>""", unsafe_allow_html=True)
    else:
        st.info(f"No appointments on {date}.")

# ── Bill helpers ───────────────────────────────────────────────────────────────
def ui_generate_bill():
    st.subheader("🧾 Generate Bill")
    with st.form("gen_bill"):
        name  = st.text_input("Patient Name")
        doc_f = st.number_input("Doctor Fee (₹)", 0, step=100)
        room  = st.number_input("Room Charges (₹)", 0, step=100)
        med   = st.number_input("Medicine Charges (₹)", 0, step=100)
        if st.form_submit_button("Generate Bill", type="primary"):
            if name:
                total = doc_f + room + med
                b = {"id": next_id(st.session_state.bill_list), "name": name,
                     "doc_fee": doc_f, "room": room, "med": med, "total": total}
                st.session_state.bill_list.append(b)
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,#f0fdf4,#ccfbf1);border-radius:14px;padding:28px;border:1px solid #6ee7b7;">
                  <h3 style="font-family:'Playfair Display',serif;color:#0f172a;">🧾 Bill #{b['id']}</h3>
                  <p style="color:#334155;font-size:.95rem;line-height:2;">
                  Patient: <b>{name}</b><br>
                  Doctor Fee: ₹{doc_f} &nbsp;|&nbsp; Room: ₹{room} &nbsp;|&nbsp; Medicine: ₹{med}<br>
                  <span style="font-size:1.3rem;font-weight:700;color:#0d9488;">Total: ₹{total}</span>
                  </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Enter patient name.")

def ui_view_bills():
    st.subheader("💰 All Bills")
    bl = st.session_state.bill_list
    if not bl:
        st.info("No bills generated yet."); return
    rows = "".join(f"<tr><td>{b['id']}</td><td>{b['name']}</td><td>₹{b['doc_fee']}</td><td>₹{b['room']}</td><td>₹{b['med']}</td><td><b>₹{b['total']}</b></td></tr>" for b in bl)
    st.markdown(f"""<table class="data-table"><thead><tr><th>ID</th><th>Patient</th><th>Doctor Fee</th><th>Room</th><th>Medicine</th><th>Total</th></tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

# ── Salary helpers ─────────────────────────────────────────────────────────────
def ui_add_salary():
    st.subheader("💵 Add Salary Record")
    with st.form("add_sal"):
        emp  = st.text_input("Employee Name")
        etype = st.selectbox("Type", ["Doctor", "Nurse", "Staff"])
        basic = st.number_input("Basic Salary (₹)", 0, step=1000)
        hra   = st.number_input("HRA %", 0.0, 100.0, value=10.0, step=0.5)
        da    = st.number_input("DA %",  0.0, 100.0, value=5.0,  step=0.5)
        pf    = st.number_input("PF %",  0.0, 100.0, value=12.0, step=0.5)
        month = st.selectbox("Month", ["January","February","March","April","May","June","July","August","September","October","November","December"])
        year  = st.text_input("Year", "2025")
        if st.form_submit_button("Generate Salary Slip", type="primary"):
            if emp:
                hra_a = (hra/100)*basic; da_a = (da/100)*basic
                pf_a  = (pf/100)*basic;  gross = basic+hra_a+da_a; net = gross-pf_a
                s = {"id": next_id(st.session_state.salary_list), "name": emp, "type": etype,
                     "basic": basic, "hra": hra_a, "da": da_a, "pf": pf_a,
                     "gross": gross, "net": net, "month": month, "year": year}
                st.session_state.salary_list.append(s)
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,#f0fdf4,#ccfbf1);border-radius:14px;padding:28px;border:1px solid #6ee7b7;">
                  <h3 style="font-family:'Playfair Display',serif;color:#0f172a;">💵 Salary Slip — {emp}</h3>
                  <p style="color:#334155;line-height:2;font-size:.95rem;">
                  Type: {etype} &nbsp;|&nbsp; Month: {month} {year}<br>
                  Basic: ₹{basic} &nbsp;|&nbsp; HRA: ₹{hra_a:.0f} &nbsp;|&nbsp; DA: ₹{da_a:.0f}<br>
                  Gross: ₹{gross:.0f} &nbsp;|&nbsp; PF Deduction: ₹{pf_a:.0f}<br>
                  <span style="font-size:1.3rem;font-weight:700;color:#0d9488;">Net Salary: ₹{net:.0f}</span>
                  </p>
                </div>
                """, unsafe_allow_html=True)

def ui_view_salaries():
    st.subheader("📋 All Salary Records")
    sl = st.session_state.salary_list
    if not sl:
        st.info("No records yet."); return
    rows = "".join(f"<tr><td>{s['id']}</td><td>{s['name']}</td><td>{s['type']}</td><td>₹{s['basic']}</td><td>₹{s['gross']:.0f}</td><td><b>₹{s['net']:.0f}</b></td><td>{s['month']} {s['year']}</td></tr>" for s in sl)
    st.markdown(f"""<table class="data-table"><thead><tr><th>ID</th><th>Name</th><th>Type</th><th>Basic</th><th>Gross</th><th>Net</th><th>Month</th></tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

def ui_search_salary():
    st.subheader("🔍 Search Salary")
    q = st.text_input("Employee name")
    if q:
        found = [s for s in st.session_state.salary_list if q.lower() in s['name'].lower()]
        if found:
            for s in found:
                st.markdown(f"""<div class="dash-card"><h4>{s['name']} ({s['type']})</h4><p>Month: {s['month']} {s['year']} &nbsp;|&nbsp; Net Salary: ₹{s['net']:.0f}</p></div>""", unsafe_allow_html=True)
        else:
            st.error("No record found.")

def ui_salary_calculator():
    st.subheader("🧮 Salary Calculator")
    with st.form("sal_calc"):
        basic = st.number_input("Basic Salary (₹)", 0, step=1000)
        hra   = st.number_input("HRA %", 0.0, 100.0, value=10.0)
        da    = st.number_input("DA %",  0.0, 100.0, value=5.0)
        pf    = st.number_input("PF %",  0.0, 100.0, value=12.0)
        if st.form_submit_button("Calculate", type="primary"):
            hra_a = (hra/100)*basic; da_a = (da/100)*basic
            pf_a  = (pf/100)*basic;  gross = basic+hra_a+da_a; net = gross-pf_a
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("Gross Salary", f"₹{gross:,.0f}")
            c2.metric("HRA", f"₹{hra_a:,.0f}")
            c3.metric("DA",  f"₹{da_a:,.0f}")
            c4.metric("Net Salary", f"₹{net:,.0f}")

def ui_delete_salary():
    st.subheader("🗑️ Delete Salary Record")
    ids = [s['id'] for s in st.session_state.salary_list]
    if not ids:
        st.info("No records."); return
    sel = st.selectbox("Select Salary ID", ids)
    if st.button("Delete", type="primary"):
        st.session_state.salary_list = [s for s in st.session_state.salary_list if s['id'] != sel]
        st.success("Deleted.")

# ══════════════════════════════════════════════════════════════════════════════
#  DASHBOARDS
# ══════════════════════════════════════════════════════════════════════════════

def admin_dashboard():
    dashboard_header("admin")
    st.markdown('<div class="section-head">Admin Dashboard</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stats-row">

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.doctor_list)}</div>
    <div class="stat-label">Doctors</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.patient_list)}</div>
    <div class="stat-label">Patients</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.appointment_list)}</div>
    <div class="stat-label">Appointments</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.bill_list)}</div>
    <div class="stat-label">Bills</div>
    </div>

    </div>
    """, unsafe_allow_html=True)



    st.sidebar.markdown("## 🏥 Navigation")

    menu = st.sidebar.radio(
        "Select Option",
        [
            "🏠 Home",

            "👨‍⚕️ Add Doctor",
            "👨‍⚕️ View Doctors",
            "🔍 Search Doctor",
            "🗑️ Delete Doctor",

            "🧑 Add Patient",
            "🧑 View Patients",
            "🔍 Search Patient",

            "📅 Book Appointment",
            "📋 View Appointments",
            "🔍 Search Appointment",

            "🧾 Generate Bill",
            "💰 View Bills",

            "💵 Add Salary",
            "📋 View Salaries",
            "🔍 Search Salary",
            "🧮 Salary Calculator",
            "🗑️ Delete Salary",
        ]
    )
    
    dispatch = {
        "👨‍⚕️ Add Doctor": ui_add_doctor,
        "👨‍⚕️ View Doctors": ui_view_doctors,
        "🔍 Search Doctor": ui_search_doctor,
        "🗑️ Delete Doctor": ui_delete_doctor,

        "🧑 Add Patient": ui_add_patient,
        "🧑 View Patients": ui_view_patients,
        "🔍 Search Patient": ui_search_patient,

        "📅 Book Appointment": ui_book_appointment,
        "📋 View Appointments": ui_view_appointments,
        "🔍 Search Appointment": ui_search_appointment,

        "🧾 Generate Bill": ui_generate_bill,
        "💰 View Bills": ui_view_bills,

        "💵 Add Salary": ui_add_salary,
        "📋 View Salaries": ui_view_salaries,
        "🔍 Search Salary": ui_search_salary,

        "🧮 Salary Calculator": ui_salary_calculator,
        "🗑️ Delete Salary": ui_delete_salary,
    }

    if menu == "🏠 Home":
        st.markdown("""
        <div class="dash-card">
          <h4>Welcome, Admin 🛡️</h4>
          <p>Use the sidebar to manage doctors, patients, appointments, bills, and salary records.</p>
        </div>
        """, unsafe_allow_html=True)
        st.subheader("⚡ Quick Actions")

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("➕ Add Doctor", use_container_width=True):
                ui_add_doctor()

        with c2:
            if st.button("➕ Add Patient", use_container_width=True):
                ui_add_patient()

        with c3:
            if st.button("📅 Book Appointment", use_container_width=True):
                ui_book_appointment()

    elif menu in dispatch:
        dispatch[menu]()


def doctor_dashboard():
    dashboard_header("doctor")
    st.sidebar.markdown("""
    <h2 style='text-align:center;color:white;'>👨‍⚕️ Doctor Panel</h2>
    <hr>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dash-card">
    <h4>👨‍⚕️ Doctor Panel</h4>
    <p>Manage patients, appointments, and medical records efficiently.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stats-row">

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.patient_list)}</div>
    <div class="stat-label">Patients</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.appointment_list)}</div>
    <div class="stat-label">Appointments</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.doctor_list)}</div>
    <div class="stat-label">Doctors</div>
    </div>

    </div>
    """, unsafe_allow_html=True)




    menu = st.sidebar.selectbox("📌 Menu", [
    "🏠 Dashboard",
    "👁️ View Patients",
    "🔍 Search Patient",
    "📅 View Appointments",
    "👨‍⚕️ View Doctors"
])
    dispatch = {
        "👨‍⚕️ View Doctors": ui_view_doctors,
        "👁️ View Patients": ui_view_patients,
        "🔍 Search Patient": ui_search_patient,
        "📅 View Appointments": ui_view_appointments,
    }
    if menu == "🏠 Dashboard":
        st.info("Welcome Doctor 👨‍⚕️")
    else:
        dispatch[menu]()


def reception_dashboard():
    dashboard_header("reception")

    st.sidebar.markdown("""
    <h2 style='text-align:center;color:white;'>🗂️ Reception Panel</h2>
    <hr>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="dash-card">
    <h4>🗂️ Reception Dashboard</h4>
    <p>Manage patient entry, appointments and billing.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stats-row">

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.patient_list)}</div>
    <div class="stat-label">Patients</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.appointment_list)}</div>
    <div class="stat-label">Appointments</div>
    </div>

    <div class="stat-card">
    <div class="stat-number">{len(st.session_state.bill_list)}</div>
    <div class="stat-label">Bills</div>
    </div>

    </div>
    """, unsafe_allow_html=True)

    menu = st.sidebar.selectbox(
        "📌 Menu",
        [
            "🏠 Dashboard",
            "➕ Add Patient",
            "👁️ View Patients",
            "📅 Book Appointment",
            "🧾 Generate Bill"
        ]
    )

    dispatch = {
        "➕ Add Patient": ui_add_patient,
        "👁️ View Patients": ui_view_patients,
        "📅 Book Appointment": ui_book_appointment,
        "🧾 Generate Bill": ui_generate_bill,
    }

    if menu == "🏠 Dashboard":
        st.info("Welcome Receptionist 🗂️")
    else:
        dispatch[menu]()
# ══════════════════════════════════════════════════════════════════════════════
#  MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════

if st.session_state.logged_in:
    role = st.session_state.role
    if role == "admin":
        admin_dashboard()
    elif role == "doctor":
        doctor_dashboard()
    elif role == "reception":
        reception_dashboard()

elif st.session_state.show_login:
    show_login_page()

else:
    show_landing()
