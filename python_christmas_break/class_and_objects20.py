class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

class Transaction:
    def __init__(self, account, transaction_type, amount):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class ATMSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, pin, balance, user):
        if account_number not in self.accounts:
            account = Account(account_number, pin, balance)
            self.accounts[account_number] = {'account': account, 'user': user}
            print(f"Account {account_number} added successfully for {user.name}.")
        else:
            print(f"Account {account_number} already exists in the system.")

    def authenticate_user(self, account_number, entered_pin):
        if account_number in self.accounts:
            account = self.accounts[account_number]['account']
            return account.check_pin(entered_pin)
        else:
            return False

    def perform_transaction(self, account_number, transaction_type, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]['account']
            user = self.accounts[account_number]['user']
            transaction = Transaction(account, transaction_type, amount)

            if transaction_type == 'withdraw':
                if account.withdraw_cash(amount):
                    print(f"Withdrawal of ${amount} successful for {user.name}. New balance: ${account.check_balance()}.")
                    return transaction
                else:
                    print(f"Withdrawal failed for {user.name}. Insufficient funds or invalid amount.")
                    return None

            elif transaction_type == 'check_balance':
                print(f"Balance check for {user.name}. Current balance: ${account.check_balance()}.")
                return transaction

        else:
            print("Account not found. Please check the account number.")
            return None

# Example Usage:
atm_system = ATMSystem()

user1 = User(1, "John Doe")
atm_system.add_account("123456789", "1234", 1000, user1)

account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")

if atm_system.authenticate_user(account_number, pin):
    while True:
        print("\n1. Withdraw Cash\n2. Check Balance\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the amount to withdraw: "))
            atm_system.perform_transaction(account_number, 'withdraw', amount)
        elif choice == '2':
            atm_system.perform_transaction(account_number, 'check_balance', 0)
        elif choice == '3':
            break
        else:
            print("Invalid Choice. Please enter a valid option.")
else:
    print("Authentication failed. Please check your account number and PIN.")
