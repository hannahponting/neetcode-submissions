class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for i in operations:
            if i == "C":
                results.pop()
            elif i == "D":
                results.append(results[-1]*2)
            elif i == "+":
                results.append(results[-1]+results[-2])
            else:
                results.append(int(i))
        print(results)
        return sum(results)