# Get name
import streamlit as st

# Page layout
st.set_page_config(page_title="Greeting Generator", page_icon="🙋‍♂️")
st.title("Greeting Generator")

# Initialize session state
if "greeting_shown" not in st.session_state:
    st.session_state.greeting_shown = False
if "user_name" not in st.session_state:
    st.session_state.user_name = "Sophia"

# Function to return the name
def get_name():
    return st.session_state.user_name

# Explanation of the program
st.write("""
### What This Program Does
This program displays a greeting with a name.
- Enter your name in the sidebar (default is Sophia).
- Click 'Show Greeting' to see the greeting.
- Click 'Clear' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Greeting Controls")
    name_input = st.text_input("Enter your name:", value="Sophia")
    show_button = st.button("Show Greeting")
    clear_button = st.button("Clear")

# Update the name in session state
if name_input:
    st.session_state.user_name = name_input

# Handle the show button
if show_button:
    st.session_state.greeting_shown = True
    name = get_name()
    st.write("### Greeting")
    st.success(f"Howdy {name} ! 🙋‍♂️")

# Handle the clear button
if clear_button:
    st.session_state.greeting_shown = False
    st.session_state.user_name = "Sophia"
    st.rerun()

# Display the greeting if it exists
if st.session_state.greeting_shown and not show_button:
    st.write("### Greeting")
    name = get_name()
    st.success(f"Howdy {name} ! 🙋‍♂️")