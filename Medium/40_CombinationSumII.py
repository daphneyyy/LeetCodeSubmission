# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution(object):
    from collections import deque
    
    def backtrack(self, queue, idx, nums, res, target):
        if target == 0:
            res.append(list(queue))
        elif target < 0:
            return
        prev = -1
        for i in range(idx, len(nums)):
            if nums[i] == prev:
                continue
            queue.append(nums[i])
            self.backtrack(queue, i+1, nums, res, target-nums[i])
            prev = nums[i]
            queue.pop()
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lst_sorted = sorted(candidates)
        res = []
        queue = deque()
        self.backtrack(queue, 0, lst_sorted, res, target)
        return res
        
