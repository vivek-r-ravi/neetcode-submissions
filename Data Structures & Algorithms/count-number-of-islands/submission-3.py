# canonical solution 1: DFS for each island
# O(m*n) time and space
class SolutionV1:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        lands = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "1"}
        if not lands:
            return 0

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0" or (r, c) not in lands:
                return
            lands.remove((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        out = 0
        while lands:
            dfs(*next(iter(lands)))
            out += 1

        return out


# canonical solution 2: Use BFS to solve this iteratively
# avoiding lands set by submerging visited lands "0"
# O(m*n) time and space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        out = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    q = deque([(r, c)])
                    while q:
                        for _ in range(len(q)):
                            ro, co = q.popleft()
                            grid[ro][co] = "0"
                            for dr, dc in directions:
                                if (
                                    0 <= ro + dr < rows
                                    and 0 <= co + dc < cols
                                    and grid[ro + dr][co + dc] == "1"
                                ):
                                    q.append((ro + dr, co + dc))
                                    grid[ro + dr][co + dc] = "0"
                    out += 1
        return out


# canonical solution 3: Use union-find to find number of connected components
# O(m*n) time and space
class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True


class SolutionUF:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = UnionFind(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands
