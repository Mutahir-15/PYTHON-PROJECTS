# Chaotic Counting
import streamlit as st
import random
import time

if "numbers" not in st.session_state:
    st.session_state.numbers = []
if "done_counting" not in st.session_state:
    st.session_state.done_counting = False

# Probability of stopping
DONE_LIKELIHOOD = 0.3

# Function to check if counting should stop
def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

# Function to perform chaotic counting
def chaotic_counting():
    numbers = []
    for i in range(10):
        curr_num = i + 1
        if done():
            return numbers
        numbers.append(curr_num)
    return numbers

# Set the title of the app
st.title("Chaotic Counting")

# Explanation of the program
st.write("""
### What This Program Does
This program counts from 1 to 10, but might stop early.
- Click 'Start Counting' to begin.
- The counting stops randomly based on a probability.
- Click 'Clear' to start over.
""")

# Sidebar for buttons
with st.sidebar:
    st.header("Counting Controls")
    start_button = st.button("Start Counting")
    clear_button = st.button("Clear")

# Handle the start button
if start_button and not st.session_state.done_counting:
    st.session_state.numbers = chaotic_counting()
    st.session_state.done_counting = True
    
    # Display the numbers with a small delay
    st.write("### Counting")
    for num in st.session_state.numbers:
        st.success(f"{num}")
        time.sleep(0.5)
    st.success("I'm done")

# Handle the clear button
if clear_button:
    st.session_state.numbers = []
    st.session_state.done_counting = False
    st.rerun()

# Display the numbers if they exist
if st.session_state.numbers and not start_button:
    st.write("### Counting")
    for num in st.session_state.numbers:
        st.success(f"{num}")
    st.success("I'm done")