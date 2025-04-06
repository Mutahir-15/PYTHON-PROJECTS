# Liftoff (Countdown)
import streamlit as st
import time

# Page layout
st.set_page_config(page_title="Spaceship Liftoff Countdown")
st.title("Spaceship Liftoff Countdown")

# Initialize session state for the countdown
if "countdown_numbers" not in st.session_state:
    st.session_state.countdown_numbers = []
if "countdown_complete" not in st.session_state:
    st.session_state.countdown_complete = False

# Explanation of the program (in the main area)
st.write("""
### What This Program Does
This program simulates a spaceship launch countdown.
- Click 'Start Countdown' in the sidebar to begin.
- Watch the countdown from 10 to 1, followed by "Liftoff!".
- Click 'Clear Countdown' to start over.
""")

# Add the buttons to the sidebar
with st.sidebar:
    st.header("Countdown Controls")
    start_button = st.button("Start Countdown")
    clear_button = st.button("Clear Countdown")

# Function to generate the countdown numbers
def generate_countdown():
    return [10 - i for i in range(10)]

# Handle the start button
if start_button and not st.session_state.countdown_complete:
    st.session_state.countdown_numbers = generate_countdown()
    st.session_state.countdown_complete = True
    
    # Create a placeholder for the countdown display
    countdown_display = st.empty()
    
    # Display the countdown with a delay
    for num in st.session_state.countdown_numbers:
        countdown_display.info(f"{num}")
        time.sleep(1)
    
    # Display liftoff after the countdown
    countdown_display.success("Liftoff!")

# Handle the clear button
if clear_button:
    st.session_state.countdown_numbers = []
    st.session_state.countdown_complete = False
    st.rerun()

# Display the countdown
if st.session_state.countdown_numbers and not start_button:
    st.write("### Countdown Sequence")
    for num in st.session_state.countdown_numbers:
        st.info(f"{num}")
    st.success("Liftoff!")