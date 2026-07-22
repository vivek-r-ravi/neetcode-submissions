class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out, path = [], []
        n = len(s)

        def dfs(i):
            nonlocal n
            if i >= n:
                out.append(path.copy())
                return

            for j in range(i, n):
                if not self.is_palindrome(s[i : j + 1]):
                    continue
                path.append(s[i : j + 1])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return out

    def is_palindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
