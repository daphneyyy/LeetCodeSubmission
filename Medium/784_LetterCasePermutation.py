# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

class Solution(object):
    def backtrack(self, s, idx):
        if idx == len(s):
            return [""]
        if s[idx].isdigit():
            return [s[idx] + i for i in self.backtrack(s, idx+1)]
        else:
            res = self.backtrack(s, idx+1)
            return [s[idx].upper() + i for i in res] + [s[idx].lower() + i for i in res]
        
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.backtrack(s, 0)
