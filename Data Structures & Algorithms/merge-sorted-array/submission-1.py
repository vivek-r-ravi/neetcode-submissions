# solution 1: in-place merge using 3 pointers
# O(m+n) time O(m) space
# extra space can be avoided by modifying nums1 from back
class SolutionV1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return
        l = nums1[:m]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if l[i] <= nums2[j]:
                nums1[k] = l[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if i < m:
            nums1[k:] = l[i:m]
        else:
            nums1[k:] = nums2[j:]


# canonical: in-place merge from back using 3 pointers
# O(m+n) time O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return
        last = m + n - 1
        i, j = m - 1, n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1