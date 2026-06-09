# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution: DFS tracking max diameter and recursively calculating height
# O(n) time and O(h) space
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia=0
        def dfs(root):
            nonlocal max_dia
            if not root:
                return 0
            left_h=dfs(root.left)
            right_h=dfs(root.right)
            max_dia=max(max_dia,left_h+right_h)
            return 1+max(left_h,right_h)
        dfs(root)
        return max_dia