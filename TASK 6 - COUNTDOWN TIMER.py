#!/usr/bin/env python
# coding: utf-8

# ### TASK 6 - COUNTDOWN TIMER

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *The Countdown Timer Python project is designed to create a user-friendly timer application that counts down from a specified time. 
# #### *Utilizing libraries like tkinter for the graphical user interface and time for time-related functions, this project enhances skills in event handling and time management. Users can set custom countdown durations, making it a versatile tool for tasks like cooking, productivity sprints, or workout sessions. 
# #### *This project showcases practical application of Python in creating interactive and functional desktop tools.

# ##### Step 1: Import Required Libraries

# ##### Step 2: Create the GUI

# ##### Step 3: Countdown Logic

# In[1]:


import tkinter as tk
import time

# Countdown Timer application class
class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        # Step 4: User Input Fields for Time
        self.label = tk.Label(root, text="Enter time in HH:MM:SS format", font=("Arial", 14))
        self.label.pack()

        self.time_input = tk.Entry(root, font=("Arial", 14))
        self.time_input.pack(pady=10)

        # Step 5: Timer Display
        self.timer_label = tk.Label(root, text="", font=("Arial", 48), fg="red")
        self.timer_label.pack(pady=20)

        # Step 6: Start and Stop Buttons
        self.start_button = tk.Button(root, text="Start Countdown", command=self.start_countdown, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop Countdown", command=self.stop_countdown, font=("Arial", 14))
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        # Initialize variables
        self.is_running = False
        self.remaining_time = 0

    # Step 7: Start Countdown Method
    def start_countdown(self):
        try:
            # Parse the input time
            hours, minutes, seconds = map(int, self.time_input.get().split(':'))
            self.remaining_time = hours * 3600 + minutes * 60 + seconds
            self.is_running = True
            self.update_timer()
        except ValueError:
            self.timer_label.config(text="Invalid Input! Use HH:MM:SS")

    # Step 8: Timer Update Method
    def update_timer(self):
        if self.is_running and self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            hours, mins = divmod(mins, 60)
            self.timer_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)  # Call update_timer every second
        elif self.remaining_time == 0:
            self.timer_label.config(text="Time's up!")
            self.is_running = False

    # Step 9: Stop Countdown Method
    def stop_countdown(self):
        self.is_running = False
        self.timer_label.config(text="")

# Step 10: Main Function to Run the Application
def main():
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.geometry("400x300")  # Set window size
    root.mainloop()  # Start the GUI event loop

# Run the program
if __name__ == "__main__":
    main()

