# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

from collections import defaultdict

class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            char_cnt = defaultdict(int)
            length_cnt = 0
            for j in s[i:]:
                if j in char_cnt:
                    break
                else:
                    char_cnt[j] = 1
                    length_cnt += 1
            res = max(res, length_cnt)
        return res
