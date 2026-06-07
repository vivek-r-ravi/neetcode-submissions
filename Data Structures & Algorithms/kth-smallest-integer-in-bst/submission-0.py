# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: inorder DFS to get an array and return kth element
# O(n) on time and space
class SolutionV1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if node:
                out.append(node.val)
            inorder(node.right)
        inorder(root)
        return out[k-1]

# solution 2: inorder DFS iteratively and stop after k elements
# O(h+k) time and O(h) space
class Solution:
#class SolutionV2
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=0
        stack=[]
        curr=root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                cnt+=1
                if cnt==k:
                    return curr.val
                curr=curr.right

# solution 3: inorder DFS recursive and stop after k elements
# O(h+k) time and O(h) space
class SolutionV3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=0
        out=root.val
        def inorder(node):
            nonlocal cnt, out
            if not node:
                return
            inorder(node.left)
            cnt+=1
            if cnt==k:
                out=node.val
                return
            inorder(node.right)
        inorder(root)
        return out