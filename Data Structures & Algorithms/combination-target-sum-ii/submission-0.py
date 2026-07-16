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
