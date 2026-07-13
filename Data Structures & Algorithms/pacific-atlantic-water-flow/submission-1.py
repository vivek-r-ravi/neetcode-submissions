class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pacific = set([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        atlantic = set([(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)])

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
