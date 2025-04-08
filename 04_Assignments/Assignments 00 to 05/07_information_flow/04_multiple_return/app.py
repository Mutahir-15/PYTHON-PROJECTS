# Multiple Return
import streamlit as st

# Page layout
st.set_page_config(page_title="User Data Collector", page_icon=":bar_chart:")
st.title("User Data Collector")

# Initialize session state to store the user data
if "user_data" not in st.session_state:
    st.session_state.user_data = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to collect user data
def get_user_data(first_name, last_name, email_address):
    """
    Returns the user data as a tuple.
    """
    return first_name, last_name, email_address

# Explanation of the program
st.write("""
### What This Program Does
This program collects your first name, last name, and email address.
- Enter your information in the sidebar.
- Click 'Submit Data' to see the result.
- Click 'Clear' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("User Data Entry")
    first_name = st.text_input("What is your first name?:", value="Jane")
    last_name = st.text_input("What is your last name?:", value="Stanford")
    email_address = st.text_input("What is your email address?:", value="janestanford@stanford.edu")
    submit_button = st.button("Submit Data")
    clear_button = st.button("Clear")

# Handle the submit button
if submit_button:
    st.session_state.user_data = get_user_data(first_name, last_name, email_address)
    st.session_state.results_shown = True
    st.write("### Result")
    st.success(f"Received the following user data: {st.session_state.user_data}")

# Handle the clear button
if clear_button:
    st.session_state.user_data = None
    st.session_state.results_shown = False
    st.rerun()

# Display the result if it exists
if st.session_state.results_shown and not submit_button:
    st.write("### Result")
    st.success(f"Received the following user data: {st.session_state.user_data}")