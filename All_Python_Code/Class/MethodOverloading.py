class Arithmetic:
    def sum(self,x,y,z=None):
        if z == None:
            return x + y
        else:
            return x + y + z
    
    ## For 4 Parameter.
    # def sum(self,x,y,z=None,a=None):
    #     if z == None and a == None:
    #         return x + y
    #     elif z != None and a == None:
    #         return x + y + z
    #     else:
    #         return x + y + z + a

c = Arithmetic()
print(c.sum(10,2))
print(c.sum(10,2,3))
