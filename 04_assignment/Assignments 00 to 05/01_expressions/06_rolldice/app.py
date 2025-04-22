# Roll the Dice
import streamlit as st
import random

# Page layout
st.set_page_config(page_title="Dice Roller", page_icon=":game_die:")
st.title("🎲 Dice Roller")
st.sidebar.header("Instructions")
st.sidebar.info("Enter the number of times you want to roll the die.")

# Number of sides on the die
NUM_SIDES = 6

# Ask the user how many times to roll the die
num_rolls = st.number_input("How many times would you like to roll the die?", min_value=1, value=3, step=1, format="%d")

# Roll the die when the user clicks a button
if st.button("Roll Dice"):
    st.write(f"Rolling the die {num_rolls} time(s):")
    for i in range(num_rolls):
        roll = random.randint(1, NUM_SIDES)
        st.write(f"Roll {i + 1}: {roll}")