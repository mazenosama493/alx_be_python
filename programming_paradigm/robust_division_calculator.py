def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        result=numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("enter numeric values")
    else:
        print(f"Result is {result}")