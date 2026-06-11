class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i] or visited[r][c] == True:
                return False
            
            visited[r][c] = True
            res = (backtrack(r+1, c, i+1) or
                    backtrack(r-1, c, i+1) or
                    backtrack(r, c+1, i+1) or
                    backtrack(r, c-1, i+1)
            )
            visited[r][c] = False
            return res
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if backtrack(row, column, 0):
                    return True
        return False
        
