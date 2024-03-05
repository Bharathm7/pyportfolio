import pandas as pd;
import streamlit as st;



st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)
col1, col2= st.columns([1,1])
with col1:
    if st.button('Projects'):
        st.switch_page('pages/project.py')
with col2:
    if st.button('contact'):
        st.switch_page('pages/contact.py')


    st.image("me.png",width=400);
st.subheader('_THIS IS_  :blue[BHARATH MAHESH] :sunglasses:', divider='rainbow')
st.info("As an aspiring M.Tech candidate in Computer Science and Engineering at VIT Vellore, I am dedicated to "
        "harnessing technology for innovative solutions. Proficient in MERN stack, Java, and Python, "
        "with a comprehensive understanding of Full Stack development, my expertise spans both front-end and back-end "
        "technologies. My strong command of SQL and basic skills in C contribute to my versatile tech background. "
        "Eager to contribute to progressive projects, I blend technical acumen with a creative mindset to deliver "
        "impactful solutions, pushing the boundaries of what's possible in the tech realm.")
