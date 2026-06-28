# brute force
# O(n2) time and O(n) space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            char_map = dict()
            for j in range(n):
                char_map[board[i][j]] = char_map.get(board[i][j], 0) + 1
                if char_map[board[i][j]] > 1 and board[i][j] != ".":
                    return False
        for i in range(n):
            char_map = dict()
            for j in range(n):
                char_map[board[j][i]] = char_map.get(board[j][i], 0) + 1
                if char_map[board[j][i]] > 1 and board[j][i] != ".":
                    return False
        for p in range(0, n, n // 3):
            for q in range(0, n, n // 3):
                char_map = dict()
                for i in range(n // 3):
                    for j in range(n // 3):
                        char_map[board[i + p][j + q]] = char_map.get(board[i + p][j + q], 0) + 1
                        if char_map[board[i + p][j + q]] > 1 and board[i + p][j + q] != ".":
                            return False
        return True
