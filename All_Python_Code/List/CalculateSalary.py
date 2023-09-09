lst = [int(x) for x in (input("Enter the weekly hours separated by comma's (eg. 8,7,8,7,8,7) : ")).split(',')]
wages = int(input("Enter the hourly wages : "))

SumOfHours = sum(lst)
salary = SumOfHours * wages

print(salary)