import bisect

L = [10,20,20,30,40,50,60,70,90]
print("List :",L)
print("")

bisect.insort(L,25)
print("Inserted 25 :",L)
print('')

bisect.insort_left(L,90)
print("Inserted Left 90 :",L)
print('')

bisect.insort_right(L,60)
print("Insert Right 60 :",L)
print('')

bisect.bisect(L,60)
print("Get Position(Bisect) of 60 :",L)
print('')

bisect.bisect_left(L,30)
print("Get Position(Bisect_Left) of 30 :",L)
print('')

bisect.bisect_right(L,25)
print("Get Position(Bisect_Right) of 25 :",L)