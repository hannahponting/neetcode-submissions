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
                        allSame = False
                        break
            
            if not allSame:
                mid = n // 2
                topLeft = dfs(mid, c, r)
                topRight = dfs(mid, c+mid, r)
                bottomLeft = dfs(mid, c, r+mid)
                bottomRight = dfs(mid, c+mid, r+mid)
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
            else:
                return Node(grid[r][c], True)
        return dfs(len(grid), 0, 0)

