#!/usr/bin/env python
# coding: utf-8

# ### TASK 1 - CALCULATOR APP

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *Design a simple calculator with basic arithmetic operations.
# #### *Prompt the user to input two numbers and an operation choice.
# #### *Perform the calculation and display the result.

# ##### Step 1: Define Functions for Arithmetic Operations

# ##### Step 2: Display Options and Get User Input

# ##### Step 3: Perform the Calculation

# ##### Step 4: Display the Result

# ##### Step 5: Main Function to Run the Calculator

# In[1]:


# Import necessary modules
import math

# Define arithmetic operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return x / y

# Function to get user input
def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        operation = input("Enter the operation (+, -, *, /): ")
        
        return num1, num2, operation
    except ValueError:
        print("Invalid input! Please enter numerical values for numbers.")
        return None, None, None

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        print("Invalid operation! Please choose one of the following: +, -, *, /")
        return None

# Function to display the result
def display_result(result):
    if result is not None:
        print("\nThe result is:", result)

# Main function to run the calculator app
def main():
    print("Welcome to the Simple Calculator App!")
    
    num1, num2, operation = get_user_input()
    
    if num1 is None or num2 is None or operation is None:
        print("Calculation aborted due to invalid input.")
        return
    
    result = calculate(num1, num2, operation)
    
    display_result(result)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

