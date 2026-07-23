# reduction of House Robber (simple rob) problem so reuse that solution
# max(simple rob without last house, simple rob without first house)
# O(n) time O(n) space due to slicing
class SolutionV1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def simple_rob(nums):
            prev2 = 0
            prev1 = 0
            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2, prev1 = prev1, curr
            return prev1

        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))


# remove slicing by passing indicies
# O(n) time O(1) space due to slicing
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def simple_rob(l, r):
            prev2 = 0
            prev1 = 0
            for i in range(l, r + 1):
                curr = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, curr
            return prev1

        return max(simple_rob(0, n - 2), simple_rob(1, n - 1))
