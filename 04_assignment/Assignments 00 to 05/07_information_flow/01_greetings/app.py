#Greetings Generator
import streamlit as st

# Page layout
st.set_page_config(page_title="Greeting Generator", page_icon="👋")
st.title("Greeting Generator")

# Initialize session state
if "greeting" not in st.session_state:
    st.session_state.greeting = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Greeting function
def greet(name):
    return f"🙋‍♂️ Hello, {name}! Hope you're having a great day!"

# Description
st.write("""
### What This App Does
Generates a cheerful greeting with your name!
- Type your name in the sidebar.
- Click **'Show Greeting'** to see it.
- Click **'Clear'** to reset.
""")

# Sidebar for user input
with st.sidebar:
    st.header("Enter Your Name")
    name = st.text_input("What's your name?", value="Sophia")
    greet_button = st.button("Show Greeting")
    clear_button = st.button("Clear")

# Show greeting on button click
if greet_button:
    st.session_state.greeting = greet(name)
    st.session_state.results_shown = True
    st.write("### Result")
    st.success(st.session_state.greeting)

# Clear button
if clear_button:
    st.session_state.greeting = ""
    st.session_state.results_shown = False
    st.rerun()

# Display result if it exists
if st.session_state.results_shown and not greet_button:
    st.write("### Result")
    st.success(st.session_state.greeting)
