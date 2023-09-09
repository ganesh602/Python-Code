num = int(input("Enter a Number for Fibonacci Series : "))

first = 0
second = 1

print(first)
print(second)
fib = 0

for i in range(num - 1):
    fib = first + second
    print(fib)
    first = second
    second = fib


