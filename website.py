import streamlit as st

st.set_page_config(page_title="AI-Powered Non-Profit Recommendation and Sentiment Analysis Platform")

# Title and Subtitle
st.title("AI-Powered Non-Profit Recommendation and Sentiment Analysis Platform")
st.markdown("""
### Empowering Social Good with AI

**Non-profit organizations (NPOs)** play a critical role in addressing social, environmental, and humanitarian challenges. However, gaps remain between donors, volunteers, and beneficiaries due to:
- Lack of personalized recommendations
- Limited visibility of organizational needs
- Ineffective feedback mechanisms

This platform leverages AI to bridge those gaps!
""")

# Introduction Section
st.header("What We Do")
st.markdown("""
We help connect donors and volunteers with relevant NPOs, highlight opportunities, and analyze beneficiary feedback for greater impact. Our platform uses intelligent algorithms and interactive dashboards for a seamless experience.
""")

# Problem Statement
st.header("Why This Matters")
st.markdown("""
The main challenge is the mismatch between available resources (donors/volunteers) and the needs of NPOs and affected communities. Our AI-driven solution addresses this by:
- Building a recommendation system for donors to identify NPOs that align with their interests.
- Suggesting volunteering opportunities nearby, based on skills, availability, and organizational requirements.
- Using sentiment analysis on beneficiary feedback to assess the impact of NPO initiatives and highlight areas for improvement.
- Providing an interactive Streamlit-based website for easy access by donors, volunteers, and organizations.
""")

# Methodology and Features
st.header("How It Works")
st.markdown("""
- **Recommendation Engine:** Uses machine learning to match donors to NPOs by interest and cause.
- **Volunteer Matching:** Leverages geolocation and user skills to suggest nearby opportunities.
- **Sentiment Analysis:** Applies NLP to beneficiary feedback for actionable insights.
- **Interactive Dashboards:** Built on Streamlit for visualizing data and engagement metrics.
- **Backend Technology:** Powered by Python libraries (scikit-learn, TensorFlow/PyTorch, spaCy).

Features include:
- Personalized NPO and volunteering recommendations
- Beneficiary feedback analysis and impact scorecards
- Location-based opportunity finder
- Data-driven dashboards for all stakeholders
""")

# Expected Outcomes
st.header("Expected Outcomes")
st.markdown("""
- **Improved Donor Engagement:** Through targeted recommendations.
- **Efficient Volunteer Matching:** Connecting skills and locations with needs.
- **Actionable Insights for NPOs:** Via sentiment analysis of beneficiary feedback.
- **Ethical AI Practices:** Ensuring data privacy, fairness, and transparency.

Our platform strengthens collaboration between donors, volunteers, and non-profits for greater societal impact.
""")

# Ethical Commitment
st.header("Ethical Commitment")
st.markdown("""
We emphasize ethical AI practices to ensure data privacy, fairness, and transparency in all our solutions.

**Join us to make a difference!**
""")