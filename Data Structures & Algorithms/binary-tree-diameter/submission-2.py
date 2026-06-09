# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia=0
        def dfs(root):
            nonlocal max_dia
            if not root:
                return 0
            left_h=1+dfs(root.left) if root.left else 0
            right_h=1+dfs(root.right) if root.right else 0
            max_dia=max(max_dia,left_h+right_h)
            return max(left_h,right_h)
        root_dia=dfs(root)
        return max(root_dia,max_dia)