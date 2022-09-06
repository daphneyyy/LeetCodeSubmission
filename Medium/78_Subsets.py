# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution(object):
    from collections import deque
    
    def sub_helper(self, queue, idx, nums, res):
        for i in range(idx, len(nums)):
            queue.append(nums[i])
            res.append(list(queue))
            self.sub_helper(queue, i + 1, nums, res)
            queue.pop()
            
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if len(nums) == 0:
            return res
        queue = deque()
        self.sub_helper(queue, 0, nums, res)
        return res
    
