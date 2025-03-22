import streamlit as st
import random

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 10)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Function to reset the game
def reset_game():
    st.session_state.number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Title and instructions
st.title("Guess the Number Game")
st.write("I'm thinking of a number between 1 and 10. Can you guess it?")

# User input
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=10, key="guess")

# Button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if user_guess == st.session_state.number:
        st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True
    elif user_guess < st.session_state.number:
        st.warning("Too low! Try a higher number.")
    else:
        st.warning("Too high! Try a lower number.")

# Display attempts
st.write(f"Attempts: {st.session_state.attempts}")

# Reset game button
if st.button("New Game"):
    reset_game()
    st.write("A new number has been generated. Good luck!")

# Optional: Leaderboard (simplified example)
# This would require a backend to store scores, but here's a placeholder
st.subheader("Leaderboard")
st.write("Top Scores (Placeholder):")
st.write("1. User1 - 3 attempts")
st.write("2. User2 - 5 attempts")
st.write("3. User3 - 7 attempts")