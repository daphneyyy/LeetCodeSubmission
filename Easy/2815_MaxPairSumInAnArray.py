# You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

# Return the maximum sum or -1 if no such pair exists.

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def findMax(num):
            return max([int(x) for x in str(num)])
        lst = [findMax(i) for i in nums]
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if lst[i] == lst[j]:
                    res = max(res, nums[i] + nums[j])
        return res if res != 0 else -1
