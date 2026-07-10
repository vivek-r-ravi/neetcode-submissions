# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS pass down max value of node so far recursively
# O(n) time O(h) space
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0
            out = 0
            if node.val >= max_val:
                out += 1
                max_val = node.val
            out += dfs(node.left, max_val)
            out += dfs(node.right, max_val)
            return out

        return dfs(root, root.val)
