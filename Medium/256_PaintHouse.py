# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # 1.Sub-problems:
        #   a. Find the minimum cost to paint n houses.
        #   b. Let C[i,j] to be the minimum cost to paint houses [1,...,i] with color j 
        # 2. Base Case: 
        #   C[0,j] = 0 for j = 0,1,2
        # 3. Recursion:
        #   a. Compute C[i,0]:
        #       C[i,0] = min(C[i-1,1]+costs[i-1,0], C[i-1,2]+costs[i-1,0])
        #   b. Compute C[i,1]:
        #       C[i,1] = min(C[i-1,0]+costs[i-1,1], C[i-1,2]+costs[i-1,1])
        #   c. Compute C[i,2]:
        #       C[i,2] = min(C[i-1,0]+costs[i-1,2], C[i-1,1]+costs[i-1,2])
        # 4. Ordering: for i in n+1: for j in [0,1,2]
        # 5. Output: min(C[n,0],C[n,1],C[n,2])
        n = len(costs)
        c = [float("inf")] * 3
        C = [list(c) for i in range(n+1)]
        for j in [0,1,2]:
            C[0][j] = 0
        for i in range(1,n+1):
            C[i][0] = min(C[i-1][1]+costs[i-1][0], C[i-1][2]+costs[i-1][0])
            C[i][1] = min(C[i-1][0]+costs[i-1][1], C[i-1][2]+costs[i-1][1])
            C[i][2] = min(C[i-1][0]+costs[i-1][2], C[i-1][1]+costs[i-1][2])
        return int(min(C[n][0],C[n][1],C[n][2]))
