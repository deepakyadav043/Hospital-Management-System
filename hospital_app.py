import streamlit as st

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Sora:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* ── Main Background ── */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    color: #e2e8f0;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e3a5f 0%, #0f2744 100%);
    border-right: 1px solid rgba(99,179,237,0.15);
}
section[data-testid="stSidebar"] * { color: #cbd5e1 !important; }
section[data-testid="stSidebar"] .stRadio label { font-weight: 500; }

/* ── Cards ── */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(99,179,237,0.18);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
    backdrop-filter: blur(8px);
}
.card h4 { color: #63b3ed; margin: 0 0 8px; font-family: 'Sora', sans-serif; }
.card p  { margin: 4px 0; font-size: 14px; color: #94a3b8; }
.card p span { color: #e2e8f0; font-weight: 500; }

/* ── Section headings ── */
.section-title {
    font-family: 'Sora', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #63b3ed;
    margin-bottom: 4px;
    letter-spacing: -0.5px;
}
.section-sub { color: #64748b; font-size: 13px; margin-bottom: 20px; }

/* ── Login card ── */
.login-wrapper {
    max-width: 440px;
    margin: 60px auto 0;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 24px;
    padding: 48px 40px;
    backdrop-filter: blur(12px);
}
.login-title {
    font-family: 'Sora', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #63b3ed;
    text-align: center;
    margin-bottom: 4px;
}
.login-sub { text-align: center; color: #64748b; font-size: 13px; margin-bottom: 32px; }

/* ── Metric boxes ── */
.metric-box {
    background: rgba(99,179,237,0.08);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.metric-box .num { font-size: 36px; font-weight: 700; color: #63b3ed; }
.metric-box .lbl { font-size: 12px; color: #64748b; margin-top: 4px; }

/* ── Inputs ── */
.stTextInput>div>div>input,
.stNumberInput>div>div>input,
.stSelectbox>div>div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(99,179,237,0.25) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

/* ── Buttons ── */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    font-weight: 600 !important;
    width: 100%;
    transition: opacity .2s;
}
.stButton>button:hover { opacity: 0.88; }

/* ── Danger button ── */
.danger > .stButton > button {
    background: linear-gradient(135deg, #dc2626, #b91c1c) !important;
}

/* ── Divider ── */
hr { border-color: rgba(99,179,237,0.12) !important; }

/* ── Success / error msgs ── */
.stAlert { border-radius: 10px !important; }

/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# IN-MEMORY DATA STORES
# ─────────────────────────────────────────────
if "doctor_list"      not in st.session_state: st.session_state.doctor_list      = []
if "patient_list"     not in st.session_state: st.session_state.patient_list     = []
if "appointment_list" not in st.session_state: st.session_state.appointment_list = []
if "bill_list"        not in st.session_state: st.session_state.bill_list        = []
if "salary_list"      not in st.session_state: st.session_state.salary_list      = []
if "user_role"        not in st.session_state: st.session_state.user_role        = None

HOSPITAL = {
    "name":    "JAN KALYAN HOSPITAL",
    "location": "BIHAR",
    "email":   "jankalyan@gmail.com",
    "contact": "8989651456",
}

# ─────────────────────────────────────────────
# CREDENTIALS
# ─────────────────────────────────────────────
CREDENTIALS = {
    "admin":     ("admin",     "admin@234"),
    "doctor":    ("doctor",    "doctor@459"),
    "reception": ("reception", "recep@389"),
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def doctor_card(d):
    st.markdown(f"""
    <div class="card">
        <h4>👨‍⚕️ Dr. {d['name']}  <small style="color:#94a3b8;font-size:13px;">ID #{d['id']}</small></h4>
        <p>🩺 Specialization: <span>{d['specialization']}</span></p>
        <p>📅 Experience: <span>{d['experience']} years</span></p>
        <p>💰 Fee: <span>₹{d['fee']}</span></p>
    </div>""", unsafe_allow_html=True)

def patient_card(p):
    st.markdown(f"""
    <div class="card">
        <h4>🧑 {p['name']}  <small style="color:#94a3b8;font-size:13px;">ID #{p['id']}</small></h4>
        <p>🎂 Age: <span>{p['age']}</span></p>
        <p>🦠 Disease: <span>{p['disease']}</span></p>
        <p>🛏️ Room: <span>{p['room']}</span></p>
    </div>""", unsafe_allow_html=True)

def appointment_card(a):
    st.markdown(f"""
    <div class="card">
        <h4>📋 Appointment #{a['id']}</h4>
        <p>👨‍⚕️ Doctor: <span>{a['doctor']}</span></p>
        <p>🧑 Patient: <span>{a['patient']}</span></p>
        <p>📅 Date: <span>{a['date']}</span> &nbsp; ⏰ Time: <span>{a['time']}</span></p>
    </div>""", unsafe_allow_html=True)

def bill_card(b):
    st.markdown(f"""
    <div class="card">
        <h4>🧾 Bill #{b['id']} — {b['patient']}</h4>
        <p>Doctor Fee: <span>₹{b['doc_fee']}</span></p>
        <p>Room Charges: <span>₹{b['room']}</span></p>
        <p>Medicine Charges: <span>₹{b['med']}</span></p>
        <p style="font-size:16px;color:#63b3ed;font-weight:700;">Total: ₹{b['total']}</p>
    </div>""", unsafe_allow_html=True)

def salary_card(s):
    st.markdown(f"""
    <div class="card">
        <h4>💼 {s['name']}  <small style="color:#94a3b8;font-size:13px;">{s['type']} — {s['month']}/{s['year']}</small></h4>
        <p>Basic: <span>₹{s['basic']}</span> &nbsp; HRA ({s['hra']}%): <span>₹{s['hra_amt']:.0f}</span> &nbsp; DA ({s['da']}%): <span>₹{s['da_amt']:.0f}</span></p>
        <p>Gross: <span>₹{s['gross']:.0f}</span> &nbsp; PF ({s['pf']}%): <span>₹{s['pf_amt']:.0f}</span></p>
        <p style="font-size:16px;color:#63b3ed;font-weight:700;">Net Salary: ₹{s['net']:.0f}</p>
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LOGIN PAGE
# ─────────────────────────────────────────────
def login_page():
    st.markdown("""
    <div style="text-align:center;padding-top:30px;">
        <span style="font-size:56px;">🏥</span>
        <div style="font-family:'Sora',sans-serif;font-size:34px;font-weight:700;
                    color:#63b3ed;margin-top:8px;">Jan Kalyan Hospital</div>
        <div style="color:#475569;font-size:14px;margin-top:4px;">Management System — Secure Login</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

        role = st.selectbox("🔑 Login As", ["Admin", "Doctor", "Reception"])
        username = st.text_input("👤 Username", placeholder="Enter username")
        password = st.text_input("🔒 Password", placeholder="Enter password", type="password")

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Login →", use_container_width=True):
            role_key = role.lower()
            expected_user, expected_pass = CREDENTIALS[role_key]
            if username == expected_user and password == expected_pass:
                st.session_state.user_role = role_key
                st.success(f"✅ Welcome, {role}!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Please try again.")

        st.markdown("""
        <div style="margin-top:20px;padding:14px;background:rgba(99,179,237,0.06);
                    border-radius:10px;font-size:12px;color:#64748b;text-align:center;">
            Demo credentials are available from the administrator.
        </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR NAV
# ─────────────────────────────────────────────
def sidebar_nav():
    role = st.session_state.user_role
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:16px 0 24px;">
            <div style="font-family:'Sora',sans-serif;font-size:18px;font-weight:700;
                        color:#63b3ed;">🏥 Jan Kalyan</div>
            <div style="font-size:12px;color:#475569;margin-top:2px;">Hospital Management</div>
        </div>
        <hr style="margin-bottom:16px;">
        <div style="font-size:11px;color:#475569;font-weight:600;letter-spacing:1px;
                    margin-bottom:10px;">LOGGED IN AS</div>
        <div style="background:rgba(99,179,237,0.12);border-radius:10px;
                    padding:10px 14px;margin-bottom:24px;color:#63b3ed;font-weight:600;">
            {'👑 Admin' if role=='admin' else ('👨‍⚕️ Doctor' if role=='doctor' else '🏢 Reception')}
        </div>
        """, unsafe_allow_html=True)

        if role == "admin":
            menu_items = [
                "🏠 Dashboard", "➕ Add Doctor", "📋 View Doctors", "🔍 Search Doctor",
                "➕ Add Patient", "📋 View Patients", "🔍 Search Patient",
                "📅 Book Appointment", "📋 View Appointments", "🔍 Search Appointment",
                "🧾 Generate Bill", "📋 View Bills",
                "💼 Add Salary", "📋 View Salaries", "🔍 Search Salary",
                "🧮 Salary Calculator", "🗑️ Delete Doctor", "🗑️ Delete Salary",
            ]
        elif role == "doctor":
            menu_items = ["🏠 Dashboard", "📋 View Patients", "🔍 Search Patient", "📅 View Appointments"]
        else:
            menu_items = ["🏠 Dashboard", "➕ Add Patient", "📋 View Patients", "📅 Book Appointment", "🧾 Generate Bill"]

        choice = st.radio("Navigation", menu_items, label_visibility="collapsed")

        st.markdown("<hr>", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.user_role = None
            st.rerun()

    return choice

# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
def dashboard():
    st.markdown('<div class="section-title">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-sub">{HOSPITAL["name"]} · {HOSPITAL["location"]}</div>', unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, num, lbl in [
        (c1, len(st.session_state.doctor_list),      "Doctors"),
        (c2, len(st.session_state.patient_list),     "Patients"),
        (c3, len(st.session_state.appointment_list), "Appointments"),
        (c4, len(st.session_state.bill_list),        "Bills"),
        (c5, len(st.session_state.salary_list),      "Salary Records"),
    ]:
        with col:
            st.markdown(f'<div class="metric-box"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <h4>🏥 Hospital Info</h4>
        <p>📍 Location: <span>{HOSPITAL['location']}</span></p>
        <p>📧 Email: <span>{HOSPITAL['email']}</span></p>
        <p>📞 Contact: <span>{HOSPITAL['contact']}</span></p>
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DOCTOR PAGES
# ─────────────────────────────────────────────
def add_doctor():
    st.markdown('<div class="section-title">➕ Add Doctor</div>', unsafe_allow_html=True)
    with st.form("add_doc"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Doctor Name")
        spec = c2.text_input("Specialization")
        exp  = c1.number_input("Experience (years)", min_value=0, step=1)
        fee  = c2.number_input("Consultation Fee (₹)", min_value=0, step=100)
        if st.form_submit_button("Add Doctor ✅"):
            if name and spec:
                doc_id = len(st.session_state.doctor_list) + 1
                st.session_state.doctor_list.append({"id": doc_id, "name": name, "specialization": spec, "experience": exp, "fee": fee})
                st.success(f"Dr. {name} added successfully!")
            else:
                st.warning("Please fill in all fields.")

def view_doctors():
    st.markdown('<div class="section-title">📋 All Doctors</div>', unsafe_allow_html=True)
    dl = st.session_state.doctor_list
    if not dl:
        st.info("No doctors registered yet.")
        return
    for d in dl:
        doctor_card(d)

def search_doctor():
    st.markdown('<div class="section-title">🔍 Search Doctor</div>', unsafe_allow_html=True)
    query = st.text_input("Enter doctor name to search")
    if query:
        results = [d for d in st.session_state.doctor_list if query.lower() in d["name"].lower()]
        if results:
            for d in results: doctor_card(d)
        else:
            st.warning("No doctor found with that name.")

def delete_doctor():
    st.markdown('<div class="section-title">🗑️ Delete Doctor</div>', unsafe_allow_html=True)
    dl = st.session_state.doctor_list
    if not dl:
        st.info("No doctors to delete.")
        return
    options = {f"#{d['id']} — Dr. {d['name']}": d['id'] for d in dl}
    sel = st.selectbox("Select Doctor to Delete", list(options.keys()))
    st.markdown('<div class="danger">', unsafe_allow_html=True)
    if st.button("Delete Doctor 🗑️"):
        doc_id = options[sel]
        st.session_state.doctor_list = [d for d in dl if d["id"] != doc_id]
        st.success("Doctor deleted.")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PATIENT PAGES
# ─────────────────────────────────────────────
def add_patient():
    st.markdown('<div class="section-title">➕ Add Patient</div>', unsafe_allow_html=True)
    with st.form("add_pat"):
        c1, c2 = st.columns(2)
        name    = c1.text_input("Patient Name")
        age     = c2.number_input("Age", min_value=0, step=1)
        disease = c1.text_input("Disease / Condition")
        room    = c2.text_input("Room Number")
        if st.form_submit_button("Add Patient ✅"):
            if name and disease:
                pat_id = len(st.session_state.patient_list) + 1
                st.session_state.patient_list.append({"id": pat_id, "name": name, "age": age, "disease": disease, "room": room})
                st.success(f"Patient {name} added!")
            else:
                st.warning("Please fill in all fields.")

def view_patients():
    st.markdown('<div class="section-title">📋 All Patients</div>', unsafe_allow_html=True)
    pl = st.session_state.patient_list
    if not pl:
        st.info("No patients registered yet.")
        return
    for p in pl: patient_card(p)

def search_patient():
    st.markdown('<div class="section-title">🔍 Search Patient</div>', unsafe_allow_html=True)
    method = st.radio("Search by", ["Name", "ID"], horizontal=True)
    if method == "Name":
        query = st.text_input("Patient Name")
        if query:
            results = [p for p in st.session_state.patient_list if query.lower() in p["name"].lower()]
            if results:
                for p in results: patient_card(p)
            else:
                st.warning("Patient not found.")
    else:
        pid = st.number_input("Patient ID", min_value=1, step=1)
        if st.button("Search"):
            results = [p for p in st.session_state.patient_list if p["id"] == pid]
            if results:
                patient_card(results[0])
            else:
                st.warning("Patient not found.")

# ─────────────────────────────────────────────
# APPOINTMENT PAGES
# ─────────────────────────────────────────────
def book_appointment():
    st.markdown('<div class="section-title">📅 Book Appointment</div>', unsafe_allow_html=True)
    with st.form("book_appt"):
        c1, c2 = st.columns(2)
        doc  = c1.text_input("Doctor Name")
        pat  = c2.text_input("Patient Name")
        date = c1.date_input("Date")
        time = c2.text_input("Time (e.g. 10:00 AM)")
        if st.form_submit_button("Book Appointment ✅"):
            if doc and pat and time:
                appt_id = len(st.session_state.appointment_list) + 1
                st.session_state.appointment_list.append({"id": appt_id, "doctor": doc, "patient": pat, "date": str(date), "time": time})
                st.success("Appointment booked!")
            else:
                st.warning("Please fill in all fields.")

def view_appointments():
    st.markdown('<div class="section-title">📋 All Appointments</div>', unsafe_allow_html=True)
    al = st.session_state.appointment_list
    if not al:
        st.info("No appointments booked yet.")
        return
    for a in al: appointment_card(a)

def search_appointment():
    st.markdown('<div class="section-title">🔍 Search Appointment</div>', unsafe_allow_html=True)
    date = st.date_input("Select Date")
    if st.button("Search"):
        results = [a for a in st.session_state.appointment_list if a["date"] == str(date)]
        if results:
            for a in results: appointment_card(a)
        else:
            st.warning("No appointments on this date.")

# ─────────────────────────────────────────────
# BILL PAGES
# ─────────────────────────────────────────────
def generate_bill():
    st.markdown('<div class="section-title">🧾 Generate Bill</div>', unsafe_allow_html=True)
    with st.form("gen_bill"):
        name    = st.text_input("Patient Name")
        c1, c2, c3 = st.columns(3)
        doc_fee = c1.number_input("Doctor Fee (₹)", min_value=0, step=100)
        room_ch = c2.number_input("Room Charges (₹)", min_value=0, step=100)
        med_ch  = c3.number_input("Medicine Charges (₹)", min_value=0, step=100)
        if st.form_submit_button("Generate Bill 🧾"):
            if name:
                total   = doc_fee + room_ch + med_ch
                bill_id = len(st.session_state.bill_list) + 1
                b = {"id": bill_id, "patient": name, "doc_fee": doc_fee, "room": room_ch, "med": med_ch, "total": total}
                st.session_state.bill_list.append(b)
                bill_card(b)
                st.success("Bill generated!")
            else:
                st.warning("Please enter patient name.")

def view_bills():
    st.markdown('<div class="section-title">📋 All Bills</div>', unsafe_allow_html=True)
    bl = st.session_state.bill_list
    if not bl:
        st.info("No bills generated yet.")
        return
    for b in bl: bill_card(b)

# ─────────────────────────────────────────────
# SALARY PAGES
# ─────────────────────────────────────────────
def add_salary():
    st.markdown('<div class="section-title">💼 Add Salary Record</div>', unsafe_allow_html=True)
    with st.form("add_sal"):
        c1, c2 = st.columns(2)
        name     = c1.text_input("Employee Name")
        emp_type = c2.selectbox("Employee Type", ["Doctor", "Nurse", "Staff"])
        basic    = c1.number_input("Basic Salary (₹)", min_value=0, step=1000)
        hra      = c2.number_input("HRA %", min_value=0.0, max_value=100.0, step=0.5)
        da       = c1.number_input("DA %",  min_value=0.0, max_value=100.0, step=0.5)
        pf       = c2.number_input("PF %",  min_value=0.0, max_value=100.0, step=0.5)
        month    = c1.text_input("Month (e.g. June)")
        year     = c2.text_input("Year (e.g. 2025)")
        if st.form_submit_button("Add Salary Record ✅"):
            if name and month and year:
                hra_amt = (hra / 100) * basic
                da_amt  = (da  / 100) * basic
                pf_amt  = (pf  / 100) * basic
                gross   = basic + hra_amt + da_amt
                net     = gross - pf_amt
                sal_id  = len(st.session_state.salary_list) + 1
                s = {"id": sal_id, "name": name, "type": emp_type, "basic": basic,
                     "hra": hra, "da": da, "pf": pf, "hra_amt": hra_amt,
                     "da_amt": da_amt, "pf_amt": pf_amt, "gross": gross,
                     "net": net, "month": month, "year": year}
                st.session_state.salary_list.append(s)
                salary_card(s)
                st.success("Salary record added!")
            else:
                st.warning("Please fill in all fields.")

def view_salaries():
    st.markdown('<div class="section-title">📋 All Salary Records</div>', unsafe_allow_html=True)
    sl = st.session_state.salary_list
    if not sl:
        st.info("No salary records found.")
        return
    for s in sl: salary_card(s)

def search_salary():
    st.markdown('<div class="section-title">🔍 Search Salary</div>', unsafe_allow_html=True)
    query = st.text_input("Enter employee name")
    if query:
        results = [s for s in st.session_state.salary_list if query.lower() in s["name"].lower()]
        if results:
            for s in results: salary_card(s)
        else:
            st.warning("No salary record found.")

def salary_calculator():
    st.markdown('<div class="section-title">🧮 Salary Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Quick calculator — doesn\'t save records</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    basic = c1.number_input("Basic Salary (₹)", min_value=0, step=1000)
    hra   = c2.number_input("HRA %", min_value=0.0, max_value=100.0, step=0.5)
    da    = c1.number_input("DA %",  min_value=0.0, max_value=100.0, step=0.5)
    pf    = c2.number_input("PF %",  min_value=0.0, max_value=100.0, step=0.5)

    if st.button("Calculate 🧮"):
        hra_amt = (hra / 100) * basic
        da_amt  = (da  / 100) * basic
        pf_amt  = (pf  / 100) * basic
        gross   = basic + hra_amt + da_amt
        net     = gross - pf_amt
        st.markdown(f"""
        <div class="card">
            <h4>💼 Salary Breakdown</h4>
            <p>Basic Salary: <span>₹{basic:,}</span></p>
            <p>HRA ({hra}%): <span>₹{hra_amt:,.2f}</span></p>
            <p>DA  ({da}%):  <span>₹{da_amt:,.2f}</span></p>
            <p>Gross Salary: <span>₹{gross:,.2f}</span></p>
            <p>PF  ({pf}%):  <span>₹{pf_amt:,.2f}</span></p>
            <p style="font-size:18px;color:#63b3ed;font-weight:700;">Net Salary: ₹{net:,.2f}</p>
        </div>""", unsafe_allow_html=True)

def delete_salary():
    st.markdown('<div class="section-title">🗑️ Delete Salary Record</div>', unsafe_allow_html=True)
    sl = st.session_state.salary_list
    if not sl:
        st.info("No salary records to delete.")
        return
    options = {f"#{s['id']} — {s['name']} ({s['month']}/{s['year']})": s['id'] for s in sl}
    sel = st.selectbox("Select record to delete", list(options.keys()))
    st.markdown('<div class="danger">', unsafe_allow_html=True)
    if st.button("Delete Record 🗑️"):
        sal_id = options[sel]
        st.session_state.salary_list = [s for s in sl if s["id"] != sal_id]
        st.success("Salary record deleted.")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────
def route(page):
    dispatch = {
        "🏠 Dashboard":           dashboard,
        "➕ Add Doctor":           add_doctor,
        "📋 View Doctors":         view_doctors,
        "🔍 Search Doctor":        search_doctor,
        "➕ Add Patient":          add_patient,
        "📋 View Patients":        view_patients,
        "🔍 Search Patient":       search_patient,
        "📅 Book Appointment":     book_appointment,
        "📋 View Appointments":    view_appointments,
        "🔍 Search Appointment":   search_appointment,
        "🧾 Generate Bill":        generate_bill,
        "📋 View Bills":           view_bills,
        "💼 Add Salary":           add_salary,
        "📋 View Salaries":        view_salaries,
        "🔍 Search Salary":        search_salary,
        "🧮 Salary Calculator":    salary_calculator,
        "🗑️ Delete Doctor":        delete_doctor,
        "🗑️ Delete Salary":        delete_salary,
        "📅 View Appointments":    view_appointments,
    }
    fn = dispatch.get(page)
    if fn:
        fn()

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if st.session_state.user_role is None:
    login_page()
else:
    page = sidebar_nav()
    route(page)
