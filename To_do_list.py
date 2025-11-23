import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

tasks = []
selected_index = None

def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()

    for i, text in enumerate(tasks):
        row = ctk.CTkFrame(list_frame, fg_color="#1f2937" if i != selected_index else "#3b82f6")
        row.pack(fill="x", pady=5, padx=10)

        label = ctk.CTkLabel(row, text=text, anchor="w", font=("Arial", 16))
        label.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        row.bind("<Button-1>", lambda e, x=i: select_task(x))
        label.bind("<Button-1>", lambda e, x=i: select_task(x))

def select_task(i):
    global selected_index
    selected_index = i
    refresh_list()

def add_task():
    text = entry.get().strip()
    if text:
        tasks.append(text)
        entry.delete(0, "end")
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def update_task():
    global selected_index
    if selected_index is None:
        messagebox.showwarning("Warning", "Select a task to update")
        return

    new_text = entry.get().strip()
    if not new_text:
        messagebox.showwarning("Warning", "Enter a task")
        return

    tasks[selected_index] = new_text
    entry.delete(0, "end")
    refresh_list()

def delete_task():
    global selected_index
    if selected_index is None:
        messagebox.showwarning("Warning", "Select a task to delete")
        return

    tasks.pop(selected_index)
    selected_index = None
    refresh_list()

def mark_done():
    global selected_index
    if selected_index is None:
        messagebox.showwarning("Warning", "Select a task")
        return

    if not tasks[selected_index].startswith("✔ "):
        tasks[selected_index] = "✔ " + tasks[selected_index]

    refresh_list()

app = ctk.CTk()
app.title("To-Do List")
app.geometry("450x600")

title = ctk.CTkLabel(app, text="To-Do List", font=("Arial", 28, "bold"))
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=300, height=40, font=("Arial", 16))
entry.pack(pady=10)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

ctk.CTkButton(button_frame, text="Add", width=100, command=add_task).grid(row=0, column=0, padx=5)
ctk.CTkButton(button_frame, text="Update", width=100, command=update_task).grid(row=0, column=1, padx=5)
ctk.CTkButton(button_frame, text="Delete", width=100, command=delete_task).grid(row=0, column=2, padx=5)

ctk.CTkButton(app, text="Mark Done", width=150, command=mark_done).pack(pady=10)

list_frame = ctk.CTkFrame(app)
list_frame.pack(fill="both", expand=True, pady=20, padx=10)

app.mainloop()
