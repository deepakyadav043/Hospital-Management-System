import streamlit as st

st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide"
)

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Domine:wght@700&display=swap');

* { font-family: 'Plus Jakarta Sans', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #f5f7fb; }

/* Banner */
.banner {
    background: linear-gradient(120deg, #0d4a6b 0%, #1a7a9a 50%, #0d9488 100%);
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    box-shadow: 0 8px 32px rgba(13,74,107,0.25);
}
.banner-icon {
    font-size: 3.5rem;
    background: rgba(255,255,255,0.15);
    border-radius: 16px;
    padding: 0.5rem 0.8rem;
}
.banner h1 {
    font-family: 'Domine', serif;
    color: white;
    font-size: 2rem;
    margin: 0 0 0.2rem 0;
}
.banner p { color: #a7f3f0; margin: 0; font-size: 0.9rem; }
.banner-stats {
    margin-left: auto;
    display: flex;
    gap: 1rem;
}
.stat-pill {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    text-align: center;
    color: white;
}
.stat-pill b { display: block; font-size: 1.4rem; font-weight: 800; }
.stat-pill span { font-size: 0.75rem; opacity: 0.8; }

/* Sidebar nav */
.nav-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    cursor: pointer;
    margin-bottom: 0.3rem;
    font-weight: 600;
    font-size: 0.9rem;
    color: #4b5563;
    transition: all 0.2s;
}
.nav-item:hover { background: #e0f2fe; color: #0d4a6b; }
.nav-active { background: #0d4a6b !important; color: white !important; }

/* Cards */
.card {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
}
.card-title {
    font-family: 'Domine', serif;
    font-size: 1rem;
    color: #0d4a6b;
    font-weight: 700;
    margin-bottom: 1.2rem;
    padding-bottom: 0.6rem;
    border-bottom: 2px solid #e0f2fe;
}

/* Inputs */
label { color: #374151 !important; font-weight: 600 !important; font-size: 0.85rem !important; }
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div,
.stTextArea textarea {
    border: 1.5px solid #d1d5db !important;
    border-radius: 10px !important;
    background: #f9fafb !important;
    color: #111827 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #0d4a6b !important;
    box-shadow: 0 0 0 3px rgba(13,74,107,0.1) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0d4a6b, #0d9488) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    width: 100% !important;
    padding: 0.65rem !important;
    box-shadow: 0 4px 14px rgba(13,74,107,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(13,74,107,0.4) !important;
}

/* Table */
.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}
.data-table th {
    background: #0d4a6b;
    color: white;
    padding: 0.7rem 1rem;
    text-align: left;
    font-weight: 600;
}
.data-table th:first-child { border-radius: 10px 0 0 10px; }
.data-table th:last-child  { border-radius: 0 10px 10px 0; }
.data-table td {
    padding: 0.7rem 1rem;
    border-bottom: 1px solid #f3f4f6;
    color: #374151;
}
.data-table tr:hover td { background: #f0f9ff; }

/* Badge */
.badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 700;
}
.badge-green  { background: #d1fae5; color: #065f46; }
.badge-blue   { background: #dbeafe; color: #1e40af; }
.badge-orange { background: #ffedd5; color: #9a3412; }
.badge-red    { background: #fee2e2; color: #991b1b; }

/* Result */
.result-ok {
    background: #d1fae5; border: 2px solid #10b981;
    border-radius: 14px; padding: 1.2rem; text-align: center; margin-top: 0.5rem;
}
.result-fail {
    background: #fee2e2; border: 2px solid #ef4444;
    border-radius: 14px; padding: 1.2rem; text-align: center; margin-top: 0.5rem;
}
.result-ok   b { color: #065f46; font-size: 1.1rem; }
.result-fail b { color: #991b1b; font-size: 1.1rem; }

/* Bill Box */
.bill-box {
    background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
    border: 1px solid #bae6fd;
    border-radius: 14px;
    padding: 1.5rem;
    margin-top: 0.5rem;
}
.bill-row {
    display: flex;
    justify-content: space-between;
    padding: 0.5rem 0;
    border-bottom: 1px dashed #bae6fd;
    font-size: 0.9rem;
    color: #374151;
}
.bill-row:last-child { border-bottom: none; }
.bill-total {
    display: flex;
    justify-content: space-between;
    padding: 0.8rem 0 0 0;
    font-size: 1.1rem;
    font-weight: 800;
    color: #0d4a6b;
}

/* Section tabs style */
div[data-testid="stHorizontalBlock"] { gap: 0.5rem; }

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Classes
# ─────────────────────────────────────────────
class Hospital:
    def __init__(self, hospital_name, location):
        self.hospital_name = hospital_name
        self.location = location

class Doctor(Hospital):
    def __init__(self, hospital_name, location, doctor_id, doctor_name, specialization, experience, fee):
        super().__init__(hospital_name, location)
        self.doctor_id = doctor_id; self.doctor_name = doctor_name
        self.specialization = specialization; self.experience = experience; self.fee = fee

class Patient(Hospital):
    def __init__(self, hospital_name, location, patient_id, patient_name, age, disease, room_number):
        super().__init__(hospital_name, location)
        self.patient_id = patient_id; self.patient_name = patient_name
        self.age = age; self.disease = disease; self.room_number = room_number

class Appointment:
    def __init__(self, appointment_id, doctor_name, patient_name, date, time):
        self.appointment_id = appointment_id; self.doctor_name = doctor_name
        self.patient_name = patient_name; self.date = date; self.time = time

class Bill(Hospital):
    def __init__(self, hospital_name, location, bill_id, patient_name, doctor_fee, room_charges, medicine_charges):
        super().__init__(hospital_name, location)
        self.bill_id = bill_id; self.patient_name = patient_name
        self.doctor_fee = doctor_fee; self.room_charges = room_charges
        self.medicine_charges = medicine_charges
        self.total = doctor_fee + room_charges + medicine_charges

# ─────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────
for key in ["doctor_list", "patient_list", "appointment_list", "bill_list"]:
    if key not in st.session_state:
        st.session_state[key] = []

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ─────────────────────────────────────────────
# Banner
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="banner">
    <div class="banner-icon">🏥</div>
    <div>
        <h1>Jan Kalyan Hospital</h1>
        <p>Serving Humanity with Compassion & Care — New Delhi, India</p>
    </div>
    <div class="banner-stats">
        <div class="stat-pill"><b>{len(st.session_state.doctor_list)}</b><span>Doctors</span></div>
        <div class="stat-pill"><b>{len(st.session_state.patient_list)}</b><span>Patients</span></div>
        <div class="stat-pill"><b>{len(st.session_state.appointment_list)}</b><span>Appointments</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Navigation + Content
# ─────────────────────────────────────────────
nav_col, main_col = st.columns([1, 3.5])

with nav_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**🗂️ Navigation**")
    pages = [
        ("📊", "Dashboard"),
        ("👨‍⚕️", "Doctors"),
        ("🤒", "Patients"),
        ("📅", "Appointments"),
        ("🧾", "Billing"),
    ]
    for icon, page in pages:
        active = "nav-active" if st.session_state.page == page else ""
        if st.button(f"{icon}  {page}", key=f"nav_{page}"):
            st.session_state.page = page
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with main_col:
    page = st.session_state.page

    # ── DASHBOARD ────────────────────────────
    if page == "Dashboard":
        c1, c2, c3, c4 = st.columns(4)
        metrics = [
            ("👨‍⚕️ Doctors", len(st.session_state.doctor_list), "#0d4a6b"),
            ("🤒 Patients", len(st.session_state.patient_list), "#0d9488"),
            ("📅 Appointments", len(st.session_state.appointment_list), "#7c3aed"),
            ("🧾 Bills", len(st.session_state.bill_list), "#d97706"),
        ]
        for col, (label, val, color) in zip([c1,c2,c3,c4], metrics):
            col.markdown(f"""
            <div style="background:white; border-radius:14px; padding:1.2rem; text-align:center;
                        box-shadow:0 2px 12px rgba(0,0,0,0.07); border-top: 4px solid {color};">
                <div style="font-size:0.85rem; color:#6b7280; font-weight:600;">{label}</div>
                <div style="font-size:2.2rem; font-weight:800; color:{color};">{val}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Recent Doctors
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">👨‍⚕️ Recent Doctors</div>', unsafe_allow_html=True)
        if st.session_state.doctor_list:
            st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Fee</th></tr>', unsafe_allow_html=True)
            for d in st.session_state.doctor_list[-5:]:
                st.markdown(f'<tr><td>{d.doctor_id}</td><td>{d.doctor_name}</td><td><span class="badge badge-blue">{d.specialization}</span></td><td>₹{d.fee}</td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else:
            st.info("No doctors added yet.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Recent Patients
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🤒 Recent Patients</div>', unsafe_allow_html=True)
        if st.session_state.patient_list:
            st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Age</th><th>Disease</th><th>Room</th></tr>', unsafe_allow_html=True)
            for p in st.session_state.patient_list[-5:]:
                st.markdown(f'<tr><td>{p.patient_id}</td><td>{p.patient_name}</td><td>{p.age}</td><td><span class="badge badge-orange">{p.disease}</span></td><td>{p.room_number}</td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else:
            st.info("No patients added yet.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── DOCTORS ──────────────────────────────
    elif page == "Doctors":
        tab1, tab2, tab3 = st.tabs(["➕ Add Doctor", "📋 View All", "🔍 Search"])

        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">➕ Add New Doctor</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                d_name = st.text_input("Doctor Name", placeholder="Dr. Rajesh Kumar")
                d_exp  = st.number_input("Experience (years)", min_value=0, max_value=50, value=5)
            with c2:
                d_spec = st.text_input("Specialization", placeholder="Cardiologist")
                d_fee  = st.number_input("Consultation Fee (₹)", min_value=0, value=500, step=50)

            if st.button("✅ Add Doctor"):
                if d_name and d_spec:
                    doc_id = len(st.session_state.doctor_list) + 1
                    d = Doctor("Jan Kalyan Hospital", "New Delhi", doc_id, d_name, d_spec, d_exp, d_fee)
                    st.session_state.doctor_list.append(d)
                    st.markdown('<div class="result-ok"><b>✅ Doctor Added Successfully!</b></div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.warning("Please fill Name and Specialization.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📋 All Doctors</div>', unsafe_allow_html=True)
            if st.session_state.doctor_list:
                st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Experience</th><th>Fee</th></tr>', unsafe_allow_html=True)
                for d in st.session_state.doctor_list:
                    st.markdown(f'<tr><td>{d.doctor_id}</td><td><b>{d.doctor_name}</b></td><td><span class="badge badge-blue">{d.specialization}</span></td><td>{d.experience} yrs</td><td>₹{d.fee}</td></tr>', unsafe_allow_html=True)
                st.markdown('</table>', unsafe_allow_html=True)
            else:
                st.info("No doctors found.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🔍 Search Doctor by Name</div>', unsafe_allow_html=True)
            search_name = st.text_input("Enter Doctor Name")
            if st.button("🔍 Search"):
                results = [d for d in st.session_state.doctor_list if search_name.lower() in d.doctor_name.lower()]
                if results:
                    st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Specialization</th><th>Experience</th><th>Fee</th></tr>', unsafe_allow_html=True)
                    for d in results:
                        st.markdown(f'<tr><td>{d.doctor_id}</td><td><b>{d.doctor_name}</b></td><td>{d.specialization}</td><td>{d.experience} yrs</td><td>₹{d.fee}</td></tr>', unsafe_allow_html=True)
                    st.markdown('</table>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="result-fail"><b>❌ Doctor not found.</b></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── PATIENTS ─────────────────────────────
    elif page == "Patients":
        tab1, tab2, tab3 = st.tabs(["➕ Add Patient", "📋 View All", "🔍 Search"])

        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">➕ Add New Patient</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                p_name = st.text_input("Patient Name", placeholder="Rahul Verma")
                p_disease = st.text_input("Disease", placeholder="Fever / Diabetes...")
            with c2:
                p_age  = st.number_input("Age", min_value=1, max_value=120, value=30)
                p_room = st.text_input("Room Number", placeholder="101")

            if st.button("✅ Add Patient"):
                if p_name and p_disease and p_room:
                    pat_id = len(st.session_state.patient_list) + 1
                    p = Patient("Jan Kalyan Hospital", "New Delhi", pat_id, p_name, p_age, p_disease, p_room)
                    st.session_state.patient_list.append(p)
                    st.markdown('<div class="result-ok"><b>✅ Patient Added Successfully!</b></div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.warning("Please fill all fields.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📋 All Patients</div>', unsafe_allow_html=True)
            if st.session_state.patient_list:
                st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Age</th><th>Disease</th><th>Room</th></tr>', unsafe_allow_html=True)
                for p in st.session_state.patient_list:
                    st.markdown(f'<tr><td>{p.patient_id}</td><td><b>{p.patient_name}</b></td><td>{p.age}</td><td><span class="badge badge-orange">{p.disease}</span></td><td>{p.room_number}</td></tr>', unsafe_allow_html=True)
                st.markdown('</table>', unsafe_allow_html=True)
            else:
                st.info("No patients found.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🔍 Search Patient</div>', unsafe_allow_html=True)
            search_by = st.radio("Search by", ["Name", "ID"], horizontal=True)
            if search_by == "Name":
                q = st.text_input("Patient Name")
                if st.button("🔍 Search"):
                    results = [p for p in st.session_state.patient_list if q.lower() in p.patient_name.lower()]
                    if results:
                        st.markdown('<table class="data-table"><tr><th>ID</th><th>Name</th><th>Age</th><th>Disease</th><th>Room</th></tr>', unsafe_allow_html=True)
                        for p in results:
                            st.markdown(f'<tr><td>{p.patient_id}</td><td>{p.patient_name}</td><td>{p.age}</td><td>{p.disease}</td><td>{p.room_number}</td></tr>', unsafe_allow_html=True)
                        st.markdown('</table>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="result-fail"><b>❌ Patient not found.</b></div>', unsafe_allow_html=True)
            else:
                pid = st.number_input("Patient ID", min_value=1, step=1)
                if st.button("🔍 Search"):
                    results = [p for p in st.session_state.patient_list if p.patient_id == pid]
                    if results:
                        p = results[0]
                        st.markdown(f'<table class="data-table"><tr><th>Field</th><th>Value</th></tr><tr><td>Name</td><td>{p.patient_name}</td></tr><tr><td>Age</td><td>{p.age}</td></tr><tr><td>Disease</td><td>{p.disease}</td></tr><tr><td>Room</td><td>{p.room_number}</td></tr></table>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="result-fail"><b>❌ Patient not found.</b></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── APPOINTMENTS ─────────────────────────
    elif page == "Appointments":
        tab1, tab2, tab3 = st.tabs(["➕ Book Appointment", "📋 View All", "🔍 Search by Date"])

        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">➕ Book Appointment</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                a_doc  = st.text_input("Doctor Name", placeholder="Dr. Rajesh Kumar")
                a_date = st.text_input("Date (DD-MM-YYYY)", placeholder="28-05-2026")
            with c2:
                a_pat  = st.text_input("Patient Name", placeholder="Rahul Verma")
                a_time = st.text_input("Time", placeholder="10:00 AM")

            if st.button("✅ Book Appointment"):
                if a_doc and a_pat and a_date and a_time:
                    appt_id = len(st.session_state.appointment_list) + 1
                    a = Appointment(appt_id, a_doc, a_pat, a_date, a_time)
                    st.session_state.appointment_list.append(a)
                    st.markdown('<div class="result-ok"><b>✅ Appointment Booked Successfully!</b></div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.warning("Please fill all fields.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📋 All Appointments</div>', unsafe_allow_html=True)
            if st.session_state.appointment_list:
                st.markdown('<table class="data-table"><tr><th>ID</th><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th></tr>', unsafe_allow_html=True)
                for a in st.session_state.appointment_list:
                    st.markdown(f'<tr><td>{a.appointment_id}</td><td>{a.doctor_name}</td><td>{a.patient_name}</td><td><span class="badge badge-green">{a.date}</span></td><td>{a.time}</td></tr>', unsafe_allow_html=True)
                st.markdown('</table>', unsafe_allow_html=True)
            else:
                st.info("No appointments found.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🔍 Search Appointment by Date</div>', unsafe_allow_html=True)
            s_date = st.text_input("Enter Date (DD-MM-YYYY)", placeholder="28-05-2026")
            if st.button("🔍 Search"):
                results = [a for a in st.session_state.appointment_list if a.date == s_date]
                if results:
                    st.markdown('<table class="data-table"><tr><th>ID</th><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th></tr>', unsafe_allow_html=True)
                    for a in results:
                        st.markdown(f'<tr><td>{a.appointment_id}</td><td>{a.doctor_name}</td><td>{a.patient_name}</td><td>{a.date}</td><td>{a.time}</td></tr>', unsafe_allow_html=True)
                    st.markdown('</table>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="result-fail"><b>❌ No appointments found on this date.</b></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # ── BILLING ──────────────────────────────
    elif page == "Billing":
        tab1, tab2 = st.tabs(["🧾 Generate Bill", "📋 View All Bills"])

        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">🧾 Generate Patient Bill</div>', unsafe_allow_html=True)
            b_name  = st.text_input("Patient Name", placeholder="Rahul Verma")
            c1, c2, c3 = st.columns(3)
            with c1: b_doc = st.number_input("Doctor Fee (₹)", min_value=0, value=500, step=50)
            with c2: b_room = st.number_input("Room Charges (₹)", min_value=0, value=1000, step=100)
            with c3: b_med = st.number_input("Medicine Charges (₹)", min_value=0, value=300, step=50)

            total = b_doc + b_room + b_med
            st.markdown(f"""
            <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:10px;
                        padding:0.8rem 1.2rem; margin:0.5rem 0; text-align:right;">
                <span style="color:#6b7280; font-size:0.9rem;">Estimated Total: </span>
                <span style="color:#0d4a6b; font-size:1.3rem; font-weight:800;">₹{total}</span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🧾 Generate Bill"):
                if b_name:
                    bill_id = len(st.session_state.bill_list) + 1
                    b = Bill("Jan Kalyan Hospital", "New Delhi", bill_id, b_name, b_doc, b_room, b_med)
                    st.session_state.bill_list.append(b)
                    st.markdown(f"""
                    <div class="bill-box">
                        <div style="text-align:center; margin-bottom:1rem;">
                            <div style="font-size:1.5rem;">🧾</div>
                            <div style="font-weight:800; color:#0d4a6b; font-size:1.1rem;">Jan Kalyan Hospital</div>
                            <div style="font-size:0.8rem; color:#6b7280;">Bill ID: #{bill_id}</div>
                        </div>
                        <div class="bill-row"><span>Patient Name</span><span><b>{b_name}</b></span></div>
                        <div class="bill-row"><span>Doctor Fee</span><span>₹{b_doc}</span></div>
                        <div class="bill-row"><span>Room Charges</span><span>₹{b_room}</span></div>
                        <div class="bill-row"><span>Medicine Charges</span><span>₹{b_med}</span></div>
                        <div class="bill-total"><span>Total Amount</span><span>₹{b.total}</span></div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.warning("Please enter patient name.")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title">📋 All Bills</div>', unsafe_allow_html=True)
            if st.session_state.bill_list:
                total_rev = sum(b.total for b in st.session_state.bill_list)
                st.markdown(f'<div style="background:#d1fae5;border-radius:10px;padding:0.7rem 1rem;margin-bottom:1rem;font-weight:700;color:#065f46;">💰 Total Revenue: ₹{total_rev}</div>', unsafe_allow_html=True)
                st.markdown('<table class="data-table"><tr><th>Bill ID</th><th>Patient</th><th>Doctor Fee</th><th>Room</th><th>Medicine</th><th>Total</th></tr>', unsafe_allow_html=True)
                for b in st.session_state.bill_list:
                    st.markdown(f'<tr><td>#{b.bill_id}</td><td><b>{b.patient_name}</b></td><td>₹{b.doctor_fee}</td><td>₹{b.room_charges}</td><td>₹{b.medicine_charges}</td><td><b>₹{b.total}</b></td></tr>', unsafe_allow_html=True)
                st.markdown('</table>', unsafe_allow_html=True)
            else:
                st.info("No bills generated yet.")
            st.markdown('</div>', unsafe_allow_html=True)