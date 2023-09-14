class Rectangle:
    count = 0
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
    @classmethod   # Denotes that this is a class method
    def countRect(cls):
        print(cls.count)    # Print how many times object has created.
    
    @staticmethod
    def isSquare(len,breadth):
        return len == breadth

# Accessing Static Method.
r1 = Rectangle(10,5)
#print(r1.isSquare(10,10))       # We should not access the static method with object as it is a static method
#                                # as it doesnot access any instance variables.

print(Rectangle.isSquare(10,10)) # We should access with Class name.

# Class Variable example.

# r1 = Rectangle(10,20)
# r2 = Rectangle(10,20)
# r1.countRect()
# r2.countRect()
# Rectangle.countRect()
