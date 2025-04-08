import streamlit as st
import random
import string

# Set up the page
st.set_page_config(page_title="Hangman Game")
st.title("Welcome to the Hangman Game!")

# Predefined word list
WORD_LIST = ["python", "streamlit", "coding", "game", "hangman"]

# Initialize session variables
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORD_LIST)
if "word_display" not in st.session_state:
    st.session_state.word_display = ["_" for _ in st.session_state.word]
if "guessed_letters" not in st.session_state:
    st.session_state.guessed_letters = []
if "lives" not in st.session_state:
    st.session_state.lives = 6
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "results_shown" not in st.session_state:
    st.session_state.results_shown = False

# Explanation
st.write("""
### What This Program Does
This is a classic Hangman game:
- The computer has chosen a random word.
- The word is hidden, shown as underscores (e.g., `_ _ _ _` for a 4-letter word).
- You have 6 lives to guess the word by entering one letter at a time.
- If the letter is in the word, it will be revealed in the correct position(s).
- If the letter is not in the word, you lose a life.
- You win if you guess the word before running out of lives.
- You lose if you run out of lives.
- Enter a single letter in the sidebar and click 'Submit Guess'.
- Click 'Reset Game' to start a new game with a new word.
""")

# Sidebar for player controls
with st.sidebar:
    st.header("Your Move")
    st.write(f"Lives left: **{st.session_state.lives}**")
    st.write(f"Letters guessed: `{', '.join(st.session_state.guessed_letters) if st.session_state.guessed_letters else 'None'}`")
    st.write(f"Current word: `{ ' '.join(st.session_state.word_display) }`")

    # Player input
    guess = st.text_input("Enter a letter (a-z):", max_chars=1, value="", key="guess_input").lower()
    submit_button = st.button("Submit Guess")
    reset_button = st.button("Reset Game")

# Game reset logic
def reset_game():
    st.session_state.word = random.choice(WORD_LIST)
    st.session_state.word_display = ["_" for _ in st.session_state.word]
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.feedback = ""
    st.session_state.results_shown = False

# Handle guess submission
if submit_button and not st.session_state.game_over:
    if not guess:
        st.session_state.feedback = "Please enter a letter."
        st.session_state.results_shown = True
    elif guess not in string.ascii_lowercase:
        st.session_state.feedback = "Only letters (a-z) are allowed!"
        st.session_state.results_shown = True
    elif guess in st.session_state.guessed_letters:
        st.session_state.feedback = "You already guessed that letter!"
        st.session_state.results_shown = True
    else:
        st.session_state.guessed_letters.append(guess)

        if guess in st.session_state.word:
            for i, char in enumerate(st.session_state.word):
                if char == guess:
                    st.session_state.word_display[i] = guess
            st.session_state.feedback = "Nice! That letter is in the word."
        else:
            st.session_state.lives -= 1
            st.session_state.feedback = "Nope! That letter isn't there."

        # Win condition
        if st.session_state.word_display == list(st.session_state.word):
            st.session_state.feedback = f"You won! The word was **{st.session_state.word}**!"
            st.session_state.game_over = True
            st.session_state.results_shown = True

        # Lose condition
        if st.session_state.lives == 0:
            st.session_state.feedback = f"Game Over! The word was **{st.session_state.word}**."
            st.session_state.game_over = True
            st.session_state.results_shown = True

# Handle reset
if reset_button:
    reset_game()
    st.rerun()

# Feedback message
if st.session_state.results_shown:
    st.write("### Result")
    if st.session_state.game_over:
        if st.session_state.lives == 0:
            st.error(st.session_state.feedback)
        else:
            st.success(st.session_state.feedback)
    else:
        if "Nice" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.warning(st.session_state.feedback)