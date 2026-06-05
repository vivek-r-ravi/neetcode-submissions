# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: recursion (O(h) on time and space due to recursion stack)
class Solution:
#class SolutionV1:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val==root.val:
            return root
        if val<root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

# solution 2: iteration (O(h) on time and O(1) space)
class SolutionV2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        curr=root
        while curr:
            if val==curr.val:
                return curr
            elif val<curr.val:
                curr=curr.left
            else:
                curr=curr.right
        return None
