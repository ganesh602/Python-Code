def Flatten(items):
    for i in items:
        if hasattr(i,'__iter__') == True:
            Flatten(i)
        else:
            print(i)

items = [1,2,[3,4,[5,6],7],8]
Flatten(items)
