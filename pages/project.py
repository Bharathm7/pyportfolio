import streamlit as st
import pandas as pd
if st.button('click to go back home'):
    st.switch_page('pages/HOME.py')
st.subheader('_THESE ARE MY_  :blue[ PROJECTS]', divider='rainbow')
df = pd.read_csv('data.csv', sep=";")

col1, col2 = st.columns(2)

with col1:
    for index, row in df[:4].iterrows():
        st.image("images/" + row["image"])
        st.header(row["title"])
        st.info(row["description"])
        st.write(f"[source-code]({row['url']})")

with col2:
    for index, row in df[4:].iterrows():
        st.image("images/" + row["image"])
        st.header(row["title"])
        st.info(row["description"])
        st.write(f"[source-code]({row['url']})")



