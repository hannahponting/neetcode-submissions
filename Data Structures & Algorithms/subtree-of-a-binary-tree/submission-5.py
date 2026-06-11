# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(tree1, tree2):
            if not tree1 and not tree2:
                return True
            
            if tree1 and tree2 and tree1.val == tree2.val:
                return (sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right))
            
            return False

        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        d = deque([root])
        while d:
            tree = d.pop()
            if sameTree(tree, subRoot):
                return True
            else:
                if tree.left:
                    d.append(tree.left)
                if tree.right:
                    d.append(tree.right)
        return False