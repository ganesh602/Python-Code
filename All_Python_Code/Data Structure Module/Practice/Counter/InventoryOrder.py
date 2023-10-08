from collections import Counter

dict = {'apple':50,'mango':100,'banana':120,'orange':70}
Inventory = Counter(dict)


def Update_Inventory(order):
    # for inv in Inventory:                     # This is 1st way.
    #     if inv in order:
    #         Inventory[inv] -= order[inv]

    Inventory.subtract(order)                   # This is 2nd way using subtract method of Counter.

ord = {'apple':10,'mango':12,'banana':15,'orange':5}
order = Counter(ord)

Update_Inventory(order)
print(Inventory)