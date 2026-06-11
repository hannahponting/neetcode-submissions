# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        deq = deque([(root, float('-inf'), float('inf'))])

        while deq:
            root, minVal, maxVal = deq.popleft()
            if not minVal < root.val < maxVal:
                return False
            
            if root.left:
                deq.append((root.left, minVal, root.val))
            if root.right:
                deq.append((root.right, root.val, maxVal))
        
        return True