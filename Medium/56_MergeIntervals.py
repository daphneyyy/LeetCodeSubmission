# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        left = 0
        right = 1
        while right < len(intervals):
            [a,b] = res[left]
            [c,d] = intervals[right]
            if b >= c:
                if b <= d:
                    res[left] = [a,d]
            else:
                res.append([c,d])
                left += 1
            right += 1
        return res
