# Guess the Number Game (User)

A simple Python game where the computer tries to guess the number you are thinking of, using a binary search approach. It's a fun way to see how algorithms work while you interact with the program!

## How to Play

1. **Think of a number** between 1 and 10.
2. The computer will guess a number.
3. When prompted, provide feedback:
   - Type **H** if the guess is high.
   - Type **L** if the guess is low.
   - Type **C** if the guess is correct.
4. The game will continue adjusting its guesses until it correctly guesses your number.

## How It Works

- The program starts with an initial range (1 to 10).
- It calculates the midpoint of the range as its guess.
- Based on your feedback:
  - If the guess is **high**, the upper bound is updated.
  - If the guess is **low**, the lower bound is updated.
- This process continues until you confirm the guess is correct.

## Running the Game

You can run this game in Google Colab:

1. Open [Google Colab](https://colab.research.google.com/).
2. Copy the code from this repository into a new notebook.
3. Run the notebook and follow the on-screen instructions.

Alternatively, click the link below to open the notebook directly (replace with your actual Colab link):

[Open Guess the Number Game on Google Colab](https://colab.research.google.com/drive/1DdJnlfs7c3Nwvl8QYn0U2ISVQuQ6h9G5?usp=sharing)

## Requirements

- Python 3.x
- A web browser (if using Google Colab)
