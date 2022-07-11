# 94. Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorderHelper(node):
            if node == None:
                return []
            return inorderHelper(node.left) + [node.val] + inorderHelper(node.right)
        return inorderHelper(root)
    
        
