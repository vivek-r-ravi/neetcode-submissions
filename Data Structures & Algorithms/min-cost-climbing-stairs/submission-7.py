# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack if slicing not used
# O(n*2^n) time and O(n2) space due to slicing
class SolutionV1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==1:
            return 0
        if n==2:
            return min(cost[-2],cost[-1])
        return min(
            self.minCostClimbingStairs(cost[:-2])+cost[-2],
            self.minCostClimbingStairs(cost[:-1])+cost[-1]
            )

# solution 2: top-down DP. Improved solution with memoization and passing idx instead of slicing
# O(n) time and space
class SolutionV2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={0:0,1:0}
        def memoization(cost,cache,target_idx) -> int:
            if target_idx in cache:
                return cache[target_idx]
            cache[target_idx]=min(
                memoization(cost,cache,target_idx-2)+cost[target_idx-2],
                memoization(cost,cache,target_idx-1)+cost[target_idx-1]
            )
            return cache[target_idx]
        return memoization(cost,cache,len(cost))

# solution 3: bottom-up DP
# O(n) time and O(n) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        # define dp where dp[i] is the min cost to reach step i
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[i]

# solution 4: bottom-up DP (space optimized)
# O(n) time and O(1) space
class SolutionV4:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==1:
            return 0
        if n==2:
            return min(cost[0],cost[1])
        dp=[0,min(cost[0],cost[1])]
        i=3
        while i<n:
            dp[0],dp[1]=dp[1],min(dp[0]+cost[i-2],dp[1]+cost[i-1])
            i+=1
        return min(
            dp[0]+cost[n-2],
            dp[1]+cost[n-1]
        )