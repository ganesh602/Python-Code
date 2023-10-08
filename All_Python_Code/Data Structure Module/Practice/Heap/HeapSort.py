import heapq

def heap_sort(lst):
    heapq.heapify(lst)
    sorted_list = []

    for i in range(len(lst)):
        sorted_list.append(heapq.heappop(lst))

    return sorted_list

lst = [12,14,8,7,3,-5,6,2]
print("Original List :",lst)
result = heap_sort(lst)
print("Sorted List :",result)
