# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# concept:
# root index in inorder (mid) splits it into left and right subtree
# root is first element in preorder and mid splits preorder into left and right 

# solution 1: recursive DFS
# O(n2) time due to finding index in each recursion and O(n) space due to recursion stack
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
# O(n) time and O(n) space due to recursion stack
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:     
        indicies={val: idx for idx, val in enumerate(inorder)}
        pre_idx=0
        def dfs(l,r):
            nonlocal pre_idx
            if l>r:
                return None
            root_val=preorder[pre_idx]
            root=TreeNode(root_val)
            mid=indicies[root_val]
            pre_idx+=1
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        return dfs(0,len(preorder)-1)
