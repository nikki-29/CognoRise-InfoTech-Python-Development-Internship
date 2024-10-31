#!/usr/bin/env python
# coding: utf-8

# ### TASK 2 - PASSWORD GENERATOR

# ##### Submitted by Nikhitha Elezebeth Baby

# #### A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing user to specify the length and complexity of the password.
# #### User Input: Prompt the user to specify the desired length of the password.
# #### Generate Password: Use a combination of random characters to generate a password of the specified length.
# #### Display the Password: Print the generated password on the screen.
# 

# ##### Step 1: Import Libraries

# ##### Step 2: Define the Password Generator Function

# ##### Step 3: Validate Password Length

# ##### Step 4: Generate the Password

# ##### Step 5: Main Function for User Interaction

# ##### Step 6: Run the Program

# In[10]:


# Import the required libraries
import random
import string

def generate_password(length):
    """
    Generates a random password based on the specified length.
    
    Parameters:
        length (int): The desired length of the password.
        
    Returns:
        str: The generated password.
    """
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    # Ensure the password is of a secure length
    if length < 6:
        print("Warning: It is recommended to have a password with at least 6 characters for security.")
        return None
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    """
    Main function to handle user interaction and display the generated password.
    """
    print("Welcome to the Password Generator!")
    
    # Prompt the user for the password length
    try:
        length = int(input("Enter the desired password length (e.g., 8, 12, 16): "))
    except ValueError:
        print("Invalid input! Please enter a numerical value for the length.")
        return
    
    # Generate the password and display it
    password = generate_password(length)
    
    if password:
        print("\nGenerated Password:")
        print(password)
    else:
        print("Password generation failed due to insufficient length.")

if __name__ == "__main__":
    main()

