# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS
# O(n) time and space
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            out.append(curr.val)

        return out


# alternate canonical: DFS (preorder) but visit right before left
# O(n) time and space
class SolutionV2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(node, depth):
            if not node:
                return
            if len(out) == depth:
                out.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return out