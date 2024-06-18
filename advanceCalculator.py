import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return math.pow(x, y)

def factorial(x):
    if x < 0:
        return "Error! Factorial is not defined for negative numbers."
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

def logarithm(x, base=10):
    if x <= 0:
        return "Error! Logarithm is not defined for non-positive numbers."
    else:
        return math.log(x, base)

def display_menu():
    print("Advanced Calculator Menu (7 Functions):")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Factorial")
    print("7. Logarithm")
    print("8. Exit")
    choice = input("Enter your choice : ")
    return choice

def calculator():
    while True:
        choice = display_menu()
        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice in ('7'):  # Handle single-operand function (logarithm)
            num2 = None
        else:
            try:
                num2 = float(input("Enter the second number (or press Enter for single-operand functions): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            print("Result:", factorial(int(num1)))
        elif choice == '7':
            print("Result:", logarithm(num1, num2))

calculator()