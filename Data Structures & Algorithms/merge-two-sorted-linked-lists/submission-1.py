# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        array1,array2=[],[]
        while list1:
            array1.append(list1.val)
            list1=list1.next
        while list2:
            array2.append(list2.val)
            list2=list2.next
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
        head=None
        for i in reversed(out):
            head=ListNode(i,head)
        return head
        '''
        curr=list1 if list1.val<=list2.val else list2
        while list1 and list2:
            if list1.val<=list2.val:
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
        curr.next=list1 if list1 else list2
        return head
        '''
        '''
        # merging two sorted lists
        out=[]
        i=j=0
        while i<n1 and j<n2:
            if list1[i]<=list2[j]:
                out.append(list1[i])
                i+=1
            else:
                out.append(list2[j])
                j+=1
        if i<n1:
            out+=list1[i:]
        else:
            out+=list2[j:]
        return out
        '''