n = int(input("Enter How many digits of Number : "))
psum = 0
nsum = 0
count = 0
while count < n:
    count +=1
    num = int(input(f'Enter the {count} Positive Number : '))
    if num > 0:
        psum = psum + num
    else:
        nsum = nsum + num

print('Sum of the Positive Numbers is ', psum)
print('Sum of the Negative Numbers is ', nsum)


