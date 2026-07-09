# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# almost brute force: check every node's in order predecessor and successor
# O(nh) time O(h) space
class SolutionV1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_max = root.left
        right_min = root.right
        while left_max or right_min:
            if left_max:
                if left_max.val >= root.val:
                    return False
                left_max = left_max.right
            if right_min:
                if right_min.val <= root.val:
                    return False
                right_min = right_min.left
        return self.isValidBST(root.left) and self.isValidBST(root.right)


# convert to array inorder and check if increasing
# O(n) time and space
class SolutionV2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)

        inorder(root)
        for i in range(1, len(out)):
            if out[i] <= out[i - 1]:
                return False
        return True


# canonical solution: inorder DFS + space compression (as only prev node needed)
# O(n) time O(h) space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inorder(node):
            nonlocal prev
            if not node:
                return True

            if not inorder(node.left):
                return False

            if prev and prev.val >= node.val:
                return False
            prev = node

            if not inorder(node.right):
                return False

            return True

        return inorder(root)
