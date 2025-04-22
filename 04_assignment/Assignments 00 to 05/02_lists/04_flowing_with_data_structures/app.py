import streamlit as st

# Function to add three copies of data to a list
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

# Page layout
st.set_page_config(page_title="Flowing with Data Structures: Mutability Demo", page_icon="🔄")
st.title("Flowing with Data Structures: Mutability Demo")
st.sidebar.header("Instruction")
st.sidebar.info("This demo shows how a list (mutable) can be modified inside a function without returning it.")

# Explanation
st.write("""
### What is Mutability?
In Python, some data types are **mutable** (can be changed) and others are **immutable** (cannot be changed).
- **Immutable types** (like numbers and strings): Changes inside a function don't stick unless you return the new value.
- **Mutable types** (like lists): Changes inside a function stick, even if you don't return the list.
This program shows how a list (a mutable type) can be modified inside a function without returning it.
""")

# Initializing the list
if "my_list" not in st.session_state:
    st.session_state.my_list = []

# This will display the list *before*
st.write("**List before:**", st.session_state.my_list)

# User Input
message = st.text_input("Enter a message to copy:", value="Hello world!")

# Button to add copies
if st.button("Add Three Copies"):
    add_three_copies(st.session_state.my_list, message)

# This will display the list *after*
st.write("**List after:**", st.session_state.my_list)

# Option to reset the list
if st.button("Reset List"):
    st.session_state.my_list = []
    st.rerun()