class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        temperatures_stack = []

        for index, temp in enumerate(temperatures):
            while temperatures_stack and temp >temperatures_stack[-1][1]:
                old_index, new_temp = temperatures_stack.pop()
                result[old_index] = index-old_index
            temperatures_stack.append((index, temp))
        return result
