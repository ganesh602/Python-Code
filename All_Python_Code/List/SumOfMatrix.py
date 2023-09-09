A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
c = []
for i in range(len(A)):
    s = []
    for j in range(len(A[0])):
        s.append((A[i][j] + B[i][j]))
    c.append(s)

print(c)

