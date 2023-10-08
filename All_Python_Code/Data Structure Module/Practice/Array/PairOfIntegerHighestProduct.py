import array

def FindPairOfHighestProduct(arr):
    first = 0
    second = 0
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] * arr[y] >= first * second:
                first = arr[x]
                second = arr[y]
    return (first,second)

arr = array.array('i',[2,4,6,8,3,7,9])
result = FindPairOfHighestProduct(arr)
print("Max Product Pair :", result)
print('')

arr = array.array('i',[0,-1,-3,-5,-8,2,4])
result = FindPairOfHighestProduct(arr)
print("Max Product Pair :", result)