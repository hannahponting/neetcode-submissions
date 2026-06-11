class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_price = prices[0]
        profit = 0
        for day in prices:
            this_profit = day - min_buy_price
            profit = max(profit, this_profit)
            min_buy_price = min(min_buy_price, day)
        return profit