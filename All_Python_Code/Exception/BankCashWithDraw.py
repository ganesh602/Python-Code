InitialAmount = 10000
minimumAmount = 5000
class AccountBalanceException(Exception):
    pass

def MinimumWithdraw(amount):
    balance = InitialAmount - amount
    if balance >= minimumAmount:
        print(balance)
    else:
        raise AccountBalanceException("Enter Less Amount, with which Actual amount should be greater than 50.")

age = int(input("Enter Your age : "))
try : 
     MinimumWithdraw(age)
except AccountBalanceException as e:
        print(e)
