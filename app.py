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


# 🔥 New: history list
history = []

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '6':
        print("Exiting...")
        break

    # 🔥 Show history
    if choice == '5':
        print("History:", history)
        continue

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    print("Result:", result)

    # 🔥 Store result in history
    history.append(result)