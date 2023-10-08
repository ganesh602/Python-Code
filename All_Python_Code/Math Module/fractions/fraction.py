import fractions

f1 = fractions.Fraction(1/2)
f2 = fractions.Fraction(1/5)

f2 = f2.limit_denominator(10)

print("F1 :",f1,"   F2 :",f2)

print(f"F1 Numerator : {f1.numerator} , F1 Denominator : {f1.denominator}")
print(f"F2 Numerator : {f2.numerator} , F2 Denominator : {f2.denominator}")

print("Add :",f1+f2)
print("Sub :",f1-f2)
print("Mul :",f1*f2)
print("Div :",f1/f2)

print('')

# List of Tuples in Fraction.

L = [(1,2),(4,9),(6,8)]
T = []
print("List convert into Fraction")
for n,d in L:
    print(f"{n},{d} : ",fractions.Fraction(n,d))
    T.append(fractions.Fraction(n,d))

print(T)