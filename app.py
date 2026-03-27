# 📌 Utility Functions
def format_result(result):
    """Remove .0 if result is whole number"""
    return int(result) if isinstance(result, float) and result.is_integer() else result


def get_number(prompt):
    """Safe input for numbers"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# 📌 Calculator Operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# 📂 File Handling Functions
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


# 🔥 Load history
history = load_history()


# 🔄 Main Program Loop
while True:
    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Clear History")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '7':
        print("Exiting...")
        break

    # 📜 Show History
    if choice == '5':
        if not history:
            print("History is empty.")
        else:
            print("\n--- History ---")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
        continue

    # 🧹 Clear History
    if choice == '6':
        history.clear()
        clear_file()
        print("History cleared!")
        continue

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please try again.")
        continue

    # 🔢 Input Numbers
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    # ⚙️ Perform Operation
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"

    # 🎯 Format Result
    if isinstance(result, (int, float)):
        result = format_result(result)

    print("Result:", result)

    # 📝 Store Full Expression in History
    history_entry = f"{format_result(num1)} {operation} {format_result(num2)} = {result}"
    history.append(history_entry)

    # 💾 Save to File
    save_to_file(history_entry)