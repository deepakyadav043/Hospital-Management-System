import streamlit as st
import pandas as pd
import csv
import os
import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ──────────────────────────────────────────────────────────────────
#  PAGE CONFIG
# ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jan Kalyan Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────
#  GLOBAL STYLES
# ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root Variables ── */
:root {
    --teal:      #0f8b8d;
    --teal-lt:   #1ab5b8;
    --teal-dk:   #096466;
    --gold:      #e6a817;
    --gold-lt:   #f5c842;
    --dark:      #0d1b2a;
    --mid:       #1a2e40;
    --card:      #162232;
    --border:    rgba(15,139,141,0.25);
    --text:      #e8f4f8;
    --muted:     #8aaec0;
    --danger:    #e05c5c;
    --success:   #3dba7e;
}

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--dark);
    color: var(--text);
}
.stApp { background: var(--dark); }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a141f 0%, var(--mid) 100%);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .stRadio > label {
    color: var(--muted) !important;
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 600;
    padding: 0.2rem 0;
}
[data-testid="stSidebar"] .stRadio div[role="radio"] label {
    color: var(--text) !important;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    transition: background 0.2s;
    font-size: 0.95rem;
    font-weight: 500;
}
[data-testid="stSidebar"] .stRadio div[role="radio"] label:hover {
    background: rgba(15,139,141,0.15);
}

/* ── Header banner ── */
.hosp-header {
    background: linear-gradient(135deg, var(--teal-dk) 0%, var(--teal) 50%, var(--teal-lt) 100%);
    border-radius: 16px;
    padding: 1.8rem 2.2rem;
    margin-bottom: 1.6rem;
    display: flex;
    align-items: center;
    gap: 1.4rem;
    box-shadow: 0 8px 32px rgba(15,139,141,0.3);
    position: relative;
    overflow: hidden;
}
.hosp-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    border-radius: 50%;
    background: rgba(255,255,255,0.06);
}
.hosp-header::after {
    content: '';
    position: absolute;
    bottom: -60px; right: 60px;
    width: 250px; height: 250px;
    border-radius: 50%;
    background: rgba(255,255,255,0.04);
}
.hosp-logo { font-size: 3.2rem; line-height: 1; }
.hosp-name {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 800;
    color: #fff;
    line-height: 1.15;
    letter-spacing: -0.5px;
}
.hosp-tagline {
    font-size: 0.88rem;
    color: rgba(255,255,255,0.7);
    letter-spacing: 0.06em;
    margin-top: 0.2rem;
}
.hosp-badge {
    margin-left: auto;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 50px;
    padding: 0.35rem 1rem;
    font-size: 0.78rem;
    color: #fff;
    letter-spacing: 0.08em;
    font-weight: 600;
}

/* ── Section title ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.55rem;
    font-weight: 700;
    color: var(--text);
    border-left: 4px solid var(--teal);
    padding-left: 0.8rem;
    margin-bottom: 1.2rem;
}

/* ── Metric cards ── */
.metrics-row { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.metric-card {
    flex: 1;
    min-width: 140px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}
.metric-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(15,139,141,0.2); }
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    border-radius: 14px 14px 0 0;
}
.metric-card.teal::before   { background: linear-gradient(90deg, var(--teal), var(--teal-lt)); }
.metric-card.gold::before   { background: linear-gradient(90deg, var(--gold), var(--gold-lt)); }
.metric-card.green::before  { background: linear-gradient(90deg, #3dba7e, #5dd4a0); }
.metric-card.purple::before { background: linear-gradient(90deg, #8b5cf6, #a78bfa); }
.metric-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1;
}
.metric-label { font-size: 0.8rem; color: var(--muted); margin-top: 0.3rem; font-weight: 500; letter-spacing: 0.04em; }

/* ── Card / Panel ── */
.panel {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.panel h4 {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--teal-lt);
    margin-bottom: 0.8rem;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--teal), var(--teal-lt)) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 9px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.4rem !important;
    box-shadow: 0 4px 14px rgba(15,139,141,0.35) !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(15,139,141,0.5) !important;
}
.del-btn > button {
    background: linear-gradient(135deg, #c0392b, var(--danger)) !important;
    box-shadow: 0 4px 14px rgba(224,92,92,0.3) !important;
}

/* ── Form inputs ── */
.stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb],
.stDateInput input, .stTimeInput input {
    background: var(--mid) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 2px rgba(15,139,141,0.2) !important;
}
label { color: var(--muted) !important; font-size: 0.85rem !important; font-weight: 500 !important; }

/* ── Dataframe ── */
.stDataFrame { border-radius: 12px; overflow: hidden; border: 1px solid var(--border); }
.stDataFrame thead th {
    background: var(--teal-dk) !important;
    color: #fff !important;
    font-weight: 600 !important;
}
.stDataFrame tbody tr:nth-child(even) { background: rgba(15,139,141,0.05) !important; }
.stDataFrame tbody tr:hover { background: rgba(15,139,141,0.12) !important; }

/* ── Alerts ── */
.stSuccess { background: rgba(61,186,126,0.15) !important; border-left: 4px solid var(--success) !important; border-radius: 8px !important; }
.stError   { background: rgba(224,92,92,0.15)  !important; border-left: 4px solid var(--danger)  !important; border-radius: 8px !important; }
.stWarning { background: rgba(230,168,23,0.15) !important; border-left: 4px solid var(--gold)    !important; border-radius: 8px !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    gap: 4px;
    border-bottom: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    color: var(--muted) !important;
    background: transparent !important;
    border-radius: 8px 8px 0 0 !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.2rem !important;
}
.stTabs [aria-selected="true"] {
    color: var(--teal-lt) !important;
    border-bottom: 2px solid var(--teal-lt) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-weight: 600 !important;
}
.streamlit-expanderContent { background: var(--card) !important; border: 1px solid var(--border) !important; border-top: none !important; }

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--dark); }
::-webkit-scrollbar-thumb { background: var(--teal-dk); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────
#  CONSTANTS
# ──────────────────────────────────────────────────────────────────
HOSPITAL   = "Jan Kalyan Hospital"
LOCATION   = "Bhopal, Madhya Pradesh"
FILES      = {
    "doctors":      "jkh_doctors.csv",
    "patients":     "jkh_patients.csv",
    "appointments": "jkh_appointments.csv",
    "bills":        "jkh_bills.csv",
}

SPECIALIZATIONS = [
    "Cardiologist", "Neurologist", "Orthopedic Surgeon", "Pediatrician",
    "Gynecologist", "Dermatologist", "General Physician", "ENT Specialist",
    "Ophthalmologist", "Oncologist", "Radiologist", "Anesthesiologist",
    "Gastroenterologist", "Pulmonologist", "Endocrinologist", "Urologist",
    "Psychiatrist", "Nephrologist", "Rheumatologist", "Diabetologist",
]
DISEASES = [
    "Hypertension", "Diabetes Mellitus", "Malaria", "Typhoid",
    "Dengue Fever", "COVID-19", "Pneumonia", "Tuberculosis",
    "Asthma", "Arthritis", "Appendicitis", "Kidney Stone",
    "Heart Disease", "Liver Disease", "Fracture", "Migraine",
    "Anemia", "Thyroid Disorder", "Cancer (Stage I)", "Jaundice",
]


# ──────────────────────────────────────────────────────────────────
#  CSV HELPERS
# ──────────────────────────────────────────────────────────────────
def load_csv(key: str, columns: list) -> pd.DataFrame:
    path = FILES[key]
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            for c in columns:
                if c not in df.columns:
                    df[c] = ""
            return df
        except Exception:
            pass
    return pd.DataFrame(columns=columns)


def save_csv(key: str, df: pd.DataFrame):
    df.to_csv(FILES[key], index=False)


# ──────────────────────────────────────────────────────────────────
#  SESSION STATE
# ──────────────────────────────────────────────────────────────────
def init_state():
    if "doctors" not in st.session_state:
        st.session_state.doctors = load_csv("doctors",
            ["ID", "Name", "Specialization", "Experience (yrs)", "Fee (₹)", "Available"])
    if "patients" not in st.session_state:
        st.session_state.patients = load_csv("patients",
            ["ID", "Name", "Age", "Gender", "Disease", "Room", "Admitted On"])
    if "appointments" not in st.session_state:
        st.session_state.appointments = load_csv("appointments",
            ["ID", "Patient", "Doctor", "Date", "Time", "Status"])
    if "bills" not in st.session_state:
        st.session_state.bills = load_csv("bills",
            ["ID", "Patient", "Doctor Fee (₹)", "Room Charges (₹)",
             "Medicine (₹)", "Lab Charges (₹)", "Total (₹)", "Date", "Status"])

init_state()


# ──────────────────────────────────────────────────────────────────
#  SIDEBAR NAVIGATION
# ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 0.8rem 0 1.4rem;'>
            <div style='font-size:2.8rem;'>🏥</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.15rem;
                        font-weight:800; color:#e8f4f8; line-height:1.3; margin-top:0.4rem;'>
                JAN KALYAN<br>HOSPITAL
            </div>
            <div style='font-size:0.72rem; color:#8aaec0; letter-spacing:0.08em; margin-top:0.3rem;'>
                Bhopal, M.P.
            </div>
        </div>
        <hr style='border-color:rgba(15,139,141,0.2); margin-bottom:1rem;'>
    """, unsafe_allow_html=True)

    nav = st.radio(
        "NAVIGATION",
        ["🏠  Dashboard", "👨‍⚕️  Doctors", "🧑‍🤒  Patients",
         "📅  Appointments", "🧾  Billing", "📊  Analytics"],
        label_visibility="visible",
    )

    today = datetime.date.today()
    st.markdown(f"""
        <div style='position:absolute; bottom:1.5rem; left:1rem; right:1rem;
                    background:rgba(15,139,141,0.1); border:1px solid rgba(15,139,141,0.2);
                    border-radius:10px; padding:0.8rem 1rem; font-size:0.8rem; color:#8aaec0;'>
            <div style='font-weight:600; color:#e8f4f8; margin-bottom:0.2rem;'>📆 {today.strftime("%d %b %Y")}</div>
            <div>HMS v2.0 · JKH System</div>
        </div>
    """, unsafe_allow_html=True)

page = nav.split("  ", 1)[1].strip()


# ──────────────────────────────────────────────────────────────────
#  HEADER BANNER
# ──────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hosp-header">
    <div class="hosp-logo">🏥</div>
    <div>
        <div class="hosp-name">{HOSPITAL}</div>
        <div class="hosp-tagline">🌟 Serving Health · Spreading Hope · {LOCATION}</div>
    </div>
    <div class="hosp-badge">EST. 2005 &nbsp;|&nbsp; NABH Certified</div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────
#  HELPERS
# ──────────────────────────────────────────────────────────────────
def next_id(df):
    return 1 if df.empty else int(df["ID"].max()) + 1

def teal_badge(text):
    return f'<span style="background:rgba(15,139,141,0.2);border:1px solid var(--teal);color:#1ab5b8;border-radius:50px;padding:0.15rem 0.7rem;font-size:0.8rem;font-weight:600;">{text}</span>'

def status_badge(s):
    color = {"Scheduled":"#3dba7e","Cancelled":"#e05c5c","Completed":"#e6a817"}.get(s,"#8aaec0")
    return f'<span style="color:{color};font-weight:700;">{s}</span>'


# ══════════════════════════════════════════════════════════════════
#  DASHBOARD
# ══════════════════════════════════════════════════════════════════
if page == "Dashboard":
    docs  = st.session_state.doctors
    pats  = st.session_state.patients
    apts  = st.session_state.appointments
    bills = st.session_state.bills

    revenue = bills["Total (₹)"].astype(float).sum() if not bills.empty else 0

    st.markdown('<div class="section-title">Dashboard Overview</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-card teal">
            <div class="metric-icon">👨‍⚕️</div>
            <div class="metric-value">{len(docs)}</div>
            <div class="metric-label">Total Doctors</div>
        </div>
        <div class="metric-card gold">
            <div class="metric-icon">🧑‍🤒</div>
            <div class="metric-value">{len(pats)}</div>
            <div class="metric-label">Total Patients</div>
        </div>
        <div class="metric-card green">
            <div class="metric-icon">📅</div>
            <div class="metric-value">{len(apts)}</div>
            <div class="metric-label">Appointments</div>
        </div>
        <div class="metric-card purple">
            <div class="metric-icon">💰</div>
            <div class="metric-value">₹{revenue:,.0f}</div>
            <div class="metric-label">Total Revenue</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Specialization distribution
        if not docs.empty:
            spec_counts = docs["Specialization"].value_counts().reset_index()
            spec_counts.columns = ["Specialization", "Count"]
            fig = px.pie(
                spec_counts, values="Count", names="Specialization",
                title="Doctors by Specialization",
                hole=0.55,
                color_discrete_sequence=px.colors.sequential.Teal,
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_color="#e8f4f8", title_font_size=16,
                legend=dict(font=dict(size=10)),
                margin=dict(t=50, b=10, l=10, r=10),
            )
            fig.update_traces(textfont_color="#fff")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown('<div class="panel"><h4>Doctors by Specialization</h4><p style="color:#8aaec0">No doctor data yet.</p></div>', unsafe_allow_html=True)

    with col2:
        # Disease distribution
        if not pats.empty:
            dis_counts = pats["Disease"].value_counts().head(8).reset_index()
            dis_counts.columns = ["Disease", "Count"]
            fig2 = px.bar(
                dis_counts, x="Count", y="Disease", orientation="h",
                title="Top Diseases (Patients)",
                color="Count",
                color_continuous_scale=[[0,"#0f8b8d"],[1,"#f5c842"]],
            )
            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_color="#e8f4f8", title_font_size=16,
                showlegend=False, coloraxis_showscale=False,
                margin=dict(t=50, b=10, l=10, r=10),
                yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            )
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.markdown('<div class="panel"><h4>Disease Distribution</h4><p style="color:#8aaec0">No patient data yet.</p></div>', unsafe_allow_html=True)

    # Revenue chart
    if not bills.empty and "Date" in bills.columns:
        bills_copy = bills.copy()
        bills_copy["Date"] = pd.to_datetime(bills_copy["Date"], errors="coerce")
        bills_copy = bills_copy.dropna(subset=["Date"])
        if not bills_copy.empty:
            daily = bills_copy.groupby("Date")["Total (₹)"].sum().reset_index()
            fig3 = px.area(
                daily, x="Date", y="Total (₹)",
                title="Daily Revenue Trend",
                color_discrete_sequence=["#1ab5b8"],
            )
            fig3.update_traces(fill="tozeroy", fillcolor="rgba(15,139,141,0.15)")
            fig3.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font_color="#e8f4f8", title_font_size=16,
                margin=dict(t=50, b=10, l=10, r=10),
                xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            )
            st.plotly_chart(fig3, use_container_width=True)

    # Recent appointments
    if not apts.empty:
        st.markdown('<div class="section-title" style="font-size:1.1rem;">Recent Appointments</div>', unsafe_allow_html=True)
        recent = apts.tail(5).sort_index(ascending=False)
        st.dataframe(recent, use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════
#  DOCTORS
# ══════════════════════════════════════════════════════════════════
elif page == "Doctors":
    st.markdown('<div class="section-title">👨‍⚕️ Doctor Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📋 View & Search", "➕ Add Doctor", "✏️ Edit / Delete"])

    with tab1:
        docs = st.session_state.doctors
        col_s, col_f = st.columns([3, 1])
        with col_s:
            search = st.text_input("🔍 Search by name or specialization", placeholder="e.g. Sharma / Cardiologist")
        with col_f:
            spec_filter = st.selectbox("Filter by Specialization", ["All"] + SPECIALIZATIONS)

        filtered = docs.copy()
        if search:
            mask = (filtered["Name"].str.contains(search, case=False, na=False) |
                    filtered["Specialization"].str.contains(search, case=False, na=False))
            filtered = filtered[mask]
        if spec_filter != "All":
            filtered = filtered[filtered["Specialization"] == spec_filter]

        if filtered.empty:
            st.warning("No doctors found.")
        else:
            st.success(f"{len(filtered)} doctor(s) found")
            st.dataframe(filtered, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("add_doctor_form", clear_on_submit=True):
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#1ab5b8; margin-bottom:1rem;">Add New Doctor</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                d_name = st.text_input("Doctor Name *")
                d_spec = st.selectbox("Specialization *", SPECIALIZATIONS)
            with c2:
                d_exp  = st.number_input("Experience (years) *", min_value=0, max_value=60, value=5)
                d_fee  = st.number_input("Consultation Fee (₹) *", min_value=100, max_value=10000, value=500, step=50)
            d_avail = st.selectbox("Availability", ["Yes", "No"])
            submitted = st.form_submit_button("✅ Add Doctor")
            if submitted:
                if not d_name.strip():
                    st.error("Doctor name is required.")
                else:
                    new_row = pd.DataFrame([{
                        "ID": next_id(st.session_state.doctors),
                        "Name": d_name.strip().title(),
                        "Specialization": d_spec,
                        "Experience (yrs)": d_exp,
                        "Fee (₹)": d_fee,
                        "Available": d_avail,
                    }])
                    st.session_state.doctors = pd.concat([st.session_state.doctors, new_row], ignore_index=True)
                    save_csv("doctors", st.session_state.doctors)
                    st.success(f"✅ Dr. {d_name.strip().title()} added successfully!")

    with tab3:
        docs = st.session_state.doctors
        if docs.empty:
            st.info("No doctors to edit.")
        else:
            doc_opts = {f"ID {r['ID']} – {r['Name']}": r["ID"] for _, r in docs.iterrows()}
            sel = st.selectbox("Select Doctor", list(doc_opts.keys()))
            sel_id = doc_opts[sel]
            row = docs[docs["ID"] == sel_id].iloc[0]

            with st.form("edit_doctor_form"):
                ec1, ec2 = st.columns(2)
                with ec1:
                    new_spec = st.selectbox("Specialization", SPECIALIZATIONS,
                        index=SPECIALIZATIONS.index(row["Specialization"]) if row["Specialization"] in SPECIALIZATIONS else 0)
                    new_exp  = st.number_input("Experience (yrs)", min_value=0, max_value=60,
                        value=int(row["Experience (yrs)"]))
                with ec2:
                    new_fee   = st.number_input("Fee (₹)", min_value=100, max_value=10000,
                        value=int(row["Fee (₹)"]), step=50)
                    new_avail = st.selectbox("Available", ["Yes", "No"],
                        index=0 if row.get("Available", "Yes") == "Yes" else 1)

                upd, dele = st.columns(2)
                with upd:
                    if st.form_submit_button("💾 Update"):
                        mask = st.session_state.doctors["ID"] == sel_id
                        st.session_state.doctors.loc[mask, "Specialization"]   = new_spec
                        st.session_state.doctors.loc[mask, "Experience (yrs)"] = new_exp
                        st.session_state.doctors.loc[mask, "Fee (₹)"]          = new_fee
                        st.session_state.doctors.loc[mask, "Available"]        = new_avail
                        save_csv("doctors", st.session_state.doctors)
                        st.success("✅ Doctor updated!")
                with dele:
                    if st.form_submit_button("🗑️ Delete Doctor"):
                        st.session_state.doctors = docs[docs["ID"] != sel_id].reset_index(drop=True)
                        save_csv("doctors", st.session_state.doctors)
                        st.success("✅ Doctor deleted!")
                        st.rerun()


# ══════════════════════════════════════════════════════════════════
#  PATIENTS
# ══════════════════════════════════════════════════════════════════
elif page == "Patients":
    st.markdown('<div class="section-title">🧑‍🤒 Patient Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📋 View & Search", "➕ Admit Patient", "✏️ Edit / Discharge"])

    with tab1:
        pats = st.session_state.patients
        c1, c2 = st.columns([3, 1])
        with c1:
            srch = st.text_input("🔍 Search by name, disease, or room", placeholder="e.g. Rahul / Malaria / 101")
        with c2:
            dis_filter = st.selectbox("Filter Disease", ["All"] + DISEASES)

        fp = pats.copy()
        if srch:
            mask = (fp["Name"].str.contains(srch, case=False, na=False) |
                    fp["Disease"].str.contains(srch, case=False, na=False) |
                    fp["Room"].astype(str).str.contains(srch, case=False, na=False))
            fp = fp[mask]
        if dis_filter != "All":
            fp = fp[fp["Disease"] == dis_filter]

        if fp.empty:
            st.warning("No patients found.")
        else:
            st.success(f"{len(fp)} patient(s) found")
            st.dataframe(fp, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("add_patient_form", clear_on_submit=True):
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#1ab5b8; margin-bottom:1rem;">Admit New Patient</div>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                p_name = st.text_input("Patient Name *")
                p_age  = st.number_input("Age *", min_value=0, max_value=120, value=30)
            with c2:
                p_gen  = st.selectbox("Gender", ["Male", "Female", "Other"])
                p_dis  = st.selectbox("Disease *", DISEASES)
            with c3:
                p_room = st.text_input("Room Number *", placeholder="e.g. 201-A")
                p_date = st.date_input("Admission Date", value=datetime.date.today())
            if st.form_submit_button("✅ Admit Patient"):
                if not p_name.strip() or not p_room.strip():
                    st.error("Name and room number are required.")
                else:
                    new_p = pd.DataFrame([{
                        "ID": next_id(st.session_state.patients),
                        "Name": p_name.strip().title(),
                        "Age": p_age,
                        "Gender": p_gen,
                        "Disease": p_dis,
                        "Room": p_room.strip().upper(),
                        "Admitted On": str(p_date),
                    }])
                    st.session_state.patients = pd.concat([st.session_state.patients, new_p], ignore_index=True)
                    save_csv("patients", st.session_state.patients)
                    st.success(f"✅ {p_name.strip().title()} admitted in Room {p_room.strip().upper()}!")

    with tab3:
        pats = st.session_state.patients
        if pats.empty:
            st.info("No patients to edit.")
        else:
            p_opts = {f"ID {r['ID']} – {r['Name']} (Room {r['Room']})": r["ID"] for _, r in pats.iterrows()}
            sel_p  = st.selectbox("Select Patient", list(p_opts.keys()))
            sel_pid = p_opts[sel_p]
            prow = pats[pats["ID"] == sel_pid].iloc[0]

            with st.form("edit_patient"):
                pc1, pc2 = st.columns(2)
                with pc1:
                    new_dis  = st.selectbox("Disease", DISEASES,
                        index=DISEASES.index(prow["Disease"]) if prow["Disease"] in DISEASES else 0)
                with pc2:
                    new_room = st.text_input("Room Number", value=str(prow["Room"]))

                pu, pd_ = st.columns(2)
                with pu:
                    if st.form_submit_button("💾 Update"):
                        m = st.session_state.patients["ID"] == sel_pid
                        st.session_state.patients.loc[m, "Disease"] = new_dis
                        st.session_state.patients.loc[m, "Room"]    = new_room.strip().upper()
                        save_csv("patients", st.session_state.patients)
                        st.success("✅ Patient record updated!")
                with pd_:
                    if st.form_submit_button("🚪 Discharge Patient"):
                        st.session_state.patients = pats[pats["ID"] != sel_pid].reset_index(drop=True)
                        save_csv("patients", st.session_state.patients)
                        st.success("✅ Patient discharged!")
                        st.rerun()


# ══════════════════════════════════════════════════════════════════
#  APPOINTMENTS
# ══════════════════════════════════════════════════════════════════
elif page == "Appointments":
    st.markdown('<div class="section-title">📅 Appointment Management</div>', unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["📋 All Appointments", "➕ Book Appointment", "✏️ Update / Cancel"])

    with tab1:
        apts = st.session_state.appointments
        c1, c2, c3 = st.columns(3)
        with c1:
            date_filter = st.date_input("Filter by Date", value=None)
        with c2:
            stat_filter = st.selectbox("Status", ["All", "Scheduled", "Completed", "Cancelled"])
        with c3:
            apt_srch = st.text_input("🔍 Search Patient / Doctor")

        fa = apts.copy()
        if date_filter:
            fa = fa[fa["Date"] == str(date_filter)]
        if stat_filter != "All":
            fa = fa[fa["Status"] == stat_filter]
        if apt_srch:
            fa = fa[fa["Patient"].str.contains(apt_srch, case=False, na=False) |
                    fa["Doctor"].str.contains(apt_srch, case=False, na=False)]

        if fa.empty:
            st.warning("No appointments found.")
        else:
            st.success(f"{len(fa)} appointment(s) found")
            st.dataframe(fa, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("book_appt", clear_on_submit=True):
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#1ab5b8; margin-bottom:1rem;">Book New Appointment</div>', unsafe_allow_html=True)
            docs_list = (list(st.session_state.doctors["Name"]) if not st.session_state.doctors.empty else [])
            pats_list = (list(st.session_state.patients["Name"]) if not st.session_state.patients.empty else [])

            c1, c2 = st.columns(2)
            with c1:
                if pats_list:
                    a_pat = st.selectbox("Patient *", pats_list)
                else:
                    a_pat = st.text_input("Patient Name *", placeholder="No patients found – type manually")
                a_date = st.date_input("Date *", value=datetime.date.today())
            with c2:
                if docs_list:
                    a_doc = st.selectbox("Doctor *", docs_list)
                else:
                    a_doc = st.text_input("Doctor Name *", placeholder="No doctors found – type manually")
                a_time = st.selectbox("Time Slot *",
                    ["09:00 AM","09:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM",
                     "12:00 PM","02:00 PM","02:30 PM","03:00 PM","03:30 PM","04:00 PM","04:30 PM","05:00 PM"])

            if st.form_submit_button("✅ Book Appointment"):
                if not str(a_pat).strip() or not str(a_doc).strip():
                    st.error("Patient and doctor are required.")
                else:
                    new_a = pd.DataFrame([{
                        "ID":      next_id(st.session_state.appointments),
                        "Patient": str(a_pat).strip().title(),
                        "Doctor":  str(a_doc).strip().title(),
                        "Date":    str(a_date),
                        "Time":    a_time,
                        "Status":  "Scheduled",
                    }])
                    st.session_state.appointments = pd.concat([st.session_state.appointments, new_a], ignore_index=True)
                    save_csv("appointments", st.session_state.appointments)
                    st.success(f"✅ Appointment booked for {a_pat} with {a_doc} on {a_date} at {a_time}!")

    with tab3:
        apts = st.session_state.appointments
        if apts.empty:
            st.info("No appointments to update.")
        else:
            a_opts = {f"ID {r['ID']} – {r['Patient']} → Dr.{r['Doctor']} | {r['Date']} {r['Time']}": r["ID"]
                      for _, r in apts.iterrows()}
            sel_a   = st.selectbox("Select Appointment", list(a_opts.keys()))
            sel_aid = a_opts[sel_a]
            arow    = apts[apts["ID"] == sel_aid].iloc[0]

            with st.form("edit_appt"):
                ec1, ec2, ec3 = st.columns(3)
                with ec1:
                    n_date = st.date_input("New Date", value=pd.to_datetime(arow["Date"]).date())
                with ec2:
                    n_time = st.selectbox("New Time",
                        ["09:00 AM","09:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM",
                         "12:00 PM","02:00 PM","02:30 PM","03:00 PM","03:30 PM","04:00 PM","04:30 PM","05:00 PM"])
                with ec3:
                    n_stat = st.selectbox("Status", ["Scheduled", "Completed", "Cancelled"],
                        index=["Scheduled","Completed","Cancelled"].index(arow.get("Status","Scheduled")))

                ua, ca = st.columns(2)
                with ua:
                    if st.form_submit_button("💾 Update"):
                        m = st.session_state.appointments["ID"] == sel_aid
                        st.session_state.appointments.loc[m, "Date"]   = str(n_date)
                        st.session_state.appointments.loc[m, "Time"]   = n_time
                        st.session_state.appointments.loc[m, "Status"] = n_stat
                        save_csv("appointments", st.session_state.appointments)
                        st.success("✅ Appointment updated!")
                with ca:
                    if st.form_submit_button("❌ Cancel Appointment"):
                        m = st.session_state.appointments["ID"] == sel_aid
                        st.session_state.appointments.loc[m, "Status"] = "Cancelled"
                        save_csv("appointments", st.session_state.appointments)
                        st.success("✅ Appointment cancelled!")
                        st.rerun()


# ══════════════════════════════════════════════════════════════════
#  BILLING
# ══════════════════════════════════════════════════════════════════
elif page == "Billing":
    st.markdown('<div class="section-title">🧾 Billing & Payments</div>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["➕ Generate Bill", "📋 All Bills"])

    with tab1:
        pats_list = (list(st.session_state.patients["Name"]) if not st.session_state.patients.empty else [])
        docs_list = (list(st.session_state.doctors["Name"])  if not st.session_state.doctors.empty  else [])

        with st.form("gen_bill", clear_on_submit=False):
            st.markdown('<div style="font-family:\'Playfair Display\',serif; font-size:1.1rem; color:#1ab5b8; margin-bottom:1rem;">Generate Patient Bill</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if pats_list:
                    b_pat = st.selectbox("Patient *", pats_list)
                else:
                    b_pat = st.text_input("Patient Name *")
                b_doc_fee  = st.number_input("Doctor Consultation Fee (₹)", min_value=0, value=500, step=50)
                b_room     = st.number_input("Room Charges / Day (₹)", min_value=0, value=1000, step=100)
            with c2:
                if docs_list:
                    b_doc = st.selectbox("Attending Doctor", docs_list)
                else:
                    b_doc = st.text_input("Attending Doctor")
                b_med   = st.number_input("Medicine Charges (₹)", min_value=0, value=300, step=50)
                b_lab   = st.number_input("Lab / Diagnostic Charges (₹)", min_value=0, value=200, step=50)

            b_status = st.selectbox("Payment Status", ["Pending", "Paid", "Partial"])
            total    = b_doc_fee + b_room + b_med + b_lab

            # Live total preview
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(15,139,141,0.2),rgba(230,168,23,0.1));
                        border:1px solid rgba(15,139,141,0.3); border-radius:12px;
                        padding:1rem 1.4rem; margin:0.8rem 0; display:flex; align-items:center; gap:1rem;">
                <span style="font-size:1.8rem;">💰</span>
                <div>
                    <div style="font-size:0.8rem; color:#8aaec0; letter-spacing:0.06em;">TOTAL AMOUNT</div>
                    <div style="font-family:'Playfair Display',serif; font-size:2rem; font-weight:700; color:#f5c842;">
                        ₹{total:,}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.form_submit_button("🧾 Generate Bill"):
                if not str(b_pat).strip():
                    st.error("Patient name is required.")
                else:
                    new_b = pd.DataFrame([{
                        "ID":               next_id(st.session_state.bills),
                        "Patient":          str(b_pat).strip().title(),
                        "Doctor Fee (₹)":   b_doc_fee,
                        "Room Charges (₹)": b_room,
                        "Medicine (₹)":     b_med,
                        "Lab Charges (₹)":  b_lab,
                        "Total (₹)":        total,
                        "Date":             str(datetime.date.today()),
                        "Status":           b_status,
                    }])
                    st.session_state.bills = pd.concat([st.session_state.bills, new_b], ignore_index=True)
                    save_csv("bills", st.session_state.bills)
                    st.success(f"✅ Bill generated for {b_pat}! Total: ₹{total:,}")
                    st.balloons()

    with tab2:
        bills = st.session_state.bills
        if bills.empty:
            st.info("No bills generated yet.")
        else:
            total_rev = bills["Total (₹)"].astype(float).sum()
            paid      = bills[bills["Status"] == "Paid"]["Total (₹)"].astype(float).sum()
            pending   = bills[bills["Status"] == "Pending"]["Total (₹)"].astype(float).sum()

            c1, c2, c3 = st.columns(3)
            c1.metric("Total Revenue", f"₹{total_rev:,.0f}")
            c2.metric("Paid",          f"₹{paid:,.0f}")
            c3.metric("Pending",       f"₹{pending:,.0f}")

            st.dataframe(bills, use_container_width=True, hide_index=True)


# ══════════════════════════════════════════════════════════════════
#  ANALYTICS
# ══════════════════════════════════════════════════════════════════
elif page == "Analytics":
    st.markdown('<div class="section-title">📊 Hospital Analytics</div>', unsafe_allow_html=True)

    docs  = st.session_state.doctors
    pats  = st.session_state.patients
    apts  = st.session_state.appointments
    bills = st.session_state.bills

    # KPI row
    revenue = bills["Total (₹)"].astype(float).sum() if not bills.empty else 0
    avg_fee = docs["Fee (₹)"].astype(float).mean()  if not docs.empty  else 0
    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-card teal">
            <div class="metric-icon">🏥</div>
            <div class="metric-value">{len(docs)}</div>
            <div class="metric-label">Doctors</div>
        </div>
        <div class="metric-card gold">
            <div class="metric-icon">👥</div>
            <div class="metric-value">{len(pats)}</div>
            <div class="metric-label">Patients</div>
        </div>
        <div class="metric-card green">
            <div class="metric-icon">💰</div>
            <div class="metric-value">₹{revenue:,.0f}</div>
            <div class="metric-label">Revenue</div>
        </div>
        <div class="metric-card purple">
            <div class="metric-icon">📊</div>
            <div class="metric-value">₹{avg_fee:,.0f}</div>
            <div class="metric-label">Avg Doc Fee</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    # Appointments by status
    with c1:
        if not apts.empty:
            stat_cnt = apts["Status"].value_counts().reset_index()
            stat_cnt.columns = ["Status", "Count"]
            fig = px.pie(stat_cnt, values="Count", names="Status",
                         title="Appointment Status Breakdown",
                         color_discrete_sequence=["#3dba7e","#e05c5c","#e6a817"])
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e8f4f8",
                              title_font_size=15, margin=dict(t=50,b=10,l=10,r=10))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No appointment data.")

    # Doctor fee comparison
    with c2:
        if not docs.empty:
            top_docs = docs.nlargest(8, "Fee (₹)")
            fig2 = px.bar(top_docs, x="Fee (₹)", y="Name", orientation="h",
                          title="Top Doctors by Fee",
                          color="Fee (₹)",
                          color_continuous_scale=[[0,"#0f8b8d"],[1,"#e6a817"]])
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e8f4f8",
                               title_font_size=15, coloraxis_showscale=False,
                               margin=dict(t=50,b=10,l=10,r=10),
                               yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                               xaxis=dict(gridcolor="rgba(255,255,255,0.05)"))
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No doctor data.")

    # Age distribution
    c3, c4 = st.columns(2)
    with c3:
        if not pats.empty:
            fig3 = px.histogram(pats, x="Age", nbins=15, title="Patient Age Distribution",
                                color_discrete_sequence=["#1ab5b8"])
            fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e8f4f8",
                               title_font_size=15, bargap=0.05,
                               margin=dict(t=50,b=10,l=10,r=10),
                               plot_bgcolor="rgba(0,0,0,0)",
                               xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                               yaxis=dict(gridcolor="rgba(255,255,255,0.05)"))
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No patient data.")

    # Bill component breakdown
    with c4:
        if not bills.empty:
            doc_total  = bills["Doctor Fee (₹)"].astype(float).sum()
            room_total = bills["Room Charges (₹)"].astype(float).sum()
            med_total  = bills["Medicine (₹)"].astype(float).sum()
            lab_total  = bills["Lab Charges (₹)"].astype(float).sum()
            labels = ["Doctor Fee", "Room Charges", "Medicine", "Lab"]
            values = [doc_total, room_total, med_total, lab_total]
            fig4 = go.Figure(go.Bar(
                x=labels, y=values,
                marker_color=["#0f8b8d","#e6a817","#3dba7e","#8b5cf6"],
            ))
            fig4.update_layout(title="Revenue by Component",
                               paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="#e8f4f8", title_font_size=15,
                               margin=dict(t=50,b=10,l=10,r=10),
                               xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                               yaxis=dict(gridcolor="rgba(255,255,255,0.05)"))
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("No billing data.")

    # Gender pie
    if not pats.empty and "Gender" in pats.columns:
        gen_cnt = pats["Gender"].value_counts().reset_index()
        gen_cnt.columns = ["Gender", "Count"]
        fig5 = px.pie(gen_cnt, values="Count", names="Gender",
                      title="Patient Gender Distribution",
                      color_discrete_sequence=["#1ab5b8","#e6a817","#8b5cf6"],
                      hole=0.45)
        fig5.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#e8f4f8",
                           title_font_size=15, margin=dict(t=50,b=10,l=10,r=10))
        st.plotly_chart(fig5, use_container_width=True)


# ──────────────────────────────────────────────────────────────────
#  FOOTER
# ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(f"""
<div style="text-align:center; color:#8aaec0; font-size:0.82rem; padding:0.6rem 0;">
    🏥 <strong style="color:#1ab5b8;">Jan Kalyan Hospital</strong> &nbsp;·&nbsp;
    {LOCATION} &nbsp;·&nbsp;
    Hospital Management System v2.0 &nbsp;·&nbsp;
    © {datetime.date.today().year} All Rights Reserved
</div>
""", unsafe_allow_html=True)