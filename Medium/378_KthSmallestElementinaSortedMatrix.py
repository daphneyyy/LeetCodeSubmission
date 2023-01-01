# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n^2).
 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for l in matrix:
            arr += l
        arr.sort()
        return arr[k-1]
