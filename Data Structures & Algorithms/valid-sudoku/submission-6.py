class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        # Check rows
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                
                val = int(board[row][column])

                if val in rows[row] or val in columns[column] or val in squares[(row//3, column//3)]:
                    return False
                columns[column].add(val)
                rows[row].add(val)
                squares[(row//3, column//3)].add(val)
        return True