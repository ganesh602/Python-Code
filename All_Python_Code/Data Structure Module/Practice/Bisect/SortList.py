import bisect

def insertion_sort(lst):
    sort_List = []

    for i in lst:
        bisect.insort_left(sort_List,i)
    
    return sort_List

lst = [2,4,6,8,10,1,3,5,7,9]
sort_list = insertion_sort(lst)

print("Original List :",lst)
print("Sorted List :",sort_list)