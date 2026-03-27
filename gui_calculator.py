import tkinter as tk


# 📌 Utility Functions
def format_result(result):
    return int(result) if isinstance(result, float) and result.is_integer() else result


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


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
    with open("history.txt", "w") as file:
        pass


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

        # Evaluate safely
        result = eval(expression)
        result = format_result(result)

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

        # Save full expression
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


# 🖥️ Main Window
root = tk.Tk()
root.title("Professional Calculator")
root.geometry("400x550")


# 📟 Entry Display
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, padx=10, pady=10)


# 🔢 Buttons
frame = tk.Frame(root)
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
        btn = tk.Button(frame, text=button, font="Arial 14",
                        width=5, height=2, command=calculate)
    else:
        btn = tk.Button(frame, text=button, font="Arial 14",
                        width=5, height=2,
                        command=lambda b=button: click(b))

    btn.grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1


# 🔧 Control Buttons
tk.Button(root, text="Clear", command=clear).pack(fill=tk.BOTH, padx=10, pady=5)
tk.Button(root, text="Clear History", command=clear_history).pack(fill=tk.BOTH, padx=10, pady=5)


# 📜 History Panel
tk.Label(root, text="History", font="Arial 12").pack()

history_list = tk.Listbox(root)
history_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)


# 🔥 Load history on start
for item in load_history():
    history_list.insert(tk.END, item)


# ▶️ Run App
root.mainloop()