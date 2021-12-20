class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i) == None and len(nums) == 1:
                return i
            elif dic.get(i) == None:
                dic[i] = 1
            elif dic[i] + 1 > len(nums) // 2:
                return i
            else:
                dic[i] = dic[i] + 1