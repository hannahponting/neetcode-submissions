# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(tree: Optional[TreeNode]) -> int:
            if not tree:
                return 0
        
            return (1+ max(maxDepth(tree.left), maxDepth(tree.right)))

        if not root:
            return 0
        diameter = maxDepth(root.left) + maxDepth(root.right)

        return max(diameter, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right) ))