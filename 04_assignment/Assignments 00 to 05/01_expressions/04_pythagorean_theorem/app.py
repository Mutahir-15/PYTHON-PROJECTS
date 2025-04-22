# Pythagorean Theorem
import streamlit as st
import math

# poage layout
st.set_page_config(page_title="Pythagorean Theorem Calculator", page_icon="📐")
st.title("Pythagorean Theorem Calculator 📐")
st.sidebar.header("Instructions")
st.sidebar.info("Enter the lengths of AB and AC to calculate the length of BC (the hypotenuse).")

# Input for two sides
ab = st.number_input("Enter the length of AB:", min_value=0.0, value=0.0, step=0.1)
ac = st.number_input("Enter the length of AC:", min_value=0.0, value=0.0, step=0.1)

# Calculating the hypotenuse when both inputs are provided
if ab > 0 and ac > 0:
    bc = math.sqrt(ab**2 + ac**2)
    st.write(f"AB: {ab}")
    st.write(f"AC: {ac}")
    st.success(f"The length of BC (the hypotenuse) is: {bc}")
elif ab == 0 or ac == 0:
    st.write("Please enter values greater than 0 for both AB and AC to calculate the hypotenuse.")