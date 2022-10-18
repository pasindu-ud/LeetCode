# One-pass approach
# Time complexity = O(n)
# Space complexity = O(n)
# Exactly one and only solution exists
# nums = [.., x, .., y, ..]
# x + y = target => x = target - y
# Maintain a record of all previously accessed values in the list
# @ y, check whether x exists in the record

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_hash_map = {}
        
        for index, value in enumerate(nums):
            difference = target - value
            if difference in value_index_hash_map:
                return [value_index_hash_map[difference], index]
            else:
                value_index_hash_map[value] = index
        return

# Brute-force approach 2
# Time complexity = O(n²)
# Space complexity = O(1)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):     # Loops from (i +1) to n
#                 if (nums[i] + nums[j]) == target:
#                     return [i, j]

# Brute-force approach 1
# Time complexity = O(n²)
# Space complexity = O(1)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(n):     # Loops through the entire list
#                if ((i != j) and (nums[i] + nums[j]) == target):
#                    return [i, j]
