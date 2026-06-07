# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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