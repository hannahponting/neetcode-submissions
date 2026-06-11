# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(tree):
            if not tree:
                return None
            postorder(tree.left)
            postorder(tree.right)
            res.append(tree.val)
        

        postorder(root)
        return res