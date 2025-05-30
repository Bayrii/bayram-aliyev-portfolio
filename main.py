import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",)
with col2:
    st.title("💡 Bayram Aliyev")

    about_me = """
    I'm a highly motivated second-year Computer Science student with a deep interest in **mathematics**, **programming**, and **data-driven problem solving**.  
    Always curious and eager to grow, I continuously pursue opportunities to learn, experiment, and build real-world skills.

    I’m currently seeking a **data analytics internship** where I can apply my analytical mindset and technical background to contribute meaningfully — while learning from professionals in the field.

    Whether it’s debugging code, analyzing patterns, or diving into new frameworks, I thrive on challenges that push me to improve.
    """

    st.info(about_me)

    st.header("📚 Education")
    st.info("""
    - **BSc in Computer Science**, French-Azerbaijan University  
      _2023 - ongoing_
    - **GPA:**  3.7
    """)

st.markdown("""
<div style="text-align: center; padding: 10px 0;">
    <h2 style="margin-bottom: 0;">💼 Projects</h2>
    <p style="font-size: 18px; margin-top: 5px;">
        Take a look at some of the projects I’ve built.
    </p>
    <p style="font-size: 16px; color: gray;">
        📫 Feel free to reach out if you'd like to connect or collaborate!
    </p>
</div>
""", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pd.read_csv("data.csv", sep = ";")
with col3:
    for index, row in data[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")


with col4:
    for index, row in data[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")


