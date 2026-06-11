class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        focus = []
        l = 0
        r = len(matrix) - 1
        while l <= r:
            pointer = (l + r) // 2
            if matrix[pointer][0] > target:
                r = pointer - 1
            elif target > matrix[pointer][-1]:
                l = pointer + 1
            else:
                focus = matrix[pointer]
                break
        if not focus:
            return False
        l = 0
        r = len(focus)-1
        while l <= r:
            pointer = (l + r) // 2
            if focus[pointer] == target:
                return True
            elif focus[pointer] < target:
                l = pointer + 1
            else:
                r = pointer - 1
        return False
        