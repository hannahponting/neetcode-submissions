class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        minBuy = prices[0]

        for sell in prices:
            max_p = max(max_p, sell - minBuy)
            minBuy = min(minBuy, sell)
        return max_p

