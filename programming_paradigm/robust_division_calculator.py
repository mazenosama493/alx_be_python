def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        result=numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        print(f"Result is {result}")