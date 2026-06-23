# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force: convert to array and two pointers
# O(n) time and space
class SolutionV1:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        l = 0
        r = len(arr) - 1
        out = 0
        while l < r:
            out = max(out, arr[r] + arr[l])
            l += 1
            r -= 1
        return out


# slightly better solution: find middle with fast and slow pointers and use stack
# O(n) time and space
class SolutionV2:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        fast = head
        slow = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        out = 0
        while slow:
            out = max(out, stack.pop() + slow.val)
            slow = slow.next
        return out


# space efficient solution: fast and slow pointers and reverse list at middle
# O(n) time O(1) space
class SolutionV3:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reversed_head = None
        while slow:
            tmp = slow.next
            slow.next = reversed_head
            reversed_head = slow
            slow = tmp
        out = 0
        while reversed_head:
            out = max(reversed_head.val + head.val, out)
            head = head.next
            reversed_head = reversed_head.next
        return out


# canonical solution: reverse while finding the middle
# O(n) time O(1) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        reversed_head = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = reversed_head
            reversed_head = slow
            slow = tmp
        out = 0
        while slow:
            out = max(reversed_head.val + slow.val, out)
            slow = slow.next
            reversed_head = reversed_head.next
        return out
