n = int(input("Enter How many digits of Number : "))
count = 1
maximum = int(input(f'Enter the {count} Number : '))
while count <= n - 1:
    count += 1
    num = int(input(f'Enter the {count} Number : '))
    if num > maximum:
        maximum = num

print('Maximum Number is ', maximum)

