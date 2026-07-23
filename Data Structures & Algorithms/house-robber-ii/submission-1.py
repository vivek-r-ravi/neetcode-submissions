"""
0: 0
1: nums[0]
2: max(nums[0],nums[1]); max(dp_old[1],dp_old[1:])
3: max(nums[0],nums[1],nums[2]); max(dp_old[2],dp_old[1:])
4: max(nums[0]+nums[2],nums[1]+nums[3]); max(dp_old[3],dp_old[1:])
5: max(0+2,0+3,1+3,1+4,2+4); max(dp_old[4],dp_old[1:])
.
.
i: max(dp_old[i-1],dp_old[1:]) = max(dp[i-2],dp[i-3]+num[i-1])
"""


# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack
class SolutionV1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(l, r):
            if l > r:
                return 0
            return max(dfs(l, r - 1), dfs(l, r - 2) + nums[r])

        return max(dfs(0, n - 2), dfs(1, n - 1), nums[0])


# solution 2: top down
# O(n) time and O(n) space due to recursion stack
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            cache[(l,r)] = max(dfs(l, r - 1), dfs(l, r - 2) + nums[r])
            return cache[(l,r)]

        return max(dfs(0, n - 2), dfs(1, n - 1), nums[0])
