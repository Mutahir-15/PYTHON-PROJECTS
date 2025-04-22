# Wholsome Machine
import streamlit as st

# Page layout
st.set_page_config(page_title="Wholesome Machine")
st.title("Wholesome Machine")

# The Affirmation to match
AFFIRMATION = "I am constantly learning and growing."

# Initialize session state for the attempts and game state
if "attempts" not in st.session_state:
    st.session_state.attempts = []
if "affirmation_correct" not in st.session_state:
    st.session_state.affirmation_correct = False

# Explanation
st.write("""
### What This Program Does
This program encourages you to type a positive affirmation correctly.
- The affirmation to type is: **I am constantly learning and growing.**
- Enter your attempt in the sidebar and click 'Submit Attempt'.
- I'll let you know if your attempt is correct or not.
- Keep trying until you get it right!
- Your attempt history is displayed below.
- Click 'Clear History' to start over.
""")

# Add the input field and buttons to the sidebar
with st.sidebar:
    st.header("Type the Affirmation")
    st.write(f"Affirmation: **{AFFIRMATION}**")
    user_input = st.text_input("Your attempt:", disabled=st.session_state.affirmation_correct)
    submit_button = st.button("Submit Attempt", disabled=st.session_state.affirmation_correct)
    clear_button = st.button("Clear History")

# Submit button
if submit_button and not st.session_state.affirmation_correct:
    st.session_state.attempts.append(user_input)
    if user_input == AFFIRMATION:
        st.session_state.affirmation_correct = True
        st.write("### Latest Attempt")
        st.success("That's right! :)")
    else:
        st.write("### Latest Attempt")
        st.warning("That was not the affirmation. Try again!")

# Clear button
if clear_button:
    st.session_state.attempts = []
    st.session_state.affirmation_correct = False
    st.rerun()

# Display the attempt history
if st.session_state.attempts:
    st.write("### Attempt History")
    for i, attempt in enumerate(st.session_state.attempts, 1):
        if attempt == AFFIRMATION:
            st.success(f"Attempt {i}: {attempt} - Correct!")
        else:
            st.warning(f"Attempt {i}: {attempt} - Incorrect")