class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        minPrice = float('inf')
        for i in range(len(prices)):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return profit
