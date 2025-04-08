# Count Even Numbers
import streamlit as st

# Page layout
st.set_page_config(page_title="Count Even Numbers", page_icon=":1234:")
st.title("Count Even Numbers")

if "numbers" not in st.session_state:
    st.session_state.numbers = []
if "counted" not in st.session_state:
    st.session_state.counted = False

# Function to count even numbers in a list
def count_even(lst):
    """
    Returns number of even numbers in list.
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

# Explanation of the program
st.write("""
### What This Program Does
This program counts the number of even numbers in a list.
- Enter a number in the sidebar and click 'Add Number'.
- Repeat to add more numbers.
- Click 'Count Even Numbers' to see the result.
- Click 'Clear' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Enter Numbers")
    number = st.number_input("Enter an integer:", value=0, step=1)
    add_button = st.button("Add Number")
    count_button = st.button("Count Even Numbers")
    clear_button = st.button("Clear")

# Handle the add button
if add_button:
    st.session_state.numbers.append(number)
    st.session_state.counted = False  # Reset counted flag when adding a new number
    st.write("### Current List")
    for num in st.session_state.numbers:
        st.success(f"{num}")

# Handle the count button
if count_button and st.session_state.numbers:
    st.session_state.counted = True
    even_count = count_even(st.session_state.numbers)
    st.write("### Results")
    st.write("Your list:")
    for num in st.session_state.numbers:
        st.success(f"{num}")
    st.success(f"Number of even numbers: {even_count}")

# Handle the clear button
if clear_button:
    st.session_state.numbers = []
    st.session_state.counted = False
    st.rerun()

# Display the list if it exists and no buttons were just clicked
if st.session_state.numbers and not (add_button or count_button) and not st.session_state.counted:
    st.write("### Current List")
    for num in st.session_state.numbers:
        st.success(f"{num}")