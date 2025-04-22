# Random Number
import streamlit as st
import random

# Page layout
st.set_page_config(page_title="Random Number Generator")
st.title("Random Number Generator")

# Constants
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

# Function to generate random numbers
def generate_numbers():
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]

# Explanation How it works?
st.write("""
### What This Program Does
This program generates 10 random numbers between 1 and 100 (inclusive).
- Click 'Generate Numbers' in the sidebar to get a new set of 10 random numbers.
- Each number is labeled as 'Even' or 'Odd'.
- Each time you click, you'll see a different set of numbers.
""")

# Button to generate Random Numbers
with st.sidebar:
    st.header("Settings")
    generate_button = st.button("Generate Numbers")

# Handle the generate button
if generate_button:
    numbers = generate_numbers()
    # Display the numbers
    st.write("### Generated Numbers")
    for i, number in enumerate(numbers, 1):
        if number % 2 == 0:
            st.write(f"{i}. {number} (Even)")
        else:
            st.write(f"{i}. {number} (Odd)")