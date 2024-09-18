# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums_str.sort(key=cmp_to_key(compare))
        return str(int("".join(nums_str)))
