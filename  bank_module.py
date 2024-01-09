# bank_module.py

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return f"Balance for {self.account_holder}'s account: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal unsuccessful."
