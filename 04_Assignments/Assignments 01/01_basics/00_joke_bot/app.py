# Joke bot
import streamlit as st

# Page layout
st.set_page_config(page_title="Joke Bot",page_icon="🤖",)
st.title("Joke Bot")

# Initialize session state
if "response" not in st.session_state:
    st.session_state.response = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Joke setup
PROMPT = "Type **Joke** here."
JOKE = (
    "Here's a joke for you!\n\n"
    "Sophia is heading out to the grocery store. A programmer tells her:\n"
    "'Get a liter of milk, and if they have eggs, get 12.'\n\n"
    "Sophia returns with **13 liters of milk**.\n"
    "The programmer asks why.\n"
    "Sophia replies: 'Because they had eggs.'"
)
SORRY = "Sorry, I only tell jokes. Type 'Joke' to get one!"


# What this app does
st.write("""
### What Can I Do?
Welcome to Joke Bot! I'm programmed to tell you one joke:
- Type **'Joke'** in the sidebar and hit **Submit** to hear it.
- Type anything else and I’ll let you know I’m just here for laughs.
- Hit **Clear** to start fresh.
""")

# Sidebar inputs
with st.sidebar:
    st.header("Ask Me Something")
    user_input = st.text_input(PROMPT, value="Joke")
    submit_button = st.button("Submit")
    clear_button = st.button("Clear")

# Handle submission
if submit_button:
    if user_input.strip().lower() == "joke":
        st.session_state.response = JOKE
    else:
        st.session_state.response = SORRY
    st.session_state.results_shown = True
    st.write("### Response")
    if st.session_state.response == JOKE:
        st.success(st.session_state.response)
    else:
        st.error(st.session_state.response)

# Handle clear
if clear_button:
    st.session_state.response = ""
    st.session_state.results_shown = False
    st.rerun()

# Show saved response
if st.session_state.results_shown and not submit_button:
    st.write("### Response")
    if st.session_state.response == JOKE:
        st.success(st.session_state.response)
    else:
        st.error(st.session_state.response)