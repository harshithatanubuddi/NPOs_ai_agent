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
            font-size: 36px;
            font-weight: 800;
            text-align: center;
            color: #1A5276;
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #5D6D7E;
            margin-bottom: 25px;
        }
        .section-header {
            font-size: 24px;
            font-weight: 700;
            margin-top: 25px;
            margin-bottom: 10px;
            color: #1A5276;
        }
        .info-card {
            background-color: #FDFEFE;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #E5E7E9;
            box-shadow: 1px 1px 6px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Title & Subtitle
# ----------------------------
st.markdown('<div class="main-title">🌍 AI-Powered Non-Profit Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Connecting donors, volunteers, and communities with AI-driven solutions</div>', unsafe_allow_html=True)

st.write("---")

# ----------------------------
# What We Do Section
# ----------------------------
st.markdown('<div class="section-header">💡 What We Do</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-card">
    We connect <b>donors</b> and <b>volunteers</b> with relevant NPOs, highlight opportunities,  
    and analyze <b>beneficiary feedback</b> for greater impact.  

    👉 Our platform ensures <b>seamless engagement</b> through AI-powered recommendations and dashboards.
    </div>
    """, unsafe_allow_html=True
)

# ----------------------------
# Why This Matters
# ----------------------------
st.markdown('<div class="section-header">🚨 Why This Matters</div>', unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown(
        """
        <div class="info-card">
        The main challenge is the gap between resources and community needs.  
        Our platform addresses this by:  
        - 🎯 Personalized donor recommendations  
        - 🤝 Volunteer matching (skills + location)  
        - 💬 Feedback analysis for impact  
        - 🖥️ Easy web access for all stakeholders
        </div>
        """, unsafe_allow_html=True
    )
with cols[1]:
    st.image("https://cdn-icons-png.flaticon.com/512/1077/1077012.png", width=220)

# ----------------------------
# How It Works
# ----------------------------
st.markdown('<div class="section-header">⚙️ How It Works</div>', unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown(
        """
        <div class="info-card">
        - 🤖 <b>Recommendation Engine:</b> Matches donors & NPOs  
        - 📍 <b>Volunteer Matching:</b> Location & skills-based suggestions  
        - 💬 <b>Sentiment Analysis:</b> NLP on beneficiary feedback  
        - 📈 <b>Interactive Dashboards:</b> Streamlit visualizations  
        - 🛠️ <b>Tech Stack:</b> Python, scikit-learn, TensorFlow, spaCy  
        </div>
        """, unsafe_allow_html=True
    )
with cols[1]:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)

# ----------------------------
# Expected Outcomes
# ----------------------------
st.markdown('<div class="section-header">📌 Expected Outcomes</div>', unsafe_allow_html=True)

outcomes = [
    ("🌱", "Improved donor engagement"),
    ("🤲", "Better volunteer matching"),
    ("📊", "Insights for NPOs"),
    ("🔒", "Ethical AI practices")
]

cols = st.columns(4)
for col, (icon, text) in zip(cols, outcomes):
    with col:
        st.markdown(f"""
        <div class="info-card" style="text-align:center;">
            <h3>{icon}</h3>
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
    We commit to <b>responsible AI</b>, ensuring:  
    - 🔐 Data privacy  
    - ⚖️ Fairness & inclusivity  
    - 🔍 Transparency in decisions  

    <b>Join us to make a difference!</b>
    </div>
    """, unsafe_allow_html=True
)
