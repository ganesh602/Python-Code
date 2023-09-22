class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

    def make_sound(self):
        print("Meow Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

    def make_sound(self):
        print("Bow wow")

def my_pet(pet):
    pet.info()
    pet.make_sound()

c = Cat('Pinky',2)
d = Dog('Raju',2)

my_pet(c)

