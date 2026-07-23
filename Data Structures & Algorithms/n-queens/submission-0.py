class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out, path, placed, placed_rows = [], [], set(), set()

        def dfs(c):
            if c == n:
                out.append(path.copy())
                return

            for r in range(n):
                if self.isBlocked(n, r, c, placed, placed_rows):
                    continue
                row = "." * r + "Q" + "." * (n - r - 1)
                path.append(row)
                placed.add((r, c))
                placed_rows.add(r)
                dfs(c + 1)
                placed_rows.remove(r)
                placed.remove((r, c))
                path.pop()

        dfs(0)
        return out

    def isBlocked(self, n, r, c, placed, placed_rows) -> bool:
        if r in placed_rows:
            return True
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if (i, j) in placed:
                return True
        for i, j in zip(range(r + 1, n), range(c - 1, -1, -1)):
            if (i, j) in placed:
                return True
        return False
