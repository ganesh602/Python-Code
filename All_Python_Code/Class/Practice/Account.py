class MinimumBalanceError(Exception):
    pass

class Account:
    AccountNumber = 100 
    def __init__(self,name,balance = 1000):
        if balance < 1000:
            raise MinimumBalanceError("Minimum Balance required is 1000, but you are providing ",balance)    
        self.name = name
        Account.AccountNumber += 1
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError('Minimum Balance should be 1000')
        self.balance = self.balance - amount
    
    def show_Details(self):
        print("Account No.  : ",Account.AccountNumber)
        print("Account Name : ",self.name)
        print("Account Balance : ",self.balance)
    
a = Account('John',2000)
a.deposit(1500)
try:
    a.withdraw(5500)
except MinimumBalanceError as min:
    print(min)
a.show_Details()
print('')
a = Account('Ajay',3000)
a.show_Details()