class Hospital:
    def __init__(self,hospital_name,location):
        self.hospital_name = hospital_name
        self.location = location

    def display(self):
        print(f"Hospital Name = {self.hospital_name}\nLocation = {self.location}")


##Doctor class
doctor_list = []
class Doctor(Hospital):
    def __init__(self,hospital_name,location,doctor_id,doctor_name,specialization,experience,fee):
        super().__init__(hospital_name,location)
        self.doctor_id      = doctor_id
        self.doctor_name    = doctor_name
        self.specialization = specialization
        self.experience     = experience
        self.fee            = fee

    def display(self):
        print("-------- Doctor Details --------")
        super().display()
        print(f"Doctor ID:      {self.doctor_id}")
        print(f"Doctor Name:    {self.doctor_name}")
        print(f"Specialization: {self.specialization}")
        print(f"Experience:     {self.experience} years")
        print(f"Fee:            ₹{self.fee}")
        print("--------------------------------")

def add_doctor():
    print("\n--- Add Doctor ---")
    name = input("Doctor Name:")
    spec = input("Specialization:")
    exp = int(input("Experience (years):"))
    fee = int(input("fee:"))
    doc_id = len(doctor_list) + 1
    d = Doctor("AIIMS","Delhi",doc_id,name,spec,exp,fee)
    doctor_list.append(d)
    print("Doctor Added!")

def view_doctors():
    if not doctor_list:
        print("No doctors found")
    for d in doctor_list:
        d.display()

def search_doctor():
    print("\n--- Search Doctor ---")
    name = input("  Enter Doctor Name : ").lower()
    found = False

    for d in doctor_list:
        if name in d.doctor_name.lower():  # naam match karo
            d.display()
            found = True

    if not found:
        print("  ❌ Doctor not found.")


# classes/patient.py


patient_list = []

class Patient(Hospital):
    def __init__(self, hospital_name, location, patient_id,
                 patient_name, age, disease, room_number):
        super().__init__(hospital_name, location)
        self.patient_id   = patient_id
        self.patient_name = patient_name
        self.age          = age
        self.disease      = disease
        self.room_number  = room_number

    def display(self):
        print("-------- Patient Details --------")
        super().display()
        print(f"Patient ID:   {self.patient_id}")
        print(f"Patient Name: {self.patient_name}")
        print(f"Age:          {self.age}")
        print(f"Disease:      {self.disease}")
        print(f"Room Number:  {self.room_number}")
        print("---------------------------------")


def add_patient():
    print("\n--- Add Patient ---")
    name   = input("Patient Name: ")
    age    = int(input("Age: "))
    disease = input("Disease: ")
    room   = input("Room Number: ")
    pat_id = len(patient_list) + 1
    p = Patient("AIIMS", "Delhi", pat_id, name, age, disease, room)
    patient_list.append(p)
    print("✅ Patient Added!")


def view_patients():
    if not patient_list:
        print("No patients found.")
    for p in patient_list:
        p.display()


def search_patient():
    print("\n--- Search Patient ---")
    print("  1. Search by Name")
    print("  2. Search by ID")
    choice = input("  Enter choice : ")
    found = False

    if choice == "1":
        name = input("  Enter Patient Name : ").lower()
        for p in patient_list:
            if name in p.patient_name.lower():  # naam match karo
                p.display()
                found = True

    elif choice == "2":
        pat_id = int(input("  Enter Patient ID : "))
        for p in patient_list:
            if p.patient_id == pat_id:          # ID match karo
                p.display()
                found = True

    if not found:
        print("  ❌ Patient not found.")

# classes/appointment.py

appointment_list = []

class Appointment:
    def __init__(self, appointment_id, doctor_name,
                 patient_name, date, time):
        self.appointment_id = appointment_id
        self.doctor_name    = doctor_name
        self.patient_name   = patient_name
        self.date           = date
        self.time           = time

    def display(self):
        print("-------- Appointment Details --------")
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Doctor:         {self.doctor_name}")
        print(f"Patient:        {self.patient_name}")
        print(f"Date:           {self.date}")
        print(f"Time:           {self.time}")
        print("-------------------------------------")


def book_appointment():
    print("\n--- Book Appointment ---")
    doc  = input("Doctor Name: ")
    pat  = input("Patient Name: ")
    date = input("Date (DD-MM-YYYY): ")
    time = input("Time (e.g. 10:00 AM): ")
    appt_id = len(appointment_list) + 1
    a = Appointment(appt_id, doc, pat, date, time)
    appointment_list.append(a)
    print("✅ Appointment Booked!")


def view_appointments():
    if not appointment_list:
        print("No appointments found.")
    for a in appointment_list:
        a.display()


def search_appointment():
    print("\n--- Search Appointment ---")
    date = input("  Enter Date (DD-MM-YYYY) : ")
    found = False

    for a in appointment_list:
        if a.date == date:              # date match karo
            a.display()
            found = True

    if not found:
        print("  ❌ No appointment found on this date.")

# ── Bill ──────────────────────────────────────
bill_list = []

class Bill(Hospital):
    def __init__(self, hospital_name, location, bill_id,
                 patient_name, doctor_fee, room_charges, medicine_charges):
        super().__init__(hospital_name, location)
        self.bill_id           = bill_id
        self.patient_name      = patient_name
        self.doctor_fee        = doctor_fee
        self.room_charges      = room_charges
        self.medicine_charges  = medicine_charges
        self.total             = doctor_fee + room_charges + medicine_charges

    def display(self):
        print("\n  ======== Bill Details ========")
        super().display()
        print(f"  Bill ID           : {self.bill_id}")
        print(f"  Patient Name      : {self.patient_name}")
        print(f"  Doctor Fee        : Rs.{self.doctor_fee}")
        print(f"  Room Charges      : Rs.{self.room_charges}")
        print(f"  Medicine Charges  : Rs.{self.medicine_charges}")
        print("  ------------------------------")
        print(f"  Total Amount      : Rs.{self.total}")
        print("  ==============================")


def generate_bill():
    print("\n--- Generate Bill ---")
    name    = input("  Patient Name        : ")
    doc_fee = int(input("  Doctor Fee          : "))
    room_ch = int(input("  Room Charges        : "))
    med_ch  = int(input("  Medicine Charges    : "))
    bill_id = len(bill_list) + 1
    b = Bill("AIIMS", "Delhi", bill_id, name, doc_fee, room_ch, med_ch)
    bill_list.append(b)
    b.display()
    print("✅ Bill Generated!")


def view_bills():
    print("\n--- All Bills ---")
    if not bill_list:
        print("  No bills found.")
        return
    for b in bill_list:
        b.display()



while True:
    print("\n====== Hospital Management System ======")
    print("1.  Add Doctor")
    print("2.  View All Doctors")
    print("3.  Search Doctor")           
    print("4.  Add Patient")
    print("5.  View All Patients")
    print("6.  Search Patient")          
    print("7.  Book Appointment")
    print("8.  View All Appointments")
    print("9.  Search Appointment")      
    print("10. Generate Bill")
    print("11. View All Bills")
    print("0.  Exit")

    choice = input("\nEnter your choice: ")

    if   choice == "1":  add_doctor()
    elif choice == "2":  view_doctors()
    elif choice == "3":  search_doctor()       
    elif choice == "4":  add_patient()
    elif choice == "5":  view_patients()
    elif choice == "6":  search_patient()      
    elif choice == "7":  book_appointment()
    elif choice == "8":  view_appointments()
    elif choice == "9":  search_appointment()  
    elif choice == "10": generate_bill()
    elif choice == "11": view_bills()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice!")