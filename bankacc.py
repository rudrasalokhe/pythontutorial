class bankacc:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_balance(self):
        print(f"The total balance in your account is: {self.balance}")

object = bankacc("Rudra", 19)
object.withdraw(2)
object.display_balance()