"""
You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

Return the number of unique paths from the top-left corner of Grid to the bottom-right corner 
such that all traversed cells are land cells. You may only move vertically or horizontally 
through land cells. For an individual unique path you cannot visit the same cell twice.
"""


# O(4^mn) time and O(mn) space
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, visit):

            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            visit.add((r, c))
            count = 0
            count += dfs(r - 1, c, visit)
            count += dfs(r + 1, c, visit)
            count += dfs(r, c - 1, visit)
            count += dfs(r, c + 1, visit)
            visit.remove((r, c))

            return count

        return dfs(0, 0, set())
