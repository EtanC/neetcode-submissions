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
        let result = 0;  // lives here, persists across all recursive calls

        const dfs = (node) => {
            if (!node) return 0;

            let left = dfs(node.left);
            let right = dfs(node.right);

            result = Math.max(result, left + right);  // updates the outer result

            return 1 + Math.max(left, right);
        }

        dfs(root);
        return result;
    }
}
