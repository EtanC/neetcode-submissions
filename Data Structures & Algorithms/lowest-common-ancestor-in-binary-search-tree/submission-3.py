# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root: 
        #     return None

        # if root.val == p or root.val == q: 
        #     return root

        # left_result = self.lowestCommonAncestor(root.left, p, q)
        # right_result = self.lowestCommonAncestor(root.right, p, q)

        # if left_result and right_result: 
        #     return root 
        
        # return left_result if left_result else right_result
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root