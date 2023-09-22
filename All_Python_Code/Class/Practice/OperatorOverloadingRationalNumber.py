class Rational:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def __add__(self,other):
        p = (self.p * other.q) + (other.p * self.q)
        q = (self.q * other.q)
        sum = Rational(p,q)
        return sum
    
    def __sub__(self,other):
        p = (self.p * other.q) - (other.p * self.q)
        q = (self.q * other.q)
        sub = Rational(p,q)
        return sub
    
    def __str__(self):
        return str(self.p) + '/' + str(self.q)
    
r1 = Rational(2,3)
r2 = Rational(1,2)
add = r1 + r2
print(r1,'+',r2,'=',add)

# r1 = Rational(2,3)
# r2 = Rational(1,2)
sub = r1 - r2
print(r1,'-',r2,'=',sub)
