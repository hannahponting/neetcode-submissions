class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        negD = set()
        posD = set()
        col = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(i):
            if i == n:
                res.append([''.join(b) for b in board])
                return
            
            for c in range(n):
                if c in col or c+i in posD or c-i in negD:
                    continue
                col.add(c)
                posD.add(c+i)
                negD.add(c-i)
                board[i][c] = 'Q'
                backtrack(i+1)
                col.remove(c)
                posD.remove(c+i)
                negD.remove(c-i)
                board[i][c] = '.'
            
            
        backtrack(0)
        return res