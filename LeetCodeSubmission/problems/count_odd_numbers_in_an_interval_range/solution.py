class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        l = (high - low) // 2
        if (low % 2 == 0) & (high % 2 == 0):
            return l
        else:
            return l+1