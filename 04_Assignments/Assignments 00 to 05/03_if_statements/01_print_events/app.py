# Print Event
import streamlit as st

# Page layout
st.set_page_config(page_title="Print Event", page_icon="📜")
st.title("Print the First 20 Even or Odd Numbers")

# Method: Using an if-statement
def print_events_with_if(number_type):
    numbers = []
    count = 0
    num = 0
    target_remainder = 0 if number_type == "Even Numbers" else 1
    while count < 20:
        if num % 2 == target_remainder:
            numbers.append(num)
            count += 1
        num += 1
    return numbers

# Explanation of the program
st.write("""
### What This Program Does
This program prints the first 20 numbers of your choice (even or odd).
- Choose whether to print even or odd numbers using the selectbox in the sidebar.
- The program uses an if-statement to check each number and determine if it matches your selection.
""")

# Added the even/odd selectbox to the sidebar
with st.sidebar:
    st.header("Settings")
    number_type = st.selectbox("Choose the type of numbers to print:", ("Even Numbers", "Odd Numbers"))

# Button to generate the numbers
if st.button("Show Numbers"):
    numbers = print_events_with_if(number_type)
    st.write(f"**First 20 {number_type.lower()}:**")
    for i, num in enumerate(numbers, 1):
        st.write(f"{i}. {num}")