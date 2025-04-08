# Countdown Timer
import streamlit as st
import time

# Page layout
st.set_page_config(page_title="Countdown Timer", page_icon="🕐")
st.title("Countdown Timer")

# Initialize session state
if "countdown_started" not in st.session_state:
    st.session_state.countdown_started = False
if "countdown_result" not in st.session_state:
    st.session_state.countdown_result = []

# Explanation
st.write("""
### What This Program Does
This is a simple countdown timer:
- Enter the number of seconds in the sidebar.
- Click 'Start Countdown' to begin.
- The timer will count down from your number to zero, updating each second.
- A message will appear when the timer reaches zero.
- Click 'Reset' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Timer Settings")
    seconds = st.number_input("Enter the number of seconds to count down:", min_value=1, value=5, step=1)
    start_button = st.button("Start Countdown")
    reset_button = st.button("Reset Timer")

# Start button
if start_button:
    if seconds <= 0:
        st.error("Please enter a positive number of seconds.")
    else:
        st.session_state.countdown_started = True
        st.session_state.countdown_result = []
        
        # Perform the countdown
        st.write("### Countdown")
        for i in range(seconds, 0, -1):
            st.session_state.countdown_result.append(i)
            st.write(i)
            time.sleep(1)  # Pause for 1 second
        st.session_state.countdown_result.append("Time's up!")
        st.success("Time's up!")

# Reset button
if reset_button:
    st.session_state.countdown_started = False
    st.session_state.countdown_result = []
    st.rerun()

# Display the countdown result if it exists
if st.session_state.countdown_started and not start_button:
    st.write("### Countdown")
    for result in st.session_state.countdown_result:
        if result == "Time's up!":
            st.success(result)
        else:
            st.write(result)