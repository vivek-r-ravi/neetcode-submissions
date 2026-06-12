class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        
        lands={(r,c) for r in range(rows) for c in range(cols) if grid[r][c]=="1"}
        if not lands:
            return 0

        def dfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or grid[r][c]=="0" or (r,c) not in lands:
                return
            lands.remove((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        out=0
        while lands:
            dfs(*next(iter(lands)))
            out+=1
        
        return out
            