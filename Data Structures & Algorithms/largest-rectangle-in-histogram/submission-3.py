class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, value in enumerate(heights):
            index_to_use = index
            if not stack or value > stack[-1][1]:
                stack.append((index, value))
            else:
                while stack and value < stack[-1][1]:
                    new_index, new_value = stack.pop()
                    max_area = max(max_area, (index-new_index)*new_value)
                    index_to_use = new_index
                stack.append((index_to_use, value))
        n = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, (n - index) * height)
        return max_area

