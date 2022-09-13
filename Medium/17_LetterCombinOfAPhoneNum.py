# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def backtrack(idx, queue):
            if len(queue) == len(digits):
                if len(queue) > 0:
                    res.append(queue)
                return
            for i in numLetter[digits[idx]]:
                queue += i
                backtrack(idx+1, queue)
                queue = queue[:-1]
        numLetter =  {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res = []
        backtrack(0, "")
        return res
        
