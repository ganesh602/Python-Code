dict1 = {'stoic':'a person who can endure pain or hardship without showing their feelings or complaining.',
         'meditation':'awareness, and achieve a mentally clear and emotionally calm and stable state.',
         'god':'the supreme or ultimate reality'}

# count = 100000
# count1 = 0
# ShortWord = ''
# LongWord = ''
# for i in dict1:
#     ind = len(dict1[i])
#     ind1 = len(dict1[i])
#     if ind < count:
#         count = ind
#         ShortWord = i
#     if ind > count1:
#         count1 = ind1
#         LongWord = i
# print('Shortest -' ,ShortWord ,':', dict1[ShortWord])
# print('Longest -' ,LongWord ,':', dict1[LongWord])


keys = list(dict1.keys())
values = list(dict1.values())
length = [len(x) for x in values]

max = max(length)
min = min(length)

max_index = length.index(max)
min_index = length.index(min)

print(keys[min_index],values[min_index])
print(keys[max_index],values[max_index])
