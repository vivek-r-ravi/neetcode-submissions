# canonical solution: DFS for each island
# O(m*n) time and space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        lands={(r,c) for r in range(rows) for c in range(cols) if grid[r][c]=="1"}
        if not lands:
            return 0

        def dfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or grid[r][c]=="0" or (r,c) not in lands:
                return
            lands.remove((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        out=0
        while lands:
            dfs(*next(iter(lands)))
            out+=1
        
        return out
            
# alternate solution: lands set can be avoided by submerging visited lands "0"
# alternate solution: Use BFS to solve this iteratively