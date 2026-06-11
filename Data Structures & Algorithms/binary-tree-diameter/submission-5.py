# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(tree):
            if not tree:
                return 0
            
            return 1 + max(maxDepth(tree.left), maxDepth(tree.right))
        if not root:
            return 0
        leftHeight =  maxDepth(root.left) 
        rightHeight = maxDepth(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)
