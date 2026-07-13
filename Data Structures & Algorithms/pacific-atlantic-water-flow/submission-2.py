# multi-source expansion BFS
# O(mn) time space
class SolutionV1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pacific = {(r, 0) for r in range(rows)} | {(0, c) for c in range(cols)}
        atlantic = {(r, cols - 1) for r in range(rows)} | {(rows - 1, c) for c in range(cols)}

        def bfs(ocean):
            q = deque(ocean)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in ocean
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        ocean.add((nr, nc))
                        q.append((nr, nc))

        bfs(pacific)
        bfs(atlantic)
        result = pacific & atlantic

        return [[r, c] for r, c in result]


# multi-source expansion DFS
# DFS also works as we care about reachability, not distance or time
# O(mn) time space
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, prev_height):
            if (
                0 <= r < rows
                and 0 <= c < cols
                and (r, c) not in ocean
                and heights[r][c] >= prev_height
            ):
                ocean.add((r, c))
                dfs(r + 1, c, ocean, heights[r][c])
                dfs(r - 1, c, ocean, heights[r][c])
                dfs(r, c + 1, ocean, heights[r][c])
                dfs(r, c - 1, ocean, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        result = pacific & atlantic

        return [[r, c] for r, c in result]
