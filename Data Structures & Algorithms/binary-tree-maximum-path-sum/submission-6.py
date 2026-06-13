# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(tree):
            nonlocal res

            if not tree:
                return 0
            
            right = max(dfs(tree.right), 0)
            left = max(dfs(tree.left), 0)

            res = max(res, tree.val + right + left)
            return tree.val + max(left, right)

        dfs(root)
        return res