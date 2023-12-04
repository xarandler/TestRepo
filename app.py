import streamlit as st
from homepage import show_homepage
from integral_calculator import show_integral_calculator
from history_of_integral import show_history_of_integral

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Homepage", "Integral Calculator", "History of Integral"], index=0)

if page == "Homepage":
    show_homepage()
elif page == "Integral Calculator":
    show_integral_calculator()
elif page == "History of Integral":
    show_history_of_integral()
