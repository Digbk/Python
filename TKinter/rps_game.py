import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0
ties = 0


def play(player):
    global player_score, computer_score, ties

    computer = random.choice(choices)

    player_choice.config(text="You: " + player)
    computer_choice.config(text="Computer: " + computer)

    if player == computer:
        result.config(text="It's a Tie!")
        ties += 1

    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        result.config(text="You Win!")
        player_score += 1

    else:
        result.config(text="Computer Wins!")
        computer_score += 1

    score.config(
        text="You: " + str(player_score) +
             "   Computer: " + str(computer_score) +
             "   Ties: " + str(ties)
    )


def reset():
    global player_score, computer_score, ties

    player_score = 0
    computer_score = 0
    ties = 0

    player_choice.config(text="You: -")
    computer_choice.config(text="Computer: -")
    result.config(text="Choose Rock, Paper or Scissors")

    score.config(text="You: 0   Computer: 0   Ties: 0")


# Window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("450x400")


# Title
title = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)


# Score
score = tk.Label(
    window,
    text="You: 0   Computer: 0   Ties: 0",
    font=("Arial", 12, "bold")
)
score.pack(pady=10)


# Choices
player_choice = tk.Label(
    window,
    text="You: -",
    font=("Arial", 15)
)
player_choice.pack(pady=5)


computer_choice = tk.Label(
    window,
    text="Computer: -",
    font=("Arial", 15)
)
computer_choice.pack(pady=5)


# Result
result = tk.Label(
    window,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 15, "bold")
)
result.pack(pady=20)


# Buttons
button_frame = tk.Frame(window)
button_frame.pack()

for choice in choices:
    button = tk.Button(
        button_frame,
        text=choice,
        width=10,
        command=lambda x=choice: play(x)
    )
    button.pack(side="left", padx=5)


# Reset button
reset_button = tk.Button(
    window,
    text="Reset Game",
    command=reset
)
reset_button.pack(pady=25)


window.mainloop()