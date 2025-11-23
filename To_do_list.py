import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Task:
    def __init__(self, text):
        self.text = text
        self.checked = ctk.BooleanVar()

tasks = []

def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()

    for idx, task in enumerate(tasks):
        frame = ctk.CTkFrame(list_frame)
        frame.pack(fill="x", pady=5)

        chk = ctk.CTkCheckBox(frame, text=task.text,
                              variable=task.checked, width=20)
        chk.pack(side="left", padx=10)

        edit_btn = ctk.CTkButton(frame, text="Edit", width=50,
                                 command=lambda i=idx: load_for_update(i))
        edit_btn.pack(side="right", padx=5)

        del_btn = ctk.CTkButton(frame, text="X", width=50, fg_color="red",
                                command=lambda i=idx: delete_task(i))
        del_btn.pack(side="right", padx=5)

def add_task():
    text = entry.get()
    if text.strip():
        tasks.append(Task(text))
        entry.delete(0, "end")
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def load_for_update(index):
    global update_index
    update_index = index
    entry.delete(0, "end")
    entry.insert(0, tasks[index].text)
    add_btn.configure(state="disabled")
    update_btn.configure(state="normal")

def update_task():
    text = entry.get()
    if text.strip():
        tasks[update_index].text = text
        entry.delete(0, "end")
        add_btn.configure(state="normal")
        update_btn.configure(state="disabled")
        refresh_list()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task(index):
    tasks.pop(index)
    refresh_list()

app = ctk.CTk()
app.title("To-Do List with Checkboxes")
app.geometry("500x650")

title = ctk.CTkLabel(app, text="To-Do List", font=("Arial", 28, "bold"))
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=350, height=40, font=("Arial", 16))
entry.pack(pady=10)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

add_btn = ctk.CTkButton(btn_frame, text="Add Task", width=120, command=add_task)
add_btn.grid(row=0, column=0, padx=10)

update_btn = ctk.CTkButton(btn_frame, text="Update Task", width=120,
                           command=update_task, state="disabled")
update_btn.grid(row=0, column=1, padx=10)

list_frame = ctk.CTkScrollableFrame(app, width=450, height=450)
list_frame.pack(pady=20, fill="both", expand=True)

update_index = None

app.mainloop()
