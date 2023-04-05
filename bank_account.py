class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
account1 = BankAccount(0.01, 100)
account2 = BankAccount(0.02, 200)

account1.deposit(30).deposit(10).deposit(20).withdraw(15).yield_interest().display_account_info()
account2.deposit(20).deposit(40).withdraw(15).withdraw(20).withdraw(30).withdraw(15).yield_interest().display_account_info()