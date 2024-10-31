#!/usr/bin/env python
# coding: utf-8

# ### TASK 5 - DICE ROLLING SIMULATOR

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *Create a simple Python program that simulates rolling dice. Users can specify the number of sides on the dice and the number of rolls. 
# #### *The program generates random numbers for each roll and displays the results. 
# #### *It's a quick and fun way to emulate the experience of rolling dice, commonly used in board games or tabletop role-playing games. 
# #### *The simulator allows users to explore the outcomes of dice rolls without the physical dice.

# ##### Step 1: Import Required Libraries

# ##### Step 2: Define the Dice Rolling Function

# In[3]:


# Step 1: Import Required Libraries
import random

# Dice Rolling Simulator function
def roll_dice():
    # Step 3: User Input for Number of Sides on the Dice
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard dice): "))
            if num_sides < 2:
                print("Please enter a number greater than 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Step 4: User Input for Number of Rolls
    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Step 5: Perform Rolls and Display Results
    print(f"\nRolling a {num_sides}-sided dice {num_rolls} times:")
    roll_results = []
    
    for i in range(num_rolls):
        roll_result = random.randint(1, num_sides)  # Generate a random number between 1 and num_sides
        roll_results.append(roll_result)  # Append the result to the list of rolls
        print(f"Roll {i + 1}: {roll_result}")

    # Optional: Display Summary of Results
    print("\nSummary of Rolls:", roll_results)

# Main function to run the simulator
def main():
    while True:
        roll_dice()  # Call the dice rolling function
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for using the Dice Rolling Simulator!")
            break

# Run the program
if __name__ == "__main__":
    main()

