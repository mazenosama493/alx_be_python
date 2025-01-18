def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        result=numerator/denominator
    except ZeroDivisionError:
        print("cannot div by zero")
    except ValueError:
        print("enter numeric values")
    else:
        print(f"Result is {result}")