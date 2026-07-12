# canonical solution: DFS for each island
# O(m*n) time and space
class SolutionV1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        max_area = 0
        lands = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1}
        if not lands:
            return max_area

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) not in lands:
                return 0
            lands.remove((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        while lands:
            max_area =max(max_area, dfs(*next(iter(lands))))

        return max_area


# canonical solution 2: BFS to solve this iteratively
# avoiding lands set by submerging visited lands "0"
# O(m*n) time and space
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        out = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q = deque([(r, c)])
                    grid[r][c] = 0
                    area = 1
                    while q:
                        for _ in range(len(q)):
                            ro, co = q.popleft()
                            for dr, dc in directions:
                                if (
                                    0 <= ro + dr < rows
                                    and 0 <= co + dc < cols
                                    and grid[ro + dr][co + dc] == 1
                                ):
                                    q.append((ro + dr, co + dc))
                                    grid[ro + dr][co + dc] = 0
                                    area += 1
                    out = max(out, area)
        return out
