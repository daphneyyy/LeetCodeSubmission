# 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return (
            self.postorderTraversal(root.left) +
            self.postorderTraversal(root.right) + 
            [root.val]
        )
