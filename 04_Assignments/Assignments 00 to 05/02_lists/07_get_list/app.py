# Get list
import streamlit as st

# Set the title of the app
st.title("Build a List")

# Explanation of the program
st.write("""
### How This Works
This program lets you build a list by adding values one at a time.
- Enter a value and click 'Add Value' to add it to the list.
- When you're done, click 'Show List' to see the final list.
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

# Button to show the final list
if st.button("Show List"):
    st.write("**Here's the list:**", st.session_state.my_list)

# Button to reset the list
if st.button("Reset List"):
    st.session_state.my_list = []
    st.rerun()