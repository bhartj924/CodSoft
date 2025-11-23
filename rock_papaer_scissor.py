import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_choice_label.configure(text=f"Your Choice: {user_choice}")
    computer_choice_label.configure(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.configure(text="Result: It's a Tie")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.configure(text="Result: You Win")
        user_score += 1
    else:
        result_label.configure(text="Result: You Lose")
        computer_score += 1

    score_label.configure(text=f"Score  You: {user_score}  |  Computer: {computer_score}")

def reset_game():
    user_choice_label.configure(text="Your Choice: ")
    computer_choice_label.configure(text="Computer Choice: ")
    result_label.configure(text="Result: ")
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.configure(text="Score  You: 0  |  Computer: 0")

app = ctk.CTk()
app.title("Rock Paper Scissors")
app.geometry("450x600")

title_label = ctk.CTkLabel(app, text="Rock - Paper - Scissors", font=("Arial", 28, "bold"))
title_label.pack(pady=20)

user_choice_label = ctk.CTkLabel(app, text="Your Choice: ", font=("Arial", 18))
user_choice_label.pack(pady=10)

computer_choice_label = ctk.CTkLabel(app, text="Computer Choice: ", font=("Arial", 18))
computer_choice_label.pack(pady=10)

result_label = ctk.CTkLabel(app, text="Result: ", font=("Arial", 20, "bold"))
result_label.pack(pady=15)

score_label = ctk.CTkLabel(app, text="Score  You: 0  |  Computer: 0", font=("Arial", 18))
score_label.pack(pady=10)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

rock_btn = ctk.CTkButton(button_frame, text="Rock", width=120, height=50,
                         command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = ctk.CTkButton(button_frame, text="Paper", width=120, height=50,
                          command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = ctk.CTkButton(button_frame, text="Scissors", width=120, height=50,
                             command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = ctk.CTkButton(app, text="Play Again (Reset Score)", width=200, height=45,
                          command=reset_game)
reset_btn.pack(pady=20)

app.mainloop()
