# reduction of House Robber (simple rob) problem
# max(simple rob without last house, simple rob without first house)
# O(n) time O(n) space due to slicing
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def simple_rob(nums):
            n = len(nums)
            prev2 = 0
            prev1 = 0
            for i in range(1, n + 1):
                curr = max(prev1, prev2 + nums[i - 1])
                prev2, prev1 = prev1, curr
            return prev1

        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))
