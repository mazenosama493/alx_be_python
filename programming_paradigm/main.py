
from bank_account import *
from robust_division_calculator import *
from library_management import *
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
#task 3
library=Library()
library.add_book("The Great Gatsby","F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird","Harper Lee")
library.add_book("Pride and Prejudice","Jane Austen")
library.list_available_books()
library.check_out_book("The Great Gatsby")
library.list_available_books()
library.return_book("The Great Gatsby")
library.list_available_books()
