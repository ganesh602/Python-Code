def closure(msg):
    def display():
        print("*" * 10)
        print(msg)
        print("*" * 10)
    return display

d = closure("Hii,Ganesh")
d()