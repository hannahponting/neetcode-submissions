class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if (row1 <= row and row <= row2) and (col1 <= col and col <= col2):
                    total += self.matrix[row][col]
        return total






# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)