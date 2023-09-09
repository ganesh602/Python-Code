l1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']
result = []

# Using Count Method :
for x in range(len(l1)):
    count = l1.count(l1[x])
    if l1[x] not in result:
        result.append(l1[x])
        result.append(count)
print(result)

# # WithOut Using Count Method :
# for x in range(len(l1)):
#     count = 1
#     for y in range(len(l1)):
#         if l1[x] == l1[y]:
#             count += 1
#     if l1[x] not in result:
#         result.append(l1[x])
#         result.append(count)
# print(result)

