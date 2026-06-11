class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = defaultdict(set)
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] != '.':
                    if board[row][column] in seen[("row", row)] or board[row][column] in seen[("column", column)] or board[row][column] in seen[("square", row//3, column//3)]:
                        return False
                    else:
                        seen[("row", row)].add(board[row][column])
                        seen[("column", column)].add(board[row][column])
                        seen[("square", row//3, column//3)].add(board[row][column])
        return True