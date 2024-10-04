class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        lst = sorted(set(arr))
        d = {val: idx for idx, val in list(enumerate(lst, 1))}
    
        return [d[i] for i in arr]
