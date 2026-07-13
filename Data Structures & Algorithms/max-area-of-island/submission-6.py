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
            max_area = max(max_area, dfs(*next(iter(lands))))

        return max_area


# canonical solution 2: BFS to solve this iteratively
# avoiding lands set by submerging visited lands "0"
# O(m*n) time and space
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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


# canonical solution 3: Use union-find to find number of connected components
# convert 2D matrix to m*n 1D array to use union find
# O(m*n) time and space
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return self.size[p1]
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
            return self.size[p2]
        elif self.rank[p2] < self.rank[p1]:
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
            return self.size[p1]
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
            self.size[p2] += self.size[p1]
            return self.size[p2]


class SolutionUF:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dsu = UnionFind(rows * cols)

        def index(r, c):
            return r * cols + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        directions = [(1, 0), (0, 1)]  # check only 2 sides to reduce duplicate work
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, 1)
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                            continue
                        max_area = max(max_area, dsu.union(index(r, c), index(nr, nc)))

        return max_area
