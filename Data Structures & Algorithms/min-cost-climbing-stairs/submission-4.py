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

# solution 2: top-down DP. Improved solution with memoization and passing idx instead of slicing
# O(n) time and space
class SolutionV2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={1:0,2:min(cost[0],cost[1])}
        def memoization(cost,cache,idx) -> int:
            if idx in cache:
                return cache[idx]
            cache[idx]=min(
                memoization(cost,cache,idx-2)+cost[idx-2],
                memoization(cost,cache,idx-1)+cost[idx-1]
            )
            print(cache)
            return cache[idx]
        return memoization(cost,cache,len(cost))

# solution 3: bottom-up DP
# O(n) time and O(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0,min(cost[0],cost[1])]
        n=len(cost)
        i=3
        while i<n:
            dp[0],dp[1]=dp[1],min(dp[0]+cost[i-2],dp[1]+cost[i-1])
            i+=1
        return min(
            dp[0]+cost[n-2],
            dp[1]+cost[n-1]
        )