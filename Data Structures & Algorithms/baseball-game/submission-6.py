class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        total = 0

        for i in operations:
            if i == '+':
                total += results[-1] + results[-2]
                results.append(results[-1]+results[-2])
            elif i =='D':
                total += results[-1]*2
                results.append(results[-1]*2)
            elif i =='C':
                total -= results[-1]
                results.pop()
            else:
                results.append(int(i))
                total += int(i)
        return total
