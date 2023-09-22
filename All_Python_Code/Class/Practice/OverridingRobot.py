class Robot:
    def __init__(self,name):
        self.name = name

    def say_hii(self):
        print("Hii,This is Robot.")

class PoliceRobot(Robot):

    def say_hii(self):
        print("Hii,This is Ploice Robot.")
        print("I am here for your Safety.")

r = Robot('Jacky')
r.say_hii()

p = PoliceRobot('Micky')
p.say_hii()