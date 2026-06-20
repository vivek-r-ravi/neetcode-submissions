class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        L=0
        for R in range(1,n):
            if prices[R]<prices[L]:
                L=R
            profit=max(profit,prices[R]-prices[L])
        return profit