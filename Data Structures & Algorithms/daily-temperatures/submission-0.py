class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        response = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j]> temperatures[i]:
                    response[i] = j-i
                    break
        return response