class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        if n < 3:
            return 1
        res = [0] * (n+1)
        res[1] = 1
        res[2] = 1

        for j in range(3, n+1):
            res[j] = res[j-1] + res[j-2] + res[j-3]
        return res[-1]