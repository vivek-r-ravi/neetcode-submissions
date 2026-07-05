import random


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
class SolutionV3:
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


# solution 4: quick select with 3 way partition (elements <,=,> pivot) instead of 2 way
# O(n) avg time and O(1) space
# class SolutionV4:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(l: int, r: int) -> tuple[int, int]:
            random_idx = random.randint(l, r)
            nums[r], nums[random_idx] = nums[random_idx], nums[r]
            pivot = nums[r]
            lt = l  # less than pivot
            i = l  # equal to pivot
            gt = r  # greater than pivot
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt  # range where nums == pivot

        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            lt, gt = partition(l, r)
            if gt < n - k:
                l = gt + 1
            elif lt > n - k:
                r = lt - 1
            else:
                return nums[n - k]
