import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Settings ---
st.set_page_config(page_title="Mujakkir Ahmad | Portfolio", layout="wide")

# --- Sidebar ---
st.sidebar.image("profile.jpg", width=150)
st.sidebar.title("👨‍💻 Mujakkir Ahmad")
st.sidebar.markdown("📊 Data Analyst | Accountant")
st.sidebar.markdown("📍 Dhaka, Bangladesh")
st.sidebar.markdown("[📧 Email](mailto:mujakkirar@gmail.com)")
st.sidebar.markdown("[🔗 LinkedIn](https://linkedin.com/in/mujakkir-dv)")
st.sidebar.markdown("[💻 GitHub](https://github.com/mujakkirdv)")

page = st.sidebar.radio("📂 Navigate", ["Home", "Data Projects", "Resume", "Contact", "About Me"])

# --- HOME ---
if page == "Home":
    st.title("👋 Welcome to Mujakkir Web Portfolio")
    st.image("assets/profile.jpg", width=300)
    st.markdown("""
I’m **Mujakkir Ahmad**, a passionate Data Analyst and Accounts Executive with experience in 
Python, Streamlit, Pandas, and sales dashboards. I love turning raw data into meaningful insights 
and building automation tools for everyday business needs.
    """)
    st.subheader("🎯 Career Objective")
    st.write("""
To obtain a position as a **Data Analyst** or **Senior Executive – Accounts & Finance**, where I can apply my skills in Python, Excel, and data visualization tools to support business decisions through automation, insights, and process optimization.
    """)

# --- DATA PROJECTS ---
elif page == "Data Projects":
    st.title("📊 Data Projects")
    
    try:
        df = pd.read_excel("sales.xlsx")
        st.subheader("📁 Sample Sales Data")
        st.dataframe(df.head())

        st.markdown("### 📈 Sales Amount by Sales Executive")
        sales_exec = df.groupby("sales_executive")["sales_amount"].sum().reset_index()
        fig1 = px.bar(sales_exec, x="sales_executive", y="sales_amount", color="sales_executive",
                      title="Total Sales by Sales Executive")
        st.plotly_chart(fig1)

        st.markdown("### 🧾 Sales by Customer")
        cust_sales = df.groupby("customer_name")["sales_amount"].sum().reset_index()
        fig2 = px.pie(cust_sales, names="customer_name", values="sales_amount",
                      title="Sales Distribution by Customer")
        st.plotly_chart(fig2)

        st.markdown("### 💹 Company Profit Breakdown")
        profit_df = df[["executive_commission", "teamleader_commission", "gm_commission", "company_profit"]].sum().reset_index()
        profit_df.columns = ["Category", "Amount"]
        fig3 = px.bar(profit_df, x="Category", y="Amount", color="Category", title="Profit & Commission Summary")
        st.plotly_chart(fig3)
    
    except Exception as e:
        st.warning("⚠️ Please make sure 'sales.xlsx' file is available in the 'data/' folder.")
        st.error(e)

# --- RESUME ---
elif page == "Resume":
    st.title("📄 Mujakkir Ahmad – Resume")

    with open("Mujakkir_Ahmad_CV_2025.pdf", "rb") as f:
        st.download_button("📥 Download My CV", f, file_name="Mujakkir_Ahmad_CV_2025.pdf")


    st.header("🧠 Professional Summary")
    st.write("""
Self-motivated and detail-oriented professional with diverse experience across sales, pharmaceutical operations, 
software systems, and data analysis. Currently working as an Accountant (Data Analyst) with strong expertise in Python (Pandas, Streamlit, Plotly), Excel, and sales dashboards.
    """)

    st.header("🧾 Work Experience")
    st.markdown("""
- **Welburg Metal Pvt Ltd** – *Account Automation Executive*  
- **CT Health Limited** – *Product Data Executive*  
- **Popular Diagnostic Center** – *Sales Executive*  
- **Libra Pharmaceuticals Ltd** – *Operator / Section In-Charge*    
- **Gel Well Ltd** – *Blister Assistant Operator *  
    """)

    st.header("🎓 Education")
    st.markdown("""
- **B.A.**, Brindaban Govt. College, Habigonj  
- **HSC (Science)**, Shaistaganj Degree College  
- **SSC (Science)**, Masud Chaudhary School  
    """)

    st.header("🛠️ Technical Skills")
    st.markdown("""
- **Python** – Pandas, NumPy, Streamlit, Plotly, Matplotlib, Tkinter  
- **Visualization** – Google Sheets Dashboards, Excel Charts  
- **Tools** – MS Excel, Power BI, Google Sheets, MySQL  
- **Reports** – Sales, Commission, Dues, Deposits  
- **Web** – HTML, Django (Basic), Facebook Shop  
- **Version Control** – GitHub  
    """)

    st.header("📘 Certifications & Learning")
    st.markdown("""
- FreeCodeCamp – Data Analytics  
- PGD in Data Analytics (2025 Applied)  
- GitHub Projects: [mujakkirdv](https://github.com/mujakkirdv)  
    """)

    st.header("🌐 Languages")
    st.markdown("- Bangla – Native\n- English – Basic")

    st.header("👤 Personal Details")
    st.markdown("""
- Father: Abdul Zahir  
- Mother: Mst. Monuara Khatun  
- Date of Birth: 21 June 1999  
- Address: Chunarughat, Habigonj  
- NID: 9577341333  
- Marital Status: Single
    """)

    st.header("✅ Declaration")
    st.write("I hereby declare that the above information is true and accurate to the best of my knowledge and belief.")

# --- CONTACT ---
elif page == "Contact":
    st.title("📞 Contact Me")
    st.markdown("📧 Email: mujakkirar@gmail.com")
    st.markdown("💻 LinkedIn: [📎 LinkedIn](https://linkedin.com/in/mujakkir-dv)")
    st.markdown("💻 GitHub: [💻 GitHub](https://github.com/mujakkirdv)")
    st.markdown("📱 Facebook: [📱 Facebook](https://facebook.com/mujakkirdv)")
    st.markdown("📱 Phone No: +8801787933422 | +8801601933422")

# --- ABOUT ME ---
elif page == "About Me":
    st.title("🧑‍💼 About Me")
    st.markdown("""
Hi, I'm **Mujakkir Ahmad**, a detail-driven professional who started in pharma and retail, and evolved into a **Data Analyst**.

I bring:
- 5+ years of experience in pharma, diagnostics, and accounts
- Strong expertise in **Python**, **Pandas**, **Streamlit**, and **Excel**
- Real-world dashboards and reports used by management

I focus on:
- **Automation** of reports and workflows
- **Dashboards** for decision-making
- Building apps in **Streamlit**

In my free time, I explore new tech tools, contribute to GitHub, and create AI and data-related content for social media.
    """)
