class Rectangle:
    count = 0
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        Rectangle.count += 1
    
    # Accessor and Mutators Method For reading and Modifing properties.
    def getLength(self):
        return self.length
    
    def setLength(self,length):
        self.length = length

    def getBreadth(self):
        return self.length
    
    def setBreadth(self,breadth):
        self.breadth = breadth
    #------------------------------------------------------------------

r = Rectangle(10,5)
print(r.getLength())

r.setLength(20)
print(r.getLength())