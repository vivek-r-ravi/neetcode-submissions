# brute force
# O(n2) time and O(n) space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            seen = set()
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for i in range(n):
            seen = set()
            for j in range(n):
                val = board[j][i]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for p in range(0, n, n // 3):
            for q in range(0, n, n // 3):
                seen = set()
                for i in range(n // 3):
                    for j in range(n // 3):
                        val = board[i + p][j + q]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True
