# How old are you? Web-App
import streamlit as st
from datetime import datetime

# Page Layout
st.set_page_config(page_title="How old are You?", page_icon="🎂", layout="centered", initial_sidebar_state="expanded")
st.title("🎂 How old are You?")
st.sidebar.header("Instructions")
st.sidebar.info("Enter names and years of birth, then click the button to calculate ages.")

# Age Calculation 
def how_old_are_they():
    num_people = st.number_input("Enter number of people", min_value=1, step=1)
    
    names = []
    birth_years = []
    
# For loop to get names and birth years    
    for i in range(num_people):
        name = st.text_input(f"Enter name of person {i+1}")
        birth_year = st.number_input(f"Enter birth year of {name}", min_value=1900, max_value=datetime.now().year, step=1, key=f"year_{i}")
        
        if name and birth_year:
            names.append(name)
            birth_years.append(birth_year)

# Final Results    
    if st.button("Calculate Ages"):
        current_year = datetime.now().year
        results = "\n".join([f"{names[i]} is {current_year - birth_years[i]} years old" for i in range(len(names))])
        st.write("**Results Section:**")
        st.text_area("Results:", value=results, height=100)
        
if __name__ == "__main__":
    how_old_are_they()