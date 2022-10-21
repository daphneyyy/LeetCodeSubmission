# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

# The frequency of a letter x is the number of times it occurs in the string.


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        chars = set()
        for i in [*word1]:
            chars.add(i)
        for i in [*word2]:
            chars.add(i)
        for i in chars:
            a = word1.count(i)
            b = word2.count(i)
            if abs(a - b) > 3:
                return False
        return True
        
