class NegativeAgeException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def CheckAge(age):
    if age > 0 and age < 13:
        print("Kid")
    elif age >= 13 and age < 19:
        print("Teen")
    elif age >= 19 and age < 50:
        print("Teen")
    elif age >= 50:
        print("Old")
    else:
        raise NegativeAgeException("Age should not be Negative")

age = int(input("Enter Your Age : "))
try:
    CheckAge(age)
except NegativeAgeException as e:
    print(e)
