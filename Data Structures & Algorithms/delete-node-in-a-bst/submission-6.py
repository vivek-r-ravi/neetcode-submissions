# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: standard recursion solution with node value copying
# O(h) on both time and space
class SolutionV1:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            minValNode = self.minValueNode(root.right)
            root.val = minValNode.val
            root.right = self.deleteNode(root.right, minValNode.val)

        return root

    def minValueNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        curr = root
        while curr.left:
            curr = curr.left
        return curr


# solution 2: recursion with node restructuring
# O(h) on both time and space
# class SolutionV2:
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            minValNode = self.minValueNode(root.right)
            minValNode.left = root.left
            return root.right

        return root

    def minValueNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        curr = root
        while curr.left:
            curr = curr.left
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

        if not curr:
            return root

        # Node with only one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent:  # if we're deleting root and it has 0/1 child
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with two children
            parMinValNode, minValNode = self.minValueNode(curr.right)

            if parMinValNode:  # if right child of current node isn't the successor
                parMinValNode.left = minValNode.right
                minValNode.right = curr.right

            minValNode.left = curr.left

            if not parent:  # if we're deleting root
                return minValNode

            if parent.left == curr:
                parent.left = minValNode
            else:
                parent.right = minValNode

        return root

    def minValueNode(self, root: TreeNode):
        curr = root
        par = None
        while curr and curr.left:
            par = curr
            curr = curr.left
        return par, curr
