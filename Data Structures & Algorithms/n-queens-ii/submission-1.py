class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        negD = set()
        posD = set()
        col = set()
        res = 0
        board = [["."] * n for i in range(n)]

        def backtrack(i):
            nonlocal res
            if i == n:
                res += 1
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