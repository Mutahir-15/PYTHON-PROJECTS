# Average
import streamlit as st

# Page layout
st.set_page_config(page_title="Average Calculator")
st.title("Average Calculator")

if "averages" not in st.session_state:
    st.session_state.averages = []

# Function to compute the average of two numbers
def average(a, b):
    return (a + b) / 2

# Explanation of the program
st.write("""
### What This Program Does
This program calculates the average of two numbers.
- Enter two numbers for Pair 1 and click 'Calculate Pair 1'.
- Enter two numbers for Pair 2 and click 'Calculate Pair 2'.
- The final average of the two averages will be shown.
- Click 'Clear' to start over.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Enter Numbers")
    
    # First pair of numbers
    st.write("Pair 1")
    num1 = st.number_input("First number (Pair 1):", value=0.0, step=1.0, key="num1")
    num2 = st.number_input("Second number (Pair 1):", value=10.0, step=1.0, key="num2")
    calc_button1 = st.button("Calculate Pair 1")
    
    # Second pair of numbers
    st.write("Pair 2")
    num3 = st.number_input("First number (Pair 2):", value=8.0, step=1.0, key="num3")
    num4 = st.number_input("Second number (Pair 2):", value=10.0, step=1.0, key="num4")
    calc_button2 = st.button("Calculate Pair 2", disabled=len(st.session_state.averages) < 1)
    
    # Clear button
    clear_button = st.button("Clear")

# Handle the first calculate button
if calc_button1:
    avg1 = average(num1, num2)
    if len(st.session_state.averages) == 0:  # Only add the first average if not already added
        st.session_state.averages.append(avg1)
    st.write("### Results")
    st.success(f"Average of Pair 1: {avg1}")

# Handle the second calculate button
if calc_button2:
    avg2 = average(num3, num4)
    if len(st.session_state.averages) == 1:  # Only add the second average if the first is already added
        st.session_state.averages.append(avg2)
    st.write("### Results")
    st.success(f"Average of Pair 1: {st.session_state.averages[0]}")
    st.success(f"Average of Pair 2: {st.session_state.averages[1]}")
    final_avg = average(st.session_state.averages[0], st.session_state.averages[1])
    st.success(f"Final Average: {final_avg}")

# Handle the clear button
if clear_button:
    st.session_state.averages = []
    st.rerun()

# Display the results if they exist
if st.session_state.averages and not (calc_button1 or calc_button2):
    st.write("### Results")
    if len(st.session_state.averages) >= 1:
        st.success(f"Average of Pair 1: {st.session_state.averages[0]}")
    if len(st.session_state.averages) == 2:
        st.success(f"Average of Pair 2: {st.session_state.averages[1]}")
        final_avg = average(st.session_state.averages[0], st.session_state.averages[1])
        st.success(f"Final Average: {final_avg}")