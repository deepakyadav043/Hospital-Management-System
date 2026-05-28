bash

cat > /mnt/user-data/outputs/hospital_advanced.py << 'PYEOF'
import streamlit as st
import csv, os
from datetime import datetime

st.set_page_config(page_title="AIIMS Hospital System", page_icon="🏥", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*{font-family:'Inter',sans-serif;margin:0;padding:0;box-sizing:border-box;}
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:#0f1117;}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"]{background:#161b27!important;border-right:1px solid #1e2740!important;}
section[data-testid="stSidebar"] *{color:#94a3b8!important;}

/* ── MAIN BG ── */
.block-container{padding:1.5rem 2rem!important;background:#0f1117;}

/* ── METRIC CARDS ── */
.metric-card{background:linear-gradient(135deg,#1e2740,#1a2235);border:1px solid #2a3a5c;border-radius:16px;padding:1.4rem 1.6rem;position:relative;overflow:hidden;}
.metric-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
.mc-blue::before{background:linear-gradient(90deg,#3b82f6,#60a5fa);}
.mc-green::before{background:linear-gradient(90deg,#10b981,#34d399);}
.mc-purple::before{background:linear-gradient(90deg,#8b5cf6,#a78bfa);}
.mc-orange::before{background:linear-gradient(90deg,#f59e0b,#fbbf24);}
.mc-red::before{background:linear-gradient(90deg,#ef4444,#f87171);}
.metric-icon{font-size:1.8rem;margin-bottom:0.5rem;}
.metric-val{font-size:2.2rem;font-weight:800;color:#f1f5f9;}
.metric-label{font-size:0.78rem;color:#64748b;font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-top:0.2rem;}
.metric-sub{font-size:0.75rem;color:#22c55e;margin-top:0.4rem;}

/* ── SECTION TITLE ── */
.sec-title{font-size:1.4rem;font-weight:700;color:#f1f5f9;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.6rem;}
.sec-title span{font-size:1.2rem;}

/* ── CARDS ── */
.glass-card{background:#161b27;border:1px solid #1e2740;border-radius:16px;padding:1.5rem;margin-bottom:1rem;}

/* ── TABLE ── */
.modern-table{width:100%;border-collapse:collapse;font-size:0.85rem;}
.modern-table thead tr{background:#1e2740;}
.modern-table thead th{padding:0.8rem 1rem;text-align:left;color:#94a3b8;font-weight:600;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.5px;}
.modern-table tbody tr{border-bottom:1px solid #1e2740;transition:background 0.15s;}
.modern-table tbody tr:hover{background:#1a2235;}
.modern-table tbody td{padding:0.8rem 1rem;color:#cbd5e1;}

/* ── BADGES ── */
.badge{display:inline-block;padding:0.2rem 0.75rem;border-radius:20px;font-size:0.75rem;font-weight:600;}
.b-blue{background:#1e3a5f;color:#60a5fa;}
.b-green{background:#064e3b;color:#34d399;}
.b-orange{background:#451a03;color:#fbbf24;}
.b-red{background:#450a0a;color:#f87171;}
.b-purple{background:#2e1065;color:#a78bfa;}

/* ── INPUTS ── */
label{color:#94a3b8!important;font-size:0.85rem!important;font-weight:600!important;}
.stTextInput>div>div>input,.stNumberInput>div>div>input,.stTextArea textarea,.stSelectbox>div>div{background:#1e2740!important;border:1.5px solid #2a3a5c!important;border-radius:10px!important;color:#f1f5f9!important;font-family:'Inter',sans-serif!important;}
.stTextInput>div>div>input:focus,.stNumberInput>div>div>input:focus{border-color:#3b82f6!important;box-shadow:0 0 0 3px rgba(59,130,246,0.15)!important;}

/* ── BUTTONS ── */
.stButton>button{background:linear-gradient(135deg,#2563eb,#3b82f6)!important;color:white!important;border:none!important;border-radius:10px!important;font-weight:600!important;font-family:'Inter',sans-serif!important;padding:0.6rem 1.5rem!important;width:100%!important;transition:all 0.2s!important;}
.stButton>button:hover{transform:translateY(-1px)!important;box-shadow:0 6px 20px rgba(59,130,246,0.4)!important;}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"]{background:#161b27;border-radius:12px;padding:0.3rem;gap:0.3rem;border:1px solid #1e2740;}
.stTabs [data-baseweb="tab"]{background:transparent;border-radius:8px;color:#64748b!important;font-weight:600;font-size:0.85rem;padding:0.5rem 1.2rem;}
.stTabs [aria-selected="true"]{background:#1e2740!important;color:#f1f5f9!important;}

/* ── RESULT BOXES ── */
.res-ok{background:#052e16;border:1px solid #16a34a;border-radius:12px;padding:1rem 1.2rem;color:#4ade80;}
.res-fail{background:#1c0606;border:1px solid #dc2626;border-radius:12px;padding:1rem 1.2rem;color:#f87171;}

/* ── BILL RECEIPT ── */
.receipt{background:#161b27;border:1px solid #2a3a5c;border-radius:16px;padding:2rem;max-width:480px;margin:1rem auto;}
.receipt-header{text-align:center;border-bottom:1px dashed #2a3a5c;padding-bottom:1rem;margin-bottom:1rem;}
.receipt-row{display:flex;justify-content:space-between;padding:0.45rem 0;border-bottom:1px solid #1e2740;color:#94a3b8;font-size:0.9rem;}
.receipt-row span:last-child{color:#f1f5f9;font-weight:500;}
.receipt-total{display:flex;justify-content:space-between;padding:0.8rem 0 0 0;font-weight:800;font-size:1.1rem;}

/* ── REPORT CARD ── */
.report-card{background:#161b27;border:1px solid #1e2740;border-radius:14px;padding:1.2rem 1.5rem;display:flex;align-items:center;gap:1rem;margin-bottom:0.8rem;}
.report-card-icon{font-size:2rem;background:#1e2740;border-radius:10px;padding:0.5rem 0.8rem;}
.report-card-info h4{color:#f1f5f9;font-size:1rem;font-weight:700;}
.report-card-info p{color:#64748b;font-size:0.8rem;margin-top:0.2rem;}
.report-card-val{margin-left:auto;font-size:1.8rem;font-weight:800;color:#3b82f6;}

/* ── SEARCH BOX ── */
.search-result{background:#1a2235;border-left:4px solid #3b82f6;border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.5rem;color:#cbd5e1;font-size:0.88rem;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Classes
# ─────────────────────────────────────────────
class Hospital:
    def __init__(self,h,l): self.hospital_name=h; self.location=l

class Doctor(Hospital):
    def __init__(self,hname,loc,did,dname,spec,exp,fee):
        super().__init__(hname,loc)
        self.doctor_id=did;self.doctor_name=dname;self.specialization=spec;self.experience=exp;self.fee=fee

class Patient(Hospital):
    def __init__(self,hname,loc,pid,pname,age,disease,room):
        super().__init__(hname,loc)
        self.patient_id=pid;self.patient_name=pname;self.age=age;self.disease=disease;self.room_number=room

class Appointment:
    def __init__(self,aid,doc,pat,date,time):
        self.appointment_id=aid;self.doctor_name=doc;self.patient_name=pat;self.date=date;self.time=time

class Bill(Hospital):
    def __init__(self,hname,loc,bid,pname,dfee,rcharge,mcharge):
        super().__init__(hname,loc)
        self.bill_id=bid;self.patient_name=pname;self.doctor_fee=dfee
        self.room_charges=rcharge;self.medicine_charges=mcharge
        self.total=dfee+rcharge+mcharge

# ─────────────────────────────────────────────
# CSV Save / Load
# ─────────────────────────────────────────────
def save_doctors():
    with open("doctors.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["doctor_id","doctor_name","specialization","experience","fee"])
        for d in st.session_state.doctors: w.writerow([d.doctor_id,d.doctor_name,d.specialization,d.experience,d.fee])

def save_patients():
    with open("patients.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["patient_id","patient_name","age","disease","room_number"])
        for p in st.session_state.patients: w.writerow([p.patient_id,p.patient_name,p.age,p.disease,p.room_number])

def save_appointments():
    with open("appointments.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["appointment_id","doctor_name","patient_name","date","time"])
        for a in st.session_state.appointments: w.writerow([a.appointment_id,a.doctor_name,a.patient_name,a.date,a.time])

def save_bills():
    with open("bills.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["bill_id","patient_name","doctor_fee","room_charges","medicine_charges","total"])
        for b in st.session_state.bills: w.writerow([b.bill_id,b.patient_name,b.doctor_fee,b.room_charges,b.medicine_charges,b.total])

def load_all():
    if "loaded" not in st.session_state:
        st.session_state.doctors=[]
        st.session_state.patients=[]
        st.session_state.appointments=[]
        st.session_state.bills=[]
        if os.path.exists("doctors.csv"):
            for r in csv.DictReader(open("doctors.csv")):
                st.session_state.doctors.append(Doctor("AIIMS","Delhi",int(r["doctor_id"]),r["doctor_name"],r["specialization"],int(r["experience"]),int(r["fee"])))
        if os.path.exists("patients.csv"):
            for r in csv.DictReader(open("patients.csv")):
                st.session_state.patients.append(Patient("AIIMS","Delhi",int(r["patient_id"]),r["patient_name"],int(r["age"]),r["disease"],r["room_number"]))
        if os.path.exists("appointments.csv"):
            for r in csv.DictReader(open("appointments.csv")):
                st.session_state.appointments.append(Appointment(int(r["appointment_id"]),r["doctor_name"],r["patient_name"],r["date"],r["time"]))
        if os.path.exists("bills.csv"):
            for r in csv.DictReader(open("bills.csv")):
                st.session_state.bills.append(Bill("AIIMS","Delhi",int(r["bill_id"]),r["patient_name"],int(r["doctor_fee"]),int(r["room_charges"]),int(r["medicine_charges"]))))
        st.session_state.loaded=True

load_all()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 0 1rem 0;border-bottom:1px solid #1e2740;margin-bottom:1.5rem;">
        <div style="font-size:3rem">🏥</div>
        <div style="font-weight:800;font-size:1.1rem;color:#f1f5f9;margin-top:0.5rem;">AIIMS Hospital</div>
        <div style="font-size:0.75rem;color:#64748b;margin-top:0.2rem;">Management System</div>
    </div>
    """, unsafe_allow_html=True)

    pages = {
        "📊 Dashboard":    "Dashboard",
        "👨‍⚕️ Doctors":    "Doctors",
        "🤒 Patients":     "Patients",
        "📅 Appointments": "Appointments",
        "🧾 Billing":      "Billing",
        "📈 Reports":      "Reports",
    }

    if "page" not in st.session_state: st.session_state.page="Dashboard"

    for label, key in pages.items():
        active_style = "background:#1e2740;color:#f1f5f9!important;" if st.session_state.page==key else ""
        st.markdown(f'<div style="padding:0.1rem 0">', unsafe_allow_html=True)
        if st.button(label, key=f"sb_{key}", use_container_width=True):
            st.session_state.page=key; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="position:absolute;bottom:2rem;left:1rem;right:1rem;border-top:1px solid #1e2740;padding-top:1rem;">
        <div style="font-size:0.75rem;color:#475569;text-align:center;">
            📍 AIIMS, New Delhi<br>📞 011-26588500<br>
            <span style="color:#22c55e">● System Online</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

page = st.session_state.page

# ─────────────────────────────────────────────
# Helper: render table
# ─────────────────────────────────────────────
def render_table(headers, rows):
    th = "".join(f'<th style="padding:0.8rem 1rem;text-align:left;color:#64748b;font-weight:600;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.5px;background:#1e2740">{h}</th>' for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f'<td style="padding:0.8rem 1rem;color:#cbd5e1;border-bottom:1px solid #1e2740">{c}</td>' for c in row)
        trs += f'<tr style="transition:background 0.15s" onmouseover="this.style.background=\'#1a2235\'" onmouseout="this.style.background=\'transparent\'">{tds}</tr>'
    st.markdown(f'<div style="overflow-x:auto;border-radius:12px;border:1px solid #1e2740"><table style="width:100%;border-collapse:collapse;font-size:0.85rem"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════
if page == "Dashboard":
    st.markdown('<div class="sec-title"><span>📊</span> Dashboard Overview</div>', unsafe_allow_html=True)

    total_rev = sum(b.total for b in st.session_state.bills)
    c1,c2,c3,c4,c5 = st.columns(5)
    cards = [
        (c1,"mc-blue","👨‍⚕️",len(st.session_state.doctors),"Total Doctors","Active Staff"),
        (c2,"mc-green","🤒",len(st.session_state.patients),"Total Patients","Registered"),
        (c3,"mc-purple","📅",len(st.session_state.appointments),"Appointments","Scheduled"),
        (c4,"mc-orange","🧾",len(st.session_state.bills),"Bills Generated","Invoices"),
        (c5,"mc-red","💰",f"₹{total_rev:,}","Total Revenue","Collected"),
    ]
    for col,cls,icon,val,label,sub in cards:
        with col:
            st.markdown(f'<div class="metric-card {cls}"><div class="metric-icon">{icon}</div><div class="metric-val">{val}</div><div class="metric-label">{label}</div><div class="metric-sub">↑ {sub}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title"><span>👨‍⚕️</span> Recent Doctors</div>', unsafe_allow_html=True)
        if st.session_state.doctors:
            rows = [[f'<span class="badge b-blue">#{d.doctor_id}</span>',f'<b style="color:#f1f5f9">{d.doctor_name}</b>',f'<span class="badge b-purple">{d.specialization}</span>',f'<span style="color:#fbbf24">₹{d.fee}</span>'] for d in st.session_state.doctors[-5:]]
            render_table(["ID","Name","Specialization","Fee"], rows)
        else: st.markdown('<p style="color:#475569;font-size:0.9rem">No doctors added yet.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title"><span>🤒</span> Recent Patients</div>', unsafe_allow_html=True)
        if st.session_state.patients:
            rows = [[f'<span class="badge b-green">#{p.patient_id}</span>',f'<b style="color:#f1f5f9">{p.patient_name}</b>',str(p.age),f'<span class="badge b-red">{p.disease}</span>',f'Room {p.room_number}'] for p in st.session_state.patients[-5:]]
            render_table(["ID","Name","Age","Disease","Room"], rows)
        else: st.markdown('<p style="color:#475569;font-size:0.9rem">No patients added yet.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.appointments:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title"><span>📅</span> Upcoming Appointments</div>', unsafe_allow_html=True)
        rows = [[f'<span class="badge b-blue">#{a.appointment_id}</span>',a.doctor_name,a.patient_name,f'<span class="badge b-green">{a.date}</span>',a.time] for a in st.session_state.appointments[-5:]]
        render_table(["ID","Doctor","Patient","Date","Time"], rows)
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# DOCTORS
# ═══════════════════════════════════════════
elif page == "Doctors":
    st.markdown('<div class="sec-title"><span>👨‍⚕️</span> Doctor Management</div>', unsafe_allow_html=True)
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["➕ Add","📋 View All","🔍 Search","✏️ Update Fee","🗑️ Delete"])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            dname = st.text_input("Doctor Name", placeholder="Dr. Rajesh Kumar")
            dexp  = st.number_input("Experience (years)", 0, 50, 10)
        with c2:
            dspec = st.text_input("Specialization", placeholder="Cardiologist")
            dfee  = st.number_input("Consultation Fee (₹)", 0, 10000, 500, 50)
        if st.button("✅ Add Doctor"):
            if dname.strip() and dspec.strip():
                did = len(st.session_state.doctors)+1
                st.session_state.doctors.append(Doctor("AIIMS","Delhi",did,dname,dspec,dexp,dfee))
                save_doctors()
                st.markdown(f'<div class="res-ok">✅ <b>Dr. {dname}</b> added successfully! ID: #{did}</div>', unsafe_allow_html=True)
                st.rerun()
            else: st.warning("Fill Name & Specialization.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if st.session_state.doctors:
            rows = [[f'<span class="badge b-blue">#{d.doctor_id}</span>',f'<b style="color:#f1f5f9">{d.doctor_name}</b>',f'<span class="badge b-purple">{d.specialization}</span>',f'{d.experience} yrs',f'<span style="color:#fbbf24;font-weight:700">₹{d.fee}</span>',d.hospital_name] for d in st.session_state.doctors]
            render_table(["ID","Name","Specialization","Experience","Fee","Hospital"], rows)
        else: st.markdown('<p style="color:#475569">No doctors found.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        q = st.text_input("Search Doctor by Name", placeholder="Type doctor name...")
        if st.button("🔍 Search"):
            res = [d for d in st.session_state.doctors if q.lower() in d.doctor_name.lower()]
            if res:
                for d in res:
                    st.markdown(f'<div class="search-result">🩺 <b style="color:#f1f5f9">{d.doctor_name}</b> &nbsp;|&nbsp; <span class="badge b-purple">{d.specialization}</span> &nbsp;|&nbsp; {d.experience} yrs &nbsp;|&nbsp; <span style="color:#fbbf24">₹{d.fee}</span></div>', unsafe_allow_html=True)
            else: st.markdown('<div class="res-fail">❌ Doctor not found.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        uid = st.number_input("Enter Doctor ID to Update", min_value=1, step=1)
        match = next((d for d in st.session_state.doctors if d.doctor_id==uid), None)
        if match:
            st.markdown(f'<div class="search-result">Found: <b style="color:#f1f5f9">{match.doctor_name}</b> — Current Fee: <span style="color:#fbbf24">₹{match.fee}</span></div>', unsafe_allow_html=True)
            new_fee = st.number_input("New Fee (₹)", 0, 10000, match.fee, 50)
            if st.button("✏️ Update Fee"):
                match.fee = new_fee; save_doctors()
                st.markdown('<div class="res-ok">✅ Fee updated successfully!</div>', unsafe_allow_html=True)
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        del_id = st.number_input("Enter Doctor ID to Delete", min_value=1, step=1, key="del_doc")
        match = next((d for d in st.session_state.doctors if d.doctor_id==del_id), None)
        if match:
            st.markdown(f'<div class="search-result">⚠️ Will delete: <b style="color:#f87171">{match.doctor_name}</b> — {match.specialization}</div>', unsafe_allow_html=True)
            if st.button("🗑️ Confirm Delete"):
                st.session_state.doctors.remove(match); save_doctors()
                st.markdown('<div class="res-ok">✅ Doctor deleted.</div>', unsafe_allow_html=True)
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# PATIENTS
# ═══════════════════════════════════════════
elif page == "Patients":
    st.markdown('<div class="sec-title"><span>🤒</span> Patient Management</div>', unsafe_allow_html=True)
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["➕ Add","📋 View All","🔍 Search","✏️ Update Room","🗑️ Delete"])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            pname   = st.text_input("Patient Name", placeholder="Rahul Verma")
            pdisease= st.text_input("Disease", placeholder="Fever / Diabetes")
        with c2:
            page_age= st.number_input("Age", 1, 120, 30)
            proom   = st.text_input("Room Number", placeholder="101-A")
        if st.button("✅ Add Patient"):
            if pname.strip() and pdisease.strip() and proom.strip():
                pid = len(st.session_state.patients)+1
                st.session_state.patients.append(Patient("AIIMS","Delhi",pid,pname,page_age,pdisease,proom))
                save_patients()
                st.markdown(f'<div class="res-ok">✅ Patient <b>{pname}</b> admitted. ID: #{pid}</div>', unsafe_allow_html=True)
                st.rerun()
            else: st.warning("Fill all fields.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if st.session_state.patients:
            rows = [[f'<span class="badge b-green">#{p.patient_id}</span>',f'<b style="color:#f1f5f9">{p.patient_name}</b>',str(p.age),f'<span class="badge b-red">{p.disease}</span>',f'<span class="badge b-orange">Room {p.room_number}</span>'] for p in st.session_state.patients]
            render_table(["ID","Name","Age","Disease","Room"], rows)
        else: st.markdown('<p style="color:#475569">No patients found.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        sb = st.radio("Search by", ["Name","ID"], horizontal=True)
        if sb=="Name":
            q = st.text_input("Patient Name")
            if st.button("🔍 Search"):
                res=[p for p in st.session_state.patients if q.lower() in p.patient_name.lower()]
                if res:
                    for p in res: st.markdown(f'<div class="search-result">🤒 <b style="color:#f1f5f9">{p.patient_name}</b> | Age:{p.age} | <span class="badge b-red">{p.disease}</span> | Room {p.room_number}</div>', unsafe_allow_html=True)
                else: st.markdown('<div class="res-fail">❌ Patient not found.</div>', unsafe_allow_html=True)
        else:
            pid2=st.number_input("Patient ID",1,step=1)
            if st.button("🔍 Search"):
                res=[p for p in st.session_state.patients if p.patient_id==pid2]
                if res:
                    p=res[0]; st.markdown(f'<div class="search-result">🤒 <b style="color:#f1f5f9">{p.patient_name}</b> | Age:{p.age} | {p.disease} | Room {p.room_number}</div>', unsafe_allow_html=True)
                else: st.markdown('<div class="res-fail">❌ Not found.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        uid=st.number_input("Patient ID to Update Room",1,step=1,key="upd_pat")
        match=next((p for p in st.session_state.patients if p.patient_id==uid),None)
        if match:
            st.markdown(f'<div class="search-result">Found: <b style="color:#f1f5f9">{match.patient_name}</b> — Current Room: <span class="badge b-orange">{match.room_number}</span></div>', unsafe_allow_html=True)
            new_room=st.text_input("New Room Number")
            if st.button("✏️ Update Room"):
                match.room_number=new_room; save_patients()
                st.markdown('<div class="res-ok">✅ Room updated!</div>', unsafe_allow_html=True); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        del_id=st.number_input("Patient ID to Delete",1,step=1,key="del_pat")
        match=next((p for p in st.session_state.patients if p.patient_id==del_id),None)
        if match:
            st.markdown(f'<div class="search-result">⚠️ Will discharge: <b style="color:#f87171">{match.patient_name}</b></div>', unsafe_allow_html=True)
            if st.button("🗑️ Confirm Delete"):
                st.session_state.patients.remove(match); save_patients()
                st.markdown('<div class="res-ok">✅ Patient removed.</div>', unsafe_allow_html=True); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# APPOINTMENTS
# ═══════════════════════════════════════════
elif page == "Appointments":
    st.markdown('<div class="sec-title"><span>📅</span> Appointment Management</div>', unsafe_allow_html=True)
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["📅 Book","📋 View All","🔍 Search by Date","✏️ Update","❌ Cancel"])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        c1,c2=st.columns(2)
        with c1:
            adoc =st.text_input("Doctor Name",placeholder="Dr. Rajesh Kumar")
            adate=st.text_input("Date (DD-MM-YYYY)",placeholder="28-05-2026")
        with c2:
            apat =st.text_input("Patient Name",placeholder="Rahul Verma")
            atime=st.text_input("Time",placeholder="10:00 AM")
        if st.button("📅 Book Appointment"):
            if adoc and apat and adate and atime:
                aid=len(st.session_state.appointments)+1
                st.session_state.appointments.append(Appointment(aid,adoc,apat,adate,atime))
                save_appointments()
                st.markdown(f'<div class="res-ok">✅ Appointment #{aid} booked for <b>{apat}</b> with <b>{adoc}</b></div>', unsafe_allow_html=True); st.rerun()
            else: st.warning("Fill all fields.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if st.session_state.appointments:
            rows=[[f'<span class="badge b-blue">#{a.appointment_id}</span>',a.doctor_name,a.patient_name,f'<span class="badge b-green">{a.date}</span>',a.time] for a in st.session_state.appointments]
            render_table(["ID","Doctor","Patient","Date","Time"],rows)
        else: st.markdown('<p style="color:#475569">No appointments.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        sdate=st.text_input("Enter Date (DD-MM-YYYY)")
        if st.button("🔍 Search"):
            res=[a for a in st.session_state.appointments if a.date==sdate]
            if res:
                for a in res: st.markdown(f'<div class="search-result">📅 <b style="color:#f1f5f9">{a.doctor_name}</b> → {a.patient_name} | {a.date} {a.time}</div>', unsafe_allow_html=True)
            else: st.markdown('<div class="res-fail">❌ No appointments on this date.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        uid=st.number_input("Appointment ID to Update",1,step=1,key="upd_appt")
        match=next((a for a in st.session_state.appointments if a.appointment_id==uid),None)
        if match:
            st.markdown(f'<div class="search-result">Found: <b style="color:#f1f5f9">{match.doctor_name}</b> → {match.patient_name} | {match.date} {match.time}</div>', unsafe_allow_html=True)
            c1,c2=st.columns(2)
            with c1: nd=st.text_input("New Date (DD-MM-YYYY)",value=match.date)
            with c2: nt=st.text_input("New Time",value=match.time)
            if st.button("✏️ Update"):
                match.date=nd;match.time=nt;save_appointments()
                st.markdown('<div class="res-ok">✅ Appointment updated!</div>', unsafe_allow_html=True); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        del_id=st.number_input("Appointment ID to Cancel",1,step=1,key="del_appt")
        match=next((a for a in st.session_state.appointments if a.appointment_id==del_id),None)
        if match:
            st.markdown(f'<div class="search-result">⚠️ Cancel: <b style="color:#f87171">{match.doctor_name}</b> → {match.patient_name} | {match.date}</div>', unsafe_allow_html=True)
            if st.button("❌ Confirm Cancel"):
                st.session_state.appointments.remove(match);save_appointments()
                st.markdown('<div class="res-ok">✅ Cancelled.</div>', unsafe_allow_html=True); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# BILLING
# ═══════════════════════════════════════════
elif page == "Billing":
    st.markdown('<div class="sec-title"><span>🧾</span> Billing & Invoices</div>', unsafe_allow_html=True)
    tab1,tab2 = st.tabs(["🧾 Generate Bill","📋 All Bills"])

    with tab1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        bname=st.text_input("Patient Name",placeholder="Rahul Verma")
        c1,c2,c3=st.columns(3)
        with c1: bdfee=st.number_input("Doctor Fee (₹)",0,value=500,step=50)
        with c2: broom=st.number_input("Room Charges (₹)",0,value=1000,step=100)
        with c3: bmed =st.number_input("Medicine (₹)",0,value=300,step=50)
        total=bdfee+broom+bmed
        st.markdown(f'<div style="background:#1e2740;border-radius:10px;padding:0.8rem 1.5rem;text-align:right;margin:0.5rem 0"><span style="color:#64748b">Estimated Total: </span><span style="color:#fbbf24;font-size:1.5rem;font-weight:800">₹{total:,}</span></div>', unsafe_allow_html=True)
        if st.button("🧾 Generate Bill"):
            if bname.strip():
                bid=len(st.session_state.bills)+1
                b=Bill("AIIMS","Delhi",bid,bname,bdfee,broom,bmed)
                st.session_state.bills.append(b); save_bills()
                st.markdown(f"""
                <div class="receipt">
                    <div class="receipt-header">
                        <div style="font-size:2rem">🏥</div>
                        <div style="font-weight:800;color:#f1f5f9;font-size:1.1rem;margin-top:0.3rem">AIIMS HOSPITAL</div>
                        <div style="color:#64748b;font-size:0.75rem">New Delhi | Invoice #{bid}</div>
                        <div style="color:#64748b;font-size:0.75rem">{datetime.now().strftime("%d-%m-%Y %I:%M %p")}</div>
                    </div>
                    <div class="receipt-row"><span>Patient</span><span><b>{bname}</b></span></div>
                    <div class="receipt-row"><span>Doctor Fee</span><span>₹{bdfee:,}</span></div>
                    <div class="receipt-row"><span>Room Charges</span><span>₹{broom:,}</span></div>
                    <div class="receipt-row"><span>Medicine</span><span>₹{bmed:,}</span></div>
                    <div class="receipt-total">
                        <span style="color:#f1f5f9">Total Amount</span>
                        <span style="color:#fbbf24">₹{b.total:,}</span>
                    </div>
                </div>""", unsafe_allow_html=True)
            else: st.warning("Enter patient name.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        if st.session_state.bills:
            total_rev=sum(b.total for b in st.session_state.bills)
            st.markdown(f'<div style="background:#052e16;border:1px solid #16a34a;border-radius:10px;padding:0.8rem 1.5rem;margin-bottom:1rem;font-weight:700;color:#4ade80">💰 Total Revenue: ₹{total_rev:,}</div>', unsafe_allow_html=True)
            rows=[[f'<span class="badge b-orange">#{b.bill_id}</span>',f'<b style="color:#f1f5f9">{b.patient_name}</b>',f'₹{b.doctor_fee:,}',f'₹{b.room_charges:,}',f'₹{b.medicine_charges:,}',f'<span style="color:#fbbf24;font-weight:700">₹{b.total:,}</span>'] for b in st.session_state.bills]
            render_table(["Bill#","Patient","Dr.Fee","Room","Medicine","Total"],rows)
        else: st.markdown('<p style="color:#475569">No bills yet.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════
# REPORTS
# ═══════════════════════════════════════════
elif page == "Reports":
    st.markdown('<div class="sec-title"><span>📈</span> Hospital Report</div>', unsafe_allow_html=True)
    total_rev=sum(b.total for b in st.session_state.bills)

    report_data=[
        ("👨‍⚕️","Total Doctors",len(st.session_state.doctors),"Active medical staff","b-blue"),
        ("🤒","Total Patients",len(st.session_state.patients),"Registered patients","b-green"),
        ("📅","Total Appointments",len(st.session_state.appointments),"Scheduled appointments","b-purple"),
        ("🧾","Total Bills",len(st.session_state.bills),"Generated invoices","b-orange"),
        ("💰","Total Revenue",f"₹{total_rev:,}","Total collected","b-red"),
    ]
    for icon,label,val,desc,badge in report_data:
        st.markdown(f"""
        <div class="report-card">
            <div class="report-card-icon">{icon}</div>
            <div class="report-card-info">
                <h4>{label}</h4>
                <p>{desc}</p>
            </div>
            <div class="report-card-val">{val}</div>
        </div>""", unsafe_allow_html=True)

    if st.session_state.doctors:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title"><span>💊</span> Specialization Breakdown</div>', unsafe_allow_html=True)
        specs={}
        for d in st.session_state.doctors: specs[d.specialization]=specs.get(d.specialization,0)+1
        for spec,count in specs.items():
            pct=int((count/len(st.session_state.doctors))*100)
            st.markdown(f"""
            <div style="margin-bottom:0.8rem">
                <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem">
                    <span style="color:#cbd5e1;font-size:0.85rem">{spec}</span>
                    <span style="color:#64748b;font-size:0.85rem">{count} doctor(s)</span>
                </div>
                <div style="background:#1e2740;border-radius:20px;height:8px">
                    <div style="background:linear-gradient(90deg,#3b82f6,#8b5cf6);width:{pct}%;height:8px;border-radius:20px"></div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
