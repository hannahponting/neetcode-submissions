class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0

        options = [i*i for i in range(n) if i*i <= n]
        print(options)

        for target in range(1, n+1):
            for square in options:
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[n]

