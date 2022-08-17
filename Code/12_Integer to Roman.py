# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# Constraints:
# 1 <= num <= 3999

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        
        ones = num % 10
        if ones < 5:
            if ones == 4:
                res = "IV"
            else:
                res = "I" * ones
        else:
            if ones == 9:
                res = "IX"
            else:
                res = "V" + "I" * (ones - 5)
                
        tens = (num % 100) // 10
        if tens < 5:
            if tens == 4:
                res = "XL" + res
            else:
                res = "X" * tens + res
        else:
            if tens == 9:
                res = "XC" + res
            else:
                res = "L" + "X" * (tens - 5) + res
        
        hunds = (num % 1000) // 100
        if hunds < 5:
            if hunds == 4:
                res = "CD" + res
            else:
                res = "C" * hunds + res
        else:
            if hunds == 9:
                res = "CM" + res
            else:
                res = "D" + "C" * (hunds - 5) + res
        
        thous = (num % 10000) // 1000
        res = "M" * thous + res
        
        return res
                
        
