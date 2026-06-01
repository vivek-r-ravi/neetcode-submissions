# O(m+n) on time using three pointers and extra space (O(m))
# extra space can be avoided by modifying nums1 from back

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        if m==0:
            nums1[:]=nums2
            return
        l=nums1[:m]
        i=0
        j=0
        k=0
        while i<m and j<n:
            if l[i]<=nums2[j]:
                nums1[k]=l[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        if i<m:
            nums1[k:]=l[i:m]
        else:
            nums1[k:]=nums2[j:]