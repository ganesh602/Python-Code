def PrimeNumber(num): # 5
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1  # count = count + 1
    if count == 2:
        return True 
    else:
        return False
    
def PrimeNumberTillNumber(num): # 50
    for n in range(1, num + 1):
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
        if count == 2:
            print(n ,end = " ")


number = int(input("Enter a number : "))
result = PrimeNumber(number)

if result == True:
    print(number,"is a Prime number.")
else:    
    print(number,"is not a Prime Number.")

PrimeNumberTillNumber(number)

