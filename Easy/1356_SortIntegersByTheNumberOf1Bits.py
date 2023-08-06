# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.

from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_dict = defaultdict(list)
        for i in arr:
            num_ones = str(bin(i)[2:]).count("1")
            bit_dict[num_ones].append(i)
        res = []
        for key, value in sorted(bit_dict.items()):
            res += sorted(value)
        return res
