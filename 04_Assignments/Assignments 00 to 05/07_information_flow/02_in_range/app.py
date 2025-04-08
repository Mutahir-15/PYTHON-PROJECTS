# In range
import streamlit as st

# Page layout
st.set_page_config(page_title="Range Checker", page_icon="🔢")
st.title("Range Checker")

# Initialize session state
if "in_range_result" not in st.session_state:
    st.session_state.in_range_result = None
if "numbers" not in st.session_state:
    st.session_state.numbers = {}
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to check if number is within range
def in_range(n, low, high):
    return low <= n <= high


# Program description
st.write("""
### What This App Does
It checks whether a number falls **within a specified range (inclusive)**.
- Enter a number, a lower bound, and an upper bound in the sidebar.
- Click **'Check Range'** to get the result.
- Click **'Clear'** to reset the form.
""")

# Sidebar inputs
with st.sidebar:
    st.header("🔢 Input Section")
    n = st.number_input("Number to check:", value=5, step=1)
    low = st.number_input("Lower bound:", value=1, step=1)
    high = st.number_input("Upper bound:", value=10, step=1)
    check_button = st.button("Check Range")
    clear_button = st.button("Clear")

# Logic for check button
if check_button:
    if high <= low:
        st.error("⚠️ Upper bound must be greater than lower bound.")
    else:
        st.session_state.numbers = {"n": n, "low": low, "high": high}
        st.session_state.in_range_result = in_range(n, low, high)
        st.session_state.results_shown = True
        st.write("### Result")
        st.success(f"Is {n} between {low} and {high} (inclusive)? **{st.session_state.in_range_result}**")

# Logic for clear button
if clear_button:
    st.session_state.in_range_result = None
    st.session_state.numbers = {}
    st.session_state.results_shown = False
    st.rerun()

# Display result on page load if available
if st.session_state.results_shown and not check_button:
    n = st.session_state.numbers["n"]
    low = st.session_state.numbers["low"]
    high = st.session_state.numbers["high"]
    st.write("### ✅ Result")
    st.success(f"Is {n} between {low} and {high} (inclusive)? **{st.session_state.in_range_result}**")
