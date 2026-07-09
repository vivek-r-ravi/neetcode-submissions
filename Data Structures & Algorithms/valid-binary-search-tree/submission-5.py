# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brute force: convert to array inorder and check if increasing
# O(n) time and space
class SolutionV1:
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


# canonical solution: 
# O(n) time O(h) space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev = root.left
        next = root.right
        while prev or next:
            if prev:
                if prev.val>=root.val:
                    return False
                prev = prev.right
            if next: 
                if next.val<=root.val:
                    return False
                next = next.left
        return self.isValidBST(root.left) and self.isValidBST(root.right)


        
