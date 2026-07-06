# O(log(mn)) time and O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            middle = (left + right) // 2
            i = middle // cols
            j = middle % cols
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
