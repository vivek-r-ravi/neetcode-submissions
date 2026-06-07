# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution 1: inorder traversal (recursion or iteration) in an array on init
# O(h) time and space for init, O(1) time and O(h) space for next and hasNext 
class BSTIteratorV1:

    def __init__(self, root: Optional[TreeNode]):
        self.arr=[]
        curr=root
        stack=[]
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                self.arr.append(curr.val)
                curr=curr.right
        self.cur=-1

    def next(self) -> int:
        self.cur+=1
        return self.arr[self.cur]

    def hasNext(self) -> bool:
        return True if self.cur+1<len(self.arr) else False

# solution 2: split inorder traversal (iteration) into 3 steps, one for each function
# O(1) time and O(h) space for all 3
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.curr=root

    def next(self) -> int:
        while self.curr:
            self.stack.append(self.curr)
            self.curr=self.curr.left
        self.curr=self.stack.pop()
        val=self.curr.val
        self.curr=self.curr.right
        return val

    def hasNext(self) -> bool:
        if self.curr or self.stack:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()