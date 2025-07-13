import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- Page Settings ---
st.set_page_config(
    page_title="Mujakkir Ahmad | Portfolio", 
    layout="wide",
    page_icon="📊"
)
# Add this RIGHT AFTER your set_page_config()
st.markdown("""
<style>
/* Paste the entire CSS content here */
.stApp {
    background-color: #041a30;
    padding: 2rem 4rem;
}

/* Rest of the CSS rules... */
</style>
""", unsafe_allow_html=True)

# Replace your current load_css() function with this version:
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"CSS Error: {str(e)}")

# Call this RIGHT AFTER set_page_config()
load_css()

# --- Sidebar ---
try:
    profile_img = Image.open("profile.jpg")
    st.sidebar.image(profile_img, width=150)
except:
    st.sidebar.image("https://via.placeholder.com/150", width=150)

st.sidebar.title("👨‍💻 Mujakkir Ahmad")
st.sidebar.markdown("📊 Data Analyst | Accountant")
st.sidebar.markdown("📍 Dhaka, Bangladesh")

# Contact links with icons
st.sidebar.markdown("### 📬 Contact Info")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/mujakkir-dv)")
st.sidebar.markdown("💻 [GitHub](https://github.com/mujakkirdv)")
st.sidebar.markdown("📧 [mujakkirar@gmail.com](mailto:mujakkirar@gmail.com)")
st.sidebar.markdown("📞 +8801787933422")

# Navigation
page = st.sidebar.radio("📂 Navigation", ["🏠 Home", "📊 Projects", "📄 Resume", "📞 Contact", "🧑 About Me"])

# --- HOME PAGE ---
if page == "🏠 Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            st.image(profile_img, width=300)
        except:
            st.image("https://via.placeholder.com/300", width=300)
    
    with col2:
        st.title("👋 Welcome to My Portfolio")
        st.markdown("""
        I'm **Mujakkir Ahmad**, a passionate Data Analyst and Accounts Executive with expertise in:
        - Python (Pandas, Streamlit)
        - Data Visualization (Plotly, Matplotlib)
        - Business Intelligence Dashboards
        - Financial Reporting Automation
        """)
    
    st.markdown("---")
    
    st.subheader("🎯 Career Objective")
    st.markdown("""
    Seeking a **Data Analyst** or **Senior Executive – Accounts & Finance** position where I can:
    - Utilize my skills in Python, Excel, and data visualization
    - Support data-driven decision-making
    - Build automated business reports
    - Deliver actionable insights to improve efficiency
    """)
    
    st.markdown("---")
    
    st.subheader("🛠️ Core Competencies")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**Data Analysis**")
        st.markdown("- Pandas, NumPy\n- Excel, Google Sheets\n- SQL Basics")
    
    with cols[1]:
        st.markdown("**Visualization**")
        st.markdown("- Plotly, Matplotlib\n- Streamlit Dashboards\n- Power BI")
    
    with cols[2]:
        st.markdown("**Business Skills**")
        st.markdown("- Financial Reporting\n- Sales Analysis\n- Process Automation")

# --- PROJECTS PAGE ---
elif page == "📊 Projects":
    st.title("📊 Data Analysis Projects")
    st.markdown("Here are some of my data analysis projects and visualizations:")
    
    try:
        df = pd.read_excel("sales.xlsx")
        
        # Project 1 - Sales Dashboard
        with st.expander("💰 Sales Performance Dashboard", expanded=True):
            st.markdown("### 📈 Sales by Executive")
            fig1 = px.bar(
                df.groupby("sales_executive")["sales_amount"].sum().reset_index(),
                x="sales_executive", 
                y="sales_amount",
                color="sales_executive",
                title="Total Sales by Sales Executive"
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            st.markdown("### 🏆 Top Customers")
            fig2 = px.pie(
                df.groupby("customer_name")["sales_amount"].sum().reset_index(),
                names="customer_name", 
                values="sales_amount",
                title="Sales Distribution by Customer"
            )
            st.plotly_chart(fig2, use_container_width=True)
            
            st.markdown("### 💰 Profit Breakdown")
            profit_df = df[["executive_commission", "teamleader_commission", "gm_commission", "company_profit"]].sum().reset_index()
            profit_df.columns = ["Category", "Amount"]
            fig3 = px.bar(
                profit_df, 
                x="Category", 
                y="Amount", 
                color="Category", 
                title="Profit & Commission Summary"
            )
            st.plotly_chart(fig3, use_container_width=True)
    
    except Exception as e:
        st.warning("⚠️ Sample data not found. Please ensure 'sales.xlsx' is in the 'data/' folder.")
        st.error(f"Error: {str(e)}")
    
    # Placeholder for additional projects
    with st.expander("📊 Other Projects"):
        st.markdown("""
        **Additional projects coming soon:**
        - Financial reporting automation tool
        - Inventory management dashboard
        - Sales forecasting model
        """)

# --- RESUME PAGE ---
elif page == "📄 Resume":
    st.title("📄 Professional Resume")
    
    # Download button
    try:
        with open("Mujakkir_Ahmad_CV_2025.pdf", "rb") as f:
            st.download_button(
                "📥 Download Full CV", 
                f, 
                file_name="Mujakkir_Ahmad_Resume.pdf",
                mime="application/pdf"
            )
    except:
        st.warning("CV file not found in assets folder")
    
    st.markdown("---")
    
    # Professional Summary
    st.header("🧠 Professional Summary")
    st.markdown("""
    Data Analyst and Accounts Professional with:
    - 5+ years cross-industry experience
    - Strong Python (Pandas, Streamlit) and Excel skills
    - Expertise in building business dashboards
    - Process automation capabilities
    """)
    
    st.markdown("---")
    
    # Work Experience
    st.header("💼 Work Experience")
    
    exp1 = st.container()
    with exp1:
        st.subheader("Account Automation Executive")
        st.markdown("**Welburg Metal Pvt Ltd** | *2022-Present*")
        st.markdown("""
        - Developed automated financial reports using Python
        - Created Streamlit dashboards for sales analysis
        - Implemented data validation processes
        """)
    
    exp2 = st.container()
    with exp2:
        st.subheader("Product Data Executive")
        st.markdown("**CT Health Limited** | *2020-2022*")
        st.markdown("""
        - Managed product databases
        - Generated sales performance reports
        - Assisted in inventory management
        """)
    
    st.markdown("---")
    
    # Education
    st.header("🎓 Education")
    st.markdown("""
    - **B.A.**, Brindaban Govt. College, Habigonj
    - **HSC (Science)**, Shaistaganj Degree College
    - **SSC (Science)**, Masud Chaudhary School
    """)
    
    st.markdown("---")
    
    # Skills
    st.header("🛠️ Technical Skills")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**Programming**")
        st.markdown("- Python (Pandas)\n- SQL Basics\n- HTML")
    
    with cols[1]:
        st.markdown("**Data Tools**")
        st.markdown("- Excel\n- Power BI\n- Streamlit")
    
    with cols[2]:
        st.markdown("**Other**")
        st.markdown("- Financial Reporting\n- Process Automation\n- Dashboard Design")

# --- CONTACT PAGE ---
elif page == "📞 Contact":
    st.title("📞 Contact Me")
    
    # Contact form
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name*", placeholder="Your name")
        email = st.text_input("Email*", placeholder="Your email address")
        message = st.text_area("Message*", placeholder="Your message here...", height=150)
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and message:
                st.success("Thank you for your message! I'll respond within 24 hours.")
            else:
                st.error("Please fill in all required fields (*)")
    
    st.markdown("---")
    
    # Contact information
    st.subheader("📍 Other Contact Methods")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📧 Email**")
        st.markdown("mujakkirar@gmail.com")
        
        st.markdown("**📞 Phone**")
        st.markdown("+8801787933422  \n+8801601933422")
    
    with col2:
        st.markdown("**🌐 Social Media**")
        st.markdown("- [LinkedIn](https://linkedin.com/in/mujakkir-dv)")
        st.markdown("- [GitHub](https://github.com/mujakkirdv)")
        st.markdown("- [Facebook](https://facebook.com/mujakkirdv)")
    
    # Map
    st.markdown("---")
    st.subheader("🗺️ Location")
    st.map()

# --- ABOUT ME PAGE ---
elif page == "🧑 About Me":

    # --- Sidebar Theme Selection ---
    theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

    # --- Theme CSS ---
    if theme == "Dark":
        st.markdown("""
            <style>
            body {background-color: #0E1117; color: #FAFAFA;}
            .title {color: #61dafb;}
            .subtitle {color: #BBBBBB;}
            .desc, .skillbox {color: #DDDDDD;}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            body {background-color: #FFFFFF; color: #000000;}
            .title {color: #2C3E50;}
            .subtitle {color: #34495E;}
            .desc, .skillbox {color: #2F4F4F;}
            </style>
        """, unsafe_allow_html=True)

    # --- Shared CSS ---
    st.markdown("""
        <style>
        .title {font-size:32px; font-weight:700; padding-bottom:10px;}
        .subtitle {font-size:20px; padding-bottom:10px;}
        .desc {font-size:16px; line-height:1.6;}
        .highlight {color:#E74C3C; font-weight:bold;}
        .skillbox {background-color:#f1f3f6; padding:8px 12px; display:inline-block; margin:5px; border-radius:8px;}
        .social-icons a {text-decoration: none; font-size:18px; margin-right:15px;}
        </style>
    """, unsafe_allow_html=True)

    # --- Profile Section ---
    prof_col1, prof_col2 = st.columns([1, 2], gap="large")

    with prof_col1:
        st.image("assets/profile.jpg", width=250, caption="Mujakkir Ahmad")

    with prof_col2:
        st.markdown('<div class="title">👋 Hi, I\'m Mujakkir Ahmad</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Data Analyst | Python Developer | Streamlit Enthusiast</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="desc">
            I’m Mujakkir Ahmad — a tech-savvy, hardworking, and self-driven individual whose mission is to solve problems through data and empower smarter business decisions. I currently work as a <b>Data Analyst</b> in the <b>Accounts Department of Welburg Metal Pvt Ltd</b>.<br><br>

            My responsibilities include analyzing sales, invoices, commissions, and customer data using Google Sheets; preparing reports for sales representatives and customers; and presenting insights to the Marketing General Manager and Managing Director.<br><br>

            I have completed my B.A. (Honours) from Brindaban Government College and am currently enrolled in the <b>Post Graduate Diploma in Data Analytics (PGDA)</b> under National University. I began my learning journey with <b>freeCodeCamp</b> where I learned Python, Pandas, Streamlit, Tkinter, and Flask.<br><br>

            I have built a multi-page Sales and Commission Analysis App, an automated report generator, and several business-focused dashboards.
            </div>
        """, unsafe_allow_html=True)

    # --- Social Links ---
    st.markdown("### 🔗 Connect with Me")
    st.markdown("""
        <div class="social-icons">
        <a href="https://facebook.com/mujakkirdv" target="_blank">🌐 Facebook</a>
        <a href="mailto:mujakkirar4@gmail.com">✉️ Email</a>
        <a href="https://github.com/mujakkirdv" target="_blank">💻 GitHub</a>
        <a href="https://linkedin.com/in/mujakkir-dv" target="_blank">🔗 LinkedIn</a>
        <a href="https://instagram.com/mujakkirdv" target="_blank">📸 Instagram</a>
        <a href="https://t.me/mujakkirdv" target="_blank">💬 Telegram</a>
        <a href="#" target="_blank">📱 WeChat: mujakkirdv</a>
        </div>
    """, unsafe_allow_html=True)

    # --- Redesigned Skills Section ---
    st.markdown("### 🧠 My Skill Set (Interactive View)")

    language_skills = ["🐍 Python", "🧮 Pandas", "📦 Numpy"]
    data_skills = ["📊 Data Analysis", "📈 Data Visualization", "📤 Automation"]
    web_skills = ["🌐 Streamlit", "🧪 Flask", "🖼️ Tkinter", "📄 HTML"]
    tools_skills = ["📋 Google Sheets", "📊 Excel Dashboard", "🧰 GitHub"]

    st.markdown("#### 🐍 Programming Languages & Libraries")
    c1, c2, c3 = st.columns(3)
    for i, skill in enumerate(language_skills):
        [c1, c2, c3][i % 3].markdown(f"- {skill}")

    st.markdown("#### 📊 Data Analytics & Automation")
    c4, c5, c6 = st.columns(3)
    for i, skill in enumerate(data_skills):
        [c4, c5, c6][i % 3].markdown(f"- {skill}")

    st.markdown("#### 🖥️ Web & App Development")
    c7, c8, c9 = st.columns(3)
    for i, skill in enumerate(web_skills):
        [c7, c8, c9][i % 3].markdown(f"- {skill}")

    st.markdown("#### ⚙️ Tools & Platforms")
    c10, c11, c12 = st.columns(3)
    for i, skill in enumerate(tools_skills):
        [c10, c11, c12][i % 3].markdown(f"- {skill}")

    # --- Projects ---
    st.markdown("### 🚀 Projects")
    st.markdown("""
    - ✅ [Portfolio Website](https://webmujakkir.streamlit.app/) – Showcasing profile, projects, and design  
    - ✅ [Sales & Commission App](https://welburgmetalpvtltd.streamlit.app/) – Multi-page app for data analytics  
    - ✅ Offline Python scripts for business automation and reporting
    """)

    # --- Mini Charts / Metrics ---
    st.markdown("### 📊 Metrics & Performance")
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("#### Monthly Sales Growth")
        st.line_chart({
            "Sales": [120, 180, 240, 300]
        }, use_container_width=True)

    with m2:
        st.markdown("#### Projects Completed")
        st.bar_chart({
            "Projects": [1, 2, 2, 3]
        }, use_container_width=True)

    # --- Screenshot Gallery ---
    st.markdown("### 🖼️ Project Screenshot Gallery")
    g1, g2 = st.columns(2)
    with g1:
        st.image("screenshot1.png", caption="Portfolio Website", use_container_width=True)
        st.image("screenshot2.png", caption="Sales Dashboard", use_container_width=True)
    with g2:
        st.image("screenshot3.png", caption="Commission Report App", use_container_width=True)
        st.image("screenshot4.png", caption="Data Automation Script", use_container_width=True)
