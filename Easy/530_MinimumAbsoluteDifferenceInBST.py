# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(node, nodes):
            if node is None:
                return
            inOrder(node.left, nodes)
            nodes.append(node.val)
            inOrder(node.right, nodes)
        
        nodes = []
        inOrder(root, nodes)

        min_diff = float('inf')
        for i in range(len(nodes) - 1):
            min_diff = min(nodes[i+1] - nodes[i], min_diff)
        
        return min_diff
