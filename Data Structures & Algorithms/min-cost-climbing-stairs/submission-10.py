# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack
class SolutionV1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(i):
            if i <= 1:
                return 0
            return min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])

        return dfs(n)


# solution 2: top-down DP. Improved solution with memoization and passing idx instead of slicing
# O(n) time and space
class SolutionV2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {0: 0, 1: 0}

        def memoization(i) -> int:
            if i in cache:
                return cache[i]
            cache[i] = min(memoization(i - 2) + cost[i - 2], memoization(i - 1) + cost[i - 1])
            return cache[i]

        return memoization(len(cost))


# solution 3: bottom-up DP
# O(n) time and O(n) space
class SolutionV3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # define dp where dp[i] is the min cost to reach step i
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]


# solution 4: bottom-up DP (space optimized)
# O(n) time and O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1 = 0
        prev2 = 0
        for i in range(2, n + 1):
            curr = min(prev2 + cost[i - 2], prev1 + cost[i - 1])
            prev2, prev1 = prev1, curr
        return prev1
