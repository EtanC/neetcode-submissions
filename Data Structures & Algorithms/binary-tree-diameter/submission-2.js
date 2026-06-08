/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        if (!root) return 0;

        let left = this.diameterOfBinaryTree(root.left);
        let right = this.diameterOfBinaryTree(root.right);
        let result = 0;
        result = Math.max(result, left + right);

        return 1 + Math.max(left, right);
    }
}
