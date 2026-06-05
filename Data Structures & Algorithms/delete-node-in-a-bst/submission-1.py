# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minValNode=self.minValueNode(root.right)
                root.val=minValNode.val
                root.right=self.deleteNode(root.right,minValNode.val)
        return root
    
    def minValueNode(self, root: TreeNode) -> TreeNode:
        curr=root
        while curr and curr.left:
            curr=curr.left
        return curr