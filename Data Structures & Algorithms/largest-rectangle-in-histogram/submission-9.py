class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for index, value in enumerate(heights):
            start = index
            while stack and stack[-1][1] > value:
                new_index, new_value = stack.pop()
                maxarea = max(maxarea, (index-new_index)*new_value)
                start = new_index
            stack.append((start, value))
        
        while stack:
            index, value = stack.pop()
            maxarea = max(maxarea, (len(heights)-index)*value)
        return maxarea
        