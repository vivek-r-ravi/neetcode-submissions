# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack
class SolutionV1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==1:
            return 0
        if n==2:
            return min(cost[0],cost[1])
        return min(
            self.minCostClimbingStairs(cost[:-2])+cost[-2],
            self.minCostClimbingStairs(cost[:-1])+cost[-1]
            )

# solution 2: top-down DP
# O(n) time and space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={1:0,2:min(cost[0],cost[1])}
        def memoization(cost,cache):
            n=len(cost)
            if n in cache:
                return cache[n]
            cache[n]=min(
                memoization(cost[:-2],cache)+cost[-2],
                memoization(cost[:-1],cache)+cost[-1]
            )
            return cache[n]
        return memoization(cost,cache)

# solution 3: bottom-up DP
# O(n) time and O(1) space