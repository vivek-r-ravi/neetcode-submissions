# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle and cut it
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # reverse 2nd half
        reversed_head = None
        while mid:
            tmp = mid.next
            mid.next = reversed_head
            reversed_head = mid
            mid = tmp

        # merge in-place alternating from two lists
        curr = head
        while reversed_head:
            tmp = curr.next
            curr.next = reversed_head
            curr = curr.next
            reversed_head = reversed_head.next
            curr.next = tmp
            curr = curr.next
