# Rock Paper Scissor Game
import streamlit as st
import random

# Page layout
st.set_page_config(page_title="Rock Paper Scissor Game", page_icon=":page_facing_up:")
st.title("Rock Paper Scissor Game")

# List of possible choices
CHOICES = ["Rock", "Paper", "Scissors"]

# Initialize session state
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None
if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None
if "result" not in st.session_state:
    st.session_state.result = None
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Explanation
st.write("""
### What This Program Does
This is a classic Rock Paper Scissor game:
- Select your choice (Rock, Paper, or Scissors) from the dropdown in the sidebar.
- Click 'Play' to see the computer's choice and the result.
- The game rules are:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
  - If both choices are the same, it's a tie
- The app will show your choice, the computer's choice, and the result (win, lose, or tie).
- Click 'Reset' to play again.
""")

# Sidebar for inputs
with st.sidebar:
    st.header("Game Controls")
    user_choice = st.selectbox("Select your choice:", options=[""] + CHOICES)
    play_button = st.button("Play")
    reset_button = st.button("Reset")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Play button
if play_button and user_choice:
    computer_choice = random.choice(CHOICES)
    result = determine_winner(user_choice, computer_choice)
    
    # Store the results in session state
    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.result = result
    st.session_state.results_shown = True
    
    # Results
    st.write("### Result")
    st.write(f"Your choice: **{user_choice}**")
    st.write(f"Computer's choice: **{computer_choice}**")
    if result == "You win!":
        st.success(result)
    elif result == "It's a tie!":
        st.warning(result)
    else:
        st.error(result)

# Reset button
if reset_button:
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None
    st.session_state.results_shown = False
    st.rerun()

# Display the result if it exists
if st.session_state.results_shown and not play_button:
    st.write("### Result")
    st.write(f"Your choice: **{st.session_state.user_choice}**")
    st.write(f"Computer's choice: **{st.session_state.computer_choice}**")
    if st.session_state.result == "You win!":
        st.success(st.session_state.result)
    elif st.session_state.result == "It's a tie!":
        st.warning(st.session_state.result)
    else:
        st.error(st.session_state.result)