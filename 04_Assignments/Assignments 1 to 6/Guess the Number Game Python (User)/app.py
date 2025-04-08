# Guess the Number
import streamlit as st
import random

# Page layout
st.set_page_config(page_title="Guess the Number", page_icon=":game_die:")
st.title("Guess the Number Game")

# Initialize session state
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 10)
if "num_guesses" not in st.session_state:
    st.session_state.num_guesses = 0
if "game_won" not in st.session_state:
    st.session_state.game_won = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Explanation of the program
st.write("""
### What This Program Does
The computer has chosen a random number between 1 and 10.
- Enter your guess in the sidebar (a number between 1 and 10).
- Click 'Submit Guess' to see if your guess is too high, too low, or correct.
- Keep guessing until you find the number!
- The app will track your number of guesses.
- Click 'Reset Game' to start a new game with a new number.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Game Controls")
    st.write(f"Number of guesses: {st.session_state.num_guesses}")
    guess = st.number_input("Enter your guess (1-10):", min_value=1, max_value=10, value=1, step=1)
    submit_button = st.button("Submit Guess")
    reset_button = st.button("Reset Game")

# Submit button
if submit_button and not st.session_state.game_won:
    st.session_state.num_guesses += 1
    if guess == st.session_state.target_number:
        st.session_state.feedback = f"Correct! You guessed the number in {st.session_state.num_guesses} guesses!"
        st.session_state.game_won = True
        st.session_state.results_shown = True
    elif guess < st.session_state.target_number:
        st.session_state.feedback = "Too low! Try a higher number."
        st.session_state.results_shown = True
    else:
        st.session_state.feedback = "Too high! Try a lower number."
        st.session_state.results_shown = True

# Reset button
if reset_button:
    st.session_state.target_number = random.randint(1, 10)
    st.session_state.num_guesses = 0
    st.session_state.game_won = False
    st.session_state.feedback = ""
    st.session_state.results_shown = False
    st.rerun()

# Display the feedback if it exists
if st.session_state.results_shown:
    st.write("### Result")
    if st.session_state.game_won:
        st.success(st.session_state.feedback)
    else:
        st.warning(st.session_state.feedback)