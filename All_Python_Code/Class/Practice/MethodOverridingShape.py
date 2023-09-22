import math
class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        print('Shape Area : ',self.name)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
s = Shape('shape')
s.area()

r = Rectangle(10,7)
print(r.area())

c = Circle(10)
print(c.area())