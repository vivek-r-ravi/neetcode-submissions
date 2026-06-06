# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: recursion
# O(h) on both time and space (due to recursion stack)
class Solution:
#class SolutionV1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        def preorder(node):
            if not node:
                return
            if node: 
                out.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return out
    
# solution 2: iteration
# O(h) on time and space (due to add'l stack)
class SolutionV2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        out=[]
        stack=[]
        
        while curr or stack:
            if curr:
                out.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return out