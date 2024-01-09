
from  bank_module import BankAccount

# Create a bank account
account_holder_name = input("Enter the account holder's name: ")
initial_balance = float(input("Enter the initial balance: "))

account = BankAccount(account_holder_name, initial_balance)

# Perform operations
print(account.check_balance())

deposit_amount = float(input("Enter the deposit amount: "))
print(account.deposit(deposit_amount))

withdraw_amount = float(input("Enter the withdrawal amount: "))
print(account.withdraw(withdraw_amount))

# Display the final balance
print(account.check_balance())
