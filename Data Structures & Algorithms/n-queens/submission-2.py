# canonical solution: leverage diagonal pattern
# cells on same diagonal share the property (row+col) or (row-col)
# O(n!) time and O(n) space
# alternatively, create a board and mutate it instead of creating a row everytime (O(n^2) space but readable code)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out, path, pos_diag, neg_diag, cols = [], [], set(), set(), set()

        def dfs(r):
            if r == n:
                out.append(path.copy())
                return

            for c in range(n):
                if c in cols or r + c in pos_diag or r - c in neg_diag:
                    continue
                row = "." * c + "Q" + "." * (n - c - 1)
                path.append(row)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                cols.add(c)
                dfs(r + 1)
                cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                path.pop()

        dfs(0)
        return out
