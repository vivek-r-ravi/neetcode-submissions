# brute force with nested loops
# O(n2) time O(1) space
class SolutionV1:
    def maxSubArray(self, nums: List[int]) -> int:
        out = nums[0]
        for i in range(len(nums)):
            sub_sum = 0
            for j in range(i, len(nums)):
                sub_sum += nums[j]
                out = max(out, sub_sum)
        return out


# brute force recursion
# O(n) time O(n) space
class SolutionV2:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # dfs(x) is the sum of subarray with maximum sum ending at x index
        def dfs(x):
            if x == 0:
                return nums[0]
            return max(nums[x], nums[x] + dfs(x - 1))

        return max(dfs(i) for i in range(n))


# memoization
# O(n) time O(n) space
class SolutionV3:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {0: nums[0]}

        def dfs(x):
            if x in cache:
                return cache[x]
            cache[x] = max(nums[x], nums[x] + dfs(x - 1))
            return cache[x]

        return max(dfs(i) for i in range(n))


# tabulation
# O(n) time O(n) space
class SolutionV4:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] is the sum of subarray with maximum sum ending at x index
        dp = [nums[0]] * n
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)


# tabulation with space compression (Kadane's algorithm)
# O(n) time O(1) space
class SolutionV5:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        prev = -float("inf")
        out = nums[0]
        for num in nums:
            prev = max(num, num + prev)
            out = max(out, prev)
        return out


# Kadane's algorithm (same as V5)
# O(n) time O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = nums[0]
        sub_sum = 0
        for n in nums:
            sub_sum = max(sub_sum, 0) + n  # extend subarray from start until it becomes -ve
            out = max(out, sub_sum)
        return out


# divide and conquer
# O(nlogn) time O(logn) space
class SolutionV7:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float("-inf")

            m = (l + r) // 2
            leftSum = rightSum = curSum = 0
            for i in range(m - 1, l - 1, -1):
                curSum += nums[i]
                leftSum = max(leftSum, curSum)

            curSum = 0
            for i in range(m + 1, r + 1):
                curSum += nums[i]
                rightSum = max(rightSum, curSum)

            return max(dfs(l, m - 1), dfs(m + 1, r), leftSum + nums[m] + rightSum)

        return dfs(0, len(nums) - 1)
