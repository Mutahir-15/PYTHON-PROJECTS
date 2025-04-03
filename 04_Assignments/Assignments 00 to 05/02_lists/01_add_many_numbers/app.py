# Add many Numbers (Lists)
import streamlit as st

# Page layout
st.set_page_config(page_title="Add Many Numbers", page_icon="📱")
st.title("✏ Add Many Numbers")
st.sidebar.header("Instruction")
st.sidebar.info("Enter a list of numbers separated by commas. The program will add all the numbers together and display the result.")

#Input list
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# User input
usre_input = st.text_input("Enter a list of numbers separated by commas:", key="numbers")

# Calculation
if st.button("Calculate"):
    try:
        numbers = [float(num.strip()) for num in usre_input.split(",")]
        result = sum_list(numbers)
        st.success(f"The sum of the numbers is: **{result}**")
    except ValueError:
        st.error("Invalid input. Please enter a list of numbers separated by commas.")