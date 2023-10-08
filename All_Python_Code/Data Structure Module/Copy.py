import copy

L = [1,2,3,4]

L1 = copy.copy(L)       # Shallow Copy The objects will point towards the L Value, it will not create separately.
print("Shallow Copy :",L1)
print('')

print("Id L[0] :",id(L[0]))     # L[0] id and L1[0] are both same, that means they point onto the same value.
print("ID L1[0] :",id(L1[0]))
print('')

#'''''''DeepCopy------
class Person:
    def __init__(self,name):
        self.name = name

D = [Person('John'),Person('Mickey'),Person('Rohan')]

D1 = copy.deepcopy(D)

for i in D1:
    print(i.name,end= " ")
print('')

print('')
print("Id D[0] :",id(D[0]))     # D[0] id and D1[0] are both different,
print("ID D1[0] :",id(D1[0]))   # that means it created different lists and objects.
