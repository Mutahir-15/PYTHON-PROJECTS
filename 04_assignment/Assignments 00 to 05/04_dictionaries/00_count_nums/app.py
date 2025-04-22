# Count Numbers
import streamlit as st

# page layout
st.set_page_config(page_title="Number Frequency Counter", page_icon=":bar_chart:")
st.title("Number Frequency Counter")

# Initialize session state
if "user_numbers" not in st.session_state:
    st.session_state.user_numbers = []

# Function to count numbers using a dictionary
def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

# Explanation
st.write("""
### What This Program Does
This program counts how many times each number appears in a list of numbers you provide.
- Enter a number in the sidebar and click 'Add Number' to add it to the list.
- Click 'Show Counts' to see the frequency of each number.
- Click 'Clear List' to start over.
""")

# Add the number input and buttons to the sidebar
with st.sidebar:
    st.header("Input Numbers")
    number_input = st.number_input("Enter a number:", min_value=-1000, max_value=1000, value=0, step=1)
    add_button = st.button("Add Number")
    show_button = st.button("Show Counts")
    clear_button = st.button("Clear List")

# Add button
if add_button:
    st.session_state.user_numbers.append(int(number_input))
    st.sidebar.write(f"Added: {number_input}")
    st.sidebar.write(f"Current list: {st.session_state.user_numbers}")

# Show button
if show_button:
    if not st.session_state.user_numbers:
        st.error("Please add at least one number before showing counts.")
    else:
        num_dict = count_nums(st.session_state.user_numbers)
        st.write("### Frequency Counts")
        for num in num_dict:
            st.success(f"{num} appears {num_dict[num]} times.")

# Clear Button
if clear_button:
    st.session_state.user_numbers = []
    st.rerun()

# Displaying current list of numbers
if st.session_state.user_numbers:
    st.write("### Current List of Numbers")
    st.write(st.session_state.user_numbers)