# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or k % len(nums) == 0:
            return
        m = k % len(nums) 
        lst = nums.copy()
        for i in range(m, len(nums)):
            nums[i] = lst[i - m]
        for i in range(m):
            nums[i] = lst[-m+i]
