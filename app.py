import streamlit as st
from streamlit_tags import st_tags
from v1.generate import generate_article

import os
import torch
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 

st.set_page_config(layout='wide')
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>AI Article Generator</h1>", unsafe_allow_html=True)

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.session_state.button_clicked:
    col1, col2 = st.columns([1, 1])
else:
    empty_left, col1, empty_right = st.columns([1, 1.5, 1])

with col1:
    topic = st.text_input('Topic', placeholder='The future of AI..')
    keywords = st_tags(
        label='Keywords',
        text='Press enter to add more',
        value=[],
        suggestions=[],
        maxtags=10,
        key='1'
    )

    with st.container():
        col_length, col_tone = st.columns([1, 1])
        with col_length:
            length = st.number_input("Length (words)", min_value=100, max_value=5000, value=1500)
        with col_tone:
            tone = st.selectbox("Tone", ["informative", "formal", "casual", "persuasive", "humorous"])

    with st.container():
        col_audience, col_purpose = st.columns([1, 1])
        with col_audience:
            audience = st.selectbox("Audience", ["general public", "professionals", "students"])
        with col_purpose:
            purpose = st.selectbox("Purpose", ["LinkedIn Post", "Twitter Post", "Graduate Essay", "Homework Assignment", "Blog Post", "Research Paper", "Newsletter"])

    with st.container():
        col_llm, col_temp, col_top_p = st.columns([1, 1, 1])
        with col_llm:
            llm_choice = st.selectbox("Choose LLM", ["openai", "gemini", "groq"], help="Select the LLM provider for generating your article.")
        with col_temp:
            temperature = st.slider("Temperature", 0.0, 1.0, 0.5, help="Controls creativity/randomness. 0 = more factual, 1 = more creative.")
        with col_top_p:
            top_p = st.slider("Top-p", 0.1, 1.0, 1.0, help="Controls nucleus sampling. Lower values = more focused responses.")

    auto_research = st.checkbox("Auto Research", value=True, help="Automatically research the topic using Wikipedia, Web Search, and News tools.")
    auto_outline = st.checkbox("Auto Generate Outline", value=True, help="Generate a structured outline automatically based on your topic.")
    include_summary = st.checkbox("Include Summary", value=True, help="Add a 3-5 bullet point summary at the end of the article.")

    outline = st.text_area('Outline (Comma separated)', "Introduction, Current State, Emerging Trends, Potential Impact, Conclusion")

    generate_button = st.button('Generate Article')

    if generate_button:
        st.session_state.button_clicked = True
        article_params = {
            "title": topic,
            "keywords": keywords,
            "length": length,
            "tone": tone,
            "audience": audience,
            "outline": [section.strip() for section in outline.split(",")],
            "purpose": purpose,
            "language": "en",
            "llm_choice": llm_choice,
            "auto_research": auto_research,
            "auto_outline": auto_outline,
            "include_summary": include_summary,
            "temperature": temperature,
            "top_p": top_p
        }
        article = generate_article(article_params)
        st.session_state.article = article
        st.session_state.topic = topic
        st.rerun()

if st.session_state.button_clicked:
    with col2:
        st.header(st.session_state.get('topic') or 'Add title of your own')
        st.markdown(f"""
            <div style="text-align: justify;">
                {st.session_state.get('article')}
            </div>
        """, unsafe_allow_html=True)

st.markdown("""
<style>
    .css-1d391kg { max-width: 600px; }
    .css-2trqyj { max-width: 600px; }
    .st-bd { background-color: #f0f0f5; padding: 15px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)
