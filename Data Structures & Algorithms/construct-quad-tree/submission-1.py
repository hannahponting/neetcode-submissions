"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
    
        def dfs(n, c, r):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame=False
            if allSame:
                return Node(grid[r][c], True)
            
            n = n // 2
            topLeft = dfs(n, c, r)
            topRight = dfs(n, c+n, r)
            bottomLeft = dfs(n, c, r+n)
            bottomRight = dfs(n, c+n, r+n)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(len(grid), 0, 0)