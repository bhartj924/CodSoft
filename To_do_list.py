import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def add_task():
    task = entry.get()
    if task:
        listbox.insert("end", task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Enter a task")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Enter a task")
    except:
        messagebox.showwarning("Warning", "Select a task to update")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, "✔ " + task)
    except:
        messagebox.showwarning("Warning", "Select a task to mark done")

app = ctk.CTk()
app.title("To-Do List")
app.geometry("450x600")

title = ctk.CTkLabel(app, text="To-Do List", font=("Arial", 28, "bold"))
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=300, height=40, font=("Arial", 16))
entry.pack(pady=10)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

add_btn = ctk.CTkButton(button_frame, text="Add", width=100, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = ctk.CTkButton(button_frame, text="Update", width=100, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = ctk.CTkButton(button_frame, text="Delete", width=100, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

done_btn = ctk.CTkButton(app, text="Mark Done", width=150, command=mark_done)
done_btn.pack(pady=10)

listbox = ctk.CTkTextbox(app, width=350, height=300, font=("Arial", 16))
listbox.pack(pady=20)

def insert(self, index, text):
    listbox.insert("end", text + "\n")

def delete(self, index):
    lines = listbox.get("0.0", "end").strip().split("\n")
    if 0 <= index < len(lines):
        del lines[index]
        listbox.delete("0.0", "end")
        for line in lines:
            listbox.insert("end", line + "\n")

def get(self, index):
    lines = listbox.get("0.0", "end").strip().split("\n")
    return lines[index]

def curselection(self):
    try:
        index = int(listbox.index("insert").split(".")[0]) - 1
        return [index]
    except:
        return []

listbox.insert = insert.__get__(listbox)
listbox.delete = delete.__get__(listbox)
listbox.get = get.__get__(listbox)
listbox.curselection = curselection.__get__(listbox)

app.mainloop()
