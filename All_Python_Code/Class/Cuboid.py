class Cuboid():
    def __init__(self,l,b,h):
        #print(id(self))
        self.length = l
        self.breadth = b
        self.height = h
    
    def total(self):
        return 2 * (self.length * self.breadth * self.height)
    
    def volume(self):
        return self.length * self.breadth * self.height
    
c1 = Cuboid(20,10,5)
print(c1.total())
print(c1.volume())

# By print ID of Object And Self, we can see that both are same 
# that means which object we are passing, self holds that object.

# c1 = Cuboid(10,5,3)
# print(id(c1))

# c2 = Cuboid(10,50,3)
# print(id(c2))
