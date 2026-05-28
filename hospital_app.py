import streamlit as st

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AIIMS Hospital Management",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS Styling ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --navy:    #0a1628;
    --blue:    #1a3a6e;
    --sky:     #2563eb;
    --accent:  #38bdf8;
    --gold:    #f59e0b;
    --red:     #ef4444;
    --green:   #10b981;
    --bg:      #f0f4ff;
    --card:    #ffffff;
    --text:    #1e293b;
    --muted:   #64748b;
    --border:  #e2e8f0;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, var(--navy) 0%, var(--blue) 100%);
    border-right: none;
}
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.95rem;
    padding: 0.5rem 0.75rem;
    border-radius: 8px;
    transition: background 0.2s;
}
[data-testid="stSidebar"] .stRadio label:hover { background: rgba(255,255,255,0.08); }

/* ── Banner ── */
.banner {
    background: linear-gradient(120deg, var(--navy) 0%, var(--blue) 60%, #1d4ed8 100%);
    border-radius: 20px;
    padding: 2.5rem 2.5rem 2rem;
    margin-bottom: 1.8rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 40px rgba(10,22,40,0.18);
}
.banner::before {
    content: '🏥';
    position: absolute;
    right: 2rem; top: 50%;
    transform: translateY(-50%);
    font-size: 7rem;
    opacity: 0.08;
}
.banner h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: #ffffff !important;
    margin: 0 0 0.4rem;
    letter-spacing: -0.5px;
}
.banner p { color: var(--accent) !important; font-size: 1rem; margin: 0; }
.banner-badge {
    display: inline-block;
    background: rgba(56,189,248,0.18);
    color: var(--accent) !important;
    border: 1px solid rgba(56,189,248,0.35);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

/* ── Stat Cards ── */
.stat-row { display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 140px;
    background: var(--card);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border-left: 4px solid var(--sky);
    transition: transform 0.2s, box-shadow 0.2s;
}
.stat-card:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.1); }
.stat-card .number {
    font-family: 'Playfair Display', serif;
    font-size: 2rem; font-weight: 700;
    color: var(--navy); line-height: 1;
}
.stat-card .label { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; font-weight: 500; }
.stat-card .icon  { font-size: 1.6rem; margin-bottom: 0.5rem; }

/* ── Section Title ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 700;
    color: var(--navy);
    margin: 1.8rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border);
}

/* ── Doctor Cards ── */
.doc-grid { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem; }
.doc-card {
    background: var(--card);
    border-radius: 16px;
    padding: 1.4rem;
    width: 220px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border-top: 4px solid var(--sky);
    transition: transform 0.2s, box-shadow 0.2s;
}
.doc-card:hover { transform: translateY(-4px); box-shadow: 0 8px 28px rgba(0,0,0,0.12); }
.doc-avatar {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, var(--sky), var(--accent));
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.6rem; margin-bottom: 0.8rem;
}
.doc-name { font-weight: 700; font-size: 1rem; color: var(--navy); }
.doc-spec { font-size: 0.8rem; color: var(--sky); font-weight: 600; margin: 0.15rem 0; }
.doc-exp  { font-size: 0.78rem; color: var(--muted); }
.doc-fee  {
    margin-top: 0.7rem;
    background: #eff6ff;
    border-radius: 8px;
    padding: 0.35rem 0.6rem;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--sky);
}

/* ── Form Card ── */
.form-card {
    background: var(--card);
    border-radius: 16px;
    padding: 1.8rem 2rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    margin-bottom: 1.5rem;
}

/* ── Pill Badge ── */
.pill {
    display: inline-block;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
}
.pill-blue   { background: #dbeafe; color: #1d4ed8; }
.pill-green  { background: #d1fae5; color: #065f46; }
.pill-gold   { background: #fef3c7; color: #92400e; }
.pill-red    { background: #fee2e2; color: #991b1b; }

/* ── Table ── */
.stDataFrame { border-radius: 12px; overflow: hidden; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(90deg, var(--sky), #1d4ed8);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.5rem 1.4rem;
    font-weight: 600;
    font-size: 0.9rem;
    transition: opacity 0.2s, transform 0.1s;
}
.stButton > button:hover { opacity: 0.88; transform: translateY(-1px); }

/* ── Login card ── */
.login-wrap {
    max-width: 400px; margin: 4rem auto;
    background: var(--card);
    border-radius: 20px;
    padding: 2.5rem 2.5rem;
    box-shadow: 0 8px 40px rgba(0,0,0,0.1);
    border-top: 5px solid var(--sky);
}
.login-wrap h2 {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem; font-weight: 900;
    color: var(--navy); margin-bottom: 0.3rem;
}
.login-sub { color: var(--muted); font-size: 0.9rem; margin-bottom: 1.5rem; }

/* ── Success / Error ── */
.success-box {
    background: #d1fae5; border-left: 4px solid var(--green);
    border-radius: 10px; padding: 0.9rem 1.2rem;
    color: #065f46; font-weight: 500; margin: 0.5rem 0;
}
.error-box {
    background: #fee2e2; border-left: 4px solid var(--red);
    border-radius: 10px; padding: 0.9rem 1.2rem;
    color: #991b1b; font-weight: 500; margin: 0.5rem 0;
}

/* ── Salary slip ── */
.slip {
    background: var(--card);
    border-radius: 16px;
    padding: 1.6rem 2rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    border: 1px solid var(--border);
}
.slip-row { display: flex; justify-content: space-between; padding: 0.45rem 0; border-bottom: 1px dashed var(--border); font-size: 0.92rem; }
.slip-row:last-child { border-bottom: none; }
.slip-total { font-weight: 700; font-size: 1.05rem; color: var(--green); }
</style>
""", unsafe_allow_html=True)

# ─── Session State Init ────────────────────────────────────────────────────────
for key, default in {
    "logged_in": False,
    "user_role": None,
    "doctors":      [],
    "patients":     [],
    "appointments": [],
    "bills":        [],
    "salaries":     [],
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ─── Credentials ──────────────────────────────────────────────────────────────
CREDENTIALS = {
    "admin":     ("admin",     "admin@234"),
    "doctor":    ("doctor",    "doctor@459"),
    "reception": ("reception", "recep@389"),
}

# ══════════════════════════════════════════════════════════════════════════════
# LOGIN PAGE
# ══════════════════════════════════════════════════════════════════════════════
def login_page():
    st.markdown("""
    <div style='text-align:center;margin-top:3rem;'>
      <div style='font-size:4rem;'>🏥</div>
      <h1 style='font-family:Playfair Display,serif;font-size:2rem;color:#0a1628;margin:0.3rem 0;'>AIIMS Hospital</h1>
      <p style='color:#64748b;'>Management System — Secure Login</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        role = st.selectbox("Login As", ["admin", "doctor", "reception"],
                            format_func=lambda x: {"admin":"🔐 Admin","doctor":"👨‍⚕️ Doctor","reception":"🗃️ Reception"}[x])
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login →", use_container_width=True):
            u, p = CREDENTIALS[role]
            if username == u and password == p:
                st.session_state.logged_in = True
                st.session_state.user_role = role
                st.rerun()
            else:
                st.markdown('<div class="error-box">❌ Invalid credentials. Try again.</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top:1.2rem;background:#f8fafc;border-radius:10px;padding:0.8rem 1rem;font-size:0.8rem;color:#64748b;'>
        <b>Demo Credentials</b><br>
        Admin → admin / admin@234<br>
        Doctor → doctor / doctor@459<br>
        Reception → reception / recep@389
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
def render_sidebar():
    role = st.session_state.user_role
    with st.sidebar:
        st.markdown(f"""
        <div style='text-align:center;padding:1.2rem 0 0.5rem;'>
          <div style='font-size:2.8rem;'>🏥</div>
          <div style='font-family:Playfair Display,serif;font-size:1.2rem;font-weight:900;color:#f1f5f9;'>AIIMS Hospital</div>
          <div style='font-size:0.75rem;color:#94a3b8;margin-top:0.2rem;'>Management System</div>
        </div>
        <hr style='border-color:rgba(255,255,255,0.1);margin:1rem 0;'>
        """, unsafe_allow_html=True)

        role_icons = {"admin": "🔐 Admin", "doctor": "👨‍⚕️ Doctor", "reception": "🗃️ Reception"}
        st.markdown(f"<div style='text-align:center;margin-bottom:1rem;'><span style='background:rgba(56,189,248,0.15);border:1px solid rgba(56,189,248,0.3);border-radius:20px;padding:0.3rem 1rem;font-size:0.82rem;color:#38bdf8;font-weight:600;'>{role_icons[role]}</span></div>", unsafe_allow_html=True)

        menus = {
            "admin": ["🏠 Dashboard", "👨‍⚕️ Doctors", "🧑‍🤝‍🧑 Patients", "📅 Appointments", "💰 Billing", "💵 Salary"],
            "doctor": ["🏠 Dashboard", "🧑‍🤝‍🧑 Patients", "📅 Appointments"],
            "reception": ["🏠 Dashboard", "🧑‍🤝‍🧑 Patients", "📅 Appointments", "💰 Billing"],
        }
        page = st.radio("Navigation", menus[role], label_visibility="collapsed")

        st.markdown("<hr style='border-color:rgba(255,255,255,0.1);margin:1rem 0;'>", unsafe_allow_html=True)
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.rerun()

    return page


# ══════════════════════════════════════════════════════════════════════════════
# BANNER
# ══════════════════════════════════════════════════════════════════════════════
def render_banner():
    st.markdown("""
    <div class="banner">
      <div class="banner-badge">⚕️ Premier Healthcare</div>
      <h1>AIIMS Hospital Management</h1>
      <p>New Delhi • Est. 1956 • jankalyan@aiims.edu • +91 89896 51456</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
def page_dashboard():
    render_banner()
    d = len(st.session_state.doctors)
    p = len(st.session_state.patients)
    a = len(st.session_state.appointments)
    b = len(st.session_state.bills)
    total_revenue = sum(x["total"] for x in st.session_state.bills)

    st.markdown(f"""
    <div class="stat-row">
      <div class="stat-card" style="border-color:#2563eb;">
        <div class="icon">👨‍⚕️</div>
        <div class="number">{d}</div>
        <div class="label">Doctors Registered</div>
      </div>
      <div class="stat-card" style="border-color:#10b981;">
        <div class="icon">🧑‍🤝‍🧑</div>
        <div class="number">{p}</div>
        <div class="label">Patients Admitted</div>
      </div>
      <div class="stat-card" style="border-color:#f59e0b;">
        <div class="icon">📅</div>
        <div class="number">{a}</div>
        <div class="label">Appointments</div>
      </div>
      <div class="stat-card" style="border-color:#8b5cf6;">
        <div class="icon">💰</div>
        <div class="number">₹{total_revenue:,}</div>
        <div class="label">Total Revenue</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Recent Doctors</div>', unsafe_allow_html=True)
        if st.session_state.doctors:
            for d in st.session_state.doctors[-3:][::-1]:
                st.markdown(f"""
                <div class="doc-card" style="width:100%;box-sizing:border-box;">
                  <div class="doc-avatar">👨‍⚕️</div>
                  <div class="doc-name">Dr. {d['name']}</div>
                  <div class="doc-spec">{d['spec']}</div>
                  <div class="doc-exp">🕐 {d['exp']} yrs experience</div>
                  <div class="doc-fee">Consultation: ₹{d['fee']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No doctors added yet.")

    with col2:
        st.markdown('<div class="section-title">Recent Patients</div>', unsafe_allow_html=True)
        if st.session_state.patients:
            import pandas as pd
            recent = st.session_state.patients[-5:][::-1]
            df = pd.DataFrame(recent)[["id", "name", "age", "disease", "room"]]
            df.columns = ["ID", "Name", "Age", "Disease", "Room"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No patients added yet.")


# ══════════════════════════════════════════════════════════════════════════════
# DOCTORS
# ══════════════════════════════════════════════════════════════════════════════
def page_doctors():
    st.markdown('<div class="section-title">👨‍⚕️ Doctor Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["➕ Add Doctor", "📋 All Doctors", "🔍 Search"])

    with tab1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Doctor Name")
            spec = st.text_input("Specialization")
        with c2:
            exp  = st.number_input("Experience (years)", min_value=0, max_value=60, value=5)
            fee  = st.number_input("Consultation Fee (₹)", min_value=0, value=500)
        if st.button("➕ Add Doctor"):
            if name and spec:
                doc_id = len(st.session_state.doctors) + 1
                st.session_state.doctors.append({"id": doc_id, "name": name, "spec": spec, "exp": exp, "fee": fee})
                st.markdown('<div class="success-box">✅ Doctor added successfully!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ Please fill all fields.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.doctors:
            st.info("No doctors registered yet.")
        else:
            st.markdown('<div class="doc-grid">', unsafe_allow_html=True)
            cols = st.columns(4)
            for i, d in enumerate(st.session_state.doctors):
                with cols[i % 4]:
                    st.markdown(f"""
                    <div class="doc-card">
                      <div class="doc-avatar">👨‍⚕️</div>
                      <div class="doc-name">Dr. {d['name']}</div>
                      <div class="doc-spec">{d['spec']}</div>
                      <div class="doc-exp">🕐 {d['exp']} yrs exp &nbsp;|&nbsp; ID: #{d['id']}</div>
                      <div class="doc-fee">₹{d['fee']} / visit</div>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-title" style="font-size:1rem;">Delete a Doctor</div>', unsafe_allow_html=True)
            del_id = st.number_input("Enter Doctor ID to delete", min_value=1, step=1)
            if st.button("🗑️ Delete Doctor"):
                before = len(st.session_state.doctors)
                st.session_state.doctors = [d for d in st.session_state.doctors if d["id"] != del_id]
                if len(st.session_state.doctors) < before:
                    st.markdown('<div class="success-box">✅ Doctor deleted.</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="error-box">❌ Doctor ID not found.</div>', unsafe_allow_html=True)

    with tab3:
        query = st.text_input("Search by name")
        if query:
            results = [d for d in st.session_state.doctors if query.lower() in d["name"].lower()]
            if results:
                cols = st.columns(min(len(results), 4))
                for i, d in enumerate(results):
                    with cols[i % 4]:
                        st.markdown(f"""
                        <div class="doc-card">
                          <div class="doc-avatar">👨‍⚕️</div>
                          <div class="doc-name">Dr. {d['name']}</div>
                          <div class="doc-spec">{d['spec']}</div>
                          <div class="doc-exp">{d['exp']} yrs · ID #{d['id']}</div>
                          <div class="doc-fee">₹{d['fee']}</div>
                        </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ No doctor found.</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PATIENTS
# ══════════════════════════════════════════════════════════════════════════════
def page_patients():
    import pandas as pd
    st.markdown('<div class="section-title">🧑‍🤝‍🧑 Patient Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["➕ Add Patient", "📋 All Patients", "🔍 Search"])

    with tab1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name    = st.text_input("Patient Name")
            age     = st.number_input("Age", min_value=0, max_value=120, value=30)
        with c2:
            disease = st.text_input("Disease / Diagnosis")
            room    = st.text_input("Room Number")
        if st.button("➕ Add Patient"):
            if name and disease and room:
                pat_id = len(st.session_state.patients) + 1
                st.session_state.patients.append({"id": pat_id, "name": name, "age": age, "disease": disease, "room": room})
                st.markdown('<div class="success-box">✅ Patient added!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ Fill all fields.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.patients:
            st.info("No patients yet.")
        else:
            df = pd.DataFrame(st.session_state.patients)
            df.columns = ["ID", "Name", "Age", "Disease", "Room"]
            st.dataframe(df, use_container_width=True, hide_index=True)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            name_q = st.text_input("Search by Name")
        with col2:
            id_q = st.number_input("Search by ID", min_value=0, step=1, value=0)

        results = []
        if name_q:
            results = [p for p in st.session_state.patients if name_q.lower() in p["name"].lower()]
        elif id_q > 0:
            results = [p for p in st.session_state.patients if p["id"] == id_q]

        if name_q or id_q > 0:
            if results:
                df = pd.DataFrame(results)
                df.columns = ["ID", "Name", "Age", "Disease", "Room"]
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.markdown('<div class="error-box">❌ No patient found.</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# APPOINTMENTS
# ══════════════════════════════════════════════════════════════════════════════
def page_appointments():
    import pandas as pd
    st.markdown('<div class="section-title">📅 Appointment Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["➕ Book", "📋 All", "🔍 Search by Date"])

    with tab1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            doc  = st.text_input("Doctor Name")
            pat  = st.text_input("Patient Name")
        with c2:
            date = st.date_input("Date")
            time = st.time_input("Time")
        if st.button("📅 Book Appointment"):
            if doc and pat:
                appt_id = len(st.session_state.appointments) + 1
                st.session_state.appointments.append({
                    "id": appt_id, "doctor": doc, "patient": pat,
                    "date": str(date), "time": str(time)
                })
                st.markdown('<div class="success-box">✅ Appointment booked!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ Fill doctor and patient names.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.appointments:
            st.info("No appointments yet.")
        else:
            df = pd.DataFrame(st.session_state.appointments)
            df.columns = ["ID", "Doctor", "Patient", "Date", "Time"]
            st.dataframe(df, use_container_width=True, hide_index=True)

    with tab3:
        search_date = st.date_input("Select Date")
        results = [a for a in st.session_state.appointments if a["date"] == str(search_date)]
        if results:
            df = pd.DataFrame(results)
            df.columns = ["ID", "Doctor", "Patient", "Date", "Time"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No appointments on this date.")


# ══════════════════════════════════════════════════════════════════════════════
# BILLING
# ══════════════════════════════════════════════════════════════════════════════
def page_billing():
    import pandas as pd
    st.markdown('<div class="section-title">💰 Billing Management</div>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["➕ Generate Bill", "📋 All Bills"])

    with tab1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        name    = st.text_input("Patient Name")
        c1, c2, c3 = st.columns(3)
        with c1: doc_fee = st.number_input("Doctor Fee (₹)", min_value=0, value=500)
        with c2: room_ch = st.number_input("Room Charges (₹)", min_value=0, value=1000)
        with c3: med_ch  = st.number_input("Medicine Charges (₹)", min_value=0, value=300)

        total = doc_fee + room_ch + med_ch
        st.markdown(f"""
        <div style='background:#f0fdf4;border-radius:10px;padding:0.8rem 1.2rem;margin:0.5rem 0;'>
          <span style='color:#065f46;font-weight:600;'>Estimated Total: ₹{total:,}</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧾 Generate Bill"):
            if name:
                bill_id = len(st.session_state.bills) + 1
                st.session_state.bills.append({
                    "id": bill_id, "patient": name,
                    "doc_fee": doc_fee, "room": room_ch,
                    "medicine": med_ch, "total": total
                })
                st.markdown('<div class="success-box">✅ Bill generated!</div>', unsafe_allow_html=True)

                st.markdown(f"""
                <div class="slip">
                  <div style='font-family:Playfair Display,serif;font-size:1.1rem;font-weight:700;color:#0a1628;margin-bottom:1rem;'>🧾 Bill Receipt — #{bill_id}</div>
                  <div class="slip-row"><span>Patient Name</span><span>{name}</span></div>
                  <div class="slip-row"><span>Doctor Fee</span><span>₹{doc_fee:,}</span></div>
                  <div class="slip-row"><span>Room Charges</span><span>₹{room_ch:,}</span></div>
                  <div class="slip-row"><span>Medicine Charges</span><span>₹{med_ch:,}</span></div>
                  <div class="slip-row slip-total"><span>NET TOTAL</span><span>₹{total:,}</span></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ Enter patient name.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.bills:
            st.info("No bills generated yet.")
        else:
            df = pd.DataFrame(st.session_state.bills)
            df.columns = ["ID", "Patient", "Doctor Fee", "Room", "Medicine", "Total"]
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.markdown(f"**Total Revenue: ₹{sum(b['total'] for b in st.session_state.bills):,}**")


# ══════════════════════════════════════════════════════════════════════════════
# SALARY
# ══════════════════════════════════════════════════════════════════════════════
def page_salary():
    import pandas as pd
    st.markdown('<div class="section-title">💵 Salary Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["➕ Add Salary", "📋 All Records", "🧮 Calculator"])

    with tab1:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            name     = st.text_input("Employee Name")
            emp_type = st.selectbox("Type", ["Doctor", "Nurse", "Staff"])
        with c2:
            month    = st.selectbox("Month", ["January","February","March","April","May","June",
                                               "July","August","September","October","November","December"])
            year     = st.number_input("Year", min_value=2020, max_value=2030, value=2025)

        basic = st.number_input("Basic Salary (₹)", min_value=0, value=30000)
        c1, c2, c3 = st.columns(3)
        with c1: hra = st.number_input("HRA %", min_value=0.0, max_value=50.0, value=10.0)
        with c2: da  = st.number_input("DA %",  min_value=0.0, max_value=50.0, value=5.0)
        with c3: pf  = st.number_input("PF %",  min_value=0.0, max_value=20.0, value=12.0)

        hra_amt = (hra / 100) * basic
        da_amt  = (da  / 100) * basic
        pf_amt  = (pf  / 100) * basic
        gross   = basic + hra_amt + da_amt
        net     = gross - pf_amt

        if st.button("💾 Save Salary Record"):
            if name:
                sal_id = len(st.session_state.salaries) + 1
                st.session_state.salaries.append({
                    "id": sal_id, "name": name, "type": emp_type,
                    "month": month, "year": year,
                    "basic": basic, "hra": hra_amt, "da": da_amt,
                    "pf": pf_amt, "gross": gross, "net": net
                })
                st.markdown(f"""
                <div class="slip">
                  <div style='font-family:Playfair Display,serif;font-size:1.1rem;font-weight:700;color:#0a1628;margin-bottom:1rem;'>💵 Salary Slip — {name} · {month} {year}</div>
                  <div class="slip-row"><span>Employee Type</span><span><span class="pill pill-blue">{emp_type}</span></span></div>
                  <div class="slip-row"><span>Basic Salary</span><span>₹{basic:,.0f}</span></div>
                  <div class="slip-row"><span>HRA ({hra}%)</span><span>₹{hra_amt:,.2f}</span></div>
                  <div class="slip-row"><span>DA  ({da}%)</span><span>₹{da_amt:,.2f}</span></div>
                  <div class="slip-row"><span>Gross Salary</span><span>₹{gross:,.2f}</span></div>
                  <div class="slip-row" style="color:#ef4444;"><span>PF Deduction ({pf}%)</span><span>- ₹{pf_amt:,.2f}</span></div>
                  <div class="slip-row slip-total"><span>NET SALARY</span><span>₹{net:,.2f}</span></div>
                </div>
                <div class="success-box" style="margin-top:0.8rem;">✅ Salary record saved!</div>
                """, unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">❌ Enter employee name.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.salaries:
            st.info("No salary records yet.")
        else:
            df = pd.DataFrame(st.session_state.salaries)
            df = df[["id","name","type","month","year","basic","gross","net"]]
            df.columns = ["ID","Name","Type","Month","Year","Basic","Gross","Net Salary"]
            st.dataframe(df, use_container_width=True, hide_index=True)

            if st.session_state.salaries:
                st.markdown(f"**Total Salary Disbursed: ₹{sum(s['net'] for s in st.session_state.salaries):,.2f}**")

    with tab3:
        st.markdown("**Quick Monthly Salary Calculator**")
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        basic = st.number_input("Basic Salary", min_value=0, value=30000, key="calc_basic")
        c1, c2, c3 = st.columns(3)
        with c1: hra = st.number_input("HRA %", value=10.0, key="calc_hra")
        with c2: da  = st.number_input("DA %",  value=5.0,  key="calc_da")
        with c3: pf  = st.number_input("PF %",  value=12.0, key="calc_pf")

        hra_a = (hra / 100) * basic
        da_a  = (da  / 100) * basic
        pf_a  = (pf  / 100) * basic
        gross = basic + hra_a + da_a
        net   = gross - pf_a

        st.markdown(f"""
        <div class="slip" style="margin-top:0.8rem;">
          <div class="slip-row"><span>Basic Salary</span><span>₹{basic:,}</span></div>
          <div class="slip-row"><span>HRA</span><span>₹{hra_a:,.2f}</span></div>
          <div class="slip-row"><span>DA</span><span>₹{da_a:,.2f}</span></div>
          <div class="slip-row"><span>Gross</span><span>₹{gross:,.2f}</span></div>
          <div class="slip-row" style="color:#ef4444;"><span>PF Deduction</span><span>- ₹{pf_a:,.2f}</span></div>
          <div class="slip-row slip-total"><span>NET SALARY</span><span>₹{net:,.2f}</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ROUTER
# ══════════════════════════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    login_page()
else:
    page = render_sidebar()
    page_key = page.split(" ", 1)[1].lower().strip()

    if page_key == "dashboard":
        page_dashboard()
    elif page_key == "doctors":
        page_doctors()
    elif page_key == "patients":
        page_patients()
    elif page_key == "appointments":
        page_appointments()
    elif page_key == "billing":
        page_billing()
    elif page_key == "salary":
        page_salary()
