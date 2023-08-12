# You are given a positive integer n.

# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

# Return an integer array answer where answer = [even, odd].

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        bi = str(bin(n)[2:])
        for i in range(len(bi)):
            if int(bi[-i-1]) == 1:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]
