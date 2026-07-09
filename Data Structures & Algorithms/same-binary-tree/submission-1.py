# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# O(n) time O(h) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return True if not q else False
        if not q:
            return False
        return (
            p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        )
