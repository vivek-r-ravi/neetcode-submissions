# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        l=0
        r=len(arr)-1
        out=0
        while l<r:
            out=max(out,arr[r]+arr[l])
            l+=1
            r-=1
        return out