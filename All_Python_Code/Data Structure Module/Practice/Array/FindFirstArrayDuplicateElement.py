import array

def find_duplicate(nums):
    num_set = set()             # Create a Set to store the number.
    for i in nums:
        if i in num_set:
            return i
        else:
            num_set.add(i)
    else:
        return -1

num = array.array('i',[10,20,13,40,50,13,10,20,40])

result = find_duplicate(num)
print(result)



