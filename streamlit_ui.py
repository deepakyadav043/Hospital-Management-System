import streamlit as st
import csv
import os

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Sans+3:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(160deg, #f0f4f8 0%, #dce8f5 50%, #e8f0fb 100%);
}

/* Hero Banner */
.hero-banner {
    background: linear-gradient(135deg, #0a2342 0%, #1a4480 40%, #1565c0 70%, #0d47a1 100%);
    border-radius: 20px;
    padding: 0;
    margin-bottom: 2rem;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(10,35,66,0.4);
    position: relative;
}

.hero-content {
    padding: 2.5rem 3rem;
    position: relative;
    z-index: 2;
}

.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
    z-index: 1;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -40px;
    width: 250px; height: 250px;
    background: rgba(255,255,255,0.03);
    border-radius: 50%;
    z-index: 1;
}

.building-svg {
    position: absolute;
    right: 3rem;
    bottom: 0;
    z-index: 2;
    opacity: 0.92;
}

.hospital-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 900;
    color: #ffffff;
    margin: 0;
    line-height: 1.1;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 20px rgba(0,0,0,0.3);
}

.hospital-subtitle {
    font-size: 1rem;
    color: #90caf9;
    margin-top: 0.5rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 300;
}

.hospital-tagline {
    font-size: 1.1rem;
    color: #bbdefb;
    margin-top: 1rem;
    font-style: italic;
    font-weight: 300;
}

.stat-pill {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(4px);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 50px;
    font-size: 0.85rem;
    margin-top: 1.5rem;
    margin-right: 0.5rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a2342 0%, #1a4480 100%) !important;
    border-right: none;
}
[data-testid="stSidebar"] * {
    color: #e3f2fd !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.95rem !important;
    padding: 0.3rem 0;
}
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.15) !important;
}

/* Section Headers */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #0a2342;
    border-bottom: 3px solid #1565c0;
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

/* Cards */
.info-card {
    background: white;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 4px 20px rgba(10,35,66,0.08);
    border-left: 5px solid #1565c0;
    margin-bottom: 1rem;
    transition: transform 0.2s;
}
.info-card:hover { transform: translateY(-2px); }

.info-card h4 {
    font-family: 'Playfair Display', serif;
    color: #0a2342;
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}
.info-card p {
    margin: 0.15rem 0;
    color: #444;
    font-size: 0.9rem;
}
.info-card .badge {
    display: inline-block;
    background: #e3f2fd;
    color: #1565c0;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
}

/* Report Cards */
.report-card {
    background: linear-gradient(135deg, #0a2342 0%, #1565c0 100%);
    color: white;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 8px 25px rgba(10,35,66,0.25);
}
.report-card .number {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 900;
    line-height: 1;
}
.report-card .label {
    font-size: 0.85rem;
    opacity: 0.8;
    margin-top: 0.3rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Form styling */
[data-testid="stForm"] {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 20px rgba(10,35,66,0.08);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0a2342, #1565c0) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

.stSelectbox label, .stTextInput label, .stNumberInput label {
    font-weight: 600;
    color: #0a2342;
}

/* Alerts */
.success-msg {
    background: #e8f5e9; border-left: 4px solid #43a047;
    padding: 0.8rem 1rem; border-radius: 8px; color: #1b5e20;
    margin: 0.5rem 0;
}
.error-msg {
    background: #ffebee; border-left: 4px solid #e53935;
    padding: 0.8rem 1rem; border-radius: 8px; color: #b71c1c;
    margin: 0.5rem 0;
}

/* Bill */
.bill-box {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 8px 30px rgba(10,35,66,0.12);
    border: 2px dashed #90caf9;
    max-width: 500px;
    margin: 0 auto;
}
.bill-box h3 {
    font-family: 'Playfair Display', serif;
    color: #0a2342;
    text-align: center;
    margin-bottom: 1rem;
}
.bill-row {
    display: flex; justify-content: space-between;
    padding: 0.5rem 0; border-bottom: 1px solid #f0f0f0;
    font-size: 0.95rem; color: #333;
}
.bill-total {
    display: flex; justify-content: space-between;
    padding: 0.8rem 0; margin-top: 0.5rem;
    font-weight: 700; font-size: 1.1rem;
    color: #0a2342;
    border-top: 2px solid #1565c0;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Data Classes
# ─────────────────────────────────────────────
class Hospital:
    def __init__(self, hospital_name, location):
        self.hospital_name = hospital_name
        self.location = location

class Doctor(Hospital):
    def __init__(self, hospital_name, location, doctor_id, doctor_name, specialization, experience, fee):
        super().__init__(hospital_name, location)
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.experience = experience
        self.fee = fee

class Patient(Hospital):
    def __init__(self, hospital_name, location, patient_id, patient_name, age, disease, room_number):
        super().__init__(hospital_name, location)
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.room_number = room_number

class Appointment:
    def __init__(self, appointment_id, doctor_name, patient_name, date, time):
        self.appointment_id = appointment_id
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.date = date
        self.time = time

class Bill(Hospital):
    def __init__(self, hospital_name, location, bill_id, patient_name, doctor_fee, room_charges, medicine_charges):
        super().__init__(hospital_name, location)
        self.bill_id = bill_id
        self.patient_name = patient_name
        self.doctor_fee = doctor_fee
        self.room_charges = room_charges
        self.medicine_charges = medicine_charges
        self.total = doctor_fee + room_charges + medicine_charges


# ─────────────────────────────────────────────
# Session State Init
# ─────────────────────────────────────────────
if "doctor_list" not in st.session_state:
    st.session_state.doctor_list = []
if "patient_list" not in st.session_state:
    st.session_state.patient_list = []
if "appointment_list" not in st.session_state:
    st.session_state.appointment_list = []
if "bill_list" not in st.session_state:
    st.session_state.bill_list = []
if "data_loaded" not in st.session_state:
    st.session_state.data_loaded = False


# ─────────────────────────────────────────────
# CSV Save & Load
# ─────────────────────────────────────────────
def save_doctors():
    with open("doctors.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["doctor_id", "doctor_name", "specialization", "experience", "fee"])
        for d in st.session_state.doctor_list:
            writer.writerow([d.doctor_id, d.doctor_name, d.specialization, d.experience, d.fee])

def save_patients():
    with open("patients.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["patient_id", "patient_name", "age", "disease", "room_number"])
        for p in st.session_state.patient_list:
            writer.writerow([p.patient_id, p.patient_name, p.age, p.disease, p.room_number])

def save_appointments():
    with open("appointments.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["appointment_id", "doctor_name", "patient_name", "date", "time"])
        for a in st.session_state.appointment_list:
            writer.writerow([a.appointment_id, a.doctor_name, a.patient_name, a.date, a.time])

def save_bills():
    with open("bills.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["bill_id", "patient_name", "doctor_fee", "room_charges", "medicine_charges", "total"])
        for b in st.session_state.bill_list:
            writer.writerow([b.bill_id, b.patient_name, b.doctor_fee, b.room_charges, b.medicine_charges, b.total])

def load_all():
    if st.session_state.data_loaded:
        return
    if os.path.exists("doctors.csv"):
        with open("doctors.csv", "r") as f:
            for row in csv.DictReader(f):
                st.session_state.doctor_list.append(
                    Doctor("JAN KALYAN HOSPITAL", "Bhopal", int(row["doctor_id"]), row["doctor_name"],
                           row["specialization"], int(row["experience"]), int(row["fee"])))
    if os.path.exists("patients.csv"):
        with open("patients.csv", "r") as f:
            for row in csv.DictReader(f):
                st.session_state.patient_list.append(
                    Patient("JAN KALYAN HOSPITAL", "Bhopal", int(row["patient_id"]), row["patient_name"],
                            int(row["age"]), row["disease"], row["room_number"]))
    if os.path.exists("appointments.csv"):
        with open("appointments.csv", "r") as f:
            for row in csv.DictReader(f):
                st.session_state.appointment_list.append(
                    Appointment(int(row["appointment_id"]), row["doctor_name"],
                                row["patient_name"], row["date"], row["time"]))
    if os.path.exists("bills.csv"):
        with open("bills.csv", "r") as f:
            for row in csv.DictReader(f):
                st.session_state.bill_list.append(
                    Bill("JAN KALYAN HOSPITAL", "Bhopal", int(row["bill_id"]), row["patient_name"],
                         int(row["doctor_fee"]), int(row["room_charges"]), int(row["medicine_charges"])))
    st.session_state.data_loaded = True

load_all()


# ─────────────────────────────────────────────
# Hero Banner with SVG Building
# ─────────────────────────────────────────────
building_svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="320" height="220" viewBox="0 0 320 220">
  <!-- Sky gradient background strip -->
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bbdefb" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#1565c0" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="wall" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e3f2fd"/>
      <stop offset="100%" stop-color="#bbdefb"/>
    </linearGradient>
    <linearGradient id="wing" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#dce8f5"/>
      <stop offset="100%" stop-color="#c5ddf7"/>
    </linearGradient>
  </defs>

  <!-- Left wing -->
  <rect x="10" y="90" width="65" height="130" fill="url(#wing)" rx="3"/>
  <!-- Left wing windows row 1 -->
  <rect x="20" y="100" width="14" height="12" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="40" y="100" width="14" height="12" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="60" y="100" width="10" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <!-- Left wing windows row 2 -->
  <rect x="20" y="120" width="14" height="12" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="40" y="120" width="14" height="12" fill="#90caf9" opacity="0.8" rx="2"/>
  <rect x="60" y="120" width="10" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <!-- Left wing windows row 3 -->
  <rect x="20" y="140" width="14" height="12" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="40" y="140" width="14" height="12" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="60" y="140" width="10" height="12" fill="#90caf9" opacity="0.5" rx="2"/>
  <!-- Left wing windows row 4 -->
  <rect x="20" y="160" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <rect x="40" y="160" width="14" height="12" fill="#90caf9" opacity="0.6" rx="2"/>
  <rect x="60" y="160" width="10" height="12" fill="#1565c0" opacity="0.4" rx="2"/>
  <!-- Left wing windows row 5 -->
  <rect x="20" y="180" width="14" height="12" fill="#90caf9" opacity="0.5" rx="2"/>
  <rect x="40" y="180" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>

  <!-- Right wing -->
  <rect x="245" y="90" width="65" height="130" fill="url(#wing)" rx="3"/>
  <!-- Right wing windows row 1 -->
  <rect x="250" y="100" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <rect x="270" y="100" width="14" height="12" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="290" y="100" width="14" height="12" fill="#90caf9" opacity="0.7" rx="2"/>
  <!-- rows 2-5 similar -->
  <rect x="250" y="120" width="14" height="12" fill="#90caf9" opacity="0.6" rx="2"/>
  <rect x="270" y="120" width="14" height="12" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="290" y="120" width="14" height="12" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="250" y="140" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <rect x="270" y="140" width="14" height="12" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="290" y="140" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <rect x="250" y="160" width="14" height="12" fill="#90caf9" opacity="0.6" rx="2"/>
  <rect x="270" y="160" width="14" height="12" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="290" y="160" width="14" height="12" fill="#90caf9" opacity="0.5" rx="2"/>
  <rect x="250" y="180" width="14" height="12" fill="#1565c0" opacity="0.5" rx="2"/>
  <rect x="270" y="180" width="14" height="12" fill="#90caf9" opacity="0.6" rx="2"/>

  <!-- Main tower -->
  <rect x="72" y="30" width="176" height="190" fill="url(#wall)" rx="4"/>

  <!-- Tower top triangular roof -->
  <polygon points="160,2 72,30 248,30" fill="#0a2342" opacity="0.85"/>

  <!-- Red cross on roof -->
  <rect x="152" y="8" width="16" height="16" fill="#e53935" rx="2"/>
  <rect x="148" y="12" width="24" height="8" fill="#e53935" rx="2"/>

  <!-- Main building windows - row 1 -->
  <rect x="88" y="45" width="18" height="15" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="114" y="45" width="18" height="15" fill="#90caf9" opacity="0.8" rx="2"/>
  <rect x="140" y="45" width="18" height="15" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="166" y="45" width="18" height="15" fill="#90caf9" opacity="0.8" rx="2"/>
  <rect x="192" y="45" width="18" height="15" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="218" y="45" width="18" height="15" fill="#90caf9" opacity="0.6" rx="2"/>

  <!-- Row 2 -->
  <rect x="88" y="70" width="18" height="15" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="114" y="70" width="18" height="15" fill="#1565c0" opacity="0.8" rx="2"/>
  <rect x="140" y="70" width="18" height="15" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="166" y="70" width="18" height="15" fill="#1565c0" opacity="0.8" rx="2"/>
  <rect x="192" y="70" width="18" height="15" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="218" y="70" width="18" height="15" fill="#1565c0" opacity="0.6" rx="2"/>

  <!-- Row 3 -->
  <rect x="88" y="95" width="18" height="15" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="114" y="95" width="18" height="15" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="140" y="95" width="18" height="15" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="166" y="95" width="18" height="15" fill="#90caf9" opacity="0.7" rx="2"/>
  <rect x="192" y="95" width="18" height="15" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="218" y="95" width="18" height="15" fill="#90caf9" opacity="0.5" rx="2"/>

  <!-- Row 4 -->
  <rect x="88" y="120" width="18" height="15" fill="#90caf9" opacity="0.6" rx="2"/>
  <rect x="114" y="120" width="18" height="15" fill="#1565c0" opacity="0.7" rx="2"/>
  <rect x="192" y="120" width="18" height="15" fill="#90caf9" opacity="0.6" rx="2"/>
  <rect x="218" y="120" width="18" height="15" fill="#1565c0" opacity="0.5" rx="2"/>

  <!-- Big Red Cross on main building -->
  <rect x="148" y="105" width="24" height="40" fill="#e53935" opacity="0.9" rx="3"/>
  <rect x="136" y="117" width="48" height="16" fill="#e53935" opacity="0.9" rx="3"/>

  <!-- Pillars at entrance -->
  <rect x="118" y="165" width="12" height="55" fill="#b0bec5" rx="2"/>
  <rect x="190" y="165" width="12" height="55" fill="#b0bec5" rx="2"/>

  <!-- Main entrance door -->
  <rect x="130" y="170" width="60" height="50" fill="#0a2342" opacity="0.85" rx="3"/>
  <rect x="136" y="174" width="22" height="40" fill="#1565c0" opacity="0.6" rx="2"/>
  <rect x="162" y="174" width="22" height="40" fill="#1565c0" opacity="0.6" rx="2"/>

  <!-- Entrance canopy -->
  <rect x="108" y="163" width="104" height="8" fill="#0a2342" opacity="0.7" rx="2"/>

  <!-- Steps -->
  <rect x="110" y="218" width="100" height="3" fill="#b0bec5" rx="1"/>
  <rect x="115" y="215" width="90" height="3" fill="#cfd8dc" rx="1"/>

  <!-- Flag pole -->
  <line x1="160" y1="2" x2="160" y2="2" stroke="white" stroke-width="2"/>
  <rect x="158" y="2" width="2" height="0" fill="white"/>
</svg>
"""

st.markdown(f"""
<div class="hero-banner">
  <div class="hero-content">
    <p class="hospital-subtitle">🏥 Serving with Compassion Since 1995</p>
    <h1 class="hospital-title">Jan Kalyan<br>Hospital</h1>
    <p class="hospital-tagline">"जन सेवा ही हमारा धर्म" &nbsp;·&nbsp; Bhopal, Madhya Pradesh</p>
    <div>
      <span class="stat-pill">🩺 NABH Accredited</span>
      <span class="stat-pill">🏨 500+ Beds</span>
      <span class="stat-pill">⚕️ 24×7 Emergency</span>
    </div>
  </div>
  <div class="building-svg">{building_svg}</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Sidebar Navigation
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏥 Navigation")
    st.markdown("---")
    section = st.radio("", [
        "🏠 Dashboard",
        "👨‍⚕️ Doctors",
        "🛏️ Patients",
        "📅 Appointments",
        "💳 Billing",
        "📊 Reports"
    ])
    st.markdown("---")
    st.markdown("**Jan Kalyan Hospital**")
    st.markdown("Bhopal, Madhya Pradesh")
    st.markdown("📞 0755-XXXXXXX")
    st.markdown("🆘 Emergency: 108")


# ─────────────────────────────────────────────
# Dashboard
# ─────────────────────────────────────────────
if section == "🏠 Dashboard":
    st.markdown('<div class="section-header">Dashboard Overview</div>', unsafe_allow_html=True)
    total_revenue = sum(b.total for b in st.session_state.bill_list)
    c1, c2, c3, c4, c5 = st.columns(5)
    for col, num, label in zip(
        [c1, c2, c3, c4, c5],
        [len(st.session_state.doctor_list), len(st.session_state.patient_list),
         len(st.session_state.appointment_list), len(st.session_state.bill_list),
         f"₹{total_revenue:,}"],
        ["Doctors", "Patients", "Appointments", "Bills", "Total Revenue"]
    ):
        with col:
            st.markdown(f"""
            <div class="report-card">
              <div class="number">{num}</div>
              <div class="label">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🆕 Recent Patients")
        recent = st.session_state.patient_list[-3:][::-1]
        if recent:
            for p in recent:
                st.markdown(f"""<div class="info-card">
                    <h4>{p.patient_name}</h4>
                    <p>🏥 Room: {p.room_number} &nbsp;|&nbsp; 🤒 {p.disease}</p>
                    <p>Age: {p.age} yrs &nbsp; <span class="badge">ID #{p.patient_id}</span></p>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No patients yet.")
    with col2:
        st.markdown("#### 📅 Upcoming Appointments")
        recent_a = st.session_state.appointment_list[-3:][::-1]
        if recent_a:
            for a in recent_a:
                st.markdown(f"""<div class="info-card">
                    <h4>{a.patient_name}</h4>
                    <p>👨‍⚕️ Dr. {a.doctor_name}</p>
                    <p>📆 {a.date} &nbsp; 🕐 {a.time} &nbsp; <span class="badge">#{a.appointment_id}</span></p>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No appointments yet.")


# ─────────────────────────────────────────────
# Doctors
# ─────────────────────────────────────────────
elif section == "👨‍⚕️ Doctors":
    st.markdown('<div class="section-header">Doctor Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["➕ Add", "📋 View All", "🔍 Search", "✏️ Update Fee", "🗑️ Delete"])

    with tab1:
        with st.form("add_doc"):
            st.subheader("Add New Doctor")
            c1, c2 = st.columns(2)
            name = c1.text_input("Doctor Name")
            spec = c2.text_input("Specialization")
            exp = c1.number_input("Experience (years)", min_value=0, max_value=60, step=1)
            fee = c2.number_input("Consultation Fee (₹)", min_value=0, step=50)
            if st.form_submit_button("✅ Add Doctor"):
                if name and spec:
                    doc_id = len(st.session_state.doctor_list) + 1
                    st.session_state.doctor_list.append(
                        Doctor("JAN KALYAN HOSPITAL", "Bhopal", doc_id, name, spec, int(exp), int(fee)))
                    save_doctors()
                    st.markdown('<div class="success-msg">✅ Doctor added successfully!</div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.markdown('<div class="error-msg">❌ Name and Specialization are required.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.doctor_list:
            st.info("No doctors found.")
        else:
            for d in st.session_state.doctor_list:
                st.markdown(f"""<div class="info-card">
                    <h4>Dr. {d.doctor_name} &nbsp; <span class="badge">{d.specialization}</span></h4>
                    <p>🏥 {d.hospital_name}, {d.location}</p>
                    <p>📅 Experience: {d.experience} yrs &nbsp;|&nbsp; 💰 Fee: ₹{d.fee} &nbsp;|&nbsp; <span class="badge">ID #{d.doctor_id}</span></p>
                </div>""", unsafe_allow_html=True)

    with tab3:
        query = st.text_input("Search by Name")
        if query:
            results = [d for d in st.session_state.doctor_list if query.lower() in d.doctor_name.lower()]
            if results:
                for d in results:
                    st.markdown(f"""<div class="info-card">
                        <h4>Dr. {d.doctor_name} &nbsp; <span class="badge">{d.specialization}</span></h4>
                        <p>📅 Experience: {d.experience} yrs &nbsp;|&nbsp; 💰 Fee: ₹{d.fee} &nbsp;|&nbsp; <span class="badge">ID #{d.doctor_id}</span></p>
                    </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-msg">❌ No doctor found.</div>', unsafe_allow_html=True)

    with tab4:
        if st.session_state.doctor_list:
            options = {f"#{d.doctor_id} - Dr. {d.doctor_name}": d for d in st.session_state.doctor_list}
            sel = st.selectbox("Select Doctor", list(options.keys()))
            doc = options[sel]
            st.write(f"Current Fee: **₹{doc.fee}**")
            new_fee = st.number_input("New Fee (₹)", min_value=0, value=doc.fee, step=50)
            if st.button("💾 Update Fee"):
                doc.fee = int(new_fee)
                save_doctors()
                st.markdown('<div class="success-msg">✅ Fee updated!</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No doctors to update.")

    with tab5:
        if st.session_state.doctor_list:
            options = {f"#{d.doctor_id} - Dr. {d.doctor_name}": d for d in st.session_state.doctor_list}
            sel = st.selectbox("Select Doctor to Delete", list(options.keys()))
            if st.button("🗑️ Delete Doctor", type="primary"):
                st.session_state.doctor_list.remove(options[sel])
                save_doctors()
                st.markdown('<div class="success-msg">✅ Doctor deleted.</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No doctors to delete.")


# ─────────────────────────────────────────────
# Patients
# ─────────────────────────────────────────────
elif section == "🛏️ Patients":
    st.markdown('<div class="section-header">Patient Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["➕ Add", "📋 View All", "🔍 Search", "✏️ Update Room", "🗑️ Delete"])

    with tab1:
        with st.form("add_pat"):
            st.subheader("Admit New Patient")
            c1, c2 = st.columns(2)
            name = c1.text_input("Patient Name")
            age = c2.number_input("Age", min_value=0, max_value=120, step=1)
            disease = c1.text_input("Disease / Diagnosis")
            room = c2.text_input("Room Number")
            if st.form_submit_button("✅ Admit Patient"):
                if name and disease and room:
                    pat_id = len(st.session_state.patient_list) + 1
                    st.session_state.patient_list.append(
                        Patient("JAN KALYAN HOSPITAL", "Bhopal", pat_id, name, int(age), disease, room))
                    save_patients()
                    st.markdown('<div class="success-msg">✅ Patient admitted!</div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.markdown('<div class="error-msg">❌ All fields are required.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.patient_list:
            st.info("No patients found.")
        else:
            for p in st.session_state.patient_list:
                st.markdown(f"""<div class="info-card">
                    <h4>{p.patient_name} &nbsp; <span class="badge">Room {p.room_number}</span></h4>
                    <p>🏥 {p.hospital_name} &nbsp;|&nbsp; Age: {p.age} yrs</p>
                    <p>🤒 Diagnosis: {p.disease} &nbsp; <span class="badge">ID #{p.patient_id}</span></p>
                </div>""", unsafe_allow_html=True)

    with tab3:
        method = st.radio("Search by", ["Name", "ID"], horizontal=True)
        if method == "Name":
            q = st.text_input("Patient Name")
            results = [p for p in st.session_state.patient_list if q.lower() in p.patient_name.lower()] if q else []
        else:
            pid = st.number_input("Patient ID", min_value=1, step=1)
            results = [p for p in st.session_state.patient_list if p.patient_id == int(pid)]
        for p in results:
            st.markdown(f"""<div class="info-card">
                <h4>{p.patient_name} &nbsp; <span class="badge">Room {p.room_number}</span></h4>
                <p>Age: {p.age} yrs &nbsp;|&nbsp; 🤒 {p.disease} &nbsp; <span class="badge">ID #{p.patient_id}</span></p>
            </div>""", unsafe_allow_html=True)
        if (method == "Name" and q and not results) or (method == "ID" and not results):
            st.markdown('<div class="error-msg">❌ Patient not found.</div>', unsafe_allow_html=True)

    with tab4:
        if st.session_state.patient_list:
            options = {f"#{p.patient_id} - {p.patient_name}": p for p in st.session_state.patient_list}
            sel = st.selectbox("Select Patient", list(options.keys()))
            pat = options[sel]
            st.write(f"Current Room: **{pat.room_number}**")
            new_room = st.text_input("New Room Number", value=pat.room_number)
            if st.button("💾 Update Room"):
                pat.room_number = new_room
                save_patients()
                st.markdown('<div class="success-msg">✅ Room updated!</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No patients to update.")

    with tab5:
        if st.session_state.patient_list:
            options = {f"#{p.patient_id} - {p.patient_name}": p for p in st.session_state.patient_list}
            sel = st.selectbox("Select Patient to Delete", list(options.keys()))
            if st.button("🗑️ Delete Patient", type="primary"):
                st.session_state.patient_list.remove(options[sel])
                save_patients()
                st.markdown('<div class="success-msg">✅ Patient record deleted.</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No patients to delete.")


# ─────────────────────────────────────────────
# Appointments
# ─────────────────────────────────────────────
elif section == "📅 Appointments":
    st.markdown('<div class="section-header">Appointment Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["➕ Book", "📋 View All", "🔍 Search by Date", "✏️ Update", "❌ Cancel"])

    with tab1:
        with st.form("book_appt"):
            st.subheader("Book New Appointment")
            c1, c2 = st.columns(2)
            doc = c1.text_input("Doctor Name")
            pat = c2.text_input("Patient Name")
            date = c1.text_input("Date (DD-MM-YYYY)")
            time = c2.text_input("Time (e.g. 10:00 AM)")
            if st.form_submit_button("✅ Book Appointment"):
                if doc and pat and date and time:
                    appt_id = len(st.session_state.appointment_list) + 1
                    st.session_state.appointment_list.append(
                        Appointment(appt_id, doc, pat, date, time))
                    save_appointments()
                    st.markdown('<div class="success-msg">✅ Appointment booked!</div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.markdown('<div class="error-msg">❌ All fields required.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.appointment_list:
            st.info("No appointments found.")
        else:
            for a in st.session_state.appointment_list:
                st.markdown(f"""<div class="info-card">
                    <h4>{a.patient_name} &nbsp; <span class="badge">#{a.appointment_id}</span></h4>
                    <p>👨‍⚕️ Dr. {a.doctor_name}</p>
                    <p>📆 {a.date} &nbsp; 🕐 {a.time}</p>
                </div>""", unsafe_allow_html=True)

    with tab3:
        date_q = st.text_input("Enter Date (DD-MM-YYYY)")
        if date_q:
            results = [a for a in st.session_state.appointment_list if a.date == date_q]
            if results:
                for a in results:
                    st.markdown(f"""<div class="info-card">
                        <h4>{a.patient_name} → Dr. {a.doctor_name}</h4>
                        <p>📆 {a.date} &nbsp; 🕐 {a.time} &nbsp; <span class="badge">#{a.appointment_id}</span></p>
                    </div>""", unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-msg">❌ No appointments on this date.</div>', unsafe_allow_html=True)

    with tab4:
        if st.session_state.appointment_list:
            options = {f"#{a.appointment_id} - {a.patient_name} ({a.date})": a for a in st.session_state.appointment_list}
            sel = st.selectbox("Select Appointment", list(options.keys()))
            appt = options[sel]
            c1, c2 = st.columns(2)
            new_date = c1.text_input("New Date (DD-MM-YYYY)", value=appt.date)
            new_time = c2.text_input("New Time", value=appt.time)
            if st.button("💾 Update Appointment"):
                appt.date = new_date
                appt.time = new_time
                save_appointments()
                st.markdown('<div class="success-msg">✅ Appointment updated!</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No appointments to update.")

    with tab5:
        if st.session_state.appointment_list:
            options = {f"#{a.appointment_id} - {a.patient_name} ({a.date})": a for a in st.session_state.appointment_list}
            sel = st.selectbox("Select Appointment to Cancel", list(options.keys()))
            if st.button("❌ Cancel Appointment", type="primary"):
                st.session_state.appointment_list.remove(options[sel])
                save_appointments()
                st.markdown('<div class="success-msg">✅ Appointment cancelled.</div>', unsafe_allow_html=True)
                st.rerun()
        else:
            st.info("No appointments to cancel.")


# ─────────────────────────────────────────────
# Billing
# ─────────────────────────────────────────────
elif section == "💳 Billing":
    st.markdown('<div class="section-header">Billing & Finance</div>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🧾 Generate Bill", "📋 View All Bills"])

    with tab1:
        with st.form("gen_bill"):
            st.subheader("Generate Patient Bill")
            name = st.text_input("Patient Name")
            c1, c2, c3 = st.columns(3)
            doc_fee = c1.number_input("Doctor Fee (₹)", min_value=0, step=100)
            room_ch = c2.number_input("Room Charges (₹)", min_value=0, step=100)
            med_ch  = c3.number_input("Medicine Charges (₹)", min_value=0, step=100)
            if st.form_submit_button("🧾 Generate Bill"):
                if name:
                    bill_id = len(st.session_state.bill_list) + 1
                    b = Bill("JAN KALYAN HOSPITAL", "Bhopal", bill_id, name, int(doc_fee), int(room_ch), int(med_ch))
                    st.session_state.bill_list.append(b)
                    save_bills()
                    st.markdown(f"""
                    <div class="bill-box">
                      <h3>🏥 Jan Kalyan Hospital<br><small style="font-size:0.75rem;color:#666;">Bhopal, Madhya Pradesh</small></h3>
                      <div class="bill-row"><span>Bill ID</span><span>#{b.bill_id}</span></div>
                      <div class="bill-row"><span>Patient Name</span><span>{b.patient_name}</span></div>
                      <div class="bill-row"><span>Doctor Fee</span><span>₹{b.doctor_fee:,}</span></div>
                      <div class="bill-row"><span>Room Charges</span><span>₹{b.room_charges:,}</span></div>
                      <div class="bill-row"><span>Medicine Charges</span><span>₹{b.medicine_charges:,}</span></div>
                      <div class="bill-total"><span>TOTAL AMOUNT</span><span>₹{b.total:,}</span></div>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown('<div class="error-msg">❌ Patient name is required.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.bill_list:
            st.info("No bills generated yet.")
        else:
            for b in st.session_state.bill_list:
                st.markdown(f"""<div class="info-card">
                    <h4>{b.patient_name} &nbsp; <span class="badge">Bill #{b.bill_id}</span></h4>
                    <p>💊 Medicine: ₹{b.medicine_charges:,} &nbsp;|&nbsp; 🛏️ Room: ₹{b.room_charges:,} &nbsp;|&nbsp; 🩺 Doctor: ₹{b.doctor_fee:,}</p>
                    <p><strong>Total: ₹{b.total:,}</strong></p>
                </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Reports
# ─────────────────────────────────────────────
elif section == "📊 Reports":
    st.markdown('<div class="section-header">Hospital Reports</div>', unsafe_allow_html=True)
    total_revenue = sum(b.total for b in st.session_state.bill_list)
    c1, c2, c3 = st.columns(3)
    metrics = [
        ("👨‍⚕️", len(st.session_state.doctor_list), "Total Doctors"),
        ("🛏️", len(st.session_state.patient_list), "Total Patients"),
        ("📅", len(st.session_state.appointment_list), "Appointments"),
    ]
    for col, (icon, num, label) in zip([c1, c2, c3], metrics):
        with col:
            st.markdown(f"""<div class="report-card">
                <div style="font-size:2rem">{icon}</div>
                <div class="number">{num}</div>
                <div class="label">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5 = st.columns(2)
    with c4:
        st.markdown(f"""<div class="report-card">
            <div style="font-size:2rem">🧾</div>
            <div class="number">{len(st.session_state.bill_list)}</div>
            <div class="label">Total Bills</div>
        </div>""", unsafe_allow_html=True)
    with c5:
        st.markdown(f"""<div class="report-card">
            <div style="font-size:2rem">💰</div>
            <div class="number">₹{total_revenue:,}</div>
            <div class="label">Total Revenue</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.session_state.doctor_list:
        st.markdown("#### 👨‍⚕️ Doctors by Specialization")
        specs = {}
        for d in st.session_state.doctor_list:
            specs[d.specialization] = specs.get(d.specialization, 0) + 1
        st.bar_chart(specs)