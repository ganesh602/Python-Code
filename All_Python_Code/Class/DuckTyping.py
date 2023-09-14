def PetLover(pet):
    pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print("Duck is talking.")
    
    def walk(self):
        print("Duck is walking.")

class Dog:
    def talk(self):
        print("Dog is talking.")
    
    def walk(self):
        print("Dog is walking.")

c = Duck()
PetLover(c)

d = Dog()
PetLover(d)