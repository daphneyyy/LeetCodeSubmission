# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        odd = 0
        for key, val in freq.items():
            if val % 2 == 0:
                res += val 
            else:
                res += val - 1
                odd = 1
        return res + odd
