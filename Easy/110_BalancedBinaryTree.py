# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class Solution:
    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
