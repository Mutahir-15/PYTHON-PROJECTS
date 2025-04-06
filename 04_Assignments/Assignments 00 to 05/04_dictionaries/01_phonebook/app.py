# Phonebook
import streamlit as st

# Page layout
st.set_page_config(page_title="Phonebook Manager", page_icon="📕")
st.title("Phonebook Manager")

# Initialize session state to store the phonebook
if "phonebook" not in st.session_state:
    st.session_state.phonebook = {}

# Explanation of the program (in the main area)
st.write("""
### What This Program Does
This program lets you manage a phonebook.
- Add a name and phone number in the sidebar and click 'Add Entry' to store it.
- The current phonebook is displayed below.
- Enter a name to look up a phone number and click 'Lookup Number'.
- Click 'Clear Phonebook' to start over.
""")

# Add the input fields and buttons to the sidebar
with st.sidebar:
    st.header("Phonebook Actions")
    
    # Add entry section
    st.subheader("Add Entry")
    name_input = st.text_input("Name:", key="name_input")
    number_input = st.text_input("Number:", key="number_input")
    add_button = st.button("Add Entry")
    
    # Lookup section
    st.subheader("Lookup Number")
    lookup_name = st.text_input("Enter name to lookup:", key="lookup_name")
    lookup_button = st.button("Lookup Number")
    
    # Clear button
    clear_button = st.button("Clear Phonebook")

# Add button
if add_button:
    if not name_input:
        st.sidebar.error("Please enter a name.")
    elif not number_input:
        st.sidebar.error("Please enter a phone number.")
    else:
        st.session_state.phonebook[name_input] = number_input
        st.sidebar.success(f"Added: {name_input} -> {number_input}")

# Lookup button
if lookup_button:
    if not lookup_name:
        st.error("Please enter a name to lookup.")
    else:
        if lookup_name not in st.session_state.phonebook:
            st.warning(f"{lookup_name} is not in the phonebook.")
        else:
            st.success(f"{lookup_name} -> {st.session_state.phonebook[lookup_name]}")

# Clear button
if clear_button:
    st.session_state.phonebook = {}
    st.rerun()

# Displaying the current phonebook
if st.session_state.phonebook:
    st.write("### Current Phonebook")
    for name in st.session_state.phonebook:
        st.success(f"{name} -> {st.session_state.phonebook[name]}")
else:
    st.write("### Current Phonebook")
    st.write("Phonebook is empty.")