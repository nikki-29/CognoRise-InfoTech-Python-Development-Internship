#!/usr/bin/env python
# coding: utf-8

# ### TASK 4 - HANGMAN GAME

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *Word List: Create a list of words for the game.
# #### *Random Word: Select a random word from the list.
# #### *Initial Display: Show empty hangman figure and underscores for unguessed letters.
# #### *User Input: Prompt the user for a letter guess.
# #### *Check Letter: Validate the guess and check if it's in the word.
# #### *Update State: Reveal correctly guessed letters in the word.
# #### *Hangman Display: Display hangman figure for incorrect guesses.
# #### *Win/Loss Check: Determine win or loss conditions.
# #### *Play Again: Ask if the player wants to play another round.
# #### *User Interface: Design a clear interface showing hangman figure, word state, and feedback.

# ##### Step 1: Import Required Libraries

# ##### Step 2: Create a Word List

# ##### Step 3: Define the Hangman Stages

# ##### Step 4: Define the Game Function

# ##### Step 5: Play Again

# ##### Step 6: Main Game Loop

# In[1]:


import random

# Word list
word_list = ["python", "developer", "machine", "learning", "hangman", "analytics", "data"]

# Hangman stages
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Game function
def play_hangman():
    word = random.choice(word_list)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 0

    word_display = ["_" for _ in word]

    print("Welcome to Hangman!")
    print(hangman_stages[attempts])
    print(" ".join(word_display))

    while attempts < len(hangman_stages) - 1:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            print(f"Good guess! '{guess}' is in the word.")
            word_letters.remove(guess)

            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = letter
        else:
            print(f"'{guess}' is not in the word.")
            attempts += 1

        print(hangman_stages[attempts])
        print(" ".join(word_display))

        if "_" not in word_display:
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Sorry, you lost. The word was:", word)

def play_again():
    choice = input("Do you want to play another round? (yes/no): ").lower()
    return choice == "yes"

def main():
    while True:
        play_hangman()
        if not play_again():
            print("Thank you for playing Hangman!")
            break

# Run the game
if __name__ == "__main__":
    main()

