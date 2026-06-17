# brute force recursion
# exponential time, O(n) space
class SolutionV1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # state: dfs(i) is max length of subsequence at end of i index in nums
        def dfs(i):
            if i==0:
                return 1
            l_max=1
            for j in range(i):
                if nums[j]<nums[i]:
                    l_max=max(l_max,1+dfs(j))
            return l_max
        return max(dfs(i) for i in range(n))

# memoization
# exponential O(n) time, O(n) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache={0:1}
        def dfs(i):
            if i in cache:
                return cache[i]
            l_max=1
            for j in range(i):
                if nums[j]<nums[i]:
                    l_max=max(l_max,1+dfs(j))
            cache[i]=l_max
            return cache[i]
        return max(dfs(i) for i in range(n))