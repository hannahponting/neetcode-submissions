class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(30, 0), ]

        for index, value in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < value:
                    _, new_index = stack.pop()
                    result[new_index] = index - new_index
            stack.append((value, index))
        return result
