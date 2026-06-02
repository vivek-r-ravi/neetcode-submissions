# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        return self.merge(self.mergeSort(pairs[:m]), self.mergeSort(pairs[m:]))

    def merge(self, nums1: List[Pair], nums2: List[Pair]) -> List[Pair]:
        if not nums2:
            return nums1
        if not nums1:
            return nums2
        i = 0
        j = 0
        out = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i].key <= nums2[j].key:
                out.append(nums1[i])
                i += 1
            else:
                out.append(nums2[j])
                j += 1
        if i < len(nums1):
            out.extend(nums1[i:])
        else:
            out.extend(nums2[j:])
        return out