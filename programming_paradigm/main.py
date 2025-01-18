
from bank_account import *
from robust_division_calculator import *
#task 0
my_account=BankAccount(1000)
my_account.deposit(500)
my_account.display_balance()
my_account.withdraw(1600)
my_account.display_balance()
#task 1
print(safe_divide(5,1))
print(safe_divide(5,0))
print(safe_divide(5,"a"))