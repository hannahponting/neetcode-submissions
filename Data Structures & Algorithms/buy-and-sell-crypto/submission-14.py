class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for index in range(len(prices)):
            if prices[index] - minprice > maxprofit:
                maxprofit = prices[index] - minprice
            if minprice > prices[index]:
                minprice = prices[index]
        return maxprofit