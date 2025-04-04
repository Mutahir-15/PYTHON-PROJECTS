# Get first element
import streamlit as st

# Page layout
st.set_page_config(page_title="Get First Element of a List", page_icon=":memo:")
st.title("Get First Element of a List")
st.sidebar.header("Instruction")
st.sidebar.info("This simple app is meant to help you build a list. It supports adding an item to the list also It shows the first element of the list.")

# Explanation of list indexing
st.write("""
### What is List Indexing?
In Python, a list is an ordered collection of items. You can access an item by its position (index):
- The first item is at index 0 (`lst[0]`).
- The second item is at index 1 (`lst[1]`), and so on.
This program lets you build a list and then shows the first element.
""")

# Initialize the list in session state
if "my_list" not in st.session_state:
    st.session_state.my_list = []

# Display the current list
st.write("**Current list:**", st.session_state.my_list)

# Input to add an element to the list
elem = st.text_input("Enter an element to add to the list:", value="", key="element_input")

# ... existing code ...
# Define the get_first_element function
def get_first_element(lst):
    first_elem = lst[0]
    st.success(f"The first element is: **{first_elem}**")

# Button to add the element
if st.button("Add Element"):
    if elem:  # Only add if the input is not empty
        st.session_state.my_list.append(elem)
        st.rerun()  # Rerun to update the display and clear the input
    else:
        st.warning("Please enter a non-empty element.")

# Button to get the first element
if st.button("Get First Element"):
    if st.session_state.my_list:  # Check if the list is non-empty
        get_first_element(st.session_state.my_list)
    else:
        st.error("The list is empty. Please add at least one element.")

# Button to reset the list
if st.button("Reset List"):
    st.session_state.my_list = []
    st.rerun()