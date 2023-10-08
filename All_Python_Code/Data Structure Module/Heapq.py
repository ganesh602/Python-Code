import heapq

H = []
heapq.heappush(H,30)        # Adding 30 to the Heap List.
print("Added 30 :",H)

heapq.heappush(H,50)        # Adding 50 to the Heap List.
print("Added 50 :",H)

heapq.heappush(H,40)        # Adding 50 to the Heap List.
print("Added 40 :",H)

heapq.heappush(H,10)        # Adding 10 to the Heap List.
print("Added 10 :",H)

heapq.heappop(H)            # Removing First element from the Heap List.
print("Removed 1st element :",H)

heapq.heappop(H)            # Removing First element from the Heap List.
print("Removed 1st element :",H)

L = [80,60,20,40,10]

heapq.heapify(L)        # Converting a List into Heap queue.
print("Heap :",L)

print("2 Largest :",heapq.nlargest(2,L))        # Will get 2 Largest elements.

print("2 Smallest :",heapq.nsmallest(2,L))      # Will get 2 Smallest elements.