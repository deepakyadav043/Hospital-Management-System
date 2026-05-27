import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="JAN KALYAN HOSPITAL",
    page_icon="🏥",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

.main {
    background-color: #eef2f7;
}

/* ---------- HERO SECTION ---------- */
.hero {
    position: relative;
    background-image: url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3");
    background-size: cover;
    background-position: center;
    height: 420px;
    border-radius: 20px;
    overflow: hidden;
    margin-bottom: 25px;
}

.overlay {
    background: rgba(0,0,0,0.6);
    height: 100%;
    padding: 40px;
}

.hospital-name {
    font-size: 55px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-top: 20px;
}

.tagline {
    text-align: center;
    font-size: 24px;
    color: #dcdcdc;
    margin-bottom: 30px;
}

.info-box {
    background: rgba(255,255,255,0.15);
    padding: 15px;
    border-radius: 15px;
    color: white;
    backdrop-filter: blur(5px);
}

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    color: #203a43;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================
if "doctors" not in st.session_state:
    st.session_state.doctors = []

if "patients" not in st.session_state:
    st.session_state.patients = []

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "bills" not in st.session_state:
    st.session_state.bills = []

# =========================================================
# HERO SECTION
# =========================================================
st.markdown("""
<div class="hero">
    <div class="overlay">

        <div class="hospital-name">
            🏥 JAN KALYAN HOSPITAL
        </div>

        <div class="tagline">
            Advanced Healthcare & Hospital Management System
        </div>

        <div style="display:flex; gap:20px; justify-content:center; flex-wrap:wrap;">

            <div class="info-box">
                📍 <b>Location</b><br>
                MP Nagar, Bhopal, Madhya Pradesh
            </div>

            <div class="info-box">
                📞 <b>Contact</b><br>
                +91 9876543210
            </div>

            <div class="info-box">
                ✉️ <b>Email</b><br>
                jankalyanhospital@gmail.com
            </div>

            <div class="info-box">
                🕒 <b>Opening Time</b><br>
                24 × 7 Emergency Services
            </div>

        </div>

    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2967/2967350.png",
    width=120
)

st.sidebar.title("🏥 JAN KALYAN HOSPITAL")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👨‍⚕️ Doctors",
        "🧑 Patients",
        "📅 Appointments",
        "💰 Billing",
        "📞 Hospital Information"
    ]
)

# =========================================================
# DASHBOARD
# =========================================================
if menu == "🏠 Dashboard":

    st.markdown(
        "<div class='section-title'>📊 Hospital Dashboard</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👨‍⚕️ Doctors", len(st.session_state.doctors))

    with col2:
        st.metric("🧑 Patients", len(st.session_state.patients))

    with col3:
        st.metric("📅 Appointments", len(st.session_state.appointments))

    with col4:
        st.metric("💰 Bills", len(st.session_state.bills))

    st.markdown("---")

    st.subheader("🏥 About JAN KALYAN HOSPITAL")

    st.write("""
    JAN KALYAN HOSPITAL is a modern healthcare center providing:
    
    ✅ Emergency Services  
    ✅ Specialist Doctors  
    ✅ ICU & Operation Theatre  
    ✅ Digital Patient Management  
    ✅ Online Appointment System  
    ✅ Advanced Billing System  
    """)

# =========================================================
# DOCTOR MANAGEMENT
# =========================================================
elif menu == "👨‍⚕️ Doctors":

    st.markdown(
        "<div class='section-title'>👨‍⚕️ Doctor Management</div>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["➕ Add Doctor", "📋 View Doctors"])

    # ---------- ADD ----------
    with tab1:

        with st.form("doctor_form"):

            col1, col2 = st.columns(2)

            with col1:
                doctor_name = st.text_input("Doctor Name")
                specialization = st.selectbox(
                    "Specialization",
                    [
                        "Cardiologist",
                        "Neurologist",
                        "Dentist",
                        "Orthopedic",
                        "General Physician",
                        "Pediatrician"
                    ]
                )

            with col2:
                experience = st.number_input("Experience", 0, 50)
                fee = st.number_input("Consultation Fee", 0)

            contact = st.text_input("Doctor Contact Number")
            email = st.text_input("Doctor Email")

            submit = st.form_submit_button("Add Doctor")

            if submit:

                doctor = {
                    "Doctor ID": len(st.session_state.doctors) + 1,
                    "Name": doctor_name,
                    "Specialization": specialization,
                    "Experience": experience,
                    "Fee": fee,
                    "Contact": contact,
                    "Email": email
                }

                st.session_state.doctors.append(doctor)

                st.success("✅ Doctor Added Successfully")

    # ---------- VIEW ----------
    with tab2:

        if st.session_state.doctors:

            df = pd.DataFrame(st.session_state.doctors)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.warning("No Doctors Available")

# =========================================================
# PATIENT MANAGEMENT
# =========================================================
elif menu == "🧑 Patients":

    st.markdown(
        "<div class='section-title'>🧑 Patient Management</div>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["➕ Add Patient", "📋 View Patients"])

    with tab1:

        with st.form("patient_form"):

            col1, col2 = st.columns(2)

            with col1:
                patient_name = st.text_input("Patient Name")
                age = st.number_input("Age", 0, 120)
                gender = st.selectbox(
                    "Gender",
                    ["Male", "Female", "Other"]
                )

            with col2:
                disease = st.text_input("Disease")
                room = st.text_input("Room Number")
                contact = st.text_input("Contact Number")

            address = st.text_area("Address")

            submit = st.form_submit_button("Add Patient")

            if submit:

                patient = {
                    "Patient ID": len(st.session_state.patients) + 1,
                    "Name": patient_name,
                    "Age": age,
                    "Gender": gender,
                    "Disease": disease,
                    "Room": room,
                    "Contact": contact,
                    "Address": address
                }

                st.session_state.patients.append(patient)

                st.success("✅ Patient Added Successfully")

    with tab2:

        if st.session_state.patients:

            df = pd.DataFrame(st.session_state.patients)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.warning("No Patients Available")

# =========================================================
# APPOINTMENT SYSTEM
# =========================================================
elif menu == "📅 Appointments":

    st.markdown(
        "<div class='section-title'>📅 Appointment System</div>",
        unsafe_allow_html=True
    )

    with st.form("appointment_form"):

        col1, col2 = st.columns(2)

        with col1:
            doctor = st.text_input("Doctor Name")
            patient = st.text_input("Patient Name")

        with col2:
            date = st.date_input("Appointment Date")
            time = st.time_input("Appointment Time")

        submit = st.form_submit_button("Book Appointment")

        if submit:

            appointment = {
                "Appointment ID": len(st.session_state.appointments) + 1,
                "Doctor": doctor,
                "Patient": patient,
                "Date": str(date),
                "Time": str(time)
            }

            st.session_state.appointments.append(appointment)

            st.success("✅ Appointment Booked Successfully")

    st.markdown("---")

    if st.session_state.appointments:

        df = pd.DataFrame(st.session_state.appointments)

        st.dataframe(
            df,
            use_container_width=True
        )

# =========================================================
# BILLING SYSTEM
# =========================================================
elif menu == "💰 Billing":

    st.markdown(
        "<div class='section-title'>💰 Billing System</div>",
        unsafe_allow_html=True
    )

    with st.form("bill_form"):

        patient_name = st.text_input("Patient Name")

        col1, col2, col3 = st.columns(3)

        with col1:
            doctor_fee = st.number_input("Doctor Fee", 0)

        with col2:
            room_charge = st.number_input("Room Charges", 0)

        with col3:
            medicine_charge = st.number_input("Medicine Charges", 0)

        total = doctor_fee + room_charge + medicine_charge

        submit = st.form_submit_button("Generate Bill")

        if submit:

            bill = {
                "Bill ID": len(st.session_state.bills) + 1,
                "Patient": patient_name,
                "Doctor Fee": doctor_fee,
                "Room Charges": room_charge,
                "Medicine Charges": medicine_charge,
                "Total": total
            }

            st.session_state.bills.append(bill)

            st.success(f"✅ Bill Generated Successfully | ₹{total}")

    st.markdown("---")

    if st.session_state.bills:

        df = pd.DataFrame(st.session_state.bills)

        st.dataframe(
            df,
            use_container_width=True
        )

# =========================================================
# HOSPITAL INFORMATION
# =========================================================
elif menu == "📞 Hospital Information":

    st.markdown(
        "<div class='section-title'>📞 Hospital Information</div>",
        unsafe_allow_html=True
    )

    st.info("""
🏥 Hospital Name: JAN KALYAN HOSPITAL

📍 Address:
MP Nagar Zone-2, Bhopal, Madhya Pradesh

📞 Contact Number:
+91 9876543210

✉️ Email:
jankalyanhospital@gmail.com

🕒 Opening Time:
24 × 7 Emergency Services

🚑 Ambulance:
Available 24 Hours

🩺 Facilities:
ICU, Emergency, X-Ray, MRI, Pharmacy, OPD
""")