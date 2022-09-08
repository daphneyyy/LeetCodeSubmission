# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(cur):
            queue.append(cur.val)
            if cur.left == None and cur.right == None:
                res.append("->".join([str(i) for i in queue]))
                queue.pop()
                return
            if cur.left != None:
                dfs(cur.left)
            if cur.right != None:
                dfs(cur.right)
            queue.pop()
        res = []
        queue = []
        dfs(root)
        return res
    
