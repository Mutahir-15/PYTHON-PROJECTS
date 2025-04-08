import streamlit as st

# Page layout
st.set_page_config(page_title="Ones Digit Finder")
st.title("Ones Digit Finder")

# Initialize session state
if "ones_digit" not in st.session_state:
    st.session_state.ones_digit = None
if "number" not in st.session_state:
    st.session_state.number = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to extract the ones digit
def get_ones_digit(num):
    return num % 10

# Description
st.write("""
### What This App Does
This simple app tells you the **ones digit** of any number you enter.
- Type a number in the sidebar.
- Click **'Find Ones Digit'** to see the result.
- Use **'Clear'** to reset the app.
""")

# Sidebar inputs
with st.sidebar:
    st.header("Input")
    number = st.number_input("Enter a number:", value=10, step=1)
    find_button = st.button("Find Ones Digit")
    clear_button = st.button("Clear")

# Handle find button
if find_button:
    st.session_state.number = number
    st.session_state.ones_digit = get_ones_digit(number)
    st.session_state.results_shown = True
    st.write("### Result")
    st.success(f"The ones digit of {number} is {st.session_state.ones_digit}")

# Handle clear button
if clear_button:
    st.session_state.ones_digit = None
    st.session_state.number = None
    st.session_state.results_shown = False
    st.rerun()

# Show result if already found
if st.session_state.results_shown and not find_button:
    st.write("### Result")
    st.success(f"The ones digit of {st.session_state.number} is {st.session_state.ones_digit}")