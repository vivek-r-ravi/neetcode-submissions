class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out, path = [], []
        n = len(s)

        def dfs(i):
            nonlocal n
            if i >= n:
                out.append(path.copy())

            for j in range(i, n):
                if s[i : j + 1] != s[i : j + 1][::-1]:
                    continue
                path.append(s[i : j + 1])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return out
