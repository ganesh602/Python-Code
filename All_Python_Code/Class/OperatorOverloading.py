class RationalNumbers:
    def __init__(self,p = 1,q = 1):
        self.p = p
        self.q = q

    def __add__(self,other):
        s = RationalNumbers()
        s.p = self.p * other.q + other.p * self.q
        s.q = self.q * other.q
        return s
    
    def __str__(self):
        return str(self.p) + "/" + str(self.q)

p = RationalNumbers(2,3)
q = RationalNumbers(2,5)
sum = p + q
print(sum)

