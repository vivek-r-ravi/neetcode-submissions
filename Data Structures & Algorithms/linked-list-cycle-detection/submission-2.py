# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# hashset (similar to find duplicates in array)
# O(n) time and space
class SolutionV1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        while head:
            hashset.add(head)
            head = head.next
            if head in hashset:
                return True
        return False


# fast and slow pointers
# O(n) time and O(1) space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


# solution below for Linked List Cycle Detection II problem
# return the node where the cycle begins
# if no cycle, return null


# hashset (similar to find duplicates in array)
# O(n) time and space
class SolutionIIV1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        while head:
            hashset.add(head)
            head = head.next
            if head in hashset:
                return head
        return


# fast and 2 slow pointers
# O(n) time and O(1) space
class SolutionII:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not (fast and fast.next):
            return

        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next

        return slow
