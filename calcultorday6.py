import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x) if x >= 0 else "Error: Cannot take square root of a negative number"

def calculator():
    print("\n--- Text-Based Calculator ---")
    print("Operations: +, -, *, /, ** (exponent), sqrt (square root), exit")

    while True:
        operation = input("\nEnter operation: ").strip().lower()

        if operation == "exit":
            print("Goodbye!")
            break

        if operation == "sqrt":
            num = float(input("Enter number: "))
            print(f"√{num} = {square_root(num)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == "-":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == "*":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == "/":
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif operation == "**":
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
            else:
                print("Invalid operation! Try again.")

if __name__ == "__main__":
    calculator()
