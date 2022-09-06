# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution(object):
  
    from collections import deque
    
    def sub_helper(self, queue, idx, nums, bit_sum, res):
        cur = bit_sum
        for i in range(idx, len(nums)):
            bit_sum ^= nums[i]
            queue.append(nums[i])
            res[0] += bit_sum
            self.sub_helper(queue, i + 1, nums, bit_sum, res)
            bit_sum = cur
            queue.pop()

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]
        bit_sum = 0
        if len(nums) == 0:
            return res
        queue = deque()
        self.sub_helper(queue, 0, nums, bit_sum, res)
        return res[0]

# from collections import deque

# def sub_helper(queue, idx, nums, bit_sum, res):
#     cur = bit_sum
#     for i in range(idx, len(nums)):
#         bit_sum ^= nums[i]
#         queue.append(nums[i])
#         res[0] += bit_sum
#         sub_helper(queue, i + 1, nums, bit_sum, res)
#         bit_sum = cur
#         queue.pop()
            
# def subsetXORSum(nums):
#     res = [0]
#     bit_sum = 0
#     if len(nums) == 0:
#         return res
#     queue = deque()
#     sub_helper(queue, 0, nums, bit_sum, res)
#     return res[0]
    
# print(subsetXORSum([5,1,6]))
# 28
