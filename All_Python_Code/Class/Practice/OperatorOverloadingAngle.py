class Angle:
    def __init__(self,degree):
        self.degree = degree

    def __add__(self,ang):
        MyAngleObj = Angle(self.degree + ang.degree)  # Here we called the Angle Class, bcz to acces the __str__ method 
        return  MyAngleObj                            # we should provide an object, for that we call the class again ,
    #                                                   so that it will return as an object.
    
    def __str__(self):
        return 'Degree ' + str(self.degree)
    
a1 = Angle(45)
a2 = Angle(90)
sum = a1 + a2
# sum = a1.__add__(a2)      # We can write this also.
print(sum)