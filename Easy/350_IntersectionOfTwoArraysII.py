class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        freq1 = dict()
        for num in nums1:
            if freq1.get(num) is None:
                freq1[num] = 1
            else:
                freq1[num] += 1

        for num in nums2:
            if freq1.get(num) is not None and freq1.get(num) > 0:
                res.append(num)
                freq1[num] -= 1
        return res
        
