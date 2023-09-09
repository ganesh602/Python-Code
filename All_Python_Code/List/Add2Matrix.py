L1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
L2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
result = []

if len(L1) != len(L2):
    exit()

for x in range(len(L1)):
    temp = []
    for y in range(len(L1[0])):
        add = L1[x][y] + L2[x][y]
        temp.append(add)
    result.append(temp)
print(result)
