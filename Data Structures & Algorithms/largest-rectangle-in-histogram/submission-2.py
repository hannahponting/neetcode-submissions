class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        other_columns = []
        max_value = 0
        for index, value in enumerate(heights+[0]):
            start = index
            while other_columns and (other_columns[-1][1]>value):
                old_index, old_value = other_columns.pop()
                max_value = max(max_value, old_value*(index-old_index))
                start = old_index
            other_columns.append((start, value))
        return max_value
        


