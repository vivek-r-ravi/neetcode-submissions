# brute force recursion
# exponential time, O(n) space
class SolutionV1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # state: dfs(i) is length of LIS at end of i index in nums
        def dfs(i):
            if i==0:
                return 1
            best=1
            for j in range(i):
                if nums[j]<nums[i]:
                    best=max(best,1+dfs(j))
            return best
        return max(dfs(i) for i in range(n))

# memoization
# O(n2) time, O(n) space
class SolutionV2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache={0:1}
        def dfs(i):
            if i in cache:
                return cache[i]
            best=1
            for j in range(i):
                if nums[j]<nums[i]:
                    best=max(best,1+dfs(j))
            cache[i]=best
            return cache[i]
        return max(dfs(i) for i in range(n))

# tabulation
# O(n2) time, O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # state: dp[i] is length of LIS at end of i index in nums
        dp=[1]*n
        dp_best=1
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],1+dp[j])
            dp_best=max(dp_best,dp[i])
        return dp_best