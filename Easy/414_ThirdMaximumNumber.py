class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_lst = sorted(list(set(nums)), reverse=True)
        return sorted_lst[2] if len(sorted_lst) >= 3 else sorted_lst[0]
