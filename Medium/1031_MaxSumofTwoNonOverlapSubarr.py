# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

# A subarray is a contiguous part of an array.

class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        all_sums = list(nums)
        for i in range(1, len(nums)):
            all_sums[i] += all_sums[i - 1]
        maxi = all_sums[firstLen+secondLen-1]
        for i in range(len(nums)+1-firstLen-secondLen):
            if i == 0:
                L = all_sums[firstLen-1]
            else:
                L = all_sums[firstLen-1+i] - all_sums[i-1]
            R = 0
            for j in range(firstLen+i, len(nums)+1-secondLen): 
                R = max(R, all_sums[j-1+secondLen] - all_sums[j-1])
            maxi = max(maxi, L + R)
            
        for i in range(len(nums)+1-firstLen-secondLen):
            if i == 0:
                L = all_sums[secondLen-1]
            else:
                L = all_sums[secondLen-1+i] - all_sums[i-1]
            R = 0
            for j in range(secondLen+i, len(nums)+1-firstLen): 
                R = max(R, all_sums[j-1+firstLen] - all_sums[j-1])
            maxi = max(maxi, L + R)
            
        return maxi
