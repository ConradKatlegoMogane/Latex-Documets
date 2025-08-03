### 💻 Full Streamlit CV App Code — Enhanced Version

import streamlit as st

# ---------- Page Setup ----------
st.set_page_config(page_title="Conrad Mogane - CV", layout="wide", initial_sidebar_state="expanded")

# ---------- Header ----------
st.title("👨‍🔬 Conrad Katlego Mogane")
st.markdown("""
📧 **Email:** conradmogane@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/conrad-mogane-55a8947b](https://www.linkedin.com/in/conrad-mogane-55a8947b)  
🐙 **GitHub:** [github.com/ConradKatlegoMogane](https://github.com/ConradKatlegoMogane)

---

**Multidisciplinary Laboratory Specialist & Data Science Practitioner**  
Bridging biomedical research with modern data science. Skilled in developing scalable data workflows, designing visual dashboards, and deploying analytical tools to improve public health decision-making.
""")

# ---------- Sidebar Navigation ----------
st.sidebar.image("https://github.com/ConradKatlegoMogane/Latex-Documets/blob/main/IMG_8372.JPG", width=150)  # Replace with your GitHub avatar URL
st.sidebar.title("📁 Professional CV")
section = st.sidebar.radio("Jump to section:", [
    "Profile Summary", "Skills", "Experience", "Education", "Certifications", "Publications", "Projects", "Contact"
])

# ---------- Profile Summary ----------
if section == "Profile Summary":
    st.header("🧭 Profile Summary")
    st.markdown("""
    - ⚗️ Biomedical specialist with hands-on lab experience across genomics, chemical analyses, and SOP-driven clinical environments  
    - 🧠 Analyst with strong Python, SQL, and R capabilities for regression modeling, automation, and dashboard development  
    - 🏥 Public health enthusiast applying structured data workflows to enhance outcome tracking and evidence-based policy  
    - 🎨 Infographic designer and Jupyter-based educator promoting visual clarity and accessibility in scientific communication
    """)

# ---------- Skills Section ----------
if section == "Skills":
    st.header("💼 Technical & Scientific Skills")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🧬 Bioinformatics")
        st.markdown("""
        - NGS pipeline workflows  
        - DNA/RNA extraction, ELISpot  
        - Western blotting & PCR  
        - Flow cytometry interpretation  
        """)
    with col2:
        st.subheader("📊 Data & Programming")
        st.markdown("""
        - Python (pandas, regex, matplotlib, statsmodels)  
        - R and R Shiny dashboards  
        - SQL database design & normalization  
        - Streamlit, Dash, Jupyter Notebooks  
        """)
    with col3:
        st.subheader("📈 Analysis & Visualization")
        st.markdown("""
        - Regression modeling & diagnostics  
        - KPI tracking via Power BI & Excel  
        - Infographic creation in artsy & academic styles  
        - Autocorrelation testing and model validation  
        """)

# ---------- Experience Section ----------
if section == "Experience":
    st.header("🧪 Professional Experience")
    
    experiences = {
        "UKZN – Laboratory Technologist": {
            "dates": "Apr 2019 – Apr 2025",
            "details": [
                "Conducted ELISpot assays and flow cytometry",
                "Tracked NGS samples and curated metadata",
                "Developed Power BI dashboards for lab KPIs",
                "Integrated Python scripts for automation"
            ]
        },
        "MRC/Wits – Clinical Scientist": {
            "dates": "Jun 2018 – Mar 2019",
            "details": [
                "Performed chemical lab testing in clinical trials",
                "Managed inventory and SOP documentation",
                "Supported MSSQL integration and QC workflows"
            ]
        },
        "Wits University – Research Assistant": {
            "dates": "Jan 2017 – Apr 2018",
            "details": [
                "Designed and led experimental protocols",
                "Presented at internal symposiums",
                "Mentored junior researchers and managed lab budgets"
            ]
        }
    }

    for role, info in experiences.items():
        with st.expander(f"🔍 {role} ({info['dates']})"):
            for point in info['details']:
                st.markdown(f"- {point}")

# ---------- Education Section ----------
if section == "Education":
    st.header("🎓 Academic Background")
    education = {
        "University of KwaZulu Natal": "Master of Public Health – Epidemiology & Biostatistics",
        "University of Zululand": "BSc (Hons) in Biochemistry"
    }
    for school, degree in education.items():
        st.markdown(f"**{school}** — *{degree}*")

# ---------- Certifications Section ----------
if section == "Certifications":
    st.header("📜 Certifications & Professional Development")
    certifications = [
        "Data Science Techniques in Bioinformatics",
        "Good Clinical Laboratory Practice (GCLP)",
        "Regression Diagnostics and Statistical Modeling",
        "Infographic Design for Scientific Communication"
    ]
    for cert in certifications:
        st.write(f"- {cert}")

# ---------- Publications Section ----------
if section == "Publications":
    st.header("📰 Publications & Visual Essays")
    st.markdown("""
    _Coming soon: Interactive infographics and write-ups from public health regression studies and qualitative sampling visualizations._  
    You can use `st.image()` or `st.markdown()` to embed charts and papers.
    """)

# ---------- Projects Section ----------
if section == "Projects":
    st.header("🧪 Featured Projects")
    st.markdown("""
    **1. Regression Diagnostics on Vehicle Pricing Dataset**  
    Explored autocorrelation, model fit, and multicollinearity using Python  
    🔗 GitHub: [View Project](https://github.com/ConradKatlegoMogane)

    **2. MSSQL-LIMS Integration**  
    Automated data pipeline syncing lab data and SQL backends

    **3. Recruitment Dashboard Using R Shiny**  
    Built real-time tracking tool for candidate metrics and lab KPIs
    """)

# ---------- Contact Section ----------
if section == "Contact":
    st.header("📬 Get in Touch")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent! I’ll be in touch soon.")


