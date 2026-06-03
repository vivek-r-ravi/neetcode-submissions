# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# 3 versions: same time complexity (O(nlogn))

# version 1: do not use, creates new arrays, readable (easy to understand) but memory inefficient
# memory = recursion space (O(logn avg to n worst case)) + array creation every step (O(n)) 
class SolutionV1:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs)<=1:
            return pairs
        pivot = pairs[len(pairs)-1]
        left = [x for x in pairs if x.key<pivot.key]
        m = [x for x in pairs if x.key==pivot.key]
        right = [x for x in pairs if x.key>pivot.key]
        return quickSort(left)+ m + quickSort(right)

# version 2: standard version using recursion
# memory = recursion space (O(logn avg to n worst case))
class Solution:
#class SolutionV2:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs,0,len(pairs)-1)
        return pairs

    # Implementation of QuickSort
    def quickSortHelper(self, arr: list[Pair], left: int, right: int) -> None:
        if left >= right:
            return

        pivot = arr[right]
        pivot_idx = left

        # Partition: elements smaller than pivot on left side
        for i in range(left,right):
            if arr[i].key < pivot.key:
                arr[pivot_idx], arr[i] = arr[i], arr[pivot_idx]
                pivot_idx += 1

        # Move pivot in-between left & right sides
        arr[right], arr[pivot_idx] = arr[pivot_idx], arr[right]
        
        # Quick sort left side
        self.quickSortHelper(arr, left, pivot_idx - 1)

        # Quick sort right side
        self.quickSortHelper(arr, pivot_idx + 1, right)