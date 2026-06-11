class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        previous_temperatures = []
        result = [0]*len(temperatures)
        for index, value in enumerate(temperatures):
            while previous_temperatures and value>previous_temperatures[-1][1]:
                old_index, _ = previous_temperatures.pop()
                result[old_index] = index-old_index
            previous_temperatures.append((index,value))
        return result

