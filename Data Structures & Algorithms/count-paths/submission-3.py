# solution 1: brute force recursion
# O(2^(m+n)) time and O(m+n) space due to recursion stack
class SolutionV1:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        def dfs(r,c):
            if r==rows or c==cols:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            return dfs(r+1,c)+dfs(r,c+1)
        return dfs(0,0)

# solution 2: top-down DP
# O(m*n) time and space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        cache=[[0]*cols for i in range(rows)]
        cache[rows-1][cols-1]=1
        def dfs(r,c):
            if r==rows or c==cols:
                return 0
            if cache[r][c]!=0:
                return cache[r][c]
            cache[r][c]=dfs(r+1,c)+dfs(r,c+1)
            return cache[r][c]
        return dfs(0,0)

# solution 3: bottom-up DP
# O(m*n) time and space
class SolutionV3:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        # define dp where dp[i][j] is the unique path count from 0,0 to i,j
        dp=[[0]*cols for i in range(rows)]
        dp[0][0]=1
        for r in range(rows):
            for c in range(cols):
                if r>0:
                    dp[r][c]+=dp[r-1][c]
                if c>0:
                    dp[r][c]+=dp[r][c-1]
        return dp[rows-1][cols-1]

# solution 4: bottom-up DP (space optimized)
# O(m*n) time and O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols=m,n
        dp=[1]*cols
        for r in range(1,rows):
            for c in range(1,cols):
                dp[c]=dp[c-1]+dp[c]
        return dp[cols-1]