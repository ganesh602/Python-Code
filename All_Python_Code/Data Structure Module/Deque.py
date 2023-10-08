from collections import deque

L = [1,2,3,4,5]

d = deque(L)        # Creating a Deque of List.
print("Creating Deque :",d)

d.append(6)        # Adding to the Last in Deque List.
print("Append :",d)

d.appendleft(7)        # Adding to the first in Deque List.
print("Append Left :",d)

d.pop()        # Remove the Last item in Deque List.
print("Pop :",d)

d.popleft()        # Remove the First item in Deque List.
print("Pop Left :",d)

d.extend([10,20,30])        # Adding to the Last in Deque List.
print("Extend :",d)

d.extendleft([11,22,33,44])        # Adding to the first in Deque List.
print("Extend Left :",d)

d.rotate(3)        # Rotate Deque List by 3.
print("Rotate :",d)