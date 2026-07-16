# DFS + backtracking
# O(m*n*4^(L)) time and O(L) space for recursion stack + visited set where L is length of word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= rows
                or c >= cols
                or board[r][c] != word[i]
                or (r, c) in visited
            ):
                return False

            visited.add((r, c))
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


# visited set space can be avoided by marking visited cells as "#" (mutation) and restoring back to original
"""
board[r][c] = "#"
.
.
board[r][c] = word[i]
"""
