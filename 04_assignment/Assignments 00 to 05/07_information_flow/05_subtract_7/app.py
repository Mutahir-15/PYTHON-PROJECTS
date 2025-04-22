# Subtract (7)
import streamlit as st

# Page layout
st.set_page_config(page_title="Subtract 7 Calculator")
st.title("Subtract 7 Calculator")

# Initialize session state
if "result" not in st.session_state:
    st.session_state.result = None
if "number" not in st.session_state:
    st.session_state.number = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to subtract 7 from a number
def subtract_seven(num):
    return num - 7

# App description
st.write("""
### What Does This App Do?
Simple math fun! Enter any number and this app will subtract **7** from it.
- Add your number in the sidebar.
- Click **'Subtract 7'** to get the answer.
- Click **'Clear'** to start over.
""")

# Sidebar inputs
with st.sidebar:
    st.header("Subtract from Your Number")
    number = st.number_input("Enter a number:", value=7, step=1)
    subtract_button = st.button("Subtract 7")
    clear_button = st.button("Clear")

# Subtract logic
if subtract_button:
    st.session_state.number = number
    st.session_state.result = subtract_seven(number)
    st.session_state.results_shown = True
    st.write("### Result")
    st.success(f"{number} - 7 = {st.session_state.result}")

# Clear logic
if clear_button:
    st.session_state.result = None
    st.session_state.number = None
    st.session_state.results_shown = False
    st.rerun()

# Show result if already computed
if st.session_state.results_shown and not subtract_button:
    st.write("### Result")
    st.success(f"{st.session_state.number} - 7 = {st.session_state.result}")
