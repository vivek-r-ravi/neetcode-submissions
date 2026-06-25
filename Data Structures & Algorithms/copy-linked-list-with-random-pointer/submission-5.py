"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# two pass and hash map
# O(n) time and space
class SolutionV1:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        orig_copy_map = {None: None}
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
            copy.random = orig_copy_map[orig.random]
            copy = copy.next
            orig = orig.next
        return dummy.next


# interweaving (A->B->C to A->A'->B->B'->C->C')
# O(n) time O(1) space
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # interweave
        orig = head
        while orig:
            orig.next = Node(orig.val, orig.next)
            orig = orig.next.next

        # assign random pointers
        orig = head
        while orig:
            orig.next.random = orig.random.next if orig.random else None
            orig = orig.next.next

        # unweave the copy (and original)
        orig = head
        dummy = Node(0)
        copy = dummy
        while orig:
            copy.next = orig.next
            orig.next = orig.next.next  # restores original list too
            copy = copy.next
            orig = orig.next
            # orig = orig.next.next         # use this instead of previous line
        return dummy.next
