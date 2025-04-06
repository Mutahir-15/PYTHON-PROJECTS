# Printing 20 Even Numbers
import streamlit as st

# Page layout
st.set_page_config(page_title="Print 20 even Numbers", page_icon="2️⃣")
st.title("Even Numbers Generator")

# Default number of even numbers
DEFAULT_COUNT = 20

# Initialize session state to store the sequence
if "even_numbers" not in st.session_state:
    st.session_state.even_numbers = []

# Explanation of the program
st.write("""
### What This Program Does
This program generates a sequence of even numbers, starting from 0.
- Enter the number of even numbers you want to generate in the sidebar (e.g., 20).
- Click 'Generate Evens' to see the sequence.
- Click 'Clear Sequence' to start over.
""")

# Add the count input and buttons to the sidebar
with st.sidebar:
    st.header("Even Numbers Settings")
    count = st.number_input(
        "Number of even numbers to generate:",
        min_value=1,
        value=DEFAULT_COUNT,
        step=1
    )
    generate_button = st.button("Generate Evens")
    clear_button = st.button("Clear Sequence")

# Function to generate the even numbers
def generate_evens(count):
    return [i * 2 for i in range(count)]

# Generate button
if generate_button:
    st.session_state.even_numbers = generate_evens(count)
    st.write("### Even Numbers Sequence")
    for i, num in enumerate(st.session_state.even_numbers, 1):
        st.success(f"Even {i}: {num}")

# Clear button
if clear_button:
    st.session_state.even_numbers = []
    st.rerun()

# Display the sequence if it exists
if st.session_state.even_numbers and not generate_button:
    st.write("### Even Numbers Sequence")
    for i, num in enumerate(st.session_state.even_numbers, 1):
        st.success(f"Even {i}: {num}")