# Given a string num which represents an integer, return true if num is a strobogrammatic number.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro_nums = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6"
        }
        new_num = "".join([stro_nums[i] for i in num if i in stro_nums][::-1])
        return new_num == num
