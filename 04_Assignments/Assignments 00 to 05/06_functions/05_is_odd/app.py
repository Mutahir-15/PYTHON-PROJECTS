# Is Odd
import streamlit as st

# Page layout
st.set_page_config(page_title="Odd or Even Classifier")
st.title("Odd or Even Classifier")

# Initialize session state to track if the results have been shown
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False
if "classifications" not in st.session_state:
    st.session_state.classifications = []

# Function to check if a number is odd
def is_odd(value):
    remainder = value % 2
    return remainder == 1

# Explanation of the program
st.write("""
### What This Program Does
This program classifies numbers from 10 to 19 as odd or even.
- Click 'Classify Numbers' to see the results.
- Click 'Clear' to start over.
""")

# Sidebar for buttons
with st.sidebar:
    st.header("Classifier Controls")
    classify_button = st.button("Classify Numbers")
    clear_button = st.button("Clear")

# Handle the classify button
if classify_button:
    st.session_state.classifications = []
    for i in range(10, 20):
        if is_odd(i):
            st.session_state.classifications.append(f"{i} odd")
        else:
            st.session_state.classifications.append(f"{i} even")
    st.session_state.results_shown = True
    st.write("### Results")
    for result in st.session_state.classifications:
        st.success(result)

# Handle the clear button
if clear_button:
    st.session_state.results_shown = False
    st.session_state.classifications = []
    st.rerun()

# Display the results if they exist
if st.session_state.results_shown and not classify_button:
    st.write("### Results")
    for result in st.session_state.classifications:
        st.success(result)