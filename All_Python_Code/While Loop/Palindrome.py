n = int(input("Enter the number : "))
rev = 0
org = n
while n > 0:
    r = n % 10  # stores last digit 
    n = n // 10 # stores numbers except last one
    rev = rev * 10 + r

if org == rev:
    print('It is a Palindrome.')
else:
    print('It is not a Palindrome.')

