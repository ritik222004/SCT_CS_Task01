import tkinter as tk
from tkinter import messagebox

# Function to store data in a file
def save_to_file(mode, input_text, shift, result_text):
    with open("history.txt", "a") as file:
        file.write(f"{mode.upper()} | Input: {input_text} | Shift: {shift} | Output: {result_text}\n")

# Caesar Cipher Encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

# Decryption Function
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption = Negative Shift

# Function to process text (Encrypt/Decrypt)
def process_text(mode):
    text = entry_text.get()
    shift = shift_value.get()

    if not text:
        messagebox.showerror("Error", "Please enter a message!")
        return

    try:
        shift = int(shift)
        if mode == "encrypt":
            result = encrypt(text, shift)
            entry_text.delete(0, tk.END)  # Clear input field
            entry_text.insert(0, result)  # Set encrypted text in input field
        else:
            result = decrypt(text, shift)

        # Store data in file
        save_to_file(mode, text, shift, result)

        # Show result in GUI
        output_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer!")

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Encryption & Decryption")
root.geometry("400x350")

tk.Label(root, text="Enter Message:", font=("Arial", 12)).pack()
entry_text = tk.Entry(root, width=30)
entry_text.pack()

tk.Label(root, text="Enter Shift Value:", font=("Arial", 12)).pack()
shift_value = tk.Entry(root, width=10)
shift_value.pack()

tk.Button(root, text="Encrypt", command=lambda: process_text("encrypt"), bg="lightblue").pack(pady=5)
tk.Button(root, text="Decrypt", command=lambda: process_text("decrypt"), bg="lightgreen").pack(pady=5)

output_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
