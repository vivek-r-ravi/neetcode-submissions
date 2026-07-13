# multi-source expansion DFS
# O(mn) time and space
class SolutionV1:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, not_surround):
            if (
                0 <= r < rows
                and 0 <= c < cols
                and (r, c) not in not_surround
                and board[r][c] == "O"
            ):
                not_surround.add((r, c))
                dfs(r + 1, c, not_surround)
                dfs(r - 1, c, not_surround)
                dfs(r, c + 1, not_surround)
                dfs(r, c - 1, not_surround)

        not_surround = set()
        for r in range(rows):
            dfs(r, 0, not_surround)
            dfs(r, cols - 1, not_surround)
        for c in range(cols):
            dfs(0, c, not_surround)
            dfs(rows - 1, c, not_surround)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in not_surround and board[r][c] == "O":
                    board[r][c] = "X"


# multi-source expansion BFS
# O(mn) time and space
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        not_surround = set()
        for r in range(rows):
            if board[r][0] == "O":
                not_surround.add((r, 0))
            if board[r][cols - 1] == "O":
                not_surround.add((r, cols - 1))
        for c in range(cols):
            if board[0][c] == "O":
                not_surround.add((0, c))
            if board[rows - 1][c] == "O":
                not_surround.add((rows - 1, c))

        def bfs(not_surround):
            q = deque(not_surround)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in not_surround
                        and board[nr][nc] == "O"
                    ):
                        not_surround.add((nr, nc))
                        q.append((nr, nc))

        bfs(not_surround)
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in not_surround and board[r][c] == "O":
                    board[r][c] = "X"
