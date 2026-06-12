class Solution:
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