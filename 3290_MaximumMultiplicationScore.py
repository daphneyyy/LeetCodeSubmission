# You are given an integer array a of size 4 and another integer array b of size at least 4.

# You need to choose 4 indices i0, i1, i2, and i3 from the array b such that i0 < i1 < i2 < i3. Your score will be equal to the value a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3].

# Return the maximum score you can achieve.
  
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [[0] * len(b) for i in range(4)]
        for i in range(len(a)):
            for j in range(len(b)):
                dp[i][j] = float("-inf")
        for j in range(len(b)):
            dp[0][j] = a[0] * b[j]
        for r in range(1, len(a)):
            max_prev = float('-inf')
            for c in range(1, len(b)):
                max_prev = max(max_prev, dp[r - 1][c - 1])
                dp[r][c] = max(dp[r][c], max_prev + a[r] * b[c])

        return max(dp[3][3:])
