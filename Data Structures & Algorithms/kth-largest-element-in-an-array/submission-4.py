"""
solution 1: naive brute force solution by sorting
O(nlogn) time and O(n) space due to Python's timsort
"""


# solution 2: min heap
# O(nlogk) time and O(k) space
class SolutionV2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]


# solution 3: quick select (faster here due to static array)
# O(n) avg time and O(1) space
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(l: int, r: int) -> int:
            random_idx = random.randint(l, r)
            nums[r], nums[random_idx] = nums[random_idx], nums[r]
            pivot_idx = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                    pivot_idx += 1
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
            return pivot_idx

        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            pivot_idx = partition(l, r)
            if pivot_idx == n - k:
                return nums[pivot_idx]
            elif pivot_idx < n - k:
                l = pivot_idx + 1
            else:
                r = pivot_idx - 1
