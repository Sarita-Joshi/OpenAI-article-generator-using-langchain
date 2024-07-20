import streamlit as st
from generate import generate_article

st.title('AI Article Generator')

topic = st.text_input('Topic', placeholder='The future of AI..')
keywords = keywords = st.text_input('Keywords')
    

length = st.number_input("Length (words)", min_value=100, max_value=5000, value=1500)

tone = st.selectbox("Tone", ["informative", "formal", "casual", "persuasive", "humorous"])



audience = st.selectbox("Audience", ["general public", "professionals", "students"])

purpose = st.selectbox("Purpose", ["LinkedIn Post", "Twitter Post", "Graduate Essay", "Homework Assignment", "Blog Post", "Research Paper", "Newsletter"])

outline = st.text_area('Outline (Comma seperated)', "Introduction, Current State, Emerging Trends, Potential Impact, Conclusion")
generate_button = st.button('Generate Article')

if generate_button:
    article_params = {
        "title": topic,
        "keywords": keywords,
        "length": length,
        "tone": tone,
        "audience": audience,
        "outline": [section.strip() for section in outline.split(",")],
        "purpose": purpose,
        "language": "en"
    }
    article = generate_article(article_params)
    st.session_state.article
