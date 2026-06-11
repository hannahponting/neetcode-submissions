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
        q = deque()
        q.append((root, 0))
        res = []

        while q:
            qlength = len(q)
            for i in range(qlength):
                li, index = q.popleft()
                if len(res) == index:
                    res.append([])
                res[index] = li.val
                if li.left:
                    q.append((li.left, 1+index))
                if li.right:
                    q.append((li.right, 1+index))
        return res
