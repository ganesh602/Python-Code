class Solution(object):
    # My Code:
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     lst = []
    #     flag = False
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i == j:
    #                 continue
    #             if nums[i] + nums[j] == target:
    #                 flag = True
    #                 lst.append(i)
    #                 lst.append(j)
    #                 return lst
    #     if flag == False:
    #         return lst
    
    #From Net
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # Create a dictionary to store the numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement required to reach the target
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]  # Return the indices of the two numbers
            
            num_dict[num] = i  # Add the current number and its index to the dictionary
        
        return []  # If no solution is found, return an empty list
Solution = Solution()
lst = [3,3,3]
target = 6
result = Solution.twoSum(lst,target)
print(result)