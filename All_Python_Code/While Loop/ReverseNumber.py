n = int(input("Enter the number : "))
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

print('Sum of the Number is ', rev)
