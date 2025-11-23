import customtkinter as ctk
import string
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def generate_passwords():
    output.delete("0.0", "end")
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())
    except:
        output.insert("end", "Invalid input")
        return

    strength = strength_var.get()
    if strength == "Easy":
        chars = string.ascii_lowercase
    elif strength == "Medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    for _ in range(count):
        password = "".join(random.choice(chars) for _ in range(length))
        output.insert("end", password + "\n")

app = ctk.CTk()
app.title("Modern Password Generator")
app.geometry("450x600")

title = ctk.CTkLabel(app, text="Password Generator", font=("Arial", 28, "bold"))
title.pack(pady=20)

length_label = ctk.CTkLabel(app, text="Password Length:", font=("Arial", 15))
length_label.pack()
length_entry = ctk.CTkEntry(app, width=120, height=40, font=("Arial", 15))
length_entry.pack(pady=5)

count_label = ctk.CTkLabel(app, text="Number of Passwords:", font=("Arial", 15))
count_label.pack()
count_entry = ctk.CTkEntry(app, width=120, height=40, font=("Arial", 15))
count_entry.pack(pady=5)

strength_label = ctk.CTkLabel(app, text="Strength:", font=("Arial", 15))
strength_label.pack(pady=10)

strength_var = ctk.StringVar(value="Strong")
strength_frame = ctk.CTkFrame(app)
strength_frame.pack()

easy_btn = ctk.CTkRadioButton(strength_frame, text="Easy", variable=strength_var, value="Easy")
easy_btn.grid(row=0, column=0, padx=10)

medium_btn = ctk.CTkRadioButton(strength_frame, text="Medium", variable=strength_var, value="Medium")
medium_btn.grid(row=0, column=1, padx=10)

strong_btn = ctk.CTkRadioButton(strength_frame, text="Strong", variable=strength_var, value="Strong")
strong_btn.grid(row=0, column=2, padx=10)

generate_btn = ctk.CTkButton(app, text="Generate Passwords", height=45, width=200, command=generate_passwords)
generate_btn.pack(pady=20)

output = ctk.CTkTextbox(app, width=350, height=250, font=("Arial", 15))
output.pack(pady=10)

app.mainloop()
