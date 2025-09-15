import streamlit as st

# Page configuration
st.set_page_config(page_title="AI Non-Profit Platform", layout="wide", page_icon="🌍")

# Custom CSS
st.markdown(
    """
    <style>
      .title {font-size:32px; font-weight:700; color:#1A5276; margin-bottom:5px;}
      .subtitle{color:#5D6D7E; font-size:18px; margin-bottom:25px;}
      .card {
        background:#fff;
        border:1px solid #E6EDF2;
        padding:20px;
        border-radius:12px;
        box-shadow:0 4px 15px rgba(13,40,57,0.05);
        margin-bottom:15px;
      }
      h3 {margin-top:0;}
      ul {margin:5px 0 5px 20px;}
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3,1])
with col1:
    st.markdown('<div class="title">🌍 AI-Powered Non-Profit Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Connecting Donors, Volunteers, and NPOs through AI-driven insights</div>', unsafe_allow_html=True)

st.write("---")

# Cards with more matter
st.markdown(
    '<div class="card"><h3>What We Do</h3>'
    '<p>We bridge the gap between donors, volunteers, and non-profit organizations (NPOs) by leveraging advanced AI technologies. '
    'Our platform identifies the most relevant NPOs for donors, matches volunteers based on their skills and location, and '
    'analyzes feedback from beneficiaries to help NPOs improve their services and measure social impact.</p></div>', 
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card"><h3>Why This Matters</h3>'
    '<ul>'
    '<li><b>Personalized Donor Engagement:</b> Donors receive recommendations aligned with their interests and philanthropic goals.</li>'
    '<li><b>Efficient Volunteer Matching:</b> Volunteers find opportunities that match their skills, availability, and location.</li>'
    '<li><b>Impact Measurement:</b> NPOs gain actionable insights through sentiment analysis of feedback and activity tracking.</li>'
    '<li><b>Privacy & Fairness:</b> All operations are designed to ensure data privacy, transparency, and fair allocation of opportunities.</li>'
    '</ul></div>', 
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card"><h3>How It Works</h3>'
    '<ul>'
    '<li><b>Recommendation Engine:</b> Uses machine learning to suggest the most suitable NPOs for each donor.</li>'
    '<li><b>Volunteer Matching:</b> Combines geolocation and skill-based filtering to find optimal volunteer opportunities.</li>'
    '<li><b>Sentiment Analysis:</b> NLP algorithms analyze feedback from beneficiaries to identify trends and areas for improvement.</li>'
    '<li><b>Interactive Dashboards:</b> Visualize donor activity, volunteer engagement, and NPO performance with easy-to-read dashboards.</li>'
    '</ul></div>', 
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card"><h3>Expected Outcomes</h3>'
    '<ul>'
    '<li>Higher donor retention and engagement due to personalized suggestions.</li>'
    '<li>Reduced time and effort in volunteer placement by leveraging AI-driven matching.</li>'
    '<li>Improved decision-making for NPOs through data-backed insights.</li>'
    '<li>Enhanced transparency and accountability across donation and volunteering processes.</li>'
    '</ul></div>', 
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card"><h3>Contact</h3>'
    '<p>For inquiries, collaborations, or feedback, reach out to us:</p>'
    '<ul>'
    '<li>Email: <a href="mailto:non_profit_platform@gmail.com">non_profit_platform@gmail.com</a></li>'
    '<li>Website: <a href="#">www.ai-npo-platform.org</a></li>'
    '</ul></div>', 
    unsafe_allow_html=True
)
