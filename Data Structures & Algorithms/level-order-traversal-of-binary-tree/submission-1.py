# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: BST
# O(n) on both time and space
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out=[]
        queue=deque()
        
        if root:
            queue.append(root)

        while queue:
            lvl_out=[]
            for i in range(len(queue)):
                curr=queue.popleft()
                lvl_out+=[curr.val]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            out.append(lvl_out)

        return out

# solution 2: DFS (inorder) with a depth parameter
# O(n) on both time and space
class SolutionV2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out=[]

        def dfs(node,depth):
            if not node:
                return
            if len(out)==depth:
                out.append([])
            out[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        return out