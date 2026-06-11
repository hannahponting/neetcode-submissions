class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = [0]*len(heights)
        maxarea = 0

        for index, height in enumerate(heights):
            if stack and stack[-1][0] > height:
                while stack and stack[-1][0] > height:
                    new_height, new_index = stack.pop()
                    maxarea = max(maxarea, new_height * (index-new_index))
                    start = new_index
                stack.append((height, new_index))
            stack.append((height, index))
        
        while stack:
            height, index = stack.pop()
            maxarea = max(maxarea, height * (len(heights)-index))
        return maxarea
