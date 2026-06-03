# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# 3 versions: same time complexity

# version 1: classic (easy to understand), uses array slicing and recursion
# memory = slice space + recursion space (O(logn)) + merge space (out array - O(n))
''' 
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        return self.merge(self.mergeSort(pairs[:m]), self.mergeSort(pairs[m:]))

    def merge(self, nums1: List[Pair], nums2: List[Pair]) -> List[Pair]:
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
'''

# version 2: optimized recursion, avoids slicing by passing indicies and aux array
# memory = recursion space (O(logn)) + merge space (aux array - O(n))
# aux array occupies same space as out (v1) but it is created only once
# out array (v1) is created during each merge operation  
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # allocate the auxiliary array EXACTLY ONCE.
        aux = pairs[:] 
        self.mergeSortHelper(pairs, aux, 0, len(pairs) - 1)
        return pairs

    def mergeSortHelper(self, pairs: List[Pair], aux: List[Pair], left: int, right: int) -> None:
        if left >= right:
            return pairs  
        m = (left + right) // 2
        self.mergeSortHelper(pairs, aux, left, m)
        self.mergeSortHelper(pairs, aux, m+1, right)
        self.merge(pairs, aux, left, m, right)

    def merge(self, pairs: List[Pair], aux: List[Pair], left: int, m: int, right: int) -> None:
        # Copy the current segment of interest into the auxiliary array
        for k in range(left, right + 1):
            aux[k] = pairs[k]
        i = left
        j = m+1
        k = left
        while i <= m and j <= right:
            if aux[i].key <= aux[j].key:
                pairs[k]=aux[i]
                i += 1
            else:
                pairs[k]=aux[j]
                j += 1
            k += 1
        while i <= m:
            pairs[k]=aux[i]
            i += 1
            k += 1
        while j <= right:
            pairs[k]=aux[j]
            j += 1
            k += 1