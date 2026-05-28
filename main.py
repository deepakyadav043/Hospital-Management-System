from getpass import getpass
class Hospital:
    def __init__(self,hospital_name,location,email_id,contact):
        self.hospital_name = hospital_name
        self.location = location
        self.email_id = email_id
        self.contact = contact

    def display(self):
        print(f"Hospital Name = {self.hospital_name}\nLocation = {self.location}\nemail_id = {self.email_id}\nContact = {self.contact}")



##Doctor class
doctor_list = []
class Doctor(Hospital):
    def __init__(self,hospital_name,location,email_id,contact,doctor_id,doctor_name,specialization,experience,fee):
        super().__init__(hospital_name,location,email_id,contact)
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
    d = Doctor("JAN KALYAN HOSPITAL","BIHAR","jankalyan@gmail.com",8989651456,doc_id,name,spec,exp,fee)
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

def delete_doctor():
    doc_id = int(input("enter Doctor ID to delete:"))

    for d in doctor_list:
        if d.doctor_id == doc_id:
            doctor_list.remove(d)
            print("Doctor Deleted!")
            return
        
    print("doctor not found")



# classes/patient.py


patient_list = []

class Patient(Hospital):
    def __init__(self, hospital_name, location,email_id,contact, patient_id,
                 patient_name, age, disease, room_number):
        super().__init__(hospital_name, location,email_id,contact)
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
    p = Patient("JAN KALYAN HOSPITAL", "BIHAR","jankalyan@gmail.com",8989651456, pat_id, name, age, disease, room)
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
    def __init__(self, hospital_name, location,email_id,contact, bill_id,
                 patient_name, doctor_fee, room_charges, medicine_charges):
        super().__init__(hospital_name, location,email_id,contact)
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
    b = Bill("JAN KALYAN HOSPITAL", "BIHAR","jankalyan@gmail.com",8789651456, bill_id, name, doc_fee, room_ch, med_ch)
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

# ── Salary Management ─────────────────────────
salary_list = []

class Salary(Hospital):
    def __init__(self, hospital_name, location, email_id, contact,
                 salary_id, employee_name, employee_type,
                 basic_salary, hra_percent, da_percent, pf_percent, month, year):
        super().__init__(hospital_name, location, email_id, contact)
        self.salary_id      = salary_id
        self.employee_name  = employee_name
        self.employee_type  = employee_type   # Doctor / Nurse / Staff
        self.basic_salary   = basic_salary
        self.hra_percent    = hra_percent      # House Rent Allowance %
        self.da_percent     = da_percent       # Dearness Allowance %
        self.pf_percent     = pf_percent       # Provident Fund deduction %
        self.month          = month
        self.year           = year

        # ── Auto-calculate ──
        self.hra            = (hra_percent / 100) * basic_salary
        self.da             = (da_percent  / 100) * basic_salary
        self.pf_deduction   = (pf_percent  / 100) * basic_salary
        self.gross_salary   = basic_salary + self.hra + self.da
        self.net_salary     = self.gross_salary - self.pf_deduction

    def display(self):
        print("\n  ======== Salary Slip ========")
        super().display()
        print(f"  Salary ID        : {self.salary_id}")
        print(f"  Employee Name    : {self.employee_name}")
        print(f"  Employee Type    : {self.employee_type}")
        print(f"  Month/Year       : {self.month}/{self.year}")
        print("  ----------------------------")
        print(f"  Basic Salary     : Rs.{self.basic_salary}")
        print(f"  HRA ({self.hra_percent}%)       : Rs.{self.hra:.2f}")
        print(f"  DA  ({self.da_percent}%)        : Rs.{self.da:.2f}")
        print(f"  Gross Salary     : Rs.{self.gross_salary:.2f}")
        print("  ----------------------------")
        print(f"  PF Deduction({self.pf_percent}%): Rs.{self.pf_deduction:.2f}")
        print("  ----------------------------")
        print(f"  NET SALARY       : Rs.{self.net_salary:.2f}")
        print("  ============================")


def add_salary_record():
    print("\n--- Add Salary Record ---")
    print("  Employee Type:")
    print("  1. Doctor")
    print("  2. Nurse")
    print("  3. Staff")
    emp_choice = input("  Choose (1/2/3): ")

    emp_types = {"1": "Doctor", "2": "Nurse", "3": "Staff"}
    emp_type = emp_types.get(emp_choice)
    if not emp_type:
        print("  ❌ Invalid choice.")
        return

    name         = input("  Employee Name      : ")
    basic        = int(input("  Basic Salary (Rs.) : "))
    hra          = float(input("  HRA %  (e.g. 10)   : "))
    da           = float(input("  DA  %  (e.g. 5)    : "))
    pf           = float(input("  PF  %  (e.g. 12)   : "))
    month        = input("  Month (e.g. June)  : ")
    year         = input("  Year  (e.g. 2025)  : ")

    sal_id = len(salary_list) + 1
    s = Salary("JAN KALYAN HOSPITAL", "BIHAR", "jankalyan@gmail.com", 8989651456,
               sal_id, name, emp_type, basic, hra, da, pf, month, year)
    salary_list.append(s)
    s.display()
    print("✅ Salary Record Added!")


def view_all_salaries():
    print("\n--- All Salary Records ---")
    if not salary_list:
        print("  No salary records found.")
        return
    for s in salary_list:
        s.display()


def search_salary():
    print("\n--- Search Salary ---")
    name = input("  Enter Employee Name : ").lower()
    found = False
    for s in salary_list:
        if name in s.employee_name.lower():
            s.display()
            found = True
    if not found:
        print("  ❌ No record found.")


def calculate_monthly_salary():
    """Quick calculator — doesn't save, just shows breakdown."""
    print("\n--- Monthly Salary Calculator ---")
    basic = int(input("  Basic Salary (Rs.) : "))
    hra   = float(input("  HRA %              : "))
    da    = float(input("  DA  %              : "))
    pf    = float(input("  PF  %              : "))

    hra_amt  = (hra / 100) * basic
    da_amt   = (da  / 100) * basic
    pf_amt   = (pf  / 100) * basic
    gross    = basic + hra_amt + da_amt
    net      = gross - pf_amt

    print(f"\n  Basic Salary    : Rs.{basic}")
    print(f"  HRA ({hra}%)      : Rs.{hra_amt:.2f}")
    print(f"  DA  ({da}%)       : Rs.{da_amt:.2f}")
    print(f"  Gross Salary    : Rs.{gross:.2f}")
    print(f"  PF  ({pf}%)       : Rs.{pf_amt:.2f}")
    print(f"  NET Salary      : Rs.{net:.2f}")


def delete_salary_record():
    sal_id = int(input("  Enter Salary ID to delete : "))
    for s in salary_list:
        if s.salary_id == sal_id:
            salary_list.remove(s)
            print("✅ Salary Record Deleted!")
            return
    print("  ❌ Record not found.")


##========Login System ======#####

admin_username = "admin"
admin_password = "admin@234"

doctor_username = "doctor"
doctor_password = "doctor@459"

reception_username = "reception"
reception_password = "recep@389"

#now
def login():

    print("\n====Hospital login System")
    print("1.Admin login\n2.Doctor login\n3.Reception login")


    choice = input("\nEnter Login Page")

    username = input("Enter Username")
    password = getpass("Enter Password")


    ## ======== Admin Login=======##
    if choice == "1":
        
        if username == admin_username and password == admin_password:
            print("\n Admin Login successfuly")
            return "admin"
        
        else:
            print("\n Invalid admin credentials")
            return None
        
    ##=======Doctor login ========##
    elif choice == "2":
        if username == doctor_username and password == doctor_password:
            print("\n Doctor login successfully")
            return "doctor"
        
        else:
            print("\n Invalid Doctor Credentials")
            return None
        

    ##======Reception Login======###
    elif choice == "3":
        if username == reception_username and password == reception_password:
            print("\nReception Login successfully")

            return "reception"
        
        else:
            print("\nInvalid Reception Credentials")
            return None

    else:
        print("\nInvalid Login Choice")
        return None
    
user_role = login()

if user_role:

    print(f"\n====== Welcome{user_role.upper()}======")

    while True:

        print("\n====== Hospital Management System ======")

        # ADMIN MENU
        if user_role == "admin":

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
            print("12. Delete Doctor")
            print("13. Add Salary Record")       
            print("14. View All Salaries")      
            print("15. Search Salary")           
            print("16. Monthly Salary Calculator") 
            print("17. Delete Salary Record")    
            print("0.  Exit")

        # DOCTOR MENU
        elif user_role == "doctor":

            print("1. View All Patients")
            print("2. Search Patient")
            print("3. View Appointments")
            print("0. Exit")

        # RECEPTION MENU
        elif user_role == "reception":

            print("1. Add Patient")
            print("2. View Patients")
            print("3. Book Appointment")
            print("4. Generate Bill")
            print("0. Exit")


        choice = input("\nEnter your choice: ")


# ================= ADMIN =================

        if user_role == "admin":

            if choice == "1":
                add_doctor()

            elif choice == "2":
                view_doctors()

            elif choice == "3":
                search_doctor()

            elif choice == "4":
                add_patient()

            elif choice == "5":
                view_patients()

            elif choice == "6":
                search_patient()

            elif choice == "7":
                book_appointment()

            elif choice == "8":
                view_appointments()

            elif choice == "9":
                search_appointment()

            elif choice == "10":
                generate_bill()

            elif choice == "11":
                view_bills()

            elif choice == "12":
                delete_doctor()

            elif choice == "13":
                add_salary_record()

            elif choice == "14":
                view_all_salaries()

            elif choice == "15":
                search_salary()

            elif choice == "16":
                calculate_monthly_salary()

            elif choice == "17":
                delete_salary_record()

            elif choice == "0":
                print("Goodbye Admin!")
                break

            else:
                print("❌ Invalid Choice")


        # ================= DOCTOR =================

        elif user_role == "doctor":

            if choice == "1":
                view_patients()

            elif choice == "2":
                search_patient()

            elif choice == "3":
                view_appointments()

            elif choice == "0":
                print("Goodbye Doctor!")
                break

            else:
                print("❌ Access Denied or Invalid Choice")


        # ================= RECEPTION =================

        elif user_role == "reception":

            if choice == "1":
                add_patient()

            elif choice == "2":
                view_patients()

            elif choice == "3":
                book_appointment()

            elif choice == "4":
                generate_bill()

            elif choice == "0":
                print("Goodbye Receptionist!")
                break

            else:
                print("❌ Access Denied or Invalid Choice")