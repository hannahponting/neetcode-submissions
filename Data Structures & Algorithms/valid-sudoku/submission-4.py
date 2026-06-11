class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        for i in range(0, len(board)):
            row = [character for character in board[i] if character != "."]
            print(row)
            if len(row) > len(set(row)):
                return False
        for i in range(0, len(board[0])-1):
            row = []
            for j in range(0, len(board[0])-1):
                if board[j][i] != ".":
                    row.append(board[j][i])
            if len(row) > len(set(row)):
                return False
        for i in [1,2,3]:
            for j in [1,2,3]:
                square = [board[3*i-3][3*j-3], board[3*i-3][3*j-2], board[3*i-3][3*j-1], board[3*i-2][3*j-3],
                board[3*i-2][3*j-2], board[3*i-2][3*j-1], board[3*i-1][3*j-3], board[3*i-1][3*j-2], board[3*i-1][3*j-1]]
                square_numbers = [character for character in square if character != "."]
                if len(square_numbers)> len(set(square_numbers)):
                    return False
        return True

     