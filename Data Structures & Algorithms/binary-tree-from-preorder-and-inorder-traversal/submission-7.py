# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# brute force DFS
# O(n2) time due to finding index in each recursion and O(n+h) space due to array slicing/copying
class SolutionV1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


# solution 2: recursive DFS with hashmap, passing in indicies to avoid extra arrays
# O(n) time and O(n+h) space due to recursion stack and hashmap
class SolutionV2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indicies = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = indicies[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(preorder) - 1)


# solution 3: recursive DFS with a limit
# O(n) time and O(h) due to recursion stack
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        in_idx = 0

        def dfs(limit):
            nonlocal pre_idx, in_idx
            if pre_idx >= len(preorder):
                return None
            if inorder[in_idx] == limit:
                in_idx += 1
                return None

            root = TreeNode(preorder[pre_idx])
            pre_idx += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root

        return dfs(float("inf"))
