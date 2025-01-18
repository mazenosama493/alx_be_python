def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {numerator/denominator}")