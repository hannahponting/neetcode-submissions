# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deq = deque([root])
        res = []

        while deq:
            res.append([])
            for i in range(len(deq)):
                node = deq.popleft()
                res[-1].append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return [i[-1] for i in res]
            