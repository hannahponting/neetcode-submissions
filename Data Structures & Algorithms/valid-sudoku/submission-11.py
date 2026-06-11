class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for row in range(len(board)):
            for column in range(len(board[0])):
                value = board[row][column]
                if value != '.':
                    if value in columns[column] or value in rows[row] or value in squares[(row//3, column//3)]:
                        return False
                    columns[column].add(value)
                    rows[row].add(value)
                    squares[(row//3, column//3)].add(value)
        return True
                 
                