# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brute force: DFS with height and diameter calculation at each node
# O(n2) time O(h) space
class SolutionV1:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.height(root.left) + self.height(root.right),
        )

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


# canonical solution: DFS tracking max diameter and recursively calculating height
# O(n) time and O(h) space
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0

        def height(root):
            nonlocal out
            if not root:
                return 0
            left_h = height(root.left)
            right_h = height(root.right)
            out = max(out, left_h + right_h)
            return 1 + max(left_h, right_h)

        height(root)
        return out
