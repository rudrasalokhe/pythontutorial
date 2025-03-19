class MobileRecharge:
    def __init__(self, phoneNo, balance):
        self.phoneNo = phoneNo
        self.balance = balance
    
    def recharge(self, amount):
        self.balance += amount
        print(f'Recharge successful. Available balance is {self.balance}')
    
    def make_call(self, cost):
        if cost > self.balance:
            print("Insufficient balance. Please recharge.")
        else:
            self.balance -= cost
            print(f"Call made. Remaining balance is {self.balance}")
    
    def balance_personal(self):
        print("Available balance is:", self.balance)

call = MobileRecharge("8103022232", 700)

call.make_call(400)  
