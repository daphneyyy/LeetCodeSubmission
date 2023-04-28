# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sumOf3 = nums[i] + nums[lo] + nums[hi]
                if sumOf3 < target:
                    res += hi-lo
                    lo += 1
                else:
                    hi -= 1
        return res