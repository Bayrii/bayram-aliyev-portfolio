import streamlit as st
from send_email import send_email

st.header("📧 Contact Me")
st.write(
    "Have a question, opportunity, or just want to connect? Fill out the form below and I’ll get back to you as soon as possible.")


with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input("Your Email Address", placeholder="you@example.com")
    raw_message = st.text_area("Your Message", placeholder="Write your message here...")

    submit_button = st.form_submit_button("Send Message")

    if submit_button:
        message = f"""\
Subject: Portfolio Contact Me - {user_email}

From: {user_email}
To: Portfolio Inbox

{raw_message}
    """
        send_email(message)
        st.session_state["email_sent"] = True
        st.success("✅ Your message has been sent successfully!")