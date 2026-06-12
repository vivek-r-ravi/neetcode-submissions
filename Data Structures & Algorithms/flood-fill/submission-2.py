# solution 1: DFS
# O(m*n) on time and space
class SolutionV1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color=image[sr][sc]
        if color==s_color:
            return image
        rows,cols=len(image),len(image[0])
        def dfs(r,c):
            if min(r,c)<0 or r==rows or c==cols or image[r][c]!=s_color:
                return
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image

# solution 2: BFS
# O(m*n) on time and space
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color=image[sr][sc]
        if color==s_color:
            return image
        rows,cols=len(image),len(image[0])
        queue=deque([(sr,sc)])
        image[sr][sc]=color
        while queue:
            r,c=queue.popleft()
            neighbors=[[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in neighbors:
                if 0<=r+dr<rows and 0<=c+dc<cols and image[r+dr][c+dc]==s_color:
                    queue.append((r+dr,c+dc))
                    image[r+dr][c+dc]=color
        return image