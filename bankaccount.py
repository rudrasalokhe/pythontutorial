class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_balance(self):
        print(f'The account balance is {self.balance}')
object = bankaccount("Rudra", 10000)
object.deposit(100)
object.display_balance()