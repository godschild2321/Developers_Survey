import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

st.write("""#### This web app uses the stack overflow annual developer salary dataset and allows users to view the salary ranges and statistics of developers from different countries, educational qualifications and years of experience. It also enables us to predict the salary of any software engineer using regression models if the user provides certain required information""")
