class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for index, value in enumerate(prices):
            if index != 0 and value > prices[index -1]:
                max_profit += (prices[index] - prices[index-1] )
        return max_profit