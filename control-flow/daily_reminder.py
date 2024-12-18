task=str(input("Enter your task:"))
Priority=str(input("Priority (high/medium/low):"))
time_bound=str(input("Is it time-bound? (yes/no):"))
match Priority:
    case "high":
        priority="high"
    case "medium":
        priority="medium"
    case "low":
        priority="low"
if time_bound=="yes":
    print(f"Reminder: '{task}' is a {Priority} priority task that requires immediate attention today!")
elif time_bound=="no":
    print(f"Note: '{task}' is a {Priority} priority task. Consider completing it when you have free time.")





