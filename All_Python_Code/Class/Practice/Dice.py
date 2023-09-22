from random import randint
class Dice:
    def __init__(self,sides):
        self.sides = sides

    def roll_dice(self):
        self.randNo = randint(1,self.sides)
        return self.randNo

MyDiceObj = Dice(12)
print(MyDiceObj.roll_dice())