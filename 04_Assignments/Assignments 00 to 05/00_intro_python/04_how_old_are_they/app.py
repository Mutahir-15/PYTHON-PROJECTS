# How old are You? Web-Application
import streamlit as st
from datetime import datetime  # Corrected import

# Page Layout
st.set_page_config(page_title="How old are You?", page_icon="🎂", layout="centered", initial_sidebar_state="expanded")
st.title("🎂 How old are You?")
st.sidebar.header("Instructions")
st.sidebar.info("Enter your year of birth and click on the button to calculate your age.")

# Input Section
year_of_birth = st.number_input("Enter your year of birth:", min_value=1900, max_value=datetime.now().year, step=1)

# Age Calculation
if st.button("Calculate Age"):
    current_year = datetime.now().year
    age = current_year - year_of_birth
    st.write(f"You are {age} years old")