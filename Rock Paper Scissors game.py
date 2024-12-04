import random
import tkinter as tk
from tkinter import messagebox

# Function to play the game
def play_game(user_choice):
    choices = ['Rock 🪨', 'Paper 📃', 'Scissors ✂️']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock 🪨' and computer_choice == 'Scissors ✂️') or \
         (user_choice == 'Paper 📃' and computer_choice == 'Rock 🪨') or \
         (user_choice == 'Scissors ✂️' and computer_choice == 'Paper 📃'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_message = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    messagebox.showinfo("Result", result_message)

# Set up
window = tk.Tk()
window.title("Rock Paper Scissors 🪨📃✂️")

# Label 
label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=('Arial', 14))
label.pack(pady=20)

# Buttons 
rock_button = tk.Button(window, text="Rock 🪨", width=10, command=lambda: play_game('Rock 🪨'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper 📃", width=10, command=lambda: play_game('Paper 📃'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors ✂️", width=10, command=lambda: play_game('Scissors ✂️'))
scissors_button.pack(pady=5)

# loop
window.mainloop()
