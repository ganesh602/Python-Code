class iphone6:
    def home(self):
        print("Iphone6 Home.")

class iphoneX(iphone6):
    def home(self):
        print("IphoneX Home.")
        super().home()

i6 = iphone6()
i6.home()

iX = iphoneX()
iX.home()