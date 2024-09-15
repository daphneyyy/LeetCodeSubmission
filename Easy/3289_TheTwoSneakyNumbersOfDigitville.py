from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = [key for key, val in freq.items() if val == 2]
        return res
