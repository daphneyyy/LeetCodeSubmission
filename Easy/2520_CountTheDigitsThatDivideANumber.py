# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for i in str(num):
            res += 1 if num % int(i) == 0 else 0
        return res 
