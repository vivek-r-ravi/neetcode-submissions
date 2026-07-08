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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)
        return out


# solution 2: iteration
# O(n) time and O(h) space (due to add'l stack)
class SolutionV2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        out = []
        stack = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                out.append(curr.val)
                curr = curr.right

        return out


# solution 3: Morris traversal
# O(n) time and O(1) space
class SolutionV3:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        out = []

        while curr:
            # if no left child, visit current node and go right
            if not curr.left:
                out.append(curr.val)
                curr = curr.right
            else:
                # find inorder predecessor (prev) of current node
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                # create temp connection between prev and curr and go left
                # this simulates the stack in standard iterative solution
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    # revert temp connection made previously
                    prev.right = None
                    out.append(curr.val)
                    curr = curr.right

        return out