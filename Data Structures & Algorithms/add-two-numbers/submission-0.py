# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 and l2:
            tmp,digit=divmod(l1.val+l2.val+carry,10)
            curr.next=ListNode(digit)
            curr=curr.next
            l1=l1.next
            l2=l2.next
            carry=tmp
        while l1:
            tmp,digit=divmod(l1.val+carry,10)
            curr.next=ListNode(digit)
            curr=curr.next
            l1=l1.next
            carry=tmp
        while l2:
            tmp,digit=divmod(l2.val+carry,10)
            curr.next=ListNode(digit)
            curr=curr.next
            l2=l2.next
            carry=tmp
        if carry>0:
            curr.next=ListNode(carry)
        return dummy.next