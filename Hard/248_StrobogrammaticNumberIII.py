# Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def findStrobogrammatic(self, n: int) -> List[int]:
        nums = {
            "0":"0",
            "1":"1",
            "8":"8",
            "6":"9",
            "9":"6"
        }
        if n == 1:
            return [0,1,8]
        def recur(length):
            if length == 1:
                return ["0","1","8"]
            elif length == 0:
                return []
            res = recur(length-2)
            if res != []:
                lst = []
                for i in nums:
                    lst += [i + j + nums[i] for j in res]
                return lst
            else:
                return [i + nums[i] for i in nums]
        result = recur(n)
        return [int(i) for i in result if i[0] != "0"]

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        res = []
        for i in range(len(low), len(high)+1):
            res += self.findStrobogrammatic(i)
        cnt = 0
        for i in res:
            if i >= int(low) and i <= int(high):
                cnt += 1
        return cnt
