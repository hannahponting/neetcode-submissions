class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = [[False for b in board[0]] for b in board]
        def dfs(i, row, column):
            if i == len(word):
                return True
            
            if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]) or board[row][column] != word[i] or seen[row][column]:
                return False
            seen[row][column] = True

            if dfs(i+1, row+1, column) or dfs(i+1, row, column+1) or dfs(i+1, row-1, column) or dfs(i+1, row, column-1):
                return True
            seen[row][column] = False
            
            return False

        for row in range(len(board)):
            for column in range(len(board[0])):
                if dfs(0, row, column):
                    return True
        return False