import streamlit as st
import pandas as pd
from datetime import date, time as dtime

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700;800&family=Outfit:wght@300;400;500;600;700&display=swap');

:root{
  --green1:#064e3b; --green2:#065f46; --green3:#047857;
  --mint:#10b981;   --teal:#34d399;   --lime:#6ee7b7;
  --gold:#d97706;   --amber:#fbbf24;
  --red:#dc2626;    --sky:#0ea5e9;
  --bg:#f0fdf8;     --card:#ffffff;
  --navy:#0f172a;   --text:#1e293b;   --muted:#64748b;
  --border:#d1fae5; --border2:#e2e8f0;
}

html,body,[class*="css"]{
  font-family:'Outfit',sans-serif;
  background:var(--bg);
  color:var(--text);
}

/* ── Sidebar ── */
[data-testid="stSidebar"]{
  background:linear-gradient(170deg,var(--green1) 0%,var(--green2) 55%,#0d7a5f 100%);
}
[data-testid="stSidebar"] *{color:#ecfdf5 !important;}
[data-testid="stSidebar"] hr{border-color:rgba(255,255,255,0.12);}

/* ── Hide default header ── */
#MainMenu,footer,header{visibility:hidden;}

/* ── Buttons ── */
.stButton>button{
  background:linear-gradient(90deg,var(--green3),var(--green2));
  color:#fff !important;border:none;border-radius:10px;
  font-weight:600;font-size:.9rem;padding:.5rem 1.5rem;
  transition:all .2s;box-shadow:0 3px 12px rgba(4,120,87,.25);
}
.stButton>button:hover{
  transform:translateY(-2px);
  box-shadow:0 6px 20px rgba(4,120,87,.35);
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"]{gap:4px;background:var(--bg);}
.stTabs [data-baseweb="tab"]{
  border-radius:10px 10px 0 0;font-weight:600;
  padding:.55rem 1.4rem;color:var(--muted);
}
.stTabs [aria-selected="true"]{
  background:white;color:var(--green2) !important;
  border-bottom:3px solid var(--mint);
}

/* ── Inputs ── */
.stTextInput>div>div>input,
.stNumberInput>div>div>input,
.stSelectbox>div>div{border-radius:10px;}

/* ── Dataframe ── */
.stDataFrame{border-radius:14px;overflow:hidden;}
</style>
""", unsafe_allow_html=True)

# ─── Session State ────────────────────────────────────────────────────────────
_defaults = {
    "logged_in": False, "user_role": None,
    "doctors": [], "patients": [], "appointments": [],
    "bills": [], "salaries": [],
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─── Credentials (matches your project exactly) ───────────────────────────────
CREDS = {
    "admin":     ("admin",     "admin@234"),
    "doctor":    ("doctor",    "doctor@459"),
    "reception": ("reception", "recep@389"),
}

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS / REUSABLE COMPONENTS
# ══════════════════════════════════════════════════════════════════════════════
def ok(msg):
    st.markdown(f"""<div style='background:#dcfce7;border-left:4px solid #16a34a;
    border-radius:10px;padding:.85rem 1.1rem;color:#14532d;font-weight:500;
    margin:.4rem 0;'>✅ {msg}</div>""", unsafe_allow_html=True)

def err(msg):
    st.markdown(f"""<div style='background:#fee2e2;border-left:4px solid #dc2626;
    border-radius:10px;padding:.85rem 1.1rem;color:#7f1d1d;font-weight:500;
    margin:.4rem 0;'>❌ {msg}</div>""", unsafe_allow_html=True)

def section(title, icon=""):
    st.markdown(f"""<div style='
      font-family:Cormorant Garamond,serif;font-size:1.55rem;font-weight:700;
      color:var(--green1);margin:1.6rem 0 1rem;padding-bottom:.5rem;
      border-bottom:2px solid var(--border);letter-spacing:-.3px;
    '>{icon} {title}</div>""", unsafe_allow_html=True)

def stat_cards(items):
    """items = list of (icon, number, label, color)"""
    cols = st.columns(len(items))
    for col, (icon, number, label, color) in zip(cols, items):
        with col:
            st.markdown(f"""<div style='
              background:white;border-radius:16px;padding:1.3rem 1.5rem;
              box-shadow:0 2px 14px rgba(0,0,0,.06);
              border-left:5px solid {color};
              transition:transform .2s;
            '>
              <div style='font-size:1.8rem;margin-bottom:.3rem'>{icon}</div>
              <div style='font-family:Cormorant Garamond,serif;font-size:2.1rem;
                font-weight:800;color:#0f172a;line-height:1'>{number}</div>
              <div style='font-size:.82rem;color:#64748b;margin-top:.3rem;
                font-weight:500'>{label}</div>
            </div>""", unsafe_allow_html=True)

def slip_row(label, value, bold=False, color="#1e293b"):
    weight = "700" if bold else "400"
    st.markdown(f"""<div style='display:flex;justify-content:space-between;
      padding:.42rem 0;border-bottom:1px dashed #e2e8f0;
      font-size:.9rem;font-weight:{weight};color:{color};'>
      <span>{label}</span><span>{value}</span>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  LOGIN
# ══════════════════════════════════════════════════════════════════════════════
def login_page():
    st.markdown("""
    <div style='text-align:center;padding:3rem 0 1rem;'>
      <div style='font-size:4.5rem;'>🏥</div>
      <div style='font-family:Cormorant Garamond,serif;font-size:2.6rem;
        font-weight:800;color:#064e3b;margin:.2rem 0;'>Jan Kalyan Hospital</div>
      <div style='color:#047857;font-size:1rem;font-weight:500;
        letter-spacing:1px;text-transform:uppercase;'>Bihar • Est. 2005</div>
      <div style='color:#64748b;font-size:.9rem;margin-top:.4rem;'>
        Secure Staff Login Portal</div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 1.1, 1])
    with mid:
        st.markdown("""<div style='background:white;border-radius:20px;
          padding:2.2rem 2.4rem;box-shadow:0 8px 40px rgba(0,0,0,.1);
          border-top:5px solid #047857;margin-top:.5rem;'>""",
          unsafe_allow_html=True)

        role = st.selectbox("Login As", ["admin","doctor","reception"],
            format_func=lambda x: {"admin":"🔐  Admin","doctor":"👨‍⚕️  Doctor",
                                    "reception":"🗃️  Receptionist"}[x])
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")

        if st.button("Login  →", use_container_width=True):
            u, p = CREDS[role]
            if username == u and password == p:
                st.session_state.logged_in = True
                st.session_state.user_role = role
                st.rerun()
            else:
                err("Invalid credentials. Please try again.")

        st.markdown("""<div style='margin-top:1.2rem;background:#f0fdf4;
          border-radius:10px;padding:.85rem 1rem;font-size:.78rem;color:#64748b;
          line-height:1.7;'>
          <b style='color:#065f46;'>Demo Credentials</b><br>
          🔐 Admin → <code>admin</code> / <code>admin@234</code><br>
          👨‍⚕️ Doctor → <code>doctor</code> / <code>doctor@459</code><br>
          🗃️ Reception → <code>reception</code> / <code>recep@389</code>
        </div></div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def render_sidebar():
    role = st.session_state.user_role
    with st.sidebar:
        st.markdown("""<div style='text-align:center;padding:1.5rem 0 .5rem;'>
          <div style='font-size:3rem;'>🏥</div>
          <div style='font-family:Cormorant Garamond,serif;font-size:1.35rem;
            font-weight:800;color:#ecfdf5;'>Jan Kalyan Hospital</div>
          <div style='font-size:.72rem;color:#6ee7b7;letter-spacing:1.5px;
            text-transform:uppercase;margin-top:.2rem;'>Bihar • Est. 2005</div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        badges = {"admin":"🔐 Admin","doctor":"👨‍⚕️ Doctor","reception":"🗃️ Receptionist"}
        st.markdown(f"""<div style='text-align:center;margin-bottom:1rem;'>
          <span style='background:rgba(110,231,183,.15);border:1px solid rgba(110,231,183,.3);
            border-radius:20px;padding:.3rem 1.1rem;font-size:.8rem;
            color:#6ee7b7;font-weight:600;'>{badges[role]}</span>
        </div>""", unsafe_allow_html=True)

        MENUS = {
            "admin":     ["🏠 Dashboard","🏥 About Hospital","👨‍⚕️ Doctors",
                          "🧑‍🤝‍🧑 Patients","📅 Appointments","💰 Billing","💵 Salary"],
            "doctor":    ["🏠 Dashboard","🏥 About Hospital",
                          "🧑‍🤝‍🧑 Patients","📅 Appointments"],
            "reception": ["🏠 Dashboard","🏥 About Hospital",
                          "🧑‍🤝‍🧑 Patients","📅 Appointments","💰 Billing"],
        }
        page = st.radio("Navigation", MENUS[role], label_visibility="collapsed")

        st.markdown("<hr>", unsafe_allow_html=True)

        # Quick stats in sidebar
        st.markdown(f"""<div style='font-size:.78rem;color:#a7f3d0;line-height:2;'>
          👨‍⚕️ Doctors: <b>{len(st.session_state.doctors)}</b><br>
          🧑‍🤝‍🧑 Patients: <b>{len(st.session_state.patients)}</b><br>
          📅 Appointments: <b>{len(st.session_state.appointments)}</b>
        </div>""", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    return page


# ══════════════════════════════════════════════════════════════════════════════
#  DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
def page_dashboard():
    role = st.session_state.user_role

    # ── Hero Banner ──
    st.markdown("""<div style='
      background:linear-gradient(120deg,#064e3b 0%,#065f46 50%,#047857 100%);
      border-radius:22px;padding:2.8rem 3rem 2.4rem;margin-bottom:1.8rem;
      position:relative;overflow:hidden;
      box-shadow:0 10px 50px rgba(6,78,59,.22);
    '>
      <div style='position:absolute;right:2.5rem;top:50%;transform:translateY(-50%);
        font-size:8rem;opacity:.07;'>🏥</div>
      <div style='position:absolute;right:10rem;top:1rem;font-size:4rem;opacity:.05;'>❤️</div>
      <div style='font-size:.75rem;letter-spacing:2px;color:#6ee7b7;
        text-transform:uppercase;font-weight:600;margin-bottom:.6rem;'>
        ⚕️ Premier Healthcare · Bihar</div>
      <div style='font-family:Cormorant Garamond,serif;font-size:2.8rem;
        font-weight:800;color:#fff;line-height:1.1;margin-bottom:.7rem;'>
        Jan Kalyan Hospital</div>
      <div style='color:#a7f3d0;font-size:.92rem;margin-bottom:1.2rem;'>
        📍 Bihar &nbsp;•&nbsp; 📧 jankalyan@gmail.com &nbsp;•&nbsp; 📞 +91 89896 51456
      </div>
      <div style='display:flex;gap:.7rem;flex-wrap:wrap;'>
        <span style='background:rgba(110,231,183,.18);border:1px solid rgba(110,231,183,.3);
          color:#6ee7b7;border-radius:20px;padding:.28rem .9rem;font-size:.78rem;
          font-weight:600;'>24/7 Emergency</span>
        <span style='background:rgba(110,231,183,.18);border:1px solid rgba(110,231,183,.3);
          color:#6ee7b7;border-radius:20px;padding:.28rem .9rem;font-size:.78rem;
          font-weight:600;'>NABH Accredited</span>
        <span style='background:rgba(110,231,183,.18);border:1px solid rgba(110,231,183,.3);
          color:#6ee7b7;border-radius:20px;padding:.28rem .9rem;font-size:.78rem;
          font-weight:600;'>ISO 9001:2015</span>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── Stat Cards ──
    total_rev = sum(b["total"] for b in st.session_state.bills)
    stat_cards([
        ("👨‍⚕️", len(st.session_state.doctors),     "Registered Doctors",   "#047857"),
        ("🧑‍🤝‍🧑", len(st.session_state.patients),    "Active Patients",      "#0ea5e9"),
        ("📅", len(st.session_state.appointments), "Appointments",         "#d97706"),
        ("💰", f"₹{total_rev:,}",                  "Total Revenue",        "#7c3aed"),
        ("💵", len(st.session_state.salaries),     "Salary Records",       "#dc2626"),
    ])

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.1, 1])

    # ── Recent Doctors ──
    with col1:
        section("Recent Doctors", "👨‍⚕️")
        if not st.session_state.doctors:
            st.info("No doctors added yet.")
        else:
            for d in st.session_state.doctors[-4:][::-1]:
                st.markdown(f"""<div style='
                  background:white;border-radius:14px;padding:1rem 1.2rem;
                  margin-bottom:.7rem;display:flex;align-items:center;gap:1rem;
                  box-shadow:0 1px 8px rgba(0,0,0,.06);
                  border-left:4px solid #047857;
                '>
                  <div style='width:48px;height:48px;border-radius:50%;flex-shrink:0;
                    background:linear-gradient(135deg,#047857,#34d399);
                    display:flex;align-items:center;justify-content:center;
                    font-size:1.4rem;'>👨‍⚕️</div>
                  <div style='flex:1'>
                    <div style='font-weight:700;font-size:.97rem;color:#0f172a;'>
                      Dr. {d["name"]}</div>
                    <div style='font-size:.8rem;color:#047857;font-weight:600;'>
                      {d["spec"]}</div>
                    <div style='font-size:.77rem;color:#64748b;margin-top:.1rem;'>
                      🕐 {d["exp"]} yrs exp</div>
                  </div>
                  <div style='background:#ecfdf5;color:#065f46;border-radius:8px;
                    padding:.3rem .7rem;font-size:.8rem;font-weight:700;'>
                    ₹{d["fee"]}</div>
                </div>""", unsafe_allow_html=True)

    # ── Recent Patients ──
    with col2:
        section("Recent Patients", "🧑‍🤝‍🧑")
        if not st.session_state.patients:
            st.info("No patients added yet.")
        else:
            recent = st.session_state.patients[-6:][::-1]
            df = pd.DataFrame(recent)[["id","name","age","disease","room"]]
            df.columns = ["ID","Name","Age","Disease","Room"]
            st.dataframe(df, use_container_width=True, hide_index=True)

        section("Upcoming Appointments", "📅")
        if not st.session_state.appointments:
            st.info("No appointments yet.")
        else:
            recent_a = st.session_state.appointments[-4:][::-1]
            for a in recent_a:
                st.markdown(f"""<div style='background:white;border-radius:12px;
                  padding:.8rem 1rem;margin-bottom:.6rem;
                  box-shadow:0 1px 8px rgba(0,0,0,.06);
                  border-left:4px solid #d97706;display:flex;
                  justify-content:space-between;align-items:center;'>
                  <div>
                    <div style='font-weight:600;font-size:.88rem;color:#0f172a;'>
                      {a["patient"]}</div>
                    <div style='font-size:.78rem;color:#64748b;'>Dr. {a["doctor"]}</div>
                  </div>
                  <div style='text-align:right;'>
                    <div style='font-size:.78rem;color:#d97706;font-weight:600;'>
                      {a["date"]}</div>
                    <div style='font-size:.75rem;color:#94a3b8;'>{a["time"]}</div>
                  </div>
                </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ABOUT HOSPITAL
# ══════════════════════════════════════════════════════════════════════════════
def page_about():
    st.markdown("""<div style='
      background:linear-gradient(120deg,#064e3b,#047857);
      border-radius:20px;padding:2.5rem 3rem;margin-bottom:2rem;
      box-shadow:0 8px 40px rgba(6,78,59,.2);
    '>
      <div style='font-size:.75rem;letter-spacing:2px;color:#6ee7b7;
        text-transform:uppercase;font-weight:600;margin-bottom:.5rem;'>
        Serving Bihar Since 2005</div>
      <div style='font-family:Cormorant Garamond,serif;font-size:2.4rem;
        font-weight:800;color:#fff;margin-bottom:.5rem;'>Jan Kalyan Hospital</div>
      <div style='color:#a7f3d0;font-size:.95rem;max-width:640px;line-height:1.7;'>
        A beacon of quality healthcare in Bihar — dedicated to compassionate,
        affordable, and evidence-based medical care for every citizen.
      </div>
    </div>""", unsafe_allow_html=True)

    # ── Mission / Vision / Values ──
    c1, c2, c3 = st.columns(3)
    cards = [
        ("🎯","Our Mission","To deliver affordable, high-quality healthcare to every citizen of Bihar, ensuring no patient is turned away due to financial constraints.",
         "#064e3b","#dcfce7"),
        ("🔭","Our Vision","To become Bihar's most trusted healthcare institution, setting benchmarks in patient care, medical education, and community health.",
         "#1d4ed8","#dbeafe"),
        ("💚","Our Values","Compassion · Integrity · Excellence · Accountability · Innovation — these five pillars guide every action of our medical team.",
         "#b45309","#fef3c7"),
    ]
    for col, (icon, title, desc, color, bg) in zip([c1,c2,c3], cards):
        with col:
            st.markdown(f"""<div style='background:{bg};border-radius:16px;
              padding:1.6rem;height:200px;border-top:4px solid {color};
              box-shadow:0 2px 12px rgba(0,0,0,.06);'>
              <div style='font-size:1.8rem;margin-bottom:.5rem;'>{icon}</div>
              <div style='font-family:Cormorant Garamond,serif;font-size:1.15rem;
                font-weight:700;color:{color};margin-bottom:.5rem;'>{title}</div>
              <div style='font-size:.83rem;color:#374151;line-height:1.6;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Services ──
    section("Our Medical Services", "🩺")
    services = [
        ("🫀","Cardiology","Advanced heart care, ECG, Echo, Angiography"),
        ("🧠","Neurology","Brain & spine disorders, Stroke management"),
        ("🦴","Orthopaedics","Joint replacement, Fracture care, Physiotherapy"),
        ("👶","Paediatrics","Child healthcare from newborn to 18 years"),
        ("🤰","Gynaecology","Women's health, Maternity, Family planning"),
        ("🫁","Pulmonology","Respiratory care, Asthma, TB treatment"),
        ("🔬","Pathology","Complete blood work, Biopsies, Lab diagnostics"),
        ("🩻","Radiology","X-Ray, MRI, CT Scan, Ultrasound"),
        ("💊","Pharmacy","24/7 in-house pharmacy with generic medicines"),
        ("🚑","Emergency","Round-the-clock trauma & emergency care"),
        ("🏥","ICU / CCU","10-bed ICU with ventilator support"),
        ("🧘","Rehabilitation","Post-surgery recovery & physiotherapy"),
    ]
    cols = st.columns(4)
    for i, (icon, name, desc) in enumerate(services):
        with cols[i % 4]:
            st.markdown(f"""<div style='background:white;border-radius:14px;
              padding:1.1rem 1rem;margin-bottom:.9rem;
              box-shadow:0 1px 8px rgba(0,0,0,.06);
              border-bottom:3px solid #047857;
              transition:transform .2s;'>
              <div style='font-size:1.6rem;'>{icon}</div>
              <div style='font-weight:700;font-size:.9rem;color:#064e3b;
                margin:.3rem 0 .2rem;'>{name}</div>
              <div style='font-size:.77rem;color:#64748b;line-height:1.5;'>{desc}</div>
            </div>""", unsafe_allow_html=True)

    # ── Facilities & Contact ──
    col1, col2 = st.columns(2)
    with col1:
        section("Facilities", "🏗️")
        facilities = [
            ("🏢","100-bed hospital with private & general wards"),
            ("🔬","NABL accredited pathology laboratory"),
            ("🩻","Digital X-ray & colour Doppler ultrasound"),
            ("🚑","24/7 ambulance service (2 vehicles)"),
            ("🍽️","In-house patient diet kitchen"),
            ("♿","Wheelchair-accessible premises"),
            ("🌐","Free Wi-Fi for patients & visitors"),
            ("💳","Cashless insurance — 15+ TPA empanelled"),
        ]
        for icon, text in facilities:
            st.markdown(f"""<div style='display:flex;align-items:flex-start;
              gap:.7rem;padding:.55rem 0;border-bottom:1px solid #f0fdf4;'>
              <span style='font-size:1.1rem;'>{icon}</span>
              <span style='font-size:.88rem;color:#374151;'>{text}</span>
            </div>""", unsafe_allow_html=True)

    with col2:
        section("Contact & Location", "📍")
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.6rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>
          <div style='font-family:Cormorant Garamond,serif;font-size:1.1rem;
            font-weight:700;color:#064e3b;margin-bottom:1rem;'>
            Jan Kalyan Hospital</div>
        """, unsafe_allow_html=True)
        contact_rows = [
            ("📍","Address","Near Civil Court, Main Road, Bihar — 800001"),
            ("📞","Phone","+91 89896 51456"),
            ("📧","Email","jankalyan@gmail.com"),
            ("⏰","OPD Hours","Mon–Sat: 8:00 AM – 8:00 PM"),
            ("🚑","Emergency","24 × 7 × 365"),
            ("🏥","Beds","100 (General + Private + ICU)"),
            ("👨‍⚕️","Specialists","20+ on panel"),
            ("🌐","Website","www.jankalyanhospital.in"),
        ]
        for icon, label, value in contact_rows:
            st.markdown(f"""<div style='display:flex;gap:.8rem;padding:.5rem 0;
              border-bottom:1px dashed #e2e8f0;font-size:.87rem;'>
              <span>{icon}</span>
              <span style='color:#64748b;min-width:80px;'>{label}</span>
              <span style='color:#0f172a;font-weight:500;'>{value}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        section("Achievements", "🏆")
        achievements = [
            ("🏅","Best District Hospital — Bihar Govt 2022"),
            ("🌟","NABH Accreditation — 2021"),
            ("🤝","10,000+ free treatments under PM-JAY"),
            ("📚","MoU with IGIMS Patna for referrals"),
        ]
        for icon, text in achievements:
            st.markdown(f"""<div style='background:#f0fdf4;border-radius:10px;
              padding:.7rem 1rem;margin-bottom:.5rem;display:flex;gap:.7rem;
              font-size:.87rem;color:#065f46;font-weight:500;'>
              <span>{icon}</span><span>{text}</span>
            </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  DOCTORS
# ══════════════════════════════════════════════════════════════════════════════
def page_doctors():
    section("Doctor Management", "👨‍⚕️")
    tab1, tab2, tab3 = st.tabs(["➕  Add Doctor", "📋  All Doctors", "🔍  Search / Delete"])

    with tab1:
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.8rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Doctor Name", placeholder="e.g. Ramesh Kumar")
            spec = st.text_input("Specialization", placeholder="e.g. Cardiology")
        with c2:
            exp  = st.number_input("Experience (years)", min_value=0, max_value=60, value=5)
            fee  = st.number_input("Consultation Fee (₹)", min_value=0, value=500, step=50)
        if st.button("➕ Add Doctor"):
            if name.strip() and spec.strip():
                doc_id = len(st.session_state.doctors) + 1
                st.session_state.doctors.append({
                    "id": doc_id, "name": name.strip(),
                    "spec": spec.strip(), "exp": exp, "fee": fee
                })
                ok(f"Dr. {name} added successfully! (ID: #{doc_id})")
            else:
                err("Doctor Name and Specialization are required.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.doctors:
            st.info("No doctors registered yet. Add one from the first tab.")
        else:
            cols = st.columns(3)
            for i, d in enumerate(st.session_state.doctors):
                with cols[i % 3]:
                    st.markdown(f"""<div style='background:white;border-radius:16px;
                      padding:1.4rem;margin-bottom:1rem;
                      box-shadow:0 2px 12px rgba(0,0,0,.07);
                      border-top:4px solid #047857;'>
                      <div style='width:54px;height:54px;border-radius:50%;
                        background:linear-gradient(135deg,#047857,#34d399);
                        display:flex;align-items:center;justify-content:center;
                        font-size:1.5rem;margin-bottom:.8rem;'>👨‍⚕️</div>
                      <div style='font-weight:700;font-size:1rem;color:#0f172a;'>
                        Dr. {d["name"]}</div>
                      <div style='font-size:.8rem;color:#047857;font-weight:600;
                        margin:.15rem 0;'>{d["spec"]}</div>
                      <div style='font-size:.78rem;color:#64748b;'>
                        🕐 {d["exp"]} yrs &nbsp;|&nbsp; ID #{d["id"]}</div>
                      <div style='margin-top:.7rem;background:#ecfdf5;
                        border-radius:8px;padding:.35rem .7rem;
                        font-size:.82rem;font-weight:700;color:#065f46;'>
                        ₹{d["fee"]} / visit</div>
                    </div>""", unsafe_allow_html=True)

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**🔍 Search by Name**")
            q = st.text_input("Doctor name to search", label_visibility="collapsed",
                              placeholder="Type doctor name...")
            if q:
                res = [d for d in st.session_state.doctors if q.lower() in d["name"].lower()]
                if res:
                    for d in res:
                        st.markdown(f"""<div style='background:#f0fdf4;border-radius:12px;
                          padding:.9rem 1.1rem;margin-bottom:.5rem;
                          border-left:4px solid #047857;'>
                          <b>Dr. {d["name"]}</b> — {d["spec"]}<br>
                          <span style='font-size:.8rem;color:#64748b;'>
                            {d["exp"]} yrs exp · ₹{d["fee"]} · ID #{d["id"]}</span>
                        </div>""", unsafe_allow_html=True)
                else:
                    err("No doctor found with that name.")

        with c2:
            st.markdown("**🗑️ Delete Doctor by ID**")
            del_id = st.number_input("Doctor ID", min_value=1, step=1,
                                     label_visibility="collapsed")
            if st.button("🗑️ Delete Doctor"):
                before = len(st.session_state.doctors)
                st.session_state.doctors = [
                    d for d in st.session_state.doctors if d["id"] != del_id
                ]
                if len(st.session_state.doctors) < before:
                    ok(f"Doctor #{del_id} deleted.")
                else:
                    err(f"No doctor with ID #{del_id}.")


# ══════════════════════════════════════════════════════════════════════════════
#  PATIENTS
# ══════════════════════════════════════════════════════════════════════════════
def page_patients():
    section("Patient Management", "🧑‍🤝‍🧑")
    tab1, tab2, tab3 = st.tabs(["➕  Add Patient", "📋  All Patients", "🔍  Search"])

    with tab1:
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.8rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name    = st.text_input("Patient Name", placeholder="Full name")
            age     = st.number_input("Age", min_value=0, max_value=120, value=30)
        with c2:
            disease = st.text_input("Disease / Diagnosis", placeholder="e.g. Typhoid")
            room    = st.text_input("Room Number", placeholder="e.g. G-12")
        if st.button("➕ Add Patient"):
            if name.strip() and disease.strip() and room.strip():
                pat_id = len(st.session_state.patients) + 1
                st.session_state.patients.append({
                    "id": pat_id, "name": name.strip(), "age": age,
                    "disease": disease.strip(), "room": room.strip()
                })
                ok(f"{name} admitted successfully! (Patient ID: #{pat_id})")
            else:
                err("All fields are required.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.patients:
            st.info("No patients admitted yet.")
        else:
            df = pd.DataFrame(st.session_state.patients)
            df.columns = ["ID","Name","Age","Disease","Room"]
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption(f"Total patients: {len(st.session_state.patients)}")

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            name_q = st.text_input("Search by Name", placeholder="Patient name...")
            if name_q:
                res = [p for p in st.session_state.patients
                       if name_q.lower() in p["name"].lower()]
                if res:
                    df = pd.DataFrame(res)
                    df.columns = ["ID","Name","Age","Disease","Room"]
                    st.dataframe(df, use_container_width=True, hide_index=True)
                else:
                    err("No patient found.")

        with c2:
            id_q = st.number_input("Search by ID", min_value=0, step=1, value=0)
            if id_q > 0:
                res = [p for p in st.session_state.patients if p["id"] == id_q]
                if res:
                    p = res[0]
                    st.markdown(f"""<div style='background:#f0fdf4;border-radius:14px;
                      padding:1.2rem 1.4rem;border-left:5px solid #047857;'>
                      <div style='font-weight:700;font-size:1.05rem;color:#064e3b;'>
                        {p["name"]}</div>
                      <div style='font-size:.85rem;color:#374151;margin-top:.4rem;
                        line-height:1.9;'>
                        🆔 ID: #{p["id"]}<br>
                        🎂 Age: {p["age"]}<br>
                        🩺 Disease: {p["disease"]}<br>
                        🛏️ Room: {p["room"]}
                      </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    err(f"No patient with ID #{id_q}.")


# ══════════════════════════════════════════════════════════════════════════════
#  APPOINTMENTS
# ══════════════════════════════════════════════════════════════════════════════
def page_appointments():
    section("Appointment Management", "📅")
    tab1, tab2, tab3 = st.tabs(["➕  Book Appointment","📋  All Appointments","🔍  Search by Date"])

    with tab1:
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.8rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            doc = st.text_input("Doctor Name", placeholder="e.g. Dr. Ramesh Kumar")
            pat = st.text_input("Patient Name", placeholder="e.g. Suresh Singh")
        with c2:
            appt_date = st.date_input("Date", value=date.today())
            appt_time = st.time_input("Time", value=dtime(10, 0))
        if st.button("📅 Book Appointment"):
            if doc.strip() and pat.strip():
                appt_id = len(st.session_state.appointments) + 1
                st.session_state.appointments.append({
                    "id": appt_id, "doctor": doc.strip(),
                    "patient": pat.strip(),
                    "date": str(appt_date),
                    "time": appt_time.strftime("%I:%M %p")
                })
                ok(f"Appointment #{appt_id} booked for {pat} on {appt_date}.")
            else:
                err("Doctor and Patient names are required.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.appointments:
            st.info("No appointments booked yet.")
        else:
            df = pd.DataFrame(st.session_state.appointments)
            df.columns = ["ID","Doctor","Patient","Date","Time"]
            st.dataframe(df, use_container_width=True, hide_index=True)

    with tab3:
        search_date = st.date_input("Select a date", value=date.today(),
                                    key="appt_search_date")
        res = [a for a in st.session_state.appointments
               if a["date"] == str(search_date)]
        if res:
            df = pd.DataFrame(res)
            df.columns = ["ID","Doctor","Patient","Date","Time"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info(f"No appointments on {search_date}.")


# ══════════════════════════════════════════════════════════════════════════════
#  BILLING
# ══════════════════════════════════════════════════════════════════════════════
def page_billing():
    section("Billing Management", "💰")
    tab1, tab2 = st.tabs(["➕  Generate Bill","📋  All Bills"])

    with tab1:
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.8rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        name    = st.text_input("Patient Name", placeholder="Patient full name")
        c1, c2, c3 = st.columns(3)
        with c1: doc_fee = st.number_input("Doctor Fee (₹)",      min_value=0, value=500,  step=50)
        with c2: room_ch = st.number_input("Room Charges (₹)",    min_value=0, value=1000, step=100)
        with c3: med_ch  = st.number_input("Medicine Charges (₹)",min_value=0, value=300,  step=50)
        total = doc_fee + room_ch + med_ch

        st.markdown(f"""<div style='background:#ecfdf5;border-radius:10px;
          padding:.8rem 1.2rem;margin:.6rem 0;display:flex;
          justify-content:space-between;align-items:center;'>
          <span style='color:#065f46;font-weight:600;'>Estimated Total</span>
          <span style='font-family:Cormorant Garamond,serif;font-size:1.4rem;
            font-weight:800;color:#064e3b;'>₹{total:,}</span>
        </div>""", unsafe_allow_html=True)

        if st.button("🧾 Generate Bill"):
            if name.strip():
                bill_id = len(st.session_state.bills) + 1
                st.session_state.bills.append({
                    "id": bill_id, "patient": name.strip(),
                    "doc_fee": doc_fee, "room": room_ch,
                    "medicine": med_ch, "total": total
                })
                ok("Bill generated successfully!")
                # Slip
                st.markdown(f"""<div style='background:white;border-radius:16px;
                  border:1px solid #e2e8f0;padding:1.8rem 2rem;
                  margin-top:1rem;max-width:480px;'>
                  <div style='text-align:center;margin-bottom:1.2rem;'>
                    <div style='font-size:1.8rem;'>🏥</div>
                    <div style='font-family:Cormorant Garamond,serif;font-size:1.2rem;
                      font-weight:800;color:#064e3b;'>Jan Kalyan Hospital</div>
                    <div style='font-size:.75rem;color:#64748b;'>Bihar • jankalyan@gmail.com</div>
                    <div style='font-size:.8rem;font-weight:600;color:#047857;
                      margin-top:.3rem;'>BILL RECEIPT #{bill_id}</div>
                  </div>
                """, unsafe_allow_html=True)
                slip_row("Patient Name", name)
                slip_row("Doctor Fee",   f"₹{doc_fee:,}")
                slip_row("Room Charges", f"₹{room_ch:,}")
                slip_row("Medicine",     f"₹{med_ch:,}")
                slip_row("NET TOTAL",    f"₹{total:,}", bold=True, color="#065f46")
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                err("Patient name is required.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.bills:
            st.info("No bills generated yet.")
        else:
            df = pd.DataFrame(st.session_state.bills)
            df.columns = ["ID","Patient","Doctor Fee","Room","Medicine","Total"]
            st.dataframe(df, use_container_width=True, hide_index=True)
            total_rev = sum(b["total"] for b in st.session_state.bills)
            st.markdown(f"""<div style='background:#ecfdf5;border-radius:12px;
              padding:1rem 1.5rem;margin-top:.8rem;display:flex;
              justify-content:space-between;align-items:center;'>
              <span style='font-weight:600;color:#065f46;'>
                Total Revenue ({len(st.session_state.bills)} bills)</span>
              <span style='font-family:Cormorant Garamond,serif;font-size:1.5rem;
                font-weight:800;color:#064e3b;'>₹{total_rev:,}</span>
            </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  SALARY
# ══════════════════════════════════════════════════════════════════════════════
def page_salary():
    section("Salary Management", "💵")
    tab1, tab2, tab3 = st.tabs(["➕  Add Salary","📋  All Records","🧮  Calculator"])

    with tab1:
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.8rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name     = st.text_input("Employee Name", placeholder="Full name")
            emp_type = st.selectbox("Employee Type", ["Doctor","Nurse","Staff"])
        with c2:
            month = st.selectbox("Month", ["January","February","March","April",
                                            "May","June","July","August",
                                            "September","October","November","December"])
            year  = st.number_input("Year", min_value=2020, max_value=2035, value=2025)

        basic = st.number_input("Basic Salary (₹)", min_value=0, value=30000, step=1000)
        c1, c2, c3 = st.columns(3)
        with c1: hra = st.number_input("HRA %", min_value=0.0, max_value=50.0, value=10.0, step=0.5)
        with c2: da  = st.number_input("DA %",  min_value=0.0, max_value=50.0, value=5.0,  step=0.5)
        with c3: pf  = st.number_input("PF %",  min_value=0.0, max_value=20.0, value=12.0, step=0.5)

        hra_a  = (hra / 100) * basic
        da_a   = (da  / 100) * basic
        pf_a   = (pf  / 100) * basic
        gross  = basic + hra_a + da_a
        net    = gross - pf_a

        # Live preview
        st.markdown(f"""<div style='background:#f0fdf4;border-radius:12px;
          padding:1rem 1.4rem;margin:.7rem 0;
          display:flex;gap:2rem;flex-wrap:wrap;'>
          <div><div style='font-size:.75rem;color:#64748b;'>Gross</div>
               <div style='font-weight:700;color:#065f46;'>₹{gross:,.0f}</div></div>
          <div><div style='font-size:.75rem;color:#64748b;'>PF Deduction</div>
               <div style='font-weight:700;color:#dc2626;'>-₹{pf_a:,.0f}</div></div>
          <div><div style='font-size:.75rem;color:#64748b;'>Net Salary</div>
               <div style='font-family:Cormorant Garamond,serif;font-size:1.4rem;
                 font-weight:800;color:#064e3b;'>₹{net:,.0f}</div></div>
        </div>""", unsafe_allow_html=True)

        if st.button("💾 Save Salary Record"):
            if name.strip():
                sal_id = len(st.session_state.salaries) + 1
                st.session_state.salaries.append({
                    "id": sal_id, "name": name.strip(), "type": emp_type,
                    "month": month, "year": year,
                    "basic": basic, "hra": round(hra_a, 2),
                    "da": round(da_a, 2), "pf": round(pf_a, 2),
                    "gross": round(gross, 2), "net": round(net, 2)
                })
                ok(f"Salary record saved for {name} — {month} {year}")
                # Salary Slip
                st.markdown(f"""<div style='background:white;border-radius:16px;
                  border:1px solid #e2e8f0;padding:1.8rem 2rem;
                  margin-top:1rem;max-width:480px;'>
                  <div style='text-align:center;margin-bottom:1.2rem;'>
                    <div style='font-size:1.8rem;'>🏥</div>
                    <div style='font-family:Cormorant Garamond,serif;font-size:1.2rem;
                      font-weight:800;color:#064e3b;'>Jan Kalyan Hospital</div>
                    <div style='font-size:.75rem;color:#64748b;'>Bihar</div>
                    <div style='font-size:.8rem;font-weight:600;color:#047857;
                      margin-top:.3rem;'>SALARY SLIP — {month.upper()} {year}</div>
                  </div>
                """, unsafe_allow_html=True)
                slip_row("Employee Name", name)
                slip_row("Employee Type", emp_type)
                slip_row("Basic Salary",  f"₹{basic:,}")
                slip_row(f"HRA ({hra}%)",  f"₹{hra_a:,.2f}")
                slip_row(f"DA  ({da}%)",   f"₹{da_a:,.2f}")
                slip_row("Gross Salary",   f"₹{gross:,.2f}")
                slip_row(f"PF  ({pf}%)",   f"-₹{pf_a:,.2f}", color="#dc2626")
                slip_row("NET SALARY",     f"₹{net:,.2f}", bold=True, color="#065f46")
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                err("Employee name is required.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.salaries:
            st.info("No salary records yet.")
        else:
            df = pd.DataFrame(st.session_state.salaries)
            df = df[["id","name","type","month","year","basic","gross","net"]]
            df.columns = ["ID","Name","Type","Month","Year","Basic","Gross","Net Salary"]
            st.dataframe(df, use_container_width=True, hide_index=True)

            total_paid = sum(s["net"] for s in st.session_state.salaries)
            c1, c2, c3 = st.columns(3)
            with c1:
                doc_sal = sum(s["net"] for s in st.session_state.salaries if s["type"]=="Doctor")
                st.markdown(f"""<div style='background:#ecfdf5;border-radius:12px;
                  padding:.9rem 1.2rem;text-align:center;'>
                  <div style='font-size:.78rem;color:#64748b;'>Doctors</div>
                  <div style='font-weight:800;color:#065f46;font-size:1.1rem;'>₹{doc_sal:,.0f}</div>
                </div>""", unsafe_allow_html=True)
            with c2:
                nur_sal = sum(s["net"] for s in st.session_state.salaries if s["type"]=="Nurse")
                st.markdown(f"""<div style='background:#eff6ff;border-radius:12px;
                  padding:.9rem 1.2rem;text-align:center;'>
                  <div style='font-size:.78rem;color:#64748b;'>Nurses</div>
                  <div style='font-weight:800;color:#1d4ed8;font-size:1.1rem;'>₹{nur_sal:,.0f}</div>
                </div>""", unsafe_allow_html=True)
            with c3:
                st_sal = sum(s["net"] for s in st.session_state.salaries if s["type"]=="Staff")
                st.markdown(f"""<div style='background:#fef3c7;border-radius:12px;
                  padding:.9rem 1.2rem;text-align:center;'>
                  <div style='font-size:.78rem;color:#64748b;'>Staff</div>
                  <div style='font-weight:800;color:#b45309;font-size:1.1rem;'>₹{st_sal:,.0f}</div>
                </div>""", unsafe_allow_html=True)

            st.markdown(f"""<div style='background:#064e3b;border-radius:12px;
              padding:1rem 1.5rem;margin-top:.8rem;display:flex;
              justify-content:space-between;align-items:center;'>
              <span style='font-weight:600;color:#a7f3d0;'>
                Total Salary Disbursed ({len(st.session_state.salaries)} records)</span>
              <span style='font-family:Cormorant Garamond,serif;font-size:1.5rem;
                font-weight:800;color:#fff;'>₹{total_paid:,.2f}</span>
            </div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown("**Quick Monthly Salary Calculator** — results not saved")
        st.markdown("""<div style='background:white;border-radius:16px;
          padding:1.6rem 2rem;box-shadow:0 2px 14px rgba(0,0,0,.07);'>""",
          unsafe_allow_html=True)
        basic = st.number_input("Basic Salary (₹)", min_value=0, value=30000,
                                 step=1000, key="c_basic")
        c1,c2,c3 = st.columns(3)
        with c1: hra = st.number_input("HRA %", value=10.0, key="c_hra")
        with c2: da  = st.number_input("DA %",  value=5.0,  key="c_da")
        with c3: pf  = st.number_input("PF %",  value=12.0, key="c_pf")

        hra_a = (hra/100)*basic; da_a = (da/100)*basic
        pf_a  = (pf/100)*basic;  gross = basic+hra_a+da_a; net = gross-pf_a

        st.markdown(f"""<div style='background:white;border-radius:14px;
          border:1px solid #e2e8f0;padding:1.4rem 1.6rem;margin-top:.8rem;
          max-width:380px;'>""", unsafe_allow_html=True)
        slip_row("Basic Salary",    f"₹{basic:,}")
        slip_row(f"HRA ({hra}%)",   f"₹{hra_a:,.2f}")
        slip_row(f"DA  ({da}%)",    f"₹{da_a:,.2f}")
        slip_row("Gross Salary",    f"₹{gross:,.2f}")
        slip_row(f"PF  ({pf}%)",    f"-₹{pf_a:,.2f}", color="#dc2626")
        slip_row("NET SALARY",      f"₹{net:,.2f}", bold=True, color="#065f46")
        st.markdown("</div></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    login_page()
else:
    page = render_sidebar()
    key  = page.split(" ", 1)[1].strip().lower()

    if   "dashboard"    in key: page_dashboard()
    elif "about"        in key: page_about()
    elif "doctor"       in key: page_doctors()
    elif "patient"      in key: page_patients()
    elif "appointment"  in key: page_appointments()
    elif "billing"      in key: page_billing()
    elif "salary"       in key: page_salary()
