import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI-Powered Non-Profit Platform",
    layout="wide",
    page_icon="🌍"
)

# ----------------------------
# Custom CSS for Styling
# ----------------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 800;
            text-align: center;
            color: #2C3E50;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #7F8C8D;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 28px;
            font-weight: 700;
            margin-top: 30px;
            margin-bottom: 10px;
            color: #2C3E50;
        }
        .info-card {
            background-color: #F8F9F9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Title & Subtitle
# ----------------------------
st.markdown('<div class="main-title">🌟 AI-Powered Non-Profit Recommendation & Sentiment Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Empowering Social Good with Artificial Intelligence</div>', unsafe_allow_html=True)

st.write("---")

# ----------------------------
# What We Do Section
# ----------------------------
st.markdown('<div class="section-header">💡 What We Do</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div class="info-card">
        We connect **donors** and **volunteers** with relevant NPOs, highlight opportunities,  
        and analyze **beneficiary feedback** for greater impact.  
        
        👉 Powered by **AI, analytics, and interactivity**.
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=250)

# ----------------------------
# Why This Matters
# ----------------------------
st.markdown('<div class="section-header">🚨 Why This Matters</div>', unsafe_allow_html=True)

cols = st.columns(4)
reasons = [
    ("🎯", "Personalized donor recommendations"),
    ("🤝", "Skill-based volunteering matches"),
    ("💬", "Impact measurement via feedback"),
    ("🖥️", "Interactive platform for all")
]
for col, (icon, text) in zip(cols, reasons):
    with col:
        st.markdown(f"""
        <div class="info-card" style="text-align:center;">
            <h2>{icon}</h2>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# How It Works
# ----------------------------
st.markdown('<div class="section-header">⚙️ How It Works</div>', unsafe_allow_html=True)

with st.container():
    step1, step2, step3 = st.columns(3)
    step1.markdown("✅ **Recommendation Engine** <br> ML to match donors & NPOs", unsafe_allow_html=True)
    step2.markdown("✅ **Volunteer Matching** <br> Geolocation + skills", unsafe_allow_html=True)
    step3.markdown("✅ **Sentiment Analysis** <br> NLP on feedback", unsafe_allow_html=True)

    step4, step5 = st.columns(2)
    step4.markdown("✅ **Interactive Dashboards** <br> Data visualizations via Streamlit", unsafe_allow_html=True)
    step5.markdown("✅ **Backend Tech** <br> Python, Scikit-learn, TensorFlow, spaCy", unsafe_allow_html=True)

# ----------------------------
# Expected Outcomes
# ----------------------------
st.markdown('<div class="section-header">📌 Expected Outcomes</div>', unsafe_allow_html=True)

outcomes = [
    ("🌱", "Improved donor engagement"),
    ("🤲", "Efficient volunteer matching"),
    ("📊", "Actionable insights for NPOs"),
    ("🔒", "Ethical AI practices")
]

cols = st.columns(4)
for col, (icon, text) in zip(cols, outcomes):
    with col:
        st.markdown(f"""
        <div class="info-card" style="text-align:center;">
            <h2>{icon}</h2>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# Ethical Commitment
# ----------------------------
st.markdown('<div class="section-header">🤝 Ethical Commitment</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="info-card">
    We are committed to **responsible AI practices**, ensuring:  
    - 🔐 **Data privacy**  
    - ⚖️ **Fairness & inclusivity**  
    - 🔍 **Transparency in decision-making**  

    ✨ <b>Join us in making a difference!</b>
    </div>
    """, unsafe_allow_html=True
)
