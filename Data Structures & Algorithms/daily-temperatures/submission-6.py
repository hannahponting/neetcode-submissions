class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]* len(temperatures)
        dq = deque()

        for index, value in enumerate(temperatures):
            while dq and value > dq[-1][0]:
                new_value, new_index = dq.pop()
                results[new_index] = index-new_index
            dq.append((value, index))
        return results
            