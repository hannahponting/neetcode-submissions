class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[target] = 1
        for total in range(target, 0, -1):
            for num in nums:
                dp[total - num] += dp[total]
        return dp[0]