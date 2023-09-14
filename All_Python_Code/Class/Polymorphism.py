def Driver(car):
    car.drive()         # 1 Statement different Actions , it does based on the Objects.

class Creta:
    def drive(self):
        print("Creta is Driving.")

class Mercedes:
    def drive(self):
        print("Mercedes is Driving.")
    
c = Creta()
Driver(c)

m= Mercedes()
Driver(m)


