import streamlit as st

st.set_page_config(page_title="AI Non-Profit Platform", layout="wide", page_icon="🌍")

st.markdown(
    """
    <style>
      .title {font-size:28px; font-weight:700; color:#1A5276}
      .subtitle{color:#5D6D7E}
      .card{background:#fff;border:1px solid #E6EDF2;padding:18px;border-radius:10px;box-shadow:0 3px 10px rgba(13,40,57,0.03)}
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown('<div class="title">🌍 AI-Powered Non-Profit Platform</div>', unsafe_allow_html=True)
    st.write('**Recommendation • Volunteer Matching • Sentiment Analysis**')
with col2:
    st.write('')

st.write("---")

st.markdown('<div class="card"><h3>What We Do</h3><p>We connect donors and volunteers with relevant NPOs, highlight opportunities, and analyze beneficiary feedback using NLP.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card" style="margin-top:12px"><h3>Why This Matters</h3><ul><li>Personalized donor recommendations</li><li>Skill & location-based volunteer matches</li><li>Measure impact via feedback</li><li>Privacy & fairness-first design</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="card" style="margin-top:12px"><h3>How It Works</h3><ul><li>Recommendation Engine (ML)</li><li>Volunteer Matching (geolocation + skills)</li><li>Sentiment Analysis (NLP)</li><li>Interactive Dashboards (Streamlit)</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="card" style="margin-top:12px"><h3>Expected Outcomes</h3><ul><li>Improved donor engagement</li><li>Faster volunteer placement</li><li>Actionable insights for NPOs</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="card" style="margin-top:12px"><h3>Contact</h3><p>Email: your-email@example.com</p></div>', unsafe_allow_html=True)
