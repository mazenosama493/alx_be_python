num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
opr=(input("Choose the operation (+, -, *, /): "))
match opr:
    case "+":
        result=int(num1+num2)
        print(f"The result is {result}.")
    case "-":
        result=int(num1-num2)
        print(f"The result is {result}.")
    case "*":
        result=int(num1*num2)
        print(f"The result is {result}.")
    case "/":
        match num2:
            case 0:
                print("Cannot divide by zero.")
            case _:
                result=float(num1/num2)
                print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")