# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = deque()
        if root:
            q.append((root, float('-inf'), float('inf')))
        else:
            return True

        while q:
            lengthq = len(q)
            for i in range(lengthq):
                res, low, high = q.popleft()
                if low < res.val < high:
                    if res.left:
                        q.append((res.left, low, res.val))
                    if res.right:
                        q.append((res.right, res.val, high))
                else:
                    return False
        return True

