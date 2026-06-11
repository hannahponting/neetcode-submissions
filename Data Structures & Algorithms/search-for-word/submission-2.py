class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]

        def backtrack(col, row, i):
            if col < 0 or col >= len(board[0]) or row < 0 or row >= len(board) or visited[row][col] or board[row][col] != word[i]:
                return False
            
            if i +1 == len(word):
                return True
            
            visited[row][col] = True

            found = (
                backtrack(col + 1, row, i + 1) or
                backtrack(col - 1, row, i + 1) or
                backtrack(col, row + 1, i + 1) or
                backtrack(col, row - 1, i + 1)
            )

            visited[row][col] = False

            return found

        for col in range(len(board[0])):
            for row in range(len(board)):
                if backtrack(col, row, 0):
                    return True
        return False
        
