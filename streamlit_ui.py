import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="JAN KALYAN HOSPITAL",
    page_icon="🏥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 45px;
    color: white;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
}

.banner {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    padding: 30px;
    border-radius: 15px;
    margin-bottom: 25px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown(f"""
<div class="banner">
    <div class="title">🏥 JAN KALYAN HOSPITAL</div>
    <div class="subtitle">Advanced Hospital Management System</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "doctors" not in st.session_state:
    st.session_state.doctors = []

if "patients" not in st.session_state:
    st.session_state.patients = []

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "bills" not in st.session_state:
    st.session_state.bills = []

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Dashboard",
        "👨‍⚕️ Doctor Management",
        "🧑 Patient Management",
        "📅 Appointment System",
        "💰 Billing System"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================
if menu == "🏠 Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Doctors", len(st.session_state.doctors))
    col2.metric("Patients", len(st.session_state.patients))
    col3.metric("Appointments", len(st.session_state.appointments))
    col4.metric("Bills", len(st.session_state.bills))

    st.image(
        "https://images.unsplash.com/photo-1586773860418-d37222d8fce3",
        use_container_width=True
    )

# =====================================================
# DOCTOR MANAGEMENT
# =====================================================
elif menu == "👨‍⚕️ Doctor Management":

    st.subheader("👨‍⚕️ Doctor Management System")

    tab1, tab2 = st.tabs(["➕ Add Doctor", "📋 View Doctors"])

    # ---------- ADD DOCTOR ----------
    with tab1:

        with st.form("doctor_form"):

            col1, col2 = st.columns(2)

            with col1:
                doctor_name = st.text_input("Doctor Name")
                specialization = st.text_input("Specialization")

            with col2:
                experience = st.number_input("Experience", 0, 50)
                fee = st.number_input("Consultation Fee", 0)

            submit = st.form_submit_button("Add Doctor")

            if submit:

                doctor = {
                    "Doctor ID": len(st.session_state.doctors) + 1,
                    "Name": doctor_name,
                    "Specialization": specialization,
                    "Experience": experience,
                    "Fee": fee
                }

                st.session_state.doctors.append(doctor)

                st.success("✅ Doctor Added Successfully")

    # ---------- VIEW DOCTOR ----------
    with tab2:

        if st.session_state.doctors:

            df = pd.DataFrame(st.session_state.doctors)
            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No Doctors Available")

# =====================================================
# PATIENT MANAGEMENT
# =====================================================
elif menu == "🧑 Patient Management":

    st.subheader("🧑 Patient Management System")

    tab1, tab2 = st.tabs(["➕ Add Patient", "📋 View Patients"])

    # ---------- ADD PATIENT ----------
    with tab1:

        with st.form("patient_form"):

            col1, col2 = st.columns(2)

            with col1:
                patient_name = st.text_input("Patient Name")
                age = st.number_input("Age", 0, 120)

            with col2:
                disease = st.text_input("Disease")
                room = st.text_input("Room Number")

            submit = st.form_submit_button("Add Patient")

            if submit:

                patient = {
                    "Patient ID": len(st.session_state.patients) + 1,
                    "Name": patient_name,
                    "Age": age,
                    "Disease": disease,
                    "Room": room
                }

                st.session_state.patients.append(patient)

                st.success("✅ Patient Added Successfully")

    # ---------- VIEW PATIENT ----------
    with tab2:

        if st.session_state.patients:

            df = pd.DataFrame(st.session_state.patients)
            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No Patients Available")

# =====================================================
# APPOINTMENT SYSTEM
# =====================================================
elif menu == "📅 Appointment System":

    st.subheader("📅 Appointment Booking System")

    tab1, tab2 = st.tabs(["➕ Book Appointment", "📋 View Appointments"])

    # ---------- BOOK ----------
    with tab1:

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

    # ---------- VIEW ----------
    with tab2:

        if st.session_state.appointments:

            df = pd.DataFrame(st.session_state.appointments)
            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No Appointments Available")

# =====================================================
# BILLING SYSTEM
# =====================================================
elif menu == "💰 Billing System":

    st.subheader("💰 Hospital Billing System")

    tab1, tab2 = st.tabs(["➕ Generate Bill", "📋 View Bills"])

    # ---------- GENERATE ----------
    with tab1:

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
                    "Total Amount": total
                }

                st.session_state.bills.append(bill)

                st.success(f"✅ Bill Generated | Total = ₹{total}")

    # ---------- VIEW ----------
    with tab2:

        if st.session_state.bills:

            df = pd.DataFrame(st.session_state.bills)
            st.dataframe(df, use_container_width=True)

        else:
            st.warning("No Bills Available")