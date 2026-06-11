class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            maxprofit = max(prices[i] - minbuy, maxprofit)
            minbuy = min(minbuy, prices[i])
        return maxprofit