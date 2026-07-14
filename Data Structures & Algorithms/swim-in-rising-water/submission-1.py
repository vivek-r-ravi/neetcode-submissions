class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set([(0,0)])
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            w, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return w 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    wt = max(grid[nr][nc], w)
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (wt, nr, nc))
