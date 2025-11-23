import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def click(text):
    global last_was_equal
    if text == "=":
        try:
            expression = display_var.get().lstrip("0") or "0"
            value = eval(expression)
            display_var.set(str(value))
            last_was_equal = True
        except:
            display_var.set("Error")
            last_was_equal = True

    elif text == "C":
        display_var.set("")
        last_was_equal = False

    else:
        if last_was_equal:
            if text.isdigit() or text == ".":
                display_var.set(text)
            else:
                display_var.set(display_var.get() + text)
            last_was_equal = False
        else:
            display_var.set(display_var.get() + text)

app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("420x600")

display_var = ctk.StringVar(value="")
last_was_equal = False

display = ctk.CTkEntry(app, textvariable=display_var, font=("Arial", 32),
                       height=80, justify="right")
display.pack(padx=20, pady=20, fill="x")

buttons = [
    ['9', '8', '7'],
    ['6', '5', '4'],
    ['3', '2', '1'],
    ['+', '-', '*'],
    ['%', '/', '='],
    ['C', '0', None]
]

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=10)

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        if text is None:
            continue
        btn = ctk.CTkButton(frame, text=text, font=("Arial", 22, "bold"),
                            width=100, height=70,
                            command=lambda t=text: click(t))
        btn.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")

for i in range(7):
    frame.rowconfigure(i, weight=1)
for j in range(3):
    frame.columnconfigure(j, weight=1)

app.mainloop()
