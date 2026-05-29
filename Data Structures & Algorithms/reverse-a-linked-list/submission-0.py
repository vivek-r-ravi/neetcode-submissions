# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1a: iteration by creating another linked list O(n) on both time and space
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:    # if empty linked list
            return head     # return empty linked list
        curr=head
        reverse_head=ListNode(curr.val)
        while curr.next:
            curr=curr.next
            reverse_head=ListNode(curr.val,reverse_head)
        return reverse_head
'''

# solution 1b: iteration efficient O(n) time and O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        return prev