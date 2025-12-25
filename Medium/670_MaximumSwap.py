# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = str(num)
        n = len(numStr)
        maxVal = num
        values = [[maxVal for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                curValue = int(numStr[:i] + numStr[j] + numStr[i+1:j] + numStr[i] + numStr[j+1:])
                values[i][j] = max(values[i][j-1], values[max(i-1, 0)][j], curValue)
        return values[n-2][n-1]
        