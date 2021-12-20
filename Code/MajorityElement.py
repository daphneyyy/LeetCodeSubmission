// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
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
