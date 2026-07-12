# standard BFS
# O(mn) time and space
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        visit = set([(0, 0)])
        queue = deque([(0, 0)])

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr == rows
                        or c + dc == cols
                        or grid[r + dr][c + dc] == 1
                        or (r + dr, c + dc) in visit
                    ):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1

        return -1


# bidirectional BFS (less operations)
# O(mn) time and space
class SolutionV2:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        if rows == 1 and cols == 1:
            return 0

        q1 = deque([(0, 0)])
        q2 = deque([(rows - 1, cols - 1)])
        grid[0][0] = -1
        grid[rows - 1][cols - 1] = -2
        length, start, end = 1, -1, -2
        while q1 and q2:
            for _ in range(len(q1)):
                r, c = q1.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == end:
                            return length
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            q1.append((nr, nc))
            q1, q2 = q2, q1
            start, end = end, start
            length += 1

        return -1
