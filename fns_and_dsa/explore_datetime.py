from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Formatted Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(f"Formatted Date and Time:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
if __name__ == "__main__":
    main()

