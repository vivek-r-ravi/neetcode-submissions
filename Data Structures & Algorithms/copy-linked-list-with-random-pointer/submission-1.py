"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# two pass
# O(n) time and space
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        orig_copy_map = dict()
        dummy = Node(0)
        copy = dummy
        orig = head
        while orig:
            copy.next = Node(orig.val)
            copy = copy.next
            orig_copy_map[orig] = copy
            orig = orig.next
        copy = dummy.next
        orig = head
        while copy:
            copy.random = orig_copy_map[orig.random] if orig.random else orig.random
            copy = copy.next
            orig = orig.next
        return dummy.next
