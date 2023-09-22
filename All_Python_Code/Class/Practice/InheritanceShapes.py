import math
class Polygon:
    def __init__(self,no_of_sides,*lstOfSides):
        self.no_Of_Sides = no_of_sides
        self.lstOfSides = lstOfSides[:3]        # Here we dont want to take the no. of sides user gives,we want how many no of sides 
        #                                         the shape have.So we slice the argument list with no. of sides.

class Triangle(Polygon):
    def __init__(self,no_of_sides,*lstOfSides):
        Polygon.__init__(self,no_of_sides,*lstOfSides)

    def area(self):
        a,b,c = self.lstOfSides
        s = (a + b + c)/2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
p = Polygon(5,2,4,5,3,6)

t = Triangle(3,10,15,9,20)
print("Area : ",t.area())