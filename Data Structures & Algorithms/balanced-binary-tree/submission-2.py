# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brute force: calculate height and running isBalanced at each node
# O(n2) time and O(h) space due to recursion stack
class SolutionV1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        if abs(self.height(root.right) - self.height(root.left)) > 1:
            return False
        return True

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


# canonical solution: DFS (postorder); calculate height, BF at same time
# O(n) time and O(h) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root: Optional[TreeNode]) -> tuple[int, bool]:
            if not root:
                return 0, True
            left_h, left_balance = height(root.left)
            right_h, right_balance = height(root.right)
            return 1 + max(left_h, right_h), left_balance and right_balance and abs(
                left_h - right_h
            ) <= 1

        return height(root)[1]


# solution 3: DFS (iterative postorder) and calculate height, BF at each step
# O(n) time and O(n) space due to storing every node's height
class SolutionV3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        height = dict()
        while stack:
            curr, visited = stack.pop()
            if curr:
                if not visited:
                    stack.append((curr, True))
                    if curr.right:
                        stack.append((curr.right, False))
                    if curr.left:
                        stack.append((curr.left, False))
                else:
                    left = height[curr.left] if curr.left else 0
                    right = height[curr.right] if curr.right else 0
                    bf = right - left
                    if abs(bf) > 1:
                        return False
                    height[curr] = 1 + max(left, right)
        return True
