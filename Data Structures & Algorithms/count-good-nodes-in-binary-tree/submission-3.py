# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxVal):
            nonlocal res

            if node.val >= maxVal:
                res = res + 1
            maxVal = max(maxVal, node.val)
            if node.left:
                dfs(node.left, maxVal)
            if node.right:
                dfs(node.right, maxVal)
        
        dfs(root, root.val)
        return res