# Guess my Number 
import streamlit as st
import random

# Initialize session state for the game
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 99)
if "guesses" not in st.session_state:
    st.session_state.guesses = []
if "game_won" not in st.session_state:
    st.session_state.game_won = False

# Page layout
st.set_page_config(page_title="Guess My Number", page_icon=":game_die:")
st.title("Guess My Number")

# Explanation of the program
st.write("""
### What This Program Does
I'm thinking of a number between 1 and 99...
- Enter your guess in the sidebar and click 'Submit Guess'.
- I'll tell you if your guess is too high, too low, or correct.
- Keep guessing until you find the number!
- Once you win, you can click 'New Game' to play again.
- Your guess history is displayed below.
""")

# Input and buttons to the sidebar
with st.sidebar:
    st.header("Make a Guess")
    guess = st.number_input("Enter your guess:", min_value=1, max_value=99, value=1, step=1)
    submit_button = st.button("Submit Guess")
    new_game_button = st.button("New Game")

# Handles the submit button
if submit_button and not st.session_state.game_won:
    st.session_state.guesses.append(guess)
    if guess == st.session_state.secret_number:
        st.session_state.game_won = True
        st.write("### Latest Guess")
        st.success(f"Congrats! The number was: {st.session_state.secret_number}")
    elif guess < st.session_state.secret_number:
        st.write("### Latest Guess")
        st.info(f"Your guess ({guess}) is too low.")
    else:
        st.write("### Latest Guess")
        st.warning(f"Your guess ({guess}) is too high.")

# Handles the new game button
if new_game_button:
    st.session_state.secret_number = random.randint(1, 99)
    st.session_state.guesses = []
    st.session_state.game_won = False
    st.rerun()

# Display the guess history
if st.session_state.guesses:
    st.write("### Guess History")
    for i, g in enumerate(st.session_state.guesses, 1):
        if g == st.session_state.secret_number:
            st.success(f"Guess {i}: {g} - Correct!")
        elif g < st.session_state.secret_number:
            st.info(f"Guess {i}: {g} - Too low")
        else:
            st.warning(f"Guess {i}: {g} - Too high")