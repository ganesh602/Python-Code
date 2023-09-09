n = int(input("Enter the number : "))
sum1 = 0
while n > 0:
    r = n % 10
    n = n // 10
    sum1 = sum1 + r

print('Sum of the Number is ',sum1)