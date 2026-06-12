class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        neighbors=[[-1,0],[1,0],[0,-1],[0,1]]
        q=deque([(r,c) for r in range(rows) for c in range(cols) if grid[r][c]==2])
        fresh_count=sum([1 for r in range(rows) for c in range(cols) if grid[r][c]==1])
        
        minutes=0
        while q and fresh_count:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in neighbors:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_count-=1
                        q.append((nr,nc))
            minutes+=1
        
        if fresh_count:
            return -1
        else:
            return minutes