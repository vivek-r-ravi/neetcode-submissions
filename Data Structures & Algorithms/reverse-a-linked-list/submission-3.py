# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1: brute force iteration by creating another array
# O(n) time and space
class SolutionV1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        # convert array to linked list using dummy
        curr = ListNode()
        dummy = curr
        for num in nums[::-1]:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next


# solution 2: brute force iteration by creating another linked list
# O(n) time and space
class SolutionV2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        while head:
            curr = ListNode(head.val, curr)
            head = head.next
        return curr


# solution 3 (canonical): pointer manipulation using two pointers
# O(n) time and O(1) space
# class SolutionV3:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


# solution 4: recursion
# O(n) on both time and space
class SolutionV4:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
