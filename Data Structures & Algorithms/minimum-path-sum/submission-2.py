class SolutionV1:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if r==0 and c==0:
                return grid[0][0]
            if r<0 or c<0:
                return float('inf')
            return min(dfs(r-1,c),dfs(r,c-1))+grid[r][c]
        return dfs(rows-1,cols-1)

class SolutionV2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        cache=[[float('inf')]*cols for _ in range(rows)]
        cache[0][0]=grid[0][0]
        def dfs(r,c):
            if r<0 or c<0:
                return float('inf')
            if cache[r][c]!=float('inf'):
                return cache[r][c]
            cache[r][c]=min(dfs(r-1,c),dfs(r,c-1))+grid[r][c]
            return cache[r][c]
        return dfs(rows-1,cols-1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[[float('inf')]*cols for _ in range(rows)]
        dp[0][0]=grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if r>=1 and c>=1:
                    dp[r][c]=min(dp[r-1][c],dp[r][c-1])+grid[r][c]
                elif r>=1:
                    dp[r][c]=dp[r-1][c]+grid[r][c]
                elif c>=1:
                    dp[r][c]=dp[r][c-1]+grid[r][c]
        return dp[rows-1][cols-1]