from abc import ABC, abstractmethod
import os
class Parent(ABC):
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print("This is parent.")

class Child(Parent):
    #This Show method is must,bcz it is an abstract method in Parent Class,
    #So it must override it in Child Class. Or Else it will throw error. 
    def show(self):
        print("This is child.")

c = Child()
c.show()
c.display()
print(os.getcwd())
