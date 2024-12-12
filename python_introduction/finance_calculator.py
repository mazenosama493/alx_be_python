
a = int(input("Enter your monthly income: "))
b = int(input("Enter your total monthly expenses: "))
monthly_savings = a - b
print(f"Your monthly savings are ${monthly_savings}")
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
