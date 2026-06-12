# solution 1: DFS
# O(m*n) on time and space
class SolutionV1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        s_color=image[sr][sc]
        def dfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or image[r][c]!=s_color or image[r][c]==color:
                return
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image

# solution 2: BFS
# O(m*m) on time and space
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
        s_color=image[sr][sc]
        queue=deque([(sr,sc)])
        image[sr][sc]=color
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                neighbors=[[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in neighbors:
                    if min(r+dr,c+dc)<0 or r+dr==rows or c+dc==cols or image[r+dr][c+dc]!=s_color or image[r+dr][c+dc]==color:
                        continue
                    queue.append((r+dr,c+dc))
                    image[r+dr][c+dc]=color
        return image