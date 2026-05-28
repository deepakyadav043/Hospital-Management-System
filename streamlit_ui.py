import streamlit as st
import pandas as pd
from datetime import date, time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

.main {
    background: #f4f7fc;
}

.stApp {
    background: linear-gradient(to right, #eef2ff, #f8fafc);
}

h1, h2, h3 {
    color: #0f172a;
}

.css-1d391kg {
    background-color: #0f172a;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

.metric-title {
    font-size: 18px;
    color: gray;
}

.metric-value {
    font-size: 35px;
    font-weight: bold;
    color: #06b6d4;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
    color: #0f172a;
}

.subtitle {
    color: gray;
    font-size: 18px;
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
# SIDEBAR
# =========================================================
st.sidebar.title("🏥 Jan Kalyan Hospital")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Doctors",
        "Patients",
        "Appointments",
        "Billing",
        "Analytics"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("24x7 Emergency Service")
st.sidebar.success("Modern Hospital Dashboard")

# =========================================================
# DASHBOARD
# =========================================================
if page == "Dashboard":

    st.markdown("""
    <div class="card">
        <div class="big-title">🏥 Jan Kalyan Hospital</div>
        <div class="subtitle">
        Modern Hospital Management System
        </div>
    </div>
    """, unsafe_allow_html=True)

    total_revenue = sum([b["Total"] for b in st.session_state.bills])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Doctors</div>
            <div class="metric-value">{len(st.session_state.doctors)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Patients</div>
            <div class="metric-value">{len(st.session_state.patients)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Appointments</div>
            <div class="metric-value">{len(st.session_state.appointments)}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Revenue</div>
            <div class="metric-value">₹{total_revenue}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1586773860418-d37222d8fce3",
        use_container_width=True
    )

# =========================================================
# DOCTORS
# =========================================================
elif page == "Doctors":

    st.title("👨‍⚕️ Doctor Management")

    with st.form("doctor_form"):

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Doctor Name")

        with col2:
            specialization = st.selectbox(
                "Specialization",
                [
                    "Cardiologist",
                    "Neurologist",
                    "ENT",
                    "Orthopedic",
                    "General Physician"
                ]
            )

        experience = st.slider("Experience", 1, 40, 5)

        fee = st.number_input("Consultation Fee", 100, 5000)

        submit = st.form_submit_button("Add Doctor")

        if submit:

            st.session_state.doctors.append({
                "Name": name,
                "Specialization": specialization,
                "Experience": experience,
                "Fee": fee
            })

            st.success("Doctor Added Successfully")

    st.markdown("---")

    if st.session_state.doctors:

        doctor_df = pd.DataFrame(st.session_state.doctors)

        st.dataframe(
            doctor_df,
            use_container_width=True
        )

# =========================================================
# PATIENTS
# =========================================================
elif page == "Patients":

    st.title("🧑‍🤝‍🧑 Patient Management")

    with st.form("patient_form"):

        col1, col2 = st.columns(2)

        with col1:
            pname = st.text_input("Patient Name")

        with col2:
            age = st.number_input("Age", 1, 120)

        disease = st.text_input("Disease")

        room = st.number_input("Room Number", 1, 500)

        submit = st.form_submit_button("Add Patient")

        if submit:

            st.session_state.patients.append({
                "Name": pname,
                "Age": age,
                "Disease": disease,
                "Room": room
            })

            st.success("Patient Added Successfully")

    st.markdown("---")

    if st.session_state.patients:

        patient_df = pd.DataFrame(st.session_state.patients)

        st.dataframe(
            patient_df,
            use_container_width=True
        )

# =========================================================
# APPOINTMENTS
# =========================================================
elif page == "Appointments":

    st.title("📅 Appointment Booking")

    with st.form("appointment_form"):

        col1, col2 = st.columns(2)

        with col1:
            doctor = st.text_input("Doctor Name")

            ap_date = st.date_input(
                "Appointment Date",
                date.today()
            )

        with col2:
            patient = st.text_input("Patient Name")

            ap_time = st.time_input(
                "Appointment Time",
                time(10, 0)
            )

        submit = st.form_submit_button("Book Appointment")

        if submit:

            st.session_state.appointments.append({
                "Doctor": doctor,
                "Patient": patient,
                "Date": ap_date,
                "Time": ap_time
            })

            st.success("Appointment Booked Successfully")

    st.markdown("---")

    if st.session_state.appointments:

        app_df = pd.DataFrame(st.session_state.appointments)

        st.dataframe(
            app_df,
            use_container_width=True
        )

# =========================================================
# BILLING
# =========================================================
elif page == "Billing":

    st.title("💰 Billing System")

    with st.form("bill_form"):

        patient = st.text_input("Patient Name")

        col1, col2, col3 = st.columns(3)

        with col1:
            doctor_fee = st.number_input("Doctor Fee", 0)

        with col2:
            room_fee = st.number_input("Room Charges", 0)

        with col3:
            medicine_fee = st.number_input("Medicine Charges", 0)

        total = doctor_fee + room_fee + medicine_fee

        st.info(f"Total Amount = ₹{total}")

        submit = st.form_submit_button("Generate Bill")

        if submit:

            st.session_state.bills.append({
                "Patient": patient,
                "Doctor Fee": doctor_fee,
                "Room Fee": room_fee,
                "Medicine Fee": medicine_fee,
                "Total": total
            })

            st.success("Bill Generated Successfully")

    st.markdown("---")

    if st.session_state.bills:

        bill_df = pd.DataFrame(st.session_state.bills)

        st.dataframe(
            bill_df,
            use_container_width=True
        )

# =========================================================
# ANALYTICS
# =========================================================
elif page == "Analytics":

    st.title("📊 Hospital Analytics")

    data = pd.DataFrame({
        "Department": [
            "Cardiology",
            "Neurology",
            "ENT",
            "Orthopedic",
            "Emergency"
        ],
        "Patients": [
            120,
            80,
            60,
            90,
            150
        ]
    })

    st.subheader("Department Wise Patients")

    st.bar_chart(
        data.set_index("Department")
    )

    st.subheader("Hospital Overview")

    st.line_chart({
        "Patients": [20, 40, 70, 100, 120, 150]
    })

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    """
    <center>
    © 2026 Jan Kalyan Hospital |
    Developed with ❤️ using Streamlit
    </center>
    """,
    unsafe_allow_html=True
)