class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # maxi = prices.index(max(prices))
        # mini = prices.index(min(prices))

        # if maxi < mini: 
        #     return 0
        # else:
        #     return prices[maxi] - prices[mini]

        mini = prices[0]
        profit = 0

        for i in prices:
            if i < mini: 
                mini = i
            if i - mini > profit:
                profit = i - mini
        return profit
        