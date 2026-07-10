# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        out = 0
        
        def dfs(node, max_val):
            nonlocal out
            if not node:
                return
            if node.val>=max_val:
                out += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, -float('inf'))
        return out
