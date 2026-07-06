class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n1 = len(nums1)
        n2 = len(nums2)
        partition_size = (n1+n2+1)//2

        # helper function to determine if x elements from small array makes a good partition
        def is_partition_good(x):
            small_idx = x-1
            large_idx = partition_size-x-1
            
            # border elements in the partition
            n1l = nums1[small_idx] if small_idx>=0 else -float('inf')
            n1r = nums1[small_idx+1] if small_idx+1<n1 else float('inf')
            n2l = nums2[large_idx] if large_idx>=0 else -float('inf')
            n2r = nums2[large_idx+1] if large_idx+1<n2 else float('inf')
            
            if n1l > n2r:
                return "too_big", n1l, n2l, n1r, n2r
            if n2l > n1r:
                return "too_small", n1l, n2l, n1r, n2r
            return "good", n1l, n2l, n1r, n2r
        
        # binary search on a range (0,n1)
        l = 0
        r = n1
        while l<=r:
            m = (l+r)//2
            status = is_partition_good(m)[0]
            if status == "good":
                break
            elif status == "too_big":
                r = m - 1
            else:
                l = m + 1

        _, n1l, n2l, n1r, n2r = is_partition_good(m)
        if (n1+n2)%2==1:
            return max(n1l, n2l)
        else:
            return (max(n1l, n2l) + min(n1r, n2r)) / 2