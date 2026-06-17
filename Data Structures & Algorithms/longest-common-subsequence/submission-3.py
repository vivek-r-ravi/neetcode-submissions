# brute force recursion
# exponential O(2^m+n) time and O(m+n) space
class SolutionV1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dfs(x,y) is the length of LCS with first x and y indicies of text1 and text2
        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if text1[x] == text2[y]:
                return 1 + dfs(x - 1, y - 1)
            else:
                return max(dfs(x, y - 1), dfs(x - 1, y))

        return dfs(m - 1, n - 1)


# memoization
# O(mn) time and O(mn) space
class SolutionV2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        cache = [[-1] * n for i in range(m)]

        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if cache[x][y] != -1:
                return cache[x][y]
            if text1[x] == text2[y]:
                cache[x][y] = 1 + dfs(x - 1, y - 1)
            else:
                cache[x][y] = max(dfs(x, y - 1), dfs(x - 1, y))
            return cache[x][y]

        return dfs(m - 1, n - 1)


# tabulation
# O(mn) time and O(mn) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # dp[x][y] is the length of LCS with first x and y elements of text1 and text2
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
