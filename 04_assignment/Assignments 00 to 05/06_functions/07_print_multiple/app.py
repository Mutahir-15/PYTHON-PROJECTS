# Print Divisor
import streamlit as st

# Page layout
st.set_page_config(page_title="Multiple")
st.title("Print Multiple")

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Function to repeat a message
def repeat_message(msg, count):
    return [msg] * count

st.write("""
### What This App Does
Repeats your message as many times as you want!
- Type a message and how many times to repeat it.
- Click 'Repeat Message' to see your message echoed.
- Hit 'Clear' to start over.
""")

# Sidebar controls
with st.sidebar:
    st.header("📝 Your Input")
    message = st.text_input("Type your message:", value="Hello!")
    repeats = st.number_input("How many times?", min_value=1, value=6, step=1)
    repeat_button = st.button("Repeat Message")
    clear_button = st.button("Clear")

# Repeat button logic
if repeat_button:
    st.session_state.messages = repeat_message(message, repeats)
    st.session_state.results_shown = True
    st.write("### Repeated Messages")
    for m in st.session_state.messages:
        st.success(m)

# Clear button logic
if clear_button:
    st.session_state.messages = []
    st.session_state.results_shown = False
    st.rerun()

# Show stored results if applicable
if st.session_state.results_shown and not repeat_button:
    st.write("### Repeated Messages")
    for m in st.session_state.messages:
        st.success(m)