class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        L = 0
        for R in range(1, n):
            profit = max(profit, prices[R] - prices[L])
            if prices[R] < prices[L]:
                L = R
        return profit
