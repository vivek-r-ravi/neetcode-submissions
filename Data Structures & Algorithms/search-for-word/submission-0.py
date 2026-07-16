class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()

        def dfs(r, c, i):
            visited.add((r, c))
            if i + 1 == len(word):
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == word[i + 1]
                    and (nr, nc) not in visited
                    and dfs(nr, nc, i + 1)
                ):
                    return True
            visited.remove((r, c))
            return False

        i = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[i] and dfs(r, c, i):
                    return True
        return False
