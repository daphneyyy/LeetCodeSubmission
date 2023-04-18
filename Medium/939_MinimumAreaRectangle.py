# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        min_area = sys.maxsize
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    min_area = min(min_area, abs(x1-x2)*abs(y1-y2))
            seen.add((x1, y1))
        return min_area if min_area != sys.maxsize else 0
