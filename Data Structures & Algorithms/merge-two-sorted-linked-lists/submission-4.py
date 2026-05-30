# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1: brute force
# convert to 2 sorted lists, use 2 pointers to merge them and convert to linked list
# O(m+n) on both time and space
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # convert to sorted lists
        array1,array2=[],[]
        while list1:
            array1.append(list1.val)
            list1=list1.next
        while list2:
            array2.append(list2.val)
            list2=list2.next
        # merge lists
        out=[]
        i=j=0
        while i<len(array1) and j<len(array2):
            if array1[i]<=array2[j]:
                out.append(array1[i])
                i+=1
            else:
                out.append(array2[j])
                j+=1
        if i<len(array1):
            out+=array1[i:]
        else:
            out+=array2[j:]
        # convert to linked list using reverse iteration
        head=None
        for i in reversed(out):
            head=ListNode(i,head)
        return head
        # (another way) convert to linked list using dummy
        dummy=ListNode()
        curr=dummy
        for i in out:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
'''

# solution 2: iterative using pointer manipulation (two pointers and dummy node)
# O(m+n) on time and O(1) space
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                curr=curr.next
                list1=list1.next
            else:
                curr.next=list2
                curr=curr.next
                list2=list2.next
        curr.next=list1 if list1 else list2
        return dummy.next
'''

# solution 3: recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val<=list2.val:
            newHead=list1
            list1=list1.next
        else:
            newHead=list2
            list2=list2.next
        newHead.next=self.mergeTwoLists(list1,list2)
        return newHead
            
