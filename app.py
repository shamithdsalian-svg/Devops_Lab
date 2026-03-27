def format_result(result):
    """Remove .0 if result is whole number"""
    return int(result) if isinstance(result, float) and result.is_integer() else result


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


# 🔥 Load history from file
history = []

try:
    with open("history.txt", "r") as file:
        for line in file:
            history.append(line.strip())
except FileNotFoundError:
    pass


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

    # 🔥 Show history (improved)
    if choice == '5':
        if not history:
            print("History is empty.")
        else:
            print("\n--- History ---")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
        continue

    # 🔥 Clear history
    if choice == '6':
        history.clear()
        with open("history.txt", "w") as file:
            pass
        print("History cleared!")
        continue

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please try again.")
        continue

    # 🔥 Input validation
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    # 🔥 Perform operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    # 🔥 Format result
    if isinstance(result, (int, float)):
        result = format_result(result)

    print("Result:", result)

    # 🔥 Save to history
    history.append(str(result))

    # 🔥 Save to file
    with open("history.txt", "a") as file:
        file.write(str(result) + "\n")