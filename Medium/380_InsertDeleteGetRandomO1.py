# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet:

    def __init__(self):
        self.lst = list()
        self.dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            self.dict[self.lst[-1]] = idx
            self.lst[idx] = self.lst[-1]
            self.lst.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
