class Solution:
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
