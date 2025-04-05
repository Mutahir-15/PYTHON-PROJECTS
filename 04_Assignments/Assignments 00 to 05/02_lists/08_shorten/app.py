"""
Program: shorten (Streamlit Version)
---------------------------------------
Builds a list by letting the user add values one at a time.
When the user clicks 'Shorten List', removes elements from the end until the list
is MAX_LENGTH items long, printing each removed element.
"""

import streamlit as st

# Constant for maximum length
MAX_LENGTH = 3

# Function to shorten the list
def shorten(lst):
    """
    Removes elements from the end of lst until it is MAX_LENGTH items long,
    printing each removed element. If lst is already shorter than MAX_LENGTH,
    leaves it unchanged.
    
    Args:
        lst (list): The list to shorten
    """
    removed_elements = []
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        removed_elements.append(last_elem)
    if removed_elements:
        st.write("**Removed elements:**")
        for elem in removed_elements:
            st.write(elem)
    else:
        st.write("No elements were removed (list is already short enough).")

# Set the title of the app
st.title("Shorten a List")

# Explanation of the program
st.write(f"""
### How This Works
This program lets you build a list by adding values one at a time.
- Enter a value and click 'Add Value' to add it to the list.
- When you're done, click 'Shorten List' to remove elements from the end until the list is {MAX_LENGTH} items long.
- Each removed element will be displayed, and the final list will be shown.
- You can reset the list at any time with the 'Reset List' button.
""")

# Initialize the list in session state
if "my_list" not in st.session_state:
    st.session_state.my_list = []

# Display the current list
st.write("**Current list:**", st.session_state.my_list)

# Input to add a value to the list
val = st.text_input("Enter a value:", value="", key="value_input")

# Button to add the value
if st.button("Add Value"):
    if val:  # Only add if the input is not empty
        st.session_state.my_list.append(val)
        st.rerun()  # Rerun to update the display and clear the input
    else:
        st.warning("Please enter a non-empty value.")

# Button to shorten the list
if st.button("Shorten List"):
    # Create a copy of the list to modify (to preserve the original for display)
    temp_list = st.session_state.my_list.copy()
    shorten(temp_list)
    st.session_state.my_list = temp_list
    st.write("**Final list after shortening:**", st.session_state.my_list)

# Button to reset the list
if st.button("Reset List"):
    st.session_state.my_list = []
    st.rerun()