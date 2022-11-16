# You are given an integer array nums with the following properties:

# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        freq = dict()
        for i in nums:
            if freq.get(i) == None:
                freq[i] = 1
            else:
                freq[i] += 1
            if freq[i] == n:
                return i
        return 0
