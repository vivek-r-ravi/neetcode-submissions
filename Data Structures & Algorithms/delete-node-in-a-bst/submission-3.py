# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: standard recursion with node value copying
# O(h) on both time and space
class Solution:
#class SolutionV1:
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

            minValNode=self.minValueNode(root.right)
            root.val=minValNode.val
            root.right=self.deleteNode(root.right,minValNode.val)
        
        return root
    
    def minValueNode(self, root: TreeNode) -> TreeNode:
        curr=root
        while curr and curr.left:
            curr=curr.left
        return curr

# solution 2: recursion with node shifting
# O(h) on both time and space
class SolutionV2:
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

            minValNode=self.minValueNode(root.right)
            minValNode.left=root.left
            return root.right
        
        return root
    
    def minValueNode(self, root: TreeNode) -> TreeNode:
        curr=root
        while curr and curr.left:
            curr=curr.left
        return curr

# solution 3: iteration but not readable
# O(h) on time and O(1) on space
class SolutionV3:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        curr = root

        # Find the node to delete
        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if not cur:
            return root

        # Node with only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with two children
            par = None  # parent of right subTree min node
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left

            if par:  # if there was a left traversal
                par.left = cur.right
                cur.right = delNode.right

            cur.left = delNode.left

            if not parent:  # if we're deleting root
                return cur

            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root