class Account:
    def __init__(self, account_number, account_holder):
        # Initialize a new account with an account number and holder's name
        # Set initial balance to 0
        self.account_no = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        # Deposit a positive amount into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Your new balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw a positive amount from the account if sufficient funds are available
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is ${self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Print the current balance of the account
        print(f"Your current balance is ${self.balance:.2f}.")
