class BankAccount:
    # Class variable
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest. New balance is {self.balance}.")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Creating two instances of BankAccount
account1 = BankAccount("masai")
account2 = BankAccount("abusolom")

# Performing deposits and withdrawals
account1.deposit(2000)
account1.withdraw(100)
account2.deposit(3500)
account2.withdraw(2500)

 Applying interest
account1.apply_interest()
account2.apply_interest()

 Displaying account information
account1.display_account_info()
account2.display_account_info()
