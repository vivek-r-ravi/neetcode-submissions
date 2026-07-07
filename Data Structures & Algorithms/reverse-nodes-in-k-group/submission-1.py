# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        global_head = head        
        group_head = head
        fast = head
        slow = head
        while slow and k!=1:
            # check if there are >= k nodes
            i = 1
            while fast and i < k:
                fast = fast.next
                i += 1
            
            # fewer than k nodes
            if not fast:
                return global_head
            
            # update head of current k group after first reversal
            if global_head != head:
                group_head.next = fast
                group_head = slow

            # reverse k nodes
            fast = fast.next
            prev = fast
            for _ in range(k):
                tmp = slow.next
                slow.next = prev
                prev = slow
                slow = tmp
            
            # update to reversed head during first reversal
            if global_head == head:
                global_head = prev

        return global_head

'''
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_head = head
        curr = head
        while curr:
            i = 1
            while curr and i < k:
                curr = curr.next
                i += 1
            if not curr:
                return dummy.next
            group_head.next = 
            prev = curr.next
            curr = group_head
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            dummy.next = prev
        return dummy.next
'''