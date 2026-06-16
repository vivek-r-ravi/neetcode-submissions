# brute force recursion
# exponential O(n^t) time and O(t) space where t is capacity
class SolutionV1:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        if capacity == 0:
            return 0
        max_profit = 0
        for i in range(len(profit)):
            if capacity >= weight[i]:
                curr = self.maximumProfit(profit, weight, capacity - weight[i])
                max_profit = max(max_profit, profit[i] + curr)
        return max_profit


# memoization
# O(n*t) time and O(t) space
class SolutionV2:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {0: 0}

        def memoization(capacity):
            if capacity in cache:
                return cache[capacity]
            max_profit = 0
            for i in range(len(profit)):
                if capacity >= weight[i]:
                    curr = memoization(capacity - weight[i])
                    max_profit = max(max_profit, profit[i] + curr)
            cache[capacity] = max_profit
            return cache[capacity]

        return memoization(capacity)


# tabulation
# O(n*t) time and O(t) space
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # define dp[i] to be the max profit at i capacity
        dp = [0] * (capacity + 1)
        for i in range(len(profit)):
            for c in range(capacity + 1):
                if c >= weight[i]:
                    dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])
        return dp[capacity]
