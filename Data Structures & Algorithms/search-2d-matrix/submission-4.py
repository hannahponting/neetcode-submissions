class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        focus = []
        for i in range(len(matrix)):
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                focus = matrix[i]
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
        