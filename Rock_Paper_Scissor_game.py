import tkinter as tk
from tkinter import messagebox
import random

def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1

    return 1

def play_game():
    user = user_choice.get()

    if user != "":
        user = int(user)

        comp = random.randint(0, 2)

        score = check(comp, user)

        user_label.config(text="You: " + choices[user])
        comp_label.config(text="Computer: " + choices[comp])

        if score == 0:
            result_label.config(text="It's a draw")
        elif score == -1:
            result_label.config(text="Sorry! You Lose")
            computer_score[0] += 1
        else:
            result_label.config(text="Congratulation! You Won")
            user_score[0] += 1

        user_score_label.config(text="Your Score: " + str(user_score[0]))
        comp_score_label.config(text="Computer Score: " + str(computer_score[0]))

    else:
        messagebox.showwarning("Warning", "Please select an option.")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

choices = ["Rock", "Paper", "Scissors"]

user_label = tk.Label(root, text="You:", font=("Times New Roman", 16))
comp_label = tk.Label(root, text="Computer:", font=("Times New Roman", 16))
result_label = tk.Label(root, text="", font=("Times New Roman", 16, "bold"))

user_choice = tk.StringVar()

rock_radio = tk.Radiobutton(root, text="Rock", variable=user_choice, value=0, font=("Times New Roman", 12))
paper_radio = tk.Radiobutton(root, text="Paper", variable=user_choice, value=1, font=("Times New Roman", 12))
scissors_radio = tk.Radiobutton(root, text="Scissors", variable=user_choice, value=2, font=("Times New Roman", 12))

play_button = tk.Button(root, text="Play", command=play_game, font=("Times New Roman", 16, "bold"), bg="#4CAF50", fg="white")

user_score = [0]
computer_score = [0]
user_score_label = tk.Label(root, text="Your Score: 0", font=("Times New Roman", 12))
comp_score_label = tk.Label(root, text="Computer Score: 0", font=("Times New Roman", 12))

user_label.grid(row=0, column=0, pady=(15,5), padx=10)
comp_label.grid(row=1, column=0, pady=5, padx=10)
result_label.grid(row=2, column=0, pady=15, padx=10)

rock_radio.grid(row=3, column=0, pady=5, padx=10)
paper_radio.grid(row=4, column=0, pady=5, padx=10)
scissors_radio.grid(row=5, column=0, pady=(5,15), padx=10)

play_button.grid(row=6, column=0, pady=5, padx=10)

user_score_label.grid(row=7, column=0, pady=5, padx=10)
comp_score_label.grid(row=8, column=0, pady=5, padx=10)

medium_width = 800
medium_height = 600
x = (root.winfo_screenwidth() // 2) - (medium_width // 2)
y = (root.winfo_screenheight() // 2) - (medium_height // 2)
root.geometry('{}x{}+{}+{}'.format(medium_width, medium_height, x, y))

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
