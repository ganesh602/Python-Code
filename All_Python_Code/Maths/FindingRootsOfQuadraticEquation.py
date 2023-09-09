import math
a = int(input('Enter the value of a :'))
b = int(input('Enter the value of b :'))
c = int(input('Enter the value of c :'))

sq = math.sqrt((b * b) - (4 * a * c))


r1 = (- b + sq) / (2 * a)
r2 = (- b - sq) / (2 * a)

print('Roots are ', r1, ' ,', r2)





