class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        q = deque([(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==0])
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==(2**31 - 1):
                        grid[nr][nc]=dist
                        q.append((nr,nc))

