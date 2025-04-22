# Tall enough to ride
import streamlit as st

# Page layout
st.set_page_config(page_title="Tall Enough to Ride")
st.title("Rollercoaster Height Checker")

# Constant for minimum height (in feet)
MINIMUM_HEIGHT = 4.5

# Initialize session state to store the history of checks
if "height_checks" not in st.session_state:
    st.session_state.height_checks = []

# Function to check if the user is tall enough
def check_height(height):
    if height >= MINIMUM_HEIGHT:
        return "You're tall enough to ride!"
    else:
        return "You're not tall enough to ride, but maybe next year!"

# Explanation of the program
st.write(f"""
### What This Program Does
This program checks if you're tall enough to ride a rollercoaster.
- The minimum height requirement is {MINIMUM_HEIGHT} feet.
- Enter your height in feet (e.g., 5.5 for 5 feet 6 inches) in the sidebar and click 'Check Height' to see if you qualify.
- You can keep checking different heights, and your history will be displayed below.
- Click 'Clear History' to start over.
""")

# Add the height input to the sidebar
with st.sidebar:
    st.header("Input Your Height")
    height = st.number_input("How tall are you (in feet)?", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    check_button = st.button("Check Height")
    clear_button = st.button("Clear History")

# Check button
if check_button:
    if height < 0:
        st.error("Please enter a valid height (0 or greater).")
    else:
        result = check_height(height)
        # Adding check to the history
        st.session_state.height_checks.append((height, result))
        # Displaying the result immediately
        st.write("### Latest Result")
        if "tall enough" in result:
            st.success(result)
        else:
            st.warning(result)

# Clear button
if clear_button:
    st.session_state.height_checks = []
    st.rerun()

# Displaying the history
if st.session_state.height_checks:
    st.write("### History of Checks")
    for i, (height, result) in enumerate(st.session_state.height_checks, 1):
        st.write(f"**Check {i}: Height = {height} feet**")
        if "tall enough" in result:
            st.write(result)
        else:
            st.warning(result)