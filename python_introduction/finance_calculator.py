
a = float(input("Enter your monthly income: "))
b = float(input("Enter your total monthly expenses: "))
monthly_savings= a - b
print(f"Your monthly savings are ${monthly_savings}")
projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
