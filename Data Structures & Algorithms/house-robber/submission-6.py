# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack
class SolutionV1:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(i):
            if i<=0:
                return 0
            return max(dfs(i-1),dfs(i-2)+nums[i-1])
        return dfs(n)

# solution 2: top-down DP
# O(n) time and space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[None]*(n+1)
        def dfs(i):
            if i<=0:
                return 0
            if cache[i]:
                return cache[i]
            cache[i]=max(dfs(i-1),dfs(i-2)+nums[i-1])
            return cache[i]
        return dfs(n)     

# solution 3: bottom-up DP
# O(n) time and O(n) space
class SolutionV3:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        dp[1]=nums[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[n]