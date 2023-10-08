from collections import deque

customers = deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust = customers.popleft()
    print(cust,"leaves the shop.")

walk_in("John")
walk_in("James")
walk_in("Smith")
serviced()
serviced()
walk_in("Mark")

print(f"Remaining Customers : {customers}")