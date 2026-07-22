class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        res = [0] * (n+1)
        res[1] = 1
        res[2] = 2

        for j in range(3, n+1):
            res[j] = res[j-1] + res[j-2]
        
        return res[-1]
