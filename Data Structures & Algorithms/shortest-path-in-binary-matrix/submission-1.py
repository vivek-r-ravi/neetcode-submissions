class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1:
            return -1

        n=len(grid)
        neighbors=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        q=deque([(0,0)])
        visit=set([(0,0)])
        
        l=1
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                if r==n-1 and c==n-1:
                    return l
                for dr,dc in neighbors:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<n and (nr,nc) not in visit and grid[nr][nc]!=1:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            l+=1
        return -1