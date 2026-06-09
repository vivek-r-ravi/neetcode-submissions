# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: DFS (recursive inorder)
# O(n) time due to visiting every node (worst case) and O(h) space due to recursion
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:                            # if empty tree
            return False
        if not root.left and not root.right:    # if leaf node
            return root.val==targetSum
        return (self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val))
        '''
        # above line equivalent to below:
        if self.hasPathSum(root.left,targetSum-root.val):   # explore left sub-tree   
            return True
        if self.hasPathSum(root.right,targetSum-root.val):  # explore right sub-tree
            return True
        '''
        return False                            # if both left and right return False

# solution 2: DFS (iterative inorder)
# O(n) time due to visiting every node (worst case) and O(h) space due to stack
# not implementing it as it's not a unique iteration solution

# solution 3: BFS
# O(n) time due to visiting every node and O(n) space due to queue
# not implementing it as it's not a unique iteration solution
class SolutionV3:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, targetSum - root.val)])
        while queue:
            node, curr_sum = queue.popleft()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
        return False