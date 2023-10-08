import heapq

def Find_KthLargestElement(lst,K_Number):

    sortList = []
    for i in lst:
        heapq.heappush(sortList, -i)           # Making the element as Negative and then Storing.

    result = 0
    for i in range(K_Number):
        result = heapq.heappop(sortList)
    
    return -result                              # Here Again Making Negative, so that it will become original.

Kth_Number = int(input("Enter the Kth Number : "))
lst = [-10,-29,-64,-90,-82,-74,-33]
lst = [10, 29, 64, 90, 82, 74, 33]

result = Find_KthLargestElement(lst,Kth_Number)
print(Kth_Number, "Largest Number :",result)