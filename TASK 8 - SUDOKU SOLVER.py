#!/usr/bin/env python
# coding: utf-8

# ### TASK 8 - SUDOKU SOLVER

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *The Sudoku Solver Python project is focused on implementing an algorithm to solve Sudoku puzzles. 
# #### *Utilizing backtracking or other solving techniques, the program takes an incomplete Sudoku grid as input and outputs the completed solution. 
# #### *This project hones skills in algorithmic problem-solving and array manipulation. Additionally, it demonstrates the practical application of Python in solving complex puzzles efficiently, offering users a tool to tackle and solve Sudoku challenges programmatically.

# ##### Step 1: Define the Sudoku Board

# ##### Step 2: Create Functions for Solving

# In[1]:


def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    """Finds an empty cell in the Sudoku board (represented by 0).
    
    Returns the row and column of the empty cell, or None if there are no empty cells.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 represents an empty cell
                return (i, j)  # row, col
    return None

def is_valid(board, guess, row, col):
    """Checks if a guessed number can be placed at the given position on the board."""
    # Check the row
    if guess in board[row]:
        return False

    # Check the column
    for r in range(9):
        if board[r][col] == guess:
            return False

    # Check the 3x3 grid
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == guess:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for guess in range(1, 10):  # Guess numbers 1 to 9
        if is_valid(board, guess, row, col):
            board[row][col] = guess  # Place the guess

            if solve_sudoku(board):  # Recursively try to solve with this guess
                return True

            board[row][col] = 0  # Reset the guess (backtrack)

    return False  # Trigger backtracking

# Example Sudoku board (0s represent empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the original Sudoku board
print("Original Sudoku Board:")
print_board(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("No solution exists.")

