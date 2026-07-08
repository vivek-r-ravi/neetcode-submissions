# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: recursion
# O(n) time and O(h) space (due to recursion stack)
# class SolutionV1:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            out.append(node.val)

        postorder(root)
        return out


# solution 2: iteration with 2 stacks
# O(n) time and O(h) space (due to add'l stack)
class SolutionV2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = [(root, False)]

        while stack:
            curr, visited = stack.pop()
            if curr:
                if not visited:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))
                else:
                    out.append(curr.val)
        return out


# solution 3: iteration with 1 stacks (reverse of preorder)
# O(n) time and O(h) space (due to add'l stack)
class SolutionV3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        out = []
        stack = []

        while curr or stack:
            if curr:
                out.append(curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left

        return out[::-1]


# solution 4: reverse preorder Morris traversal result
# O(n) time and O(1) space
class SolutionV4:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        out = []

        while curr:
            if not curr.right:
                out.append(curr.val)
                curr = curr.left
            else:
                prev = curr.right
                while prev.left and prev.left != curr:
                    prev = prev.left

                if not prev.left:
                    out.append(curr.val)
                    prev.left = curr
                    curr = curr.right
                else:
                    prev.right = None
                    curr = curr.left

        return out[::-1]