# Dijkstra's
# O(n2logn) time O(n2) space
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set([(0, 0)])
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            w, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return w
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    wt = max(grid[nr][nc], w)
                    heapq.heappush(min_heap, (wt, nr, nc))
                    # adding to visited while enqueuing as visiting again won't change weight
                    visited.add((nr, nc))


# DFS + Binary Search
# O(n2logn) time O(n2) space
class SolutionV2:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # get range for t
        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
        visited = set()

        # dfs to determine if target is reacheable for a value of t
        def dfs(r, c, t):
            if min(r, c) < 0 or max(r, c) >= n or (r, c) in visited or grid[r][c] > t:
                return False
            if r == (n - 1) and c == (n - 1):
                return True
            visited.add((r, c))
            return dfs(r + 1, c, t) or dfs(r - 1, c, t) or dfs(r, c + 1, t) or dfs(r, c - 1, t)

        # lower bound binary search on a range
        l, r = minH, maxH
        while l <= r:
            m = (l + r) // 2
            if dfs(0, 0, m):
                r = m - 1
            else:
                l = m + 1
            visited.clear()

        return l


# Kruskal's (not ideal as grid needs to be converted to array of edges)
# build MST until src and dst are connected 
# O(n2logn) time O(n2) space
class SolutionV3:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # initialize union find
        par = list(range(n * n))
        rank = [0] * (n * n)

        def find(x: int) -> int:
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> bool:
            p, q = find(x), find(y)
            if p == q:
                return False
            if rank[q] < rank[p]:
                par[q] = p
            elif rank[p] < rank[q]:
                par[p] = q
            else:
                par[p] = q
                rank[q] += 1
            return True

        def connected(x: int, y: int) -> bool:
            return find(x) == find(y)

        # sort edges
        positions = sorted((grid[r][c], r, c) for r in range(n) for c in range(n))

        # union edges for node-nei wt <= t until src and target connected
        for t, r, c in positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    union(r * n + c, nr * n + nc)
            if connected(0, n * n - 1):
                return t
