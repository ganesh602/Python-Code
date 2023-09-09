a = int(input("Enter the First Number : "))
d = int(input("Enter the Difference between the Numbers : "))
n = int(input("Enter how many terms : "))
count = 1

for i in range(a, a + (d * n), d):
    print(i)

