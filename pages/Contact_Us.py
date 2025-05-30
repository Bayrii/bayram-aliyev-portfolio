import streamlit as st

st.header("📧 Contact Me")

with st.form(key="emai_forms"):
    user_email = st.text_input("Enter your email address")
    message = st.text_area("Enter your message")
    button = st.form_submit_button("Send")
    