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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        if (root === null) return false;
        if (this.dfs(root, subRoot)) return true; 
        return isSubTree(root.left, subRoot) || isSubTree(root.right, subRoot);

        const dfs = (root, subRoot) => {
            if (root === null && subRoot === null) return true;
            if (root === null || subRoot === null) return false;
            if (root.val !== subRoot.val) return false;

            return dfs(root.left, subRoot.left) && dfs(root.right, subRoot.right);
        }
    }
}
