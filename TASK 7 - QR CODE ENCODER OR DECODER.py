#!/usr/bin/env python
# coding: utf-8

# ### TASK 7 - QR CODE ENCODER/DECODER

# ##### Submitted by Nikhitha Elezebeth Baby

# #### *The QR Code Encoder/Decoder Python project involves creating a tool to generate QR codes for information like URLs or texts and decoding QR codes to retrieve the embedded data. 
# #### *Utilizing libraries like qrcode and opencv-python, this project enhances practical skills in image processing and data encoding. 
# #### *It's a versatile project with applications in various fields, including marketing, logistics, and information sharing, showcasing the power of Python in data representation and extraction through QR codes.

# ##### Step 1: Install Required Libraries

# ##### Step 2: Create the QR Code Encoder

# ##### Step 3: Create the QR Code Decoder

# In[1]:


pip install qrcode[pil] opencv-python pillow


# In[7]:


# Import necessary libraries
import qrcode
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to generate a QR code
def generate_qr():
    """Generates a QR code from user input text."""
    input_text = qr_input.get()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to generate a QR code.")
        return

    # Create and save the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(input_text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated QR code
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("QR Code Generated", f"QR code saved as {file_path}")

# Function to decode a QR code from an image file
def decode_qr():
    """Decodes data from a selected QR code image file."""
    file_path = filedialog.askopenfilename(title="Select QR code image", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    # Read the image and attempt to decode
    img = cv2.imread(file_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        messagebox.showinfo("Decoded Data", f"Decoded data: {data}")
    else:
        messagebox.showwarning("Error", "No QR code found in the image.")

# Setting up the GUI window
root = tk.Tk()
root.title("QR Code Encoder/Decoder")
root.geometry("400x300")

# Label and Entry for QR Code input
tk.Label(root, text="Enter text to generate QR code:").pack(pady=10)
qr_input = tk.Entry(root, width=40)
qr_input.pack(pady=5)

# Buttons for generating and decoding QR codes
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

decode_button = tk.Button(root, text="Decode QR Code", command=decode_qr)
decode_button.pack(pady=10)

# Run the GUI main loop
root.mainloop()

