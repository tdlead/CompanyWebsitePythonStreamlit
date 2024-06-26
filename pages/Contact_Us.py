import pandas as pd
import streamlit as st

import functions
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    list = pd.read_csv("topics.csv")

    option = st.selectbox(
        "What Topic do you want to discuss",
        list,
        index=None,
        placeholder="Select topic...",
    )

    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    message_txt= f"""
    Subject: {option} From {user_email} \n
    From: {user_email}
    {message}
    """
    if button:
        send_email(message_txt)
        st.info("Email was send successufully")
