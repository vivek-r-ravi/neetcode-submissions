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
                    grid[r][c] = "0"
                    while q:
                        ro, co = q.popleft()
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
# convert 2D matrix to m*n 1D array to use union find
# O(m*n) time and space
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
        else:
            self.rank[p2] += 1
            self.par[p1] = p2
        return True


class SolutionUF:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dsu = UnionFind(rows * cols)

        def index(r, c):
            return r * cols + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # check all 4 sides
        directions = [(1, 0), (0, 1)]  # check only 2 sides to reduce duplicate work
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                            continue
                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands
