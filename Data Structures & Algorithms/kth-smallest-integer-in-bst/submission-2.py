# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# solution 1: inorder DFS to get an array and return kth element
# O(n) time and space
class SolutionV1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)
        return out[k - 1]


# canonical solution: inorder DFS iteratively and stop after k elements
# O(h+k) time and O(h) space
class SolutionV2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                cnt += 1
                if cnt == k:
                    return curr.val
                curr = curr.right


# canonical solution: inorder DFS recursive and stop after k elements
# O(h+k) time and O(h) space
# class SolutionV3:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        out = None

        def inorder(node):
            nonlocal cnt, out
            if not node or out is not None:
                return

            inorder(node.left)

            if out is not None:
                return

            cnt += 1
            if cnt == k:
                out = node.val
                return

            inorder(node.right)

        inorder(root)
        return out
