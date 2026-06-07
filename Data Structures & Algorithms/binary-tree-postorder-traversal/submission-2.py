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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            if node:
                out.append(node.val)
        postorder(root)
        return out        

# solution 2: iteration with 2 stacks
# O(h) on time and space (due to add'l stack)
class SolutionV2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        stack=[(root,False)]
        
        while stack:
            curr, visited=stack.pop()
            if curr:
                if not visited:
                    stack.append((curr,True))
                    stack.append((curr.right,False))
                    stack.append((curr.left,False))
                else:
                    out.append(curr.val)
        return out