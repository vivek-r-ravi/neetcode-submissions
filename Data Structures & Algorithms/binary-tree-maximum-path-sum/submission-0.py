# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS: downward +ve sum and global max path sum
# O(n) time O(h) space
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = -float("inf")

        def curSum(node):
            nonlocal out
            if not node:
                return 0
            left_sum = curSum(node.left)
            right_sum = curSum(node.right)
            out = max(out, max(left_sum,0) + max(right_sum,0) + node.val)
            return max(left_sum, right_sum, 0) + node.val

        curSum(root)
        return out
