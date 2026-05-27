import streamlit as st

# ---------------- HOSPITAL INFO ----------------
HOSPITAL_NAME = "JAN KALYAN HOSPITAL"
LOCATION = "Bhopal"

# ---------------- DATA STORAGE ----------------
doctor_list = []
patient_list = []
appointment_list = []
bill_list = []

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=HOSPITAL_NAME,
    page_icon="🏥",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    f"""
    <h1 style='text-align:center; color:#0E76A8;'>
        🏥 {HOSPITAL_NAME}
    </h1>
    <h4 style='text-align:center; color:gray;'>
        Hospital Management System
    </h4>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Doctor",
        "View Doctors",
        "Add Patient",
        "View Patients",
        "Book Appointment",
        "View Appointments",
        "Generate Bill",
        "View Bills"
    ]
)

# =========================================================
# ADD DOCTOR
# =========================================================
if menu == "Add Doctor":

    st.subheader("➕ Add Doctor")

    name = st.text_input("Doctor Name")
    specialization = st.text_input("Specialization")
    experience = st.number_input("Experience (Years)", 0, 50)
    fee = st.number_input("Consultation Fee", 0)

    if st.button("Add Doctor"):
        doctor = {
            "ID": len(doctor_list) + 1,
            "Name": name,
            "Specialization": specialization,
            "Experience": experience,
            "Fee": fee
        }

        doctor_list.append(doctor)
        st.success("Doctor Added Successfully!")

# =========================================================
# VIEW DOCTORS
# =========================================================
elif menu == "View Doctors":

    st.subheader("👨‍⚕️ Doctor List")

    if doctor_list:
        st.table(doctor_list)
    else:
        st.warning("No doctors available.")

# =========================================================
# ADD PATIENT
# =========================================================
elif menu == "Add Patient":

    st.subheader("➕ Add Patient")

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 0, 120)
    disease = st.text_input("Disease")
    room = st.text_input("Room Number")

    if st.button("Add Patient"):

        patient = {
            "ID": len(patient_list) + 1,
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Room": room
        }

        patient_list.append(patient)
        st.success("Patient Added Successfully!")

# =========================================================
# VIEW PATIENTS
# =========================================================
elif menu == "View Patients":

    st.subheader("🧑‍🤝‍🧑 Patient List")

    if patient_list:
        st.table(patient_list)
    else:
        st.warning("No patients available.")

# =========================================================
# BOOK APPOINTMENT
# =========================================================
elif menu == "Book Appointment":

    st.subheader("📅 Book Appointment")

    doctor_name = st.text_input("Doctor Name")
    patient_name = st.text_input("Patient Name")
    date = st.date_input("Appointment Date")
    time = st.time_input("Appointment Time")

    if st.button("Book Appointment"):

        appointment = {
            "ID": len(appointment_list) + 1,
            "Doctor": doctor_name,
            "Patient": patient_name,
            "Date": str(date),
            "Time": str(time)
        }

        appointment_list.append(appointment)
        st.success("Appointment Booked Successfully!")

# =========================================================
# VIEW APPOINTMENTS
# =========================================================
elif menu == "View Appointments":

    st.subheader("📋 Appointment List")

    if appointment_list:
        st.table(appointment_list)
    else:
        st.warning("No appointments available.")

# =========================================================
# GENERATE BILL
# =========================================================
elif menu == "Generate Bill":

    st.subheader("💰 Generate Bill")

    patient_name = st.text_input("Patient Name")
    doctor_fee = st.number_input("Doctor Fee", 0)
    room_charges = st.number_input("Room Charges", 0)
    medicine_charges = st.number_input("Medicine Charges", 0)

    total = doctor_fee + room_charges + medicine_charges

    if st.button("Generate Bill"):

        bill = {
            "Bill ID": len(bill_list) + 1,
            "Patient": patient_name,
            "Doctor Fee": doctor_fee,
            "Room Charges": room_charges,
            "Medicine Charges": medicine_charges,
            "Total": total
        }

        bill_list.append(bill)

        st.success("Bill Generated Successfully!")

        st.info(f"Total Amount = ₹{total}")

# =========================================================
# VIEW BILLS
# =========================================================
elif menu == "View Bills":

    st.subheader("🧾 All Bills")

    if bill_list:
        st.table(bill_list)
    else:
        st.warning("No bills available.")