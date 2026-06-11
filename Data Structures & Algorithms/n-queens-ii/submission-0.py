class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negD = set()
        posD = set()
        board = [['.' for i in range(n)] for i in range(n)]
        count = 0

        def backtrack(i):
            nonlocal count
            if i == n:
                count +=1 
                return
            
            for c in range(n):
                if c in col or i-c in negD or i+c in posD:
                    continue
                
                col.add(c)
                negD.add(i-c)
                posD.add(i+c)
                board[i][c] = 'Q'
                backtrack(i+1)
                col.remove(c)
                negD.remove(i-c)
                posD.remove(i+c)
                board[i][c] = '.'
        backtrack(0)
        return count