# Double list 
import streamlit as st

# Page layout
st.set_page_config(page_title="Double List", page_icon=":bar_chart:")
st.title("📈 Double List")
st.sidebar.header("Instaruction")
st.sidebar.info("This app will double the list you enter. Enter the numbers seperated by commas and you will get it doubled.")

# Function to calculate double list
def double_list(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2 
    return numbers  # It will return numbers[i] * 2

# Input list
st.write("Enter a list of numbers separated by commas:")
list_input = st.text_input("Enter your numbers:", value="1, 2, 3, 4")

# Convertion
if st.button("Double List"):
    try:
        numbers = [int(num.strip()) for num in list_input.split(",")]
        doubled_numbers = double_list(numbers)
        st.write(f"The original list: **{list_input}**")
        st.success(f"The doubled list: **{doubled_numbers}**")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")