# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        out = None
        if p.val > q.val:
            p, q = q, p

        def dfs(node):
            nonlocal out
            if not node:
                return
            if p.val <= node.val <= q.val:
                out = node
            elif q.val < node.val:
                dfs(node.left)
            elif node.val < p.val:
                dfs(node.right)
            else:
                return

        dfs(root)
        return out
