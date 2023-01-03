# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        nums = {
            "0":"0",
            "1":"1",
            "8":"8",
            "6":"9",
            "9":"6"
        }
        if n == 1:
            return ["0","1","8"]
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
        return [i for i in result if i[0] != "0"]
        
