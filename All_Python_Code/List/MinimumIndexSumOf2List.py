# fav1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
# fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']
# less Index means Greater Preference
# So,
# pizza = 0 + 5 = 5
# nuggets = 1 + 4 = 5
# hotdog = 2 + 1 = 3
# noodles = 3 + 2 = 5
# pasta = 4 + 3 = 7
# burger = 5 + 0 = 5
#
# Minimum is 3 , So print hotdog

fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

index1 = len(fav1) + 1
index2 = len(fav2) + 1

# # Using 2 For Loop:
# for x in range(len(fav1)):
#     for y in range(len(fav2)):
#         if fav1[x] == fav2[y]:
#             if (x + y) < (index1 + index2):
#                 index1 = x
#                 index2 = y
# print(fav1[index1])

# # Using a Single Loop.
for x in range(len(fav1)):
    indexfav = fav2.index(fav1[x])
    if (x + indexfav) < (index1 + index2):
        index1 = x
        index2 = indexfav
print(fav1[index1], index1 + index2)
