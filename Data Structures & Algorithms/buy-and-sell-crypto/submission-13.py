class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            profit = prices[i] - minprice
            maxprofit = max(maxprofit, profit)
            minprice = min(minprice, prices[i])
        return maxprofit