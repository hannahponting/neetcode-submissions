# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        deq = deque([(root, float('-inf'))])
        count = 0

        while deq:
            amount = len(deq)
            for i in range(amount):
                node = deq.popleft()
                if node[0].val >= node[1]:
                    count += 1
                if node[0].left:
                    deq.append([node[0].left, max(node[1], node[0].val)])
                if node[0].right:
                    deq.append([node[0].right, max(node[1], node[0].val)]) 
        return count  