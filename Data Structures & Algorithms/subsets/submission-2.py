# backtracking
# O(n*2^n) time O(n) space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, out = [], []

        def dfs(i):
            if i == len(nums):
                out.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # decision to exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return out
