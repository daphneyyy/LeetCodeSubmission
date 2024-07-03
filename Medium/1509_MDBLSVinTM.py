# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        sorted_lst = sorted(nums, reverse=True)
        res = sorted_lst[0] - sorted_lst[-1]
        for i in range(4):
            res = min(sorted_lst[3-i] - sorted_lst[-1-i], res)

        return res
                
