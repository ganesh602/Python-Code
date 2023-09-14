from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass

    def display(self):
        print("This is parent.")

class Child(Parent):
    def show(self):
        print("This is child.")

c = Child()
c.show()
c.display()
