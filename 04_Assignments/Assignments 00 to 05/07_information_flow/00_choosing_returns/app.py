# Choosing return
import streamlit as st

# Page layout
st.set_page_config(page_title="Adult Age Checker")
st.title("Adult Age Checker")

# Initialize session state
if "is_adult_result" not in st.session_state:
    st.session_state.is_adult_result = None
if "age" not in st.session_state:
    st.session_state.age = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Constant for adult age
ADULT_AGE : int = 18 # US and Pakistan age

# Function to check adult status
def is_adult(age):
    return age >= ADULT_AGE

# Description
st.write("""
### What This App Does
Checks if a person is considered an **adult** (18 years or older).
- Enter an age in the sidebar.
- Click **'Check Age'** to see the result.
- Use **'Clear'** to reset the app.
""")

# Sidebar input section
with st.sidebar:
    st.header("Input")
    age = st.number_input("Enter age:", min_value=0, value=18, step=1)
    check_button = st.button("Check Age")
    clear_button = st.button("Clear")

# When Check button is clicked
if check_button:
    st.session_state.age = age
    st.session_state.is_adult_result = is_adult(age)
    st.session_state.results_shown = True
    st.write("### Result")
    if st.session_state.is_adult_result:
        st.success(f"Yes! At {age}, this person is an adult.")
    else:
        st.warning(f"Nope! At {age}, this person is not an adult yet.")

# Handle clear button
if clear_button:
    st.session_state.is_adult_result = None
    st.session_state.age = None
    st.session_state.results_shown = False
    st.rerun()

# Show previous result if available
if st.session_state.results_shown and not check_button:
    st.write("### Result")
    if st.session_state.is_adult_result:
        st.success(f"Yes! At {st.session_state.age}, this person is an adult.")
    else:   
        st.warning(f"Nope! At {st.session_state.age}, this person is not an adult yet.")