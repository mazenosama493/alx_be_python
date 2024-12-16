num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
    # Get user input for the operation
operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation based on the operation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
            # Handle division by zero
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from (+, -, *, /).")