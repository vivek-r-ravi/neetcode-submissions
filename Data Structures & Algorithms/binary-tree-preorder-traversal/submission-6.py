# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: recursion
# O(h) time and O(h) space (due to recursion stack)
# class SolutionV1:
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def preorder(node):
            if not node:
                return
            out.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return out


# solution 2: iteration
# O(h) time and O(h) space (due to add'l stack)
class SolutionV2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        out = []
        stack = []

        while curr or stack:
            if curr:
                out.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return out


# solution 3: Morris traversal
# O(h) time and O(1) space
class SolutionV3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    out.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                else:
                    # revert temp connection made previously
                    prev.right = None
                    curr = curr.right

        return out
