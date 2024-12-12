a=int(input("Enter your monthly income: "))
b=int(input("Enter your total monthly expenses: "))
print(f"Your monthly savings are ${(a-b)}")
print(f"Projected savings after one year, with interest, is: ${int((a-b)*12+((a-b)*12*0.05))}.")