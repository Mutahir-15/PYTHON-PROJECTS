# Fibonacci
import streamlit as st

# Page layout
st.set_page_config(page_title="Fibonacci Sequence Generator", page_icon=":snake:")
st.title("Fibonacci Sequence Generator")

# Default maximum value
DEFAULT_MAX_TERM_VALUE = 10000

# Initialize session state to store the sequence
if "fibonacci_sequence" not in st.session_state:
    st.session_state.fibonacci_sequence = []

# Explanation of the program
st.write("""
### What This Program Does
This program generates the Fibonacci sequence, starting from Fib(0) = 0.
- The Fibonacci sequence is defined as: **Fib(0) = 0, Fib(1) = 1, Fib(n) = Fib(n-1) + Fib(n-2) for n ≥ 2**.
- Enter a maximum value in the sidebar (e.g., 10000).
- Click 'Generate Sequence' to see all Fibonacci numbers up to that value.
- Click 'Clear Sequence' to start over.
""")

# Add the maximum value input and buttons to the sidebar
with st.sidebar:
    st.header("Fibonacci Settings")
    max_term_value = st.number_input(
        "Maximum value for terms:",
        min_value=0,
        value=DEFAULT_MAX_TERM_VALUE,
        step=1000
    )
    generate_button = st.button("Generate Sequence")
    clear_button = st.button("Clear Sequence")

# Function to generate the Fibonacci sequence
def generate_fibonacci(max_value):
    sequence = []
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)
    while curr_term <= max_value:
        sequence.append(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    return sequence

# Handle the generate button
if generate_button:
    st.session_state.fibonacci_sequence = generate_fibonacci(max_term_value)
    st.write("### Fibonacci Sequence")
    if not st.session_state.fibonacci_sequence:
        st.warning("No terms generated. Try a larger maximum value.")
    else:
        for i, term in enumerate(st.session_state.fibonacci_sequence):
            st.success(f"Fib({i}) = {term}")

# Handle the clear button
if clear_button:
    st.session_state.fibonacci_sequence = []
    st.rerun()

# Display the sequence if it exists
if st.session_state.fibonacci_sequence and not generate_button:
    st.write("### Fibonacci Sequence")
    for i, term in enumerate(st.session_state.fibonacci_sequence):
        st.success(f"Fib({i}) = {term}")