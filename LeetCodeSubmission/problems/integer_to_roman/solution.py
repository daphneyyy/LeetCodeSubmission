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
                
        