import streamlit as st
import random

# Page layout
st.set_page_config(page_title="Dice Simulator", page_icon=":game_die:")
st.title("Dice Simulator 🎲")
st.sidebar.header("Instructions")
st.sidebar.info("Click the button to roll the dice. The result will be displayed below.")

# Number of sides on each die
NUM_SIDES = 6

# Function to roll two dice and return their total
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    return die1, die2, total

# Add a button to roll the dice
if st.button("Roll the Dice 3 Times"):
    st.write("Here are the results of rolling two dice three times:")
    for i in range(3):
        die1, die2, total = roll_dice()
        st.write(f"Roll {i+1}: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")