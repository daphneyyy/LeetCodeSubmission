# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = 0
        while queue:
            level_queue = []
            for i in queue:
                if i is None or i.left is None:
                    return root
                level_queue.append(i.left.val)
                level_queue.append(i.right.val)
            level += 1
            if level % 2 == 1:
                temp = []
                for i in queue:
                    i.left.val = level_queue.pop()
                    i.right.val = level_queue.pop()
                    temp.append(i.left.left)
                    temp.append(i.left.right)
                    temp.append(i.right.left)
                    temp.append(i.right.right)
                queue = temp

        return root
