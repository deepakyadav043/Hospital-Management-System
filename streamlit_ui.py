import streamlit as st

st.set_page_config(
    page_title="Jan Kalyan Hospital — Sewa Nirswarth",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; margin:0; padding:0; box-sizing:border-box; }
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #ffffff; }
section[data-testid="stSidebar"] { display: none; }

/* ── TOP RED BAR ── */
.top-bar {
    background: #e53935;
    padding: 0.45rem 3rem;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 2rem;
    font-size: 0.85rem;
    color: white;
}
.top-bar a { color: white; text-decoration: none; }
.top-bar-icons { display: flex; gap: 1rem; align-items: center; }
.top-bar-icons span { font-size: 1.1rem; cursor: pointer; }

/* ── NAVBAR ── */
.navbar {
    background: #4db6ac;
    padding: 0.8rem 3rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: sticky; top: 0; z-index: 100;
}
.logo-area { display: flex; align-items: center; gap: 0.8rem; margin-right: 2rem; }
.logo-icon { font-size: 2.5rem; }
.logo-text { line-height: 1.1; }
.logo-text .name { font-size: 1.2rem; font-weight: 800; color: #b71c1c; letter-spacing: 1px; }
.logo-text .tagline { font-size: 0.65rem; color: #004d40; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; }
.nav-links { display: flex; gap: 0.3rem; margin-left: auto; }
.nav-link {
    color: white; text-decoration: none; padding: 0.5rem 1rem;
    border-radius: 4px; font-weight: 600; font-size: 0.9rem;
    transition: background 0.2s;
}
.nav-link:hover, .nav-link.active { background: rgba(255,255,255,0.2); }

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, #f5f5f5 0%, #e0f2f1 100%);
    padding: 0;
    display: flex;
    align-items: stretch;
    min-height: 420px;
    overflow: hidden;
    position: relative;
}
.hero-left {
    flex: 1;
    padding: 4rem 3rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.hero-left h1 {
    font-size: 3rem; font-weight: 800; color: #004d40;
    line-height: 1.1; margin-bottom: 1rem;
}
.hero-left h1 span { color: #e53935; }
.hero-left p { color: #546e7a; font-size: 1rem; max-width: 500px; line-height: 1.7; margin-bottom: 1.5rem; }
.hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary {
    background: #e53935; color: white; padding: 0.75rem 2rem;
    border-radius: 6px; font-weight: 700; font-size: 0.95rem;
    text-decoration: none; display: inline-block; border: none; cursor: pointer;
    transition: background 0.2s;
}
.btn-primary:hover { background: #b71c1c; }
.btn-outline {
    background: transparent; color: #004d40; padding: 0.75rem 2rem;
    border-radius: 6px; font-weight: 700; font-size: 0.95rem;
    border: 2px solid #4db6ac; cursor: pointer; text-decoration: none;
    transition: all 0.2s;
}
.btn-outline:hover { background: #4db6ac; color: white; }
.hero-right {
    flex: 1;
    background: linear-gradient(135deg, #4db6ac, #e53935);
    display: flex; align-items: center; justify-content: center;
    font-size: 8rem;
    clip-path: ellipse(90% 100% at 100% 50%);
}

/* ── QUICK CARDS ── */
.quick-section {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    margin: 0;
}
.quick-card {
    padding: 2rem 1.5rem;
    color: white;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
.quick-card:nth-child(1) { background: #26a69a; }
.quick-card:nth-child(2) { background: #4db6ac; }
.quick-card:nth-child(3) { background: #2e7d79; }
.quick-card:nth-child(4) { background: #80cbc4; }
.quick-card h3 { font-size: 1.1rem; font-weight: 700; }
.quick-card p { font-size: 0.82rem; opacity: 0.9; line-height: 1.5; }
.quick-btn {
    display: inline-block; margin-top: 0.5rem;
    border: 2px solid white; color: white;
    padding: 0.4rem 1.2rem; border-radius: 4px;
    font-size: 0.82rem; font-weight: 600; cursor: pointer;
    width: fit-content; transition: all 0.2s;
}
.quick-btn:hover { background: white; color: #26a69a; }

/* ── SECTION TITLE ── */
.section-title {
    text-align: center;
    padding: 3rem 0 1rem 0;
}
.section-title h2 { font-size: 2rem; font-weight: 800; color: #212121; }
.section-title .underline {
    width: 80px; height: 3px; background: #212121;
    margin: 0.5rem auto 0 auto;
}

/* ── ABOUT ── */
.about-section {
    display: flex;
    align-items: center;
    gap: 3rem;
    padding: 2rem 3rem 4rem 3rem;
    max-width: 1200px;
    margin: 0 auto;
}
.about-img {
    flex: 1;
    font-size: 10rem;
    text-align: center;
    background: #e0f2f1;
    border-radius: 20px;
    padding: 2rem;
}
.about-text { flex: 1; }
.about-text p { color: #546e7a; line-height: 1.8; font-size: 0.95rem; text-align: justify; }
.know-more-btn {
    background: #212121; color: white;
    padding: 0.75rem 2.5rem; border-radius: 6px;
    font-weight: 700; margin-top: 1.5rem;
    display: inline-block; cursor: pointer;
    font-size: 0.95rem;
}

/* ── STATS ── */
.stats-section {
    background: linear-gradient(rgba(77,182,172,0.85), rgba(77,182,172,0.85)),
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100'%3E%3Ccircle cx='50' cy='50' r='40' fill='%23ffffff22'/%3E%3C/svg%3E");
    background-size: cover;
    padding: 4rem 3rem;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    text-align: center;
    gap: 2rem;
}
.stat-item h2 { font-size: 3rem; font-weight: 800; color: white; }
.stat-item p { color: white; font-weight: 600; font-size: 0.95rem; opacity: 0.9; margin-top: 0.3rem; }

/* ── SERVICES ── */
.services-section { padding: 1rem 3rem 4rem 3rem; background: #fafafa; }
.services-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2.5rem;
    max-width: 1200px;
    margin: 2rem auto 0 auto;
}
.service-card { text-align: left; }
.service-icon { font-size: 2.5rem; color: #4db6ac; margin-bottom: 0.8rem; }
.service-card h4 { font-size: 0.95rem; font-weight: 700; color: #212121; margin-bottom: 0.5rem; }
.service-card p { font-size: 0.82rem; color: #78909c; line-height: 1.6; }

/* ── APPOINTMENT FORM ── */
.appt-section {
    padding: 3rem;
    background: white;
    max-width: 1200px;
    margin: 0 auto;
}

/* ── CONTACT ── */
.contact-section {
    padding: 3rem;
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    gap: 3rem;
    align-items: flex-start;
}
.contact-left { flex: 1; font-size: 8rem; text-align: center; }
.contact-right { flex: 1.5; }
.contact-form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.contact-field {
    display: flex; flex-direction: column; gap: 0.3rem; margin-bottom: 0.8rem;
}
.contact-field label { font-size: 0.85rem; font-weight: 600; color: #37474f; }
.contact-field input, .contact-field textarea {
    border: 1.5px solid #cfd8dc;
    border-radius: 6px;
    padding: 0.65rem 1rem;
    font-family: 'Poppins', sans-serif;
    font-size: 0.9rem;
    color: #212121;
    outline: none;
    width: 100%;
    transition: border 0.2s;
}
.contact-field input:focus, .contact-field textarea:focus { border-color: #4db6ac; }

/* ── FOOTER ── */
.footer {
    background: #616161;
    padding: 3rem;
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 3rem;
    color: white;
}
.footer h3 { font-size: 1.2rem; font-weight: 700; margin-bottom: 1.2rem; }
.footer-links { list-style: none; }
.footer-links li { margin-bottom: 0.6rem; font-size: 0.88rem; }
.footer-links li::before { content: "→ "; color: #80cbc4; }
.footer-services { display: grid; grid-template-columns: 1fr 1fr; gap: 0 2rem; }
.footer-social { display: flex; gap: 0.8rem; margin-top: 1rem; }
.social-icon {
    width: 40px; height: 40px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; cursor: pointer;
}
.fb { background: #1877f2; }
.yt { background: #ff0000; }
.ig { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); }
.footer-copy {
    background: #424242;
    text-align: center;
    padding: 1rem;
    color: #bdbdbd;
    font-size: 0.82rem;
}
.footer-copy a { color: #4db6ac; }

/* streamlit override */
.stTabs [data-baseweb="tab-list"] { gap: 1rem; }
.stTabs [data-baseweb="tab"] {
    background: #f5f5f5; border-radius: 8px;
    padding: 0.5rem 1.5rem; font-weight: 600; color: #546e7a;
}
.stTabs [aria-selected="true"] { background: #4db6ac !important; color: white !important; }
label { color: #37474f !important; font-weight: 600 !important; font-size: 0.88rem !important; }
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div {
    border: 1.5px solid #cfd8dc !important;
    border-radius: 8px !important;
    font-family: 'Poppins', sans-serif !important;
}
.stButton > button {
    background: #e53935 !important; color: white !important;
    border: none !important; border-radius: 8px !important;
    font-weight: 700 !important; width: 100% !important;
    font-family: 'Poppins', sans-serif !important;
    padding: 0.65rem !important;
}

</style>
""", unsafe_allow_html=True)

# ── Session State ──
for k in ["doctors","patients","appointments","bills"]:
    if k not in st.session_state:
        st.session_state[k] = []
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# ── Classes ──
class Hospital:
    def __init__(self, name, loc): self.hospital_name=name; self.location=loc

class Doctor(Hospital):
    def __init__(self,did,dname,spec,exp,fee):
        super().__init__("Jan Kalyan Hospital","Kalyan, Maharashtra")
        self.doctor_id=did;self.doctor_name=dname;self.specialization=spec;self.experience=exp;self.fee=fee

class Patient(Hospital):
    def __init__(self,pid,pname,age,disease,room):
        super().__init__("Jan Kalyan Hospital","Kalyan, Maharashtra")
        self.patient_id=pid;self.patient_name=pname;self.age=age;self.disease=disease;self.room_number=room

class Appointment:
    def __init__(self,aid,doc,pat,date,time):
        self.appointment_id=aid;self.doctor_name=doc;self.patient_name=pat;self.date=date;self.time=time

class Bill(Hospital):
    def __init__(self,bid,pname,dfee,rcharge,mcharge):
        super().__init__("Jan Kalyan Hospital","Kalyan, Maharashtra")
        self.bill_id=bid;self.patient_name=pname;self.doctor_fee=dfee
        self.room_charges=rcharge;self.medicine_charges=mcharge
        self.total=dfee+rcharge+mcharge

# ── TOP BAR ──
st.markdown("""
<div class="top-bar">
    <div class="top-bar-icons">
        <span title="Facebook">📘</span>
        <span title="YouTube">📺</span>
        <span title="Instagram">📷</span>
    </div>
    <span>📞 +91 9967806118</span>
    <span>✉️ jankalyanhospital@gmail.com</span>
</div>
""", unsafe_allow_html=True)

# ── NAVBAR ──
pages = ["Home","About Us","Services","Doctors","Patients","Appointments","Billing","Contact Us"]
nav_html = '<div class="navbar"><div class="logo-area"><div class="logo-icon">❤️</div><div class="logo-text"><div class="name">JAN KALYAN<br>HOSPITAL</div><div class="tagline">Sewa Nirswarth</div></div></div><div class="nav-links">'
for p in pages:
    active = "active" if st.session_state.active_page == p else ""
    nav_html += f'<a class="nav-link {active}" href="#">{p}</a>'
nav_html += '</div></div>'
st.markdown(nav_html, unsafe_allow_html=True)

# ── NAV BUTTONS (hidden but functional) ──
cols = st.columns(len(pages))
for i, p in enumerate(pages):
    with cols[i]:
        if st.button(p, key=f"nav_{p}", help=p):
            st.session_state.active_page = p
            st.rerun()

page = st.session_state.active_page

# ═══════════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════════
if page == "Home":

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-left">
            <h1>Welcome to<br><span>Jan Kalyan</span><br>Hospital</h1>
            <p>Jankalyan Multispeciality Hospital aims to provide a personalised approach to clinical care and treatments that set the bar for quality health care which is also efficient and cost-effective.</p>
            <div class="hero-btns">
                <span class="btn-primary">Book Appointment</span>
                <span class="btn-outline">Our Services</span>
            </div>
        </div>
        <div class="hero-right">🏥</div>
    </div>
    """, unsafe_allow_html=True)

    # Quick Cards
    st.markdown("""
    <div class="quick-section">
        <div class="quick-card">
            <h3>Find Services</h3>
            <p>Everything you need to know about our services.</p>
            <div class="quick-btn">Find Services</div>
        </div>
        <div class="quick-card">
            <h3>Find Doctors</h3>
            <p>Why our doctors are the best. Find OUT!</p>
            <div class="quick-btn">Find Doctors</div>
        </div>
        <div class="quick-card">
            <h3>Insurance Covered</h3>
            <p>Get the facts about how your insurance covers hospital stays.</p>
            <div class="quick-btn">Insurance</div>
        </div>
        <div class="quick-card">
            <h3>Book Appointment</h3>
            <p>Make Appointment, Skip the Wait at Hospital.</p>
            <div class="quick-btn">Appointment</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # About
    st.markdown('<div class="section-title"><h2>About Hospital</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-section">
        <div class="about-img">🏗️</div>
        <div class="about-text">
            <p>Jankalyan Multispeciality Hospital aim is to provide a personalised approach to clinical care and to provide treatments that set the bar for quality health care which is also efficient and cost-effective. Our state-of-the-art surgical, Urology and Clinical Medicine and Neuropsychology Center offers individualized treatment to patients.</p>
            <p style="margin-top:1rem;">We are committed to providing the highest quality of care to our patients and their families. Our team of experienced doctors, nurses, and support staff work together to ensure that every patient receives the best possible treatment.</p>
            <div class="know-more-btn">Know More</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stats-section">
        <div class="stat-item"><h2>16+</h2><p>Yrs, Experienced Doctors</p></div>
        <div class="stat-item"><h2>12,000+</h2><p>OPD Patients</p></div>
        <div class="stat-item"><h2>4,430+</h2><p>Surgeries</p></div>
        <div class="stat-item"><h2>30+</h2><p>Insurance Covered</p></div>
    </div>
    """, unsafe_allow_html=True)

    # Services
    st.markdown('<div class="section-title"><h2>Our Services</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="services-section">
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">💉</div>
                <h4>Anesthesiology</h4>
                <p>The anesthesiologist could collaborate with a licensed nurse anesthetist (CRNA) or residents, and trainee nurse anesthetist.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">❤️</div>
                <h4>Cardiology</h4>
                <p>Cardiology is among the most vital branches in medical science. It is concerned with problems that affect the heart.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🩸</div>
                <h4>Diabetology</h4>
                <p>Diabetology is a severe and prevalent condition that affects many people. If someone is diagnosed, the blood sugar levels are very high.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🚑</div>
                <h4>Emergency & Critical Care</h4>
                <p>Critical Care Unit (CCU) is a specially designed unit for hospital patients suffering from severe health issues who require urgent attention 24/7.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🦴</div>
                <h4>Endoscopic Spine Surgery</h4>
                <p>Endoscopic Spine Surgery is a cutting-edge procedure that uses a tiny tubular systems or micro-incisions assisted by an endoscope.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🧠</div>
                <h4>Neuro Surgery</h4>
                <p>Neuro surgery (also known as Neurological surgery) is a medical field that deals by the treatment, detection, and surgical treatment of conditions.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">🔬</div>
                <h4>General & Laparoscopic Surgery</h4>
                <p>Laparoscopic Surgery is a specialized procedure used to perform complicated surgeries. It is low-risk and minimally invasive requiring tiny incisions.</p>
            </div>
            <div class="service-card">
                <div class="service-icon">💊</div>
                <h4>General Medicine</h4>
                <p>General medicine or internal medical practice is the medical field that deals with preventative, diagnostic and treatment of adult illnesses.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════
# ABOUT US
# ═══════════════════════════════════════════
elif page == "About Us":
    st.markdown('<div class="section-title"><h2>About Jan Kalyan Hospital</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-section">
        <div class="about-img">🏥</div>
        <div class="about-text">
            <p>Jankalyan Multispeciality Hospital aim is to provide a personalised approach to clinical care and to provide treatments that set the bar for quality health care which is also efficient and cost-effective.</p>
            <p style="margin-top:1rem;">Our state-of-the-art surgical, Urology and Clinical Medicine and Neuropsychology Center offers individualized treatment to patients. Best Hospital in Kalyan.</p>
            <p style="margin-top:1rem;">We have a team of 16+ years experienced doctors, modern equipment, and 30+ insurance plans covered. We have served 12,000+ OPD patients and performed 4,430+ surgeries.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="stats-section">
        <div class="stat-item"><h2>16+</h2><p>Yrs, Experienced Doctors</p></div>
        <div class="stat-item"><h2>12,000+</h2><p>OPD Patients</p></div>
        <div class="stat-item"><h2>4,430+</h2><p>Surgeries</p></div>
        <div class="stat-item"><h2>30+</h2><p>Insurance Covered</p></div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════
# SERVICES
# ═══════════════════════════════════════════
elif page == "Services":
    st.markdown('<div class="section-title"><h2>Our Services</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="services-section">
        <div class="services-grid">
            <div class="service-card"><div class="service-icon">💉</div><h4>Anesthesiology</h4><p>Collaborate with licensed nurse anesthetist (CRNA), residents, and trainee nurse anesthetist.</p></div>
            <div class="service-card"><div class="service-icon">❤️</div><h4>Cardiology</h4><p>Among the most vital branches in medical science concerned with problems that affect the heart.</p></div>
            <div class="service-card"><div class="service-icon">🩸</div><h4>Diabetology</h4><p>Severe and prevalent condition affecting many people with very high blood sugar levels.</p></div>
            <div class="service-card"><div class="service-icon">🚑</div><h4>Emergency & Critical Care</h4><p>CCU specially designed for patients suffering severe health issues requiring urgent attention 24/7.</p></div>
            <div class="service-card"><div class="service-icon">🦴</div><h4>Endoscopic Spine Surgery</h4><p>Cutting-edge procedure using tiny tubular systems or micro-incisions assisted by endoscope.</p></div>
            <div class="service-card"><div class="service-icon">🧠</div><h4>Neuro Surgery</h4><p>Medical field dealing with treatment, detection, and surgical treatment of neurological conditions.</p></div>
            <div class="service-card"><div class="service-icon">🔬</div><h4>General & Laparoscopic Surgery</h4><p>Low-risk minimally invasive procedure performing complicated surgeries with tiny incisions.</p></div>
            <div class="service-card"><div class="service-icon">💊</div><h4>General Medicine</h4><p>Preventative, diagnostic and treatment of adult illnesses — internal medical practice.</p></div>
            <div class="service-card"><div class="service-icon">🦷</div><h4>ENT Surgery</h4><p>Ear, Nose and Throat surgeries performed by expert ENT specialists with modern equipment.</p></div>
            <div class="service-card"><div class="service-icon">🦿</div><h4>Joint Replacement Surgery</h4><p>Advanced joint replacement surgeries including knee and hip replacements for better mobility.</p></div>
            <div class="service-card"><div class="service-icon">🫁</div><h4>Pulmonology</h4><p>Diagnosis and treatment of lung diseases, breathing problems and respiratory disorders.</p></div>
            <div class="service-card"><div class="service-icon">🩺</div><h4>Urology</h4><p>Treatment of urinary tract conditions and male reproductive system disorders by expert urologists.</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════
# DOCTORS
# ═══════════════════════════════════════════
elif page == "Doctors":
    st.markdown('<div class="section-title"><h2>Our Doctors</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["➕ Add Doctor", "📋 All Doctors", "🔍 Search"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            dname = st.text_input("Doctor Name", placeholder="Dr. Rajesh Kumar")
            dexp  = st.number_input("Experience (years)", 0, 50, 10)
        with c2:
            dspec = st.text_input("Specialization", placeholder="Cardiologist")
            dfee  = st.number_input("Fee (₹)", 0, 10000, 500, 50)
        if st.button("✅ Add Doctor"):
            if dname and dspec:
                did = len(st.session_state.doctors) + 1
                st.session_state.doctors.append(Doctor(did, dname, dspec, dexp, dfee))
                st.success(f"✅ Dr. {dname} added successfully!")
                st.rerun()
            else: st.warning("Fill Name & Specialization.")

    with tab2:
        if st.session_state.doctors:
            st.markdown("""<table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
            <tr style="background:#4db6ac;color:white;">
            <th style="padding:0.7rem;text-align:left;border-radius:10px 0 0 0">ID</th>
            <th style="padding:0.7rem;text-align:left;">Name</th>
            <th style="padding:0.7rem;text-align:left;">Specialization</th>
            <th style="padding:0.7rem;text-align:left;">Experience</th>
            <th style="padding:0.7rem;text-align:left;border-radius:0 10px 0 0">Fee</th></tr>""", unsafe_allow_html=True)
            for d in st.session_state.doctors:
                st.markdown(f'<tr style="border-bottom:1px solid #f0f0f0;"><td style="padding:0.7rem">{d.doctor_id}</td><td style="padding:0.7rem"><b>{d.doctor_name}</b></td><td style="padding:0.7rem"><span style="background:#e0f2f1;color:#00695c;padding:0.2rem 0.7rem;border-radius:20px;font-size:0.8rem">{d.specialization}</span></td><td style="padding:0.7rem">{d.experience} yrs</td><td style="padding:0.7rem">₹{d.fee}</td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else: st.info("No doctors added yet.")

    with tab3:
        q = st.text_input("Search by Name")
        if st.button("🔍 Search Doctor"):
            res = [d for d in st.session_state.doctors if q.lower() in d.doctor_name.lower()]
            if res:
                for d in res:
                    st.markdown(f"""<div style="background:#f9f9f9;border-left:4px solid #4db6ac;padding:1rem;border-radius:8px;margin-bottom:0.5rem;">
                    <b style="color:#004d40">{d.doctor_name}</b> | {d.specialization} | {d.experience} yrs exp | ₹{d.fee}</div>""", unsafe_allow_html=True)
            else: st.error("❌ Doctor not found.")

# ═══════════════════════════════════════════
# PATIENTS
# ═══════════════════════════════════════════
elif page == "Patients":
    st.markdown('<div class="section-title"><h2>Patient Management</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["➕ Add Patient", "📋 All Patients", "🔍 Search"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            pname   = st.text_input("Patient Name", placeholder="Rahul Verma")
            pdisease= st.text_input("Disease", placeholder="Fever / Diabetes")
        with c2:
            page2   = st.number_input("Age", 1, 120, 30)
            proom   = st.text_input("Room Number", placeholder="101")
        if st.button("✅ Add Patient"):
            if pname and pdisease and proom:
                pid = len(st.session_state.patients) + 1
                st.session_state.patients.append(Patient(pid, pname, page2, pdisease, proom))
                st.success(f"✅ Patient {pname} added!")
                st.rerun()
            else: st.warning("Fill all fields.")

    with tab2:
        if st.session_state.patients:
            st.markdown("""<table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
            <tr style="background:#e53935;color:white;">
            <th style="padding:0.7rem;text-align:left">ID</th><th style="padding:0.7rem;text-align:left">Name</th>
            <th style="padding:0.7rem;text-align:left">Age</th><th style="padding:0.7rem;text-align:left">Disease</th>
            <th style="padding:0.7rem;text-align:left">Room</th></tr>""", unsafe_allow_html=True)
            for p in st.session_state.patients:
                st.markdown(f'<tr style="border-bottom:1px solid #f0f0f0"><td style="padding:0.7rem">{p.patient_id}</td><td style="padding:0.7rem"><b>{p.patient_name}</b></td><td style="padding:0.7rem">{p.age}</td><td style="padding:0.7rem"><span style="background:#ffebee;color:#c62828;padding:0.2rem 0.7rem;border-radius:20px;font-size:0.8rem">{p.disease}</span></td><td style="padding:0.7rem">{p.room_number}</td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else: st.info("No patients added yet.")

    with tab3:
        sb = st.radio("Search by", ["Name","ID"], horizontal=True)
        if sb == "Name":
            q = st.text_input("Patient Name")
            if st.button("🔍 Search"):
                res = [p for p in st.session_state.patients if q.lower() in p.patient_name.lower()]
                if res:
                    for p in res:
                        st.markdown(f'<div style="background:#fff3f3;border-left:4px solid #e53935;padding:1rem;border-radius:8px;margin-bottom:0.5rem;"><b style="color:#b71c1c">{p.patient_name}</b> | Age: {p.age} | {p.disease} | Room: {p.room_number}</div>', unsafe_allow_html=True)
                else: st.error("❌ Patient not found.")
        else:
            pid2 = st.number_input("Patient ID", 1, step=1)
            if st.button("🔍 Search"):
                res = [p for p in st.session_state.patients if p.patient_id == pid2]
                if res:
                    p = res[0]
                    st.markdown(f'<div style="background:#fff3f3;border-left:4px solid #e53935;padding:1rem;border-radius:8px"><b>{p.patient_name}</b> | Age:{p.age} | {p.disease} | Room:{p.room_number}</div>', unsafe_allow_html=True)
                else: st.error("❌ Not found.")

# ═══════════════════════════════════════════
# APPOINTMENTS
# ═══════════════════════════════════════════
elif page == "Appointments":
    st.markdown('<div class="section-title"><h2>Book Appointment</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📅 Book Appointment", "📋 All Appointments", "🔍 Search by Date"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            adoc  = st.text_input("Doctor Name", placeholder="Dr. Rajesh Kumar")
            adate = st.text_input("Date (DD-MM-YYYY)", placeholder="28-05-2026")
        with c2:
            apat  = st.text_input("Patient Name", placeholder="Rahul Verma")
            atime = st.text_input("Time", placeholder="10:00 AM")
        if st.button("📅 Book Appointment"):
            if adoc and apat and adate and atime:
                aid = len(st.session_state.appointments) + 1
                st.session_state.appointments.append(Appointment(aid, adoc, apat, adate, atime))
                st.success("✅ Appointment Booked Successfully!")
                st.rerun()
            else: st.warning("Fill all fields.")

    with tab2:
        if st.session_state.appointments:
            st.markdown("""<table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
            <tr style="background:#4db6ac;color:white;"><th style="padding:0.7rem;text-align:left">ID</th>
            <th style="padding:0.7rem;text-align:left">Doctor</th><th style="padding:0.7rem;text-align:left">Patient</th>
            <th style="padding:0.7rem;text-align:left">Date</th><th style="padding:0.7rem;text-align:left">Time</th></tr>""", unsafe_allow_html=True)
            for a in st.session_state.appointments:
                st.markdown(f'<tr style="border-bottom:1px solid #f0f0f0"><td style="padding:0.7rem">{a.appointment_id}</td><td style="padding:0.7rem">{a.doctor_name}</td><td style="padding:0.7rem">{a.patient_name}</td><td style="padding:0.7rem"><span style="background:#e0f2f1;color:#00695c;padding:0.2rem 0.7rem;border-radius:20px;font-size:0.8rem">{a.date}</span></td><td style="padding:0.7rem">{a.time}</td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else: st.info("No appointments yet.")

    with tab3:
        sdate = st.text_input("Enter Date (DD-MM-YYYY)")
        if st.button("🔍 Search Date"):
            res = [a for a in st.session_state.appointments if a.date == sdate]
            if res:
                for a in res:
                    st.markdown(f'<div style="background:#e0f2f1;border-left:4px solid #4db6ac;padding:1rem;border-radius:8px;margin-bottom:0.5rem">{a.doctor_name} → {a.patient_name} | {a.date} {a.time}</div>', unsafe_allow_html=True)
            else: st.error("❌ No appointments on this date.")

# ═══════════════════════════════════════════
# BILLING
# ═══════════════════════════════════════════
elif page == "Billing":
    st.markdown('<div class="section-title"><h2>Patient Billing</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🧾 Generate Bill", "📋 All Bills"])

    with tab1:
        bname = st.text_input("Patient Name")
        c1,c2,c3 = st.columns(3)
        with c1: bdfee = st.number_input("Doctor Fee (₹)", 0, value=500, step=50)
        with c2: broom = st.number_input("Room Charges (₹)", 0, value=1000, step=100)
        with c3: bmed  = st.number_input("Medicine (₹)", 0, value=300, step=50)
        total = bdfee + broom + bmed
        st.markdown(f'<div style="background:#e0f2f1;border-radius:10px;padding:0.8rem 1.5rem;text-align:right;margin:0.5rem 0"><span style="color:#546e7a">Estimated Total: </span><span style="color:#004d40;font-size:1.5rem;font-weight:800">₹{total}</span></div>', unsafe_allow_html=True)
        if st.button("🧾 Generate Bill"):
            if bname:
                bid = len(st.session_state.bills) + 1
                b = Bill(bid, bname, bdfee, broom, bmed)
                st.session_state.bills.append(b)
                st.markdown(f"""
                <div style="background:#f9f9f9;border:2px solid #4db6ac;border-radius:16px;padding:2rem;max-width:500px;margin:1rem auto">
                    <div style="text-align:center;border-bottom:2px dashed #4db6ac;padding-bottom:1rem;margin-bottom:1rem">
                        <div style="font-size:1.8rem">❤️</div>
                        <div style="font-weight:800;color:#004d40;font-size:1.2rem">JAN KALYAN HOSPITAL</div>
                        <div style="color:#78909c;font-size:0.8rem">Kalyan, Maharashtra | Bill #{bid}</div>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:1px dashed #e0e0e0"><span style="color:#78909c">Patient</span><span style="font-weight:700">{bname}</span></div>
                    <div style="display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:1px dashed #e0e0e0"><span style="color:#78909c">Doctor Fee</span><span>₹{bdfee}</span></div>
                    <div style="display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:1px dashed #e0e0e0"><span style="color:#78909c">Room Charges</span><span>₹{broom}</span></div>
                    <div style="display:flex;justify-content:space-between;padding:0.4rem 0;border-bottom:2px solid #4db6ac"><span style="color:#78909c">Medicine</span><span>₹{bmed}</span></div>
                    <div style="display:flex;justify-content:space-between;padding:0.6rem 0"><span style="font-weight:800;font-size:1.1rem;color:#004d40">Total</span><span style="font-weight:800;font-size:1.3rem;color:#e53935">₹{b.total}</span></div>
                </div>""", unsafe_allow_html=True)
            else: st.warning("Enter patient name.")

    with tab2:
        if st.session_state.bills:
            total_rev = sum(b.total for b in st.session_state.bills)
            st.markdown(f'<div style="background:#e8f5e9;border-radius:10px;padding:0.8rem 1.5rem;margin-bottom:1rem;font-weight:700;color:#1b5e20">💰 Total Revenue: ₹{total_rev}</div>', unsafe_allow_html=True)
            st.markdown("""<table style="width:100%;border-collapse:collapse;font-size:0.88rem">
            <tr style="background:#e53935;color:white"><th style="padding:0.7rem;text-align:left">Bill#</th>
            <th style="padding:0.7rem;text-align:left">Patient</th><th style="padding:0.7rem;text-align:left">Dr.Fee</th>
            <th style="padding:0.7rem;text-align:left">Room</th><th style="padding:0.7rem;text-align:left">Medicine</th>
            <th style="padding:0.7rem;text-align:left">Total</th></tr>""", unsafe_allow_html=True)
            for b in st.session_state.bills:
                st.markdown(f'<tr style="border-bottom:1px solid #f0f0f0"><td style="padding:0.7rem">#{b.bill_id}</td><td style="padding:0.7rem"><b>{b.patient_name}</b></td><td style="padding:0.7rem">₹{b.doctor_fee}</td><td style="padding:0.7rem">₹{b.room_charges}</td><td style="padding:0.7rem">₹{b.medicine_charges}</td><td style="padding:0.7rem"><b style="color:#e53935">₹{b.total}</b></td></tr>', unsafe_allow_html=True)
            st.markdown('</table>', unsafe_allow_html=True)
        else: st.info("No bills generated yet.")

# ═══════════════════════════════════════════
# CONTACT US
# ═══════════════════════════════════════════
elif page == "Contact Us":
    st.markdown('<div class="section-title"><h2>Contact Us</h2><div class="underline"></div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.markdown('<div style="font-size:6rem;text-align:center;margin-top:2rem">📞</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background:#e0f2f1;border-radius:14px;padding:1.5rem;margin-top:1rem">
            <div style="margin-bottom:0.8rem;color:#004d40"><b>📍 Address</b><br><span style="color:#546e7a">Jan Kalyan Multispeciality Hospital, Kalyan Road, Maharashtra</span></div>
            <div style="margin-bottom:0.8rem;color:#004d40"><b>📞 Phone</b><br><span style="color:#546e7a">+91 9967806118</span></div>
            <div style="color:#004d40"><b>✉️ Email</b><br><span style="color:#546e7a">jankalyanhospital@gmail.com</span></div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        fc1, fc2 = st.columns(2)
        with fc1: fname = st.text_input("First Name")
        with fc2: lname = st.text_input("Last Name")
        fphone = st.text_input("Contact Number")
        femail = st.text_input("Email")
        fmsg   = st.text_area("Comment or Message", height=120)
        if st.button("📨 Send Message"):
            if fname and fphone and femail:
                st.success(f"✅ Thank you {fname}! We will contact you soon.")
            else: st.warning("Fill all required fields.")

# ═══════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════
st.markdown("""
<div class="footer">
    <div>
        <h3>Quick Links</h3>
        <ul class="footer-links">
            <li>Home</li><li>About</li><li>Doctors</li>
            <li>Services</li><li>Contact</li>
        </ul>
        <div class="footer-social">
            <div class="social-icon fb">📘</div>
            <div class="social-icon yt">📺</div>
            <div class="social-icon ig">📷</div>
        </div>
    </div>
    <div>
        <h3>Services</h3>
        <div class="footer-services">
            <ul class="footer-links">
                <li>Cardiology</li>
                <li>Laparoscopic Surgery</li>
                <li>Neuro Surgery</li>
                <li>ENT Surgery</li>
                <li>Endoscopic Spine</li>
            </ul>
            <ul class="footer-links">
                <li>Joint Replacement</li>
                <li>Diabetology</li>
                <li>General Medicine</li>
                <li>Anesthesiology</li>
                <li>Emergency & CCU</li>
            </ul>
        </div>
    </div>
    <div>
        <h3>Contact</h3>
        <p style="font-size:0.85rem;line-height:2;color:#e0e0e0">
            📍 Kalyan, Maharashtra<br>
            📞 +91 9967806118<br>
            ✉️ jankalyanhospital@gmail.com<br>
            🕐 Mon–Sat: 9AM – 6PM<br>
            🚑 Emergency: 24/7
        </p>
    </div>
</div>
<div class="footer-copy">
    Copyright © 2024 Jankalyan Hospital | Website Designed by <a href="#">Hopeland Healthcare</a>
</div>
""", unsafe_allow_html=True)