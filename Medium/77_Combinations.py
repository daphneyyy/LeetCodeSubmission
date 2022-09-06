# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

class Solution(object):
    def com_helper(self, res, num, cur, n, k):
        if (len(cur) == k):
            res.append(list(cur))
            return
        for i in range(num, n + 1):
            cur += [i]
            self.com_helper(res, i + 1, cur, n, k)
            cur.pop()
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        res = []
        self.com_helper(res, 1, [], n, k)
        return res
