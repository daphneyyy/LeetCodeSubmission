# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution(object):
    def backtrack(self, nums, res, queue):
        if len(queue) == len(nums):
            res.append(list(queue))
            return
        diff = list(set(nums) - set(queue))
        for i in range(len(diff)):
            queue.append(diff[i])
            self.backtrack(nums, res, queue)
            queue.pop()
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        self.backtrack(nums, res, queue)
        return res
