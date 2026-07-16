# backtracking with running total + subset (trivial)
# exponential time, O(t/m) space where t is target and m in min(nums)
class SolutionV1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combo, out = [], []

        def dfs(i, total):
            if total == target:
                out.append(combo.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # include candidates[i]
            combo.append(candidates[i])
            dfs(i+1, total + candidates[i])
            combo.pop()

            # exclude candidates[i]
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, total)

        dfs(0,0)
        return out


# backtracking with running total (optimal)
# exponential time, O(t/m) space where t is target and m in min(nums)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combo, out = [], []

        def dfs(i, total):
            if total == target:
                out.append(combo.copy())
                return
            if i >= len(candidates):
                return

            j = i
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                combo.append(candidates[j])
                dfs(j+1, total + candidates[j])
                combo.pop()

        dfs(0,0)
        return out
