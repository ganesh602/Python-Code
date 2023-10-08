from collections import Counter

Lst = [1,'ganesh',1,2,'mayur','ganesh',2,2,'ganesh']

c = Counter(Lst)

print(c['mayur'])      # gives counter of that item.
print(c.get('ganesh'))      # gives counter of that item.

print(c.items())       # gives all the keys.
print(c.keys())       # gives all the keys.
print(c.values())       # gives all the values.

print(c.most_common())      # gives all the items with counter in a list
print(c.most_common(2))      # gives only 2 items with counter in a list

c.update({'ajay':4})       # updates the keys in the sequence with counter i.e values.
print(c)

c.pop('ganesh')      # removes that item.
print(c)

c.popitem()      # removes the most occurring item.
print(c)

d = c.copy()      # copy the current collection and stores it in d.
print(d)

d.clear()       # clears the items.
print(d)
