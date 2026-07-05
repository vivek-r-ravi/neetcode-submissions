# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# merge sort algorithm: divide and conquer and merge 2 linked lists
# O(nlogk) time O(n) space
# space can be optimized further by passing in indicies as function argument
# instead of slicing list. e.g. (lists,0,m) instead of lists[:m]
class SolutionV1:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return
        elif k == 1:
            return lists[0]
        m = k // 2
        return self.mergeTwoLists(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))


# merge sort algorithm: divide and conquer and merge 2 linked lists
# O(nlogk) time O(logk) space
# class SolutionV2
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return dummy.next

    def mergeKListsHelper(self, lists: List[Optional[ListNode]], l, r) -> Optional[ListNode]:
        if l > r:
            return
        elif l == r:
            return lists[l]
        m = (l + r) // 2
        return self.mergeTwoLists(
            self.mergeKListsHelper(lists, l, m), self.mergeKListsHelper(lists, m + 1, r)
        )

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)


# heap solution
# O(nlogk) time O(k) space
class SolutionV3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]  # i needed for tie breaker
        heapq.heapify(heap)
        dummy = ListNode()
        curr = dummy
        while heap:
            _, idx, curr.next = heapq.heappop(heap)
            if curr.next.next:
                heapq.heappush(heap, (curr.next.next.val, idx, curr.next.next))
            curr = curr.next
        return dummy.next
