# Double it
import streamlit as st

# Page layout
st.title("Double It Until 100")

if "doubled_numbers" not in st.session_state:
    st.session_state.doubled_numbers = []

# Explanation of the program
st.write("""
### What This Program Does
This program takes a number you provide and doubles it repeatedly until the result is 100 or greater.
- Enter a starting number in the sidebar.
- Click 'Double It' to see the sequence of doubled numbers.
- Click 'Clear Sequence' to start over.
- Note: If your starting number is already 100 or greater, no sequence will be generated.
""")

# Add the number input and buttons to the sidebar
with st.sidebar:
    st.header("Doubling Settings")
    start_number = st.number_input(
        "Enter a starting number:",
        min_value=0.0,
        value=2.0,
        step=1.0
    )
    double_button = st.button("Double It")
    clear_button = st.button("Clear Sequence")

# Function to generate the doubled numbers
def generate_doubled_numbers(start):
    sequence = []
    curr_value = start
    while curr_value < 100:
        curr_value = curr_value * 2
        sequence.append(curr_value)
    return sequence

# Double button
if double_button:
    st.session_state.doubled_numbers = generate_doubled_numbers(start_number)
    st.write("### Doubled Numbers Sequence")
    if not st.session_state.doubled_numbers:
        st.warning("The starting number is already 100 or greater. No sequence generated.")
    else:
        for i, num in enumerate(st.session_state.doubled_numbers, 1):
            st.success(f"Step {i}: {num}")

# Clear button
if clear_button:
    st.session_state.doubled_numbers = []
    st.rerun()

# Display the sequence
if st.session_state.doubled_numbers and not double_button:
    st.write("### Doubled Numbers Sequence")
    for i, num in enumerate(st.session_state.doubled_numbers, 1):
        st.success(f"Step {i}: {num}")