# using Different way.
# task is we have a sequence of numbers , in that 1 number is missing,we have to find that.
import array

# def find_missingNumber(arr):    
#     orgSum = 0
#     for i in range(arr[0],arr[len(arr)-1]+1):
#         orgSum += i

#     arrSum = 0
#     for i in range(len(arr)):
#         arrSum += arr[i]

#     return (orgSum - arrSum)


# Above using methods.

def find_missingNumber(given_list):
    start = given_list[0]
    end = given_list[len(given_list)-1]

    actual_list = list(range(start,end + 1))
    actual_sum = sum(actual_list)
    given_sum = sum(given_list)

    return actual_sum - given_sum

arr = array.array('i',[12,13,14,15,17])
result = find_missingNumber(arr)
if result > 0:
    print("Missing Number :",find_missingNumber(arr))
else:
    print("No Missing number.")

# Normal way.

# def find_missingNumber(lst):
#     fy = lst[0]
#     temp = []
#     for i in range(len(lst)):
#         if fy in lst:
#             fy += 1
#         else:
#             temp.append(fy)
#             fy += 1
#     return temp
        
# num = [3,2,4,6,8]
# result = find_missingNumber(num)
# print(result)