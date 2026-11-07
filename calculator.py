# CodeOrbit Tech - Simple Calculator

try:
    print("Welcome to Simple Calculator!")

    # Get input from user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Select operation
    print("\nChoose operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")

    choice = input("Enter your choice: ")

    # Perform calculation
    if choice == "+":
        print("Result:", a + b)

    elif choice == "-":
        print("Result:", a - b)

    elif choice == "*":
        print("Result:", a * b)

    elif choice == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid operation!")

except ValueError:
    print("Please enter valid numbers!")