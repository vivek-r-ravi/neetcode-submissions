# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# hashset (similar to find duplicates in array)
# O(n) time and space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset=set()
        while head:
            hashset.add(head)
            head=head.next
            if head in hashset:
                return True
        return False

