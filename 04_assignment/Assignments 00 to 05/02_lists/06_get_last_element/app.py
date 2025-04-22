# Get last element (list)
import streamlit as st

# Function to get the last element of a list
def get_last_element(lst):
    """
    Prints the last element of a provided list.
    
    Args:
        lst (list): A non-empty list
    """
    st.success(f"The last element of the list is: **{lst[-1]}**")

# Page Layout
st.set_page_config(page_title="Get Last Element of a List", page_icon=":pencil2:")
st.title("Get Last Element of a List")

# Explanation of list indexing (including negative indices)
st.write("""
### What is List Indexing?
In Python, a list is an ordered collection of items. You can access an item by its position (index):
- The first item is at index 0 (`lst[0]`).
- The last item is at index -1 (`lst[-1]`).
- The second-to-last item is at index -2 (`lst[-2]`), and so on.
This program lets you build a list and then shows the last element.
""")

# Initialize the list in session state
if "my_list" not in st.session_state:
    st.session_state.my_list = []

# Display the current list
st.write("**Current list:**", st.session_state.my_list)

# Input to add an element to the list
elem = st.text_input("Enter an element to add to the list:", value="", key="element_input")

# Button to add the element
if st.button("Add Element"):
    if elem:  # Only add if the input is not empty
        st.session_state.my_list.append(elem)
        st.rerun()  # Rerun to update the display and clear the input
    else:
        st.warning("Please enter a non-empty element.")

# Button to get the last element
if st.button("Get Last Element"):
    if st.session_state.my_list:
        get_last_element(st.session_state.my_list)
    else:
        st.error("The list is empty. Please add at least one element.")

# Button to reset the list
if st.button("Reset List"):
    st.session_state.my_list = []
    st.rerun()