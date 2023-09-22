class Orders:
    def __init__(self):     # ,*cartItems):
        self.cart = []      # [x for x in cartItems] # Initializing a List.

    def add_to_cart(self,item):
        self.cart.append(item)

    def remove(self,item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)
    
    def __str__(self):
        store = ''
        for i in self.cart:
            store += str(i) + '\n'
        return store

o = Orders()
o.add_to_cart(45)
o.add_to_cart('Book')
o.add_to_cart('Pen')
o.add_to_cart('Bat')
o.add_to_cart('Guitar')
print(o)
o.remove('Pen')
print(o)