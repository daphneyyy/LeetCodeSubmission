// 404. Sum of Left Leaves
// Given the root of a binary tree, return the sum of all left leaves.

// A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

  /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if ((root.left == null) & (root.right == null)) {
            return 0;
        } else {
            return sumLeft(root.left, true) + sumLeft(root.right, false);
        }
    }
    
    public int sumLeft(TreeNode node, boolean isLeft) {
        if (node == null) {
            return 0;
        }
        if ((node.left == null) & (node.right == null)) {
            if (isLeft) {
                return node.val;
            } else {
                return 0;
            }
        } else if ((node.left != null) & (node.right == null)) {
            return sumLeft(node.left, true);
        } else if ((node.left == null) & (node.right != null)) {
            return sumLeft(node.right, false);
        } else {
            return sumLeft(node.left, true) + sumLeft(node.right, false);
        }
    }
}
