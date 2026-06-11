class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for r in prices:
            print(r, min_price)
            profit = max(profit, r-min_price)
            min_price = min(min_price, r)
        return profit
