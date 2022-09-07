# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.
 
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.it = []
        self.cur_idx = -1
        queue = []
        self.backtrack(characters, queue, self.it, combinationLength, 0)
        
    def backtrack(self, chars, queue, res, cLength, start):
        if len(queue) == cLength:
            res.append("".join(list(queue)))
            return
        for i in range(start, len(chars)):
            queue.append(chars[i])
            self.backtrack(chars, queue, res, cLength, i+1)
            queue.pop()
    
    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.cur_idx += 1
            res = self.it[self.cur_idx]
            return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur_idx < len(self.it) - 1:
            return True
        return False
 
