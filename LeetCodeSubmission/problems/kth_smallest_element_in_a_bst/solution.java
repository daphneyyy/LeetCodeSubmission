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
    public int kthSmallest(TreeNode root, int k) {
        TreeNode node = root;
        while (node.left != null) {
            node = node.left;
        }
        for (int i = 0; i < k - 1; i++) {
            node = successor(root, node);
        }
        return node.val;
    }
    
    private TreeNode successor(TreeNode root, TreeNode node) {
        TreeNode resultNode = node.right;
        if (resultNode != null) {
            while (resultNode.left != null) {
                resultNode = resultNode.left;
            }
            return resultNode;
        } else {
            TreeNode parNode = parent(root, node);
            TreeNode curNode = node;
            while (parNode != null && parNode.right == curNode) {
                curNode = parNode;
                parNode = parent(root, parNode);
            }
            return parNode;
        }
    }
    
    private TreeNode parent(TreeNode node, TreeNode child) {
        if (node.left == child || node.right == child) {
            return node;
        }
        if (node.val > child.val) {
            return parent(node.left, child);
        } else {
            return parent(node.right, child);
        }
    }
}