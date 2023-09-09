n = int(input("Enter a number : "))
binary = " "
rev = 0
while n > 0:
    r = n % 2
    n = n // 2
    binary = str(r) + binary
    # binary = binary * 10 + r

print('Sum of the Number is ', binary)

# while binary > 0:
#   r = binary % 10
#    binary = binary // 10
#    rev = rev * 10 + r

# print('Sum of the Number is ', rev)
