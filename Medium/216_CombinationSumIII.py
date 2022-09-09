# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

class Solution(object):
    def backtrack(self, queue, idx, res, k, n):
        if n < 0:
            return
        if n > 0 and len(queue) == k:
            return
        if n == 0:
            if len(queue) == k:
                res.append(list(queue))
            return
        for i in range(idx, 10):
            if i > n:
                return
            queue.append(i)
            self.backtrack(queue, i+1, res, k, n-i)
            queue.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        queue = []
        res = []
        self.backtrack(queue, 1, res, k, n)
        return res
