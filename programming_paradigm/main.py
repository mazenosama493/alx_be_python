
from bank_account import *
from robust_division_calculator import *

my_account=BankAccount(1000)
my_account.deposit(500)
my_account.display_balance()
my_account.withdraw(1600)
my_account.display_balance()

print(safe_divide(5,1))