# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        deq = deque([root])

        while deq:
            count = len(deq)
            res.append([])
            for i in range(count):
                tree = deq.popleft()
                res[-1].append(tree.val)
                if tree.left:
                    deq.append(tree.left)
                if tree.right:
                    deq.append(tree.right)
        return res