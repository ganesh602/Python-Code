# 1st meal order : 1,2,3,4,5
# 2nd meal should be : 2,3,4,5,1
# Whom ever got their meal should go at the last for their next meal.
from collections import deque

def serve_food(customers):
    customers.rotate(1)

customers = [1,2,3,4,5]
cust = deque(customers)

for i in range(1,6):
    print(f"Meal {i} :",cust)
    serve_food(cust)