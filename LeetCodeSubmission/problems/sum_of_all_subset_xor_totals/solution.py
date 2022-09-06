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