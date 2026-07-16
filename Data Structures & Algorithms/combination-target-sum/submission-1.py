class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        combo, out = [], []

        def dfs(i, cur_sum):
            if cur_sum == target:
                out.append(combo.copy())
                return
            elif cur_sum > target:
                return

            for j in range(i,len(nums)):
                if cur_sum + nums[j] > target:
                    break
                combo.append(nums[j])
                dfs(j, cur_sum + nums[j])
                combo.pop()

        dfs(0,0)
        return out