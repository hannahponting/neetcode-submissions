# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        dq = deque()
        if not root:
            return []
        dq.append(root)
        result = []

        while dq:
            node = dq.pop()
            result.append(node.val)
            if node.right:
                dq.append(node.right)
            if node.left:
                dq.append(node.left)
        return result