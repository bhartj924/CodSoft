import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

contacts = []

def refresh_list():
    listbox.delete("0.0", "end")
    for c in contacts:
        listbox.insert("end", f"{c['name']} - {c['phone']}\n")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        refresh_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and Phone required")

def clear_entries():
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")

def search_contact():
    q = search_entry.get().lower()
    listbox.delete("0.0", "end")
    for c in contacts:
        if q in c["name"].lower() or q in c["phone"]:
            listbox.insert("end", f"{c['name']} - {c['phone']}\n")

def get_selected_index():
    try:
        cursor = listbox.index("insert")
        line = int(cursor.split(".")[0]) - 1
        return line
    except:
        return None

def load_contact_for_update():
    idx = get_selected_index()
    if idx is None or idx >= len(contacts):
        messagebox.showwarning("Warning", "Select a contact")
        return

    c = contacts[idx]
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")

    name_entry.insert("end", c["name"])
    phone_entry.insert("end", c["phone"])
    email_entry.insert("end", c["email"])
    address_entry.insert("end", c["address"])

def update_contact():
    idx = get_selected_index()
    if idx is None or idx >= len(contacts):
        messagebox.showwarning("Warning", "Select a contact")
        return

    contacts[idx]["name"] = name_entry.get()
    contacts[idx]["phone"] = phone_entry.get()
    contacts[idx]["email"] = email_entry.get()
    contacts[idx]["address"] = address_entry.get()
    refresh_list()
    clear_entries()

def delete_contact():
    idx = get_selected_index()
    if idx is None or idx >= len(contacts):
        messagebox.showwarning("Warning", "Select a contact")
        return

    contacts.pop(idx)
    refresh_list()

app = ctk.CTk()
app.title("Modern Contact Book")
app.geometry("700x600")

title = ctk.CTkLabel(app, text="Contact Book", font=("Arial", 30, "bold"))
title.pack(pady=15)

form = ctk.CTkFrame(app)
form.pack(pady=10)

ctk.CTkLabel(form, text="Name:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=8)
name_entry = ctk.CTkEntry(form, width=250, height=40)
name_entry.grid(row=0, column=1, padx=10)

ctk.CTkLabel(form, text="Phone:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=8)
phone_entry = ctk.CTkEntry(form, width=250, height=40)
phone_entry.grid(row=1, column=1, padx=10)

ctk.CTkLabel(form, text="Email:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=8)
email_entry = ctk.CTkEntry(form, width=250, height=40)
email_entry.grid(row=2, column=1, padx=10)

ctk.CTkLabel(form, text="Address:", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=8)
address_entry = ctk.CTkEntry(form, width=250, height=40)
address_entry.grid(row=3, column=1, padx=10)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

add_btn = ctk.CTkButton(btn_frame, text="Add Contact", width=150, command=add_contact)
add_btn.grid(row=0, column=0, padx=10)

edit_btn = ctk.CTkButton(btn_frame, text="Edit Contact", width=150, command=load_contact_for_update)
edit_btn.grid(row=0, column=1, padx=10)

update_btn = ctk.CTkButton(btn_frame, text="Save Update", width=150, command=update_contact)
update_btn.grid(row=0, column=2, padx=10)

delete_btn = ctk.CTkButton(btn_frame, text="Delete Contact", width=150, fg_color="red", command=delete_contact)
delete_btn.grid(row=0, column=3, padx=10)

search_frame = ctk.CTkFrame(app)
search_frame.pack(pady=5)

ctk.CTkLabel(search_frame, text="Search:", font=("Arial", 14)).grid(row=0, column=0, padx=10)
search_entry = ctk.CTkEntry(search_frame, width=200, height=40)
search_entry.grid(row=0, column=1, padx=10)

search_btn = ctk.CTkButton(search_frame, text="Search", width=120, command=search_contact)
search_btn.grid(row=0, column=2, padx=10)

listbox = ctk.CTkTextbox(app, width=550, height=250, font=("Arial", 16))
listbox.pack(pady=20)

refresh_list()

app.mainloop()
