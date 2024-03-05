import streamlit as st
from sendmail import send_mail
import pandas as pd;

if st.button('click to go back home'):
    st.switch_page('pages/HOME.py')
df = pd.read_csv('topics.csv')

st.header("Contact-ME")

with st.form(key="contact-form"):
    email = st.text_input("enter your email address", placeholder="enter email")
    option = st.selectbox("select your topic", df["topic"])
    content = st.text_area("enter your message",placeholder="enter your message")
    message = f"""\
Subject: contacted from portfolio by {email}
  d 
from: {email}
topic: {option}
{content}     
"""
    button = st.form_submit_button("Submit");
    if button:
        send_mail(message)
        st.info("Thank you for contacting...YOUR MESSAGE WAS SENT SUCCESSFULLY!!!!")
