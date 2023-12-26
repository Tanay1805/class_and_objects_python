class Bank:
    def __init__(self):
        self.bankdetails = {}

    def bankac(self):
        self.bankacc = input("Enter your bank acc no:")
        self.bankpin = input("Enter your bank pin:")
        
        if self.bankacc in self.bankdetails:
            entered_pin = input("Enter your bank pin:")
            if entered_pin == self.bankdetails[self.bankacc]:
                print("Welcome to the bank")
            else:
                print("Incorrect Bank Pin")
                return False
        else:
           
            self.bankdetails[self.bankacc] = self.bankpin
            print("Account created. Welcome to the bank")
            return True

    def banking(self):
        self.balance = 0
        if not self.bankdetails:
            print("No accounts available. Please create an account first.")
            return

        while True:
            print("1. Deposit\n2. Withdraw\n3. Balance\n4. Logout")
            option = int(input("Enter your choice:"))

            if option == 1:
                deposit = float(input("Enter the money you want to add:"))
                self.balance += deposit
                print("Deposit successful. Current balance:", self.balance)
            elif option == 2:
                withdraw = float(input("Enter the amount you want to withdraw:"))
                if withdraw > self.balance:
                    print("You don't have sufficient balance in the account")
                else:
                    self.balance -= withdraw
                    print("Withdrawal successful. Current balance:", self.balance)
            elif option == 3:
                print("Current balance:", self.balance)
            elif option == 4:
                print("Thank you for banking with us")
                break
            else:
                print("Invalid choice. Please re-enter.")

bank_1 = Bank()
if bank_1.bankac():
    bank_1.banking()
