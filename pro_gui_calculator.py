import tkinter as tk


# 🎨 Colors (Dark Theme)
BG_COLOR = "#1e1e1e"
BTN_COLOR = "#2d2d2d"
TEXT_COLOR = "white"
ENTRY_COLOR = "#3c3f41"


# 📌 Utility
def format_result(result):
    return int(result) if isinstance(result, float) and result.is_integer() else result


# 🔒 Safe evaluation
def safe_eval(expression):
    allowed = "0123456789+-*/.() "
    if all(char in allowed for char in expression):
        return eval(expression)
    else:
        raise ValueError("Invalid expression")


# 📂 File Handling
def load_history():
    history = []
    try:
        with open("history.txt", "r") as file:
            for line in file:
                history.append(line.strip())
    except FileNotFoundError:
        pass
    return history


def save_to_file(entry):
    with open("history.txt", "a") as file:
        file.write(entry + "\n")


def clear_file():
    open("history.txt", "w").close()


# 🖱️ Button Click
def click(value):
    entry.insert(tk.END, value)


# 🧹 Clear Entry
def clear():
    entry.delete(0, tk.END)


# ⚙️ Calculate
def calculate():
    try:
        expression = entry.get()
        result = safe_eval(expression)
        result = format_result(result)

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

        history_entry = f"{expression} = {result}"
        history_list.insert(tk.END, history_entry)
        save_to_file(history_entry)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# 🧹 Clear History
def clear_history():
    history_list.delete(0, tk.END)
    clear_file()


# ⌨️ Keyboard Support
def key_event(event):
    if event.char in "0123456789+-*/.":
        click(event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get()) - 1, tk.END)


# 🖥️ Window
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("350x550")
root.configure(bg=BG_COLOR)

root.bind("<Key>", key_event)


# 📟 Entry
entry = tk.Entry(root, font=("Arial", 20),
                 bg=ENTRY_COLOR, fg=TEXT_COLOR, bd=0)
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)


# 🔢 Buttons Frame
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(frame, text=button, font=("Arial", 14),
                        bg="#4CAF50", fg="white",
                        width=5, height=2, command=calculate)
    else:
        btn = tk.Button(frame, text=button, font=("Arial", 14),
                        bg=BTN_COLOR, fg=TEXT_COLOR,
                        width=5, height=2,
                        command=lambda b=button: click(b))

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1


# 🔧 Control Buttons
tk.Button(root, text="Clear", bg="#f44336", fg="white",
          command=clear).pack(fill=tk.BOTH, padx=10, pady=5)

tk.Button(root, text="Clear History", bg="#ff9800", fg="white",
          command=clear_history).pack(fill=tk.BOTH, padx=10, pady=5)


# 📜 History (Scrollable)
tk.Label(root, text="History", bg=BG_COLOR, fg="white").pack()

history_frame = tk.Frame(root)
history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

history_list = tk.Listbox(history_frame,
                          bg="#2d2d2d", fg="white",
                          yscrollcommand=scrollbar.set)

history_list.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=history_list.yview)


# 🔥 Load History
for item in load_history():
    history_list.insert(tk.END, item)


# ▶️ Run
root.mainloop()