# Divisor Finder App
import streamlit as st

# Page layout
st.set_page_config(page_title="Divisor Finder", page_icon="🔍")
st.title("🔍 Divisor Finder")

# Initialize session state
if "divisors" not in st.session_state:
    st.session_state.divisors = []
if "number" not in st.session_state:
    st.session_state.number = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to get divisors
def get_divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# Description
st.write("""
### What This App Does
Finds all the numbers that divide your input number exactly.
- Just enter a number in the sidebar.
- Click 'Find Divisors' to see the results.
- Use 'Clear' to start fresh.
""")

# Sidebar input section
with st.sidebar:
    st.header("🧮 Input")
    number = st.number_input("Enter a number:", min_value=1, value=12, step=1)
    find_button = st.button("Find Divisors")
    clear_button = st.button("Clear")

# When Find Divisors button is clicked
if find_button:
    st.session_state.number = number
    st.session_state.divisors = get_divisors(number)
    st.session_state.results_shown = True
    st.write(f"### Divisors of {number}")
    for d in st.session_state.divisors:
        st.success(f"{d}")

# When Clear button is clicked
if clear_button:
    st.session_state.divisors = []
    st.session_state.number = None
    st.session_state.results_shown = False
    st.rerun()

# Show results if already found
if st.session_state.results_shown and not find_button:
    st.write(f"### Divisors of {st.session_state.number}")
    for d in st.session_state.divisors:
        st.success(f"{d}")