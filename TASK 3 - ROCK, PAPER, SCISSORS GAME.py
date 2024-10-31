#!/usr/bin/env python
# coding: utf-8

# ### TASK 3 - ROCK, PAPER, SCISSORS GAME

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *User Input: Prompt users to select rock, paper, or scissors.
# #### *Computer Selection: Randomly generate the computer's choice.
# #### *Game Logic: Determine the winner based on user and computer selections. Rock beats scissors, scissors beat paper, and paper beats rock.
# #### *Display Result: Present user and computer choices. Display outcomes: win, lose, or tie.
# #### *Score Tracking (Optional): Record user and computer scores for multiple rounds.
# #### *Play Again: Ask if users want another round.
# #### *User Interface: Design a user-friendly interface with clear instructions and feedback.

# ##### Step 1: Import Required Libraries

# ##### Step 2: Define the Options and Rules

# ##### Step 3: Define the Main Game Function

# ##### Step 4: Score Tracking

# ##### Step 5: Ask User to Play Again

# ##### Step 6: Display Final Scores

# ##### Step 7: Main Game Loop

# In[1]:


import random

# Define choices and game rules
choices = ["rock", "paper", "scissors"]
rules = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Define functions for each part of the game
def play_round():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        return None
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif rules[user_choice] == computer_choice:
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"

def update_scores(result, scores):
    if result == "win":
        scores["user"] += 1
    elif result == "lose":
        scores["computer"] += 1
    elif result == "tie":
        scores["ties"] += 1

def play_again():
    choice = input("Do you want to play another round? (yes/no): ").lower()
    return choice == "yes"

def display_scores(scores):
    print("\nFinal Scores:")
    print(f"You: {scores['user']}")
    print(f"Computer: {scores['computer']}")
    print(f"Ties: {scores['ties']}")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    scores = {"user": 0, "computer": 0, "ties": 0}
    
    while True:
        result = play_round()
        if result:
            update_scores(result, scores)
        
        if not play_again():
            break
    
    display_scores(scores)
    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    main()

