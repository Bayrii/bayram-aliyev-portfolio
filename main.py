import streamlit as st

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",)

    st.header("📚 Education")
    st.write("""
    - **BSc in Computer Science**, French-Azerbaijan University  
      _2023 - ongoing_
    - **GPA:**  3.7
    """)

with col2:
    st.title("Bayram Aliyev")

    about_me = """
    I'm a highly motivated second-year Computer Science student with a deep interest in **mathematics**, **programming**, and **data-driven problem solving**.  
    Always curious and eager to grow, I continuously pursue opportunities to learn, experiment, and build real-world skills.

    I’m currently seeking a **data analytics internship** where I can apply my analytical mindset and technical background to contribute meaningfully — while learning from professionals in the field.

    Whether it’s debugging code, analyzing patterns, or diving into new frameworks, I thrive on challenges that push me to improve.
    """

    st.info(about_me)

st.markdown("""
**💼 Projects**  
Take a look at some of the projects I’ve built.  
*📫 Feel free to reach out if you'd like to connect or collaborate!*
""")

