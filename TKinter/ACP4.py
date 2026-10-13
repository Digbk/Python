import tkinter as tk
import random

def play(choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if choice == computer_choice:
        result = (f"Both chose {choice}. It's a tie!")
    elif (choice == 'Rock' and computer_choice == 'Scissors') or \
         (choice == 'Paper' and computer_choice == 'Rock') or \
         (choice == 'Scissors' and computer_choice == 'Paper'):
        result = (f"You chose {choice}. Computer chose {computer_choice}. You win!")
    else:
        result = (f"You chose {choice}. Computer chose {computer_choice}. You lose!")
        