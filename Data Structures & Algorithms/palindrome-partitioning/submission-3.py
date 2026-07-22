# check if palindrome using 2 pointers, partition and explore further
# O(n^2 * 2^n) time as each partition splits string into 2 and each palindrome check is O(n)
# O(n) space
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out, path = [], []
        n = len(s)

        def dfs(i):
            if i >= n:
                out.append(path.copy())
                return

            for j in range(i, n):
                if not self.is_palindrome(s, i, j):
                    continue
                path.append(s[i : j + 1])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return out

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
