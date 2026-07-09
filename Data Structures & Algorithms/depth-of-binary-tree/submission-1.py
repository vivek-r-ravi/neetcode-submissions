# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# canonical solution: DFS
# O(n) time O(h) space
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# alternate solution: BFS
# O(n) time O(n) space
from collections import deque


class SolutionV2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
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
            level += 1

        return level
