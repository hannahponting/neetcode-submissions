class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, value in enumerate(heights):
            start = index
            while stack and value < stack[-1][1]:
                new_index, new_value = stack.pop()
                max_area = max(max_area, new_value * (index - new_index))
                start = new_index
            stack.append((start, value))
        
        while stack:
            index, value = stack.pop()
            max_area = max(max_area, value * (len(heights)-index))
        return max_area
            