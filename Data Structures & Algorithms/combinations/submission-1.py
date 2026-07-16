# backtracking + subset
# O(k*2^n) time O(n) space
class SolutionV1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo, out = [], []

        def dfs(i):
            if len(combo) == k:
                out.append(combo.copy())
                return
            if i > n:
                return

            combo.append(i)
            dfs(i + 1)
            combo.pop()

            dfs(i + 1)

        dfs(1)
        return out


# backtracking (optimal)
# O(k*C(n,k)) time O(k) space
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combo, out = [], []

        def dfs(i):
            if len(combo) == k:
                out.append(combo.copy())
                return
            if i > n:
                return

            for j in range(i, n + 1):
                combo.append(j)
                dfs(j + 1)
                combo.pop()

        dfs(1)
        return out
