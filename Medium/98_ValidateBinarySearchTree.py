# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(r: Optional[TreeNode], lst: list) -> bool:
            res = True
            if r:
                res = inorder(r.left, lst)
                if len(lst) != 0:
                    prev = lst[-1]
                    if prev >= r.val:
                        return False
                if not res: return False
                lst.append(r.val)
                res = inorder(r.right, lst)
            return res
        res = []
        return inorder(root, res)
