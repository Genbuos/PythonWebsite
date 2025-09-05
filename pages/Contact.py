import streamlit as st
from functions.send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter an email address")
    row_message = st.text_area("Your message")
    message = f"""\
Subject: New Email from {user_email}\
From: {user_email}
{row_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Submission sent successfully!")