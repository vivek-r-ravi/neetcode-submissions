# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev_group_tail = dummy
        while True:
            # check if there are >= k nodes
            i = 1
            kth = prev_group_tail.next
            while kth and i < k:
                kth = kth.next
                i += 1

            # if fewer than k nodes (kth node is null)
            if not kth:
                return dummy.next

            # update head of next k group
            next_group_head = kth.next

            # reverse k nodes
            curr = prev_group_tail.next
            prev = next_group_head
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect previous group to reversed group
            old_group_head = prev_group_tail.next
            prev_group_tail.next = kth
            prev_group_tail = old_group_head
