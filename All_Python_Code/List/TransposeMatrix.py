l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Transpose = []

for i in range(len(l1[0])):
    temp = []
    for j in range(len(l1)):
        temp.append(l1[j][i])
    Transpose.append(temp)
print(Transpose)
