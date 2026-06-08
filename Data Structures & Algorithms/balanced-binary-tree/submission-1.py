# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: brute force - calculate height of each subtree and determine BF
# O(n2) time and O(n) space due to recursion stack
class SolutionV1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balance_factor=self.height(root.right)-self.height(root.left)
        if abs(balance_factor)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        
# solution 2: DFS (postorder) and calculate height, BF at each step
# O(n) time and O(h) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if not node:
                return 0, True
            left=dfs(node.left)
            right=dfs(node.right)
            bf=right[0]-left[0]
            return 1+max(left[0],right[0]), left[1] and right[1] and abs(bf)<=1
        return dfs(root)[1]

# solution 3: DFS (iterative postorder) and calculate height, BF at each step
# O(n) time and O(n) space due to storing every node's height
class SolutionV3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack=[(root,False)]
        height=dict()
        while stack:
            curr, visited = stack.pop()
            if curr:
                if not visited:
                    stack.append((curr,True))
                    if curr.right:
                        stack.append((curr.right,False))
                    if curr.left:
                        stack.append((curr.left,False))
                else:
                    left=height[curr.left] if curr.left else 0
                    right=height[curr.right] if curr.right else 0
                    bf=right-left
                    if abs(bf)>1:
                        return False
                    height[curr]=1+max(left,right)
        return True