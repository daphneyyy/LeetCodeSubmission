class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        def com_helper(res, num, cur, n, k):
            if (len(cur) == k):
                res.append(cur.copy())
                return
            for i in range(num, n + 1):
                cur += [i]
                com_helper(res, i + 1, cur, n, k)
                cur.pop()
        res = []
        com_helper(res, 1, [], n, k)
        return res