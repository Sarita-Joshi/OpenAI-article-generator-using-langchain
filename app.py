import streamlit as st
from streamlit_tags import st_tags
from generate import generate_article

st.set_page_config(layout ='wide')

st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

# st.title('AI Article Generator')
st.markdown("<h1 style='text-align: center;'>AI Article Generator</h1>", unsafe_allow_html=True)

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.session_state.button_clicked:
    col1, col2 = st.columns([1, 1])
else:
    empty_left, col1, empty_right = st.columns([1, 1.5, 1])


with col1:
    topic = st.text_input('Topic', placeholder='The future of AI..')
    keywords = keywords = st_tags(
        label='Keywords',
        text='Press enter to add more',
        value=[],
        suggestions=[],
        maxtags=10,
        key='1'
    )
    with st.container():
        col_length, col_tone, = st.columns([1, 1])
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

    outline = st.text_area('Outline (Comma seperated)', "Introduction, Current State, Emerging Trends, Potential Impact, Conclusion")
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
            "language": "en"
        }
        article = generate_article(article_params)
        st.session_state.article = article
        st.session_state.topic = topic
        st.experimental_rerun()


if st.session_state.button_clicked:
    with col2:
        st.header(st.session_state.topic or 'Add title of your own')
        # st.write(st.session_state.article)

        st.markdown(f"""
            <div style="text-align: justify;">
                {st.session_state.article}
            </div>
        """, unsafe_allow_html=True)



st.markdown("""
<style>
    .css-1d391kg {  # Adjust width of the columns
        max-width: 600px;
    }
    .css-2trqyj {  # Adjust width of the columns
        max-width: 600px;
    }
    .st-bd {  # Style the generated article column
        background-color: #f0f0f5;
        padding: 15px;
        border-radius: 10px;
    }
</style>
            """, unsafe_allow_html=True)