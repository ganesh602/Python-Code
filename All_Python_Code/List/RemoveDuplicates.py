# lst = [int(x) for x in input("Enter the numbers (eg. 10,4,5,6) : ").split(",")]
# lst1 = []
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
#
# print(lst1)

# Using the Same List.
lst = [int(x) for x in input("Enter the numbers (eg. 10,4,5,6) : ").split(",")]
for i in range(len(lst)):
    if i > len(lst)-1:
        break
    count = 1
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i] == lst[j]:
            count += 1
    if count > 1:
        lst.pop(i)
print(lst)
