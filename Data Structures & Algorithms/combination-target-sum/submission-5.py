# backtracking with running total + subset (trivial)
# exponential time, O(t/m) space where t is target and m in min(nums)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combo, out = [], []

        def dfs(i, total):
            if total == target:
                out.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return

            # include nums[i]
            combo.append(nums[i])
            dfs(i, total + nums[i])
            combo.pop()

            # exclude nums[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return out


# backtracking with running total (optimal)
# exponential time, O(t/m) space where t is target and m in min(nums)
class SolutionV1:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combo, out = [], []

        def dfs(i, total):
            if total == target:
                out.append(combo.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                combo.append(nums[j])
                dfs(j, total + nums[j])
                combo.pop()

        dfs(0, 0)
        return out
