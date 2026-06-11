class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column_length = len(matrix)
        row_length = len(matrix[0])
        
        for ri in range(row_length):
            for ci in range(column_length):
                if matrix[ci][ri] == target:
                    return True
        return False
