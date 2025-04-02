# Remainder division
import streamlit as st

# Page layout
st.set_page_config(page_title="Remainder division", page_icon="🔢")
st.title("🔢 Remainder division")
st.sidebar.header("Instruction")
st.sidebar.info("Please enter two integers to be divided and divide by.")

# Input for the two numbers
dividend = st.number_input("Please enter an integer to be divided:", min_value=0, value=1, step=1)
divisor = st.number_input("Please enter an integer to divide by:", min_value=1, value=1, step=1)

# Calculate quotient and remainder
if divisor > 0:
    quotient = dividend // divisor
    remainder = dividend % divisor
    st.success(f"The result of this division is {quotient} with a remainder of {remainder}")
else:
    st.warning("Please enter a divisor greater than 0.")