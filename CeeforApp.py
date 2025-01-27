import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ceefor Research app",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"About": "With over six years as a clinical research analyst and clinical methodologist, we specialize in study design, data interpretation, and statistical modeling, driving evidence-based solutions that improve healthcare outcomes and research quality."
    }

)

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='color: blue;'>Welcome to Ceefor Analytics Hub</h1>
    """,
    unsafe_allow_html=True
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

sidepage=st.sidebar.radio("Go To", ["Home", "Services", "Contact Us"])

st.session_state.current_page = sidepage


if st.session_state.current_page == "Home":
    st.markdown("*Democratizing AI in health research*")
    st.markdown("#### We specialize in supporting researchers, healthcare professionals, and students by providing expert services for every stage of the research process from topic conceptualization to discussion writing.Let us help transform your ideas into impactful outcomes.")
    
    if st.button("Explore Service"):
        st.session_state.current_page = "Services"
    if st.button("Contact Us"):
        st.session_state.current_page = "Contact Us"



if st.session_state.current_page == "Services": 
    st.subheader("We render Clinical research services with professionalism. Contact us for the following services")
    checkbox1 = st.checkbox("## Literature Review Writing")
    if checkbox1:
        st.write("We provide Thoroughly crafted and meticulously researched reviews designed to align seamlessly with your study objectives, providing a solid foundation for impactful and credible research")
    checkbox2 = st.checkbox("## Research Assistant Training & Outsourcing")
    if checkbox2:
        st.write("We empower researchers by providing access to skilled assistants, ensuring seamless collaboration and efficient project execution")
    checkbox3 = st.checkbox("## Methodology Design & Sample Size Calculation")
    if checkbox3:
        st.write("Providing expert support in designing robust methodologies and questionnaires, ensuring statistically reliable sample sizes and addressing ethical concerns with utmost care")
    checkbox4 = st.checkbox("## Data Analysis & Interpretation")
    if checkbox4:
        st.write("We leveraging advanced analytics, including univariate, bivariate, and multivariate techniques, to uncover patterns, relationships, and trends in your data. Delivering clear, actionable insights that enhance the impact, relevance, and decision-making power of your research findings. We Have proficiency in using SPSS, EPI-INFO, STATA, Python and R for data analysis")
    checkbox5 = st.checkbox("## Discussion Writing")
    if checkbox5:
        st.write("Crafting meaningful discussions that connect results to existing literature and research questions")
        
    if st.button("Back to Home"):
        st.session_state.current_page = "Home"
    
    


if st.session_state.current_page == "Contact Us":
    st.subheader("You can reach us using the following channels")
    st.write ("Email: ceeforanalyticshub@gmail.com")
    st.write ("Mobile no: +234817 014 2910, +234706 110 0248, +234916 038 8907")
    st.write ("WhatApp:+23481 7014 2910")
    
    