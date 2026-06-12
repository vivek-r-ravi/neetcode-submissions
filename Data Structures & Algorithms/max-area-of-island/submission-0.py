# canonical solution: DFS for each island
# O(m*n) time and space
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        lands={(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==1}
        if not lands:
            return 0

        def dfs(r,c):
            nonlocal area
            if min(r,c)<0 or r==rows or c==cols or grid[r][c]==0 or (r,c) not in lands:
                return
            lands.remove((r,c))
            area+=1
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return area
        
        max_area=0
        while lands:
            area=0
            dfs(*next(iter(lands)))
            max_area=max(area,max_area)
        
        return max_area