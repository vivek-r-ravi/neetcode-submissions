"""
solution 1: naive brute force solution by sorting
O(nlogn) time and O(1) space due to Python's timsort
"""


# solution 2: min heap
# O(nlogk) time and O(k) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        return heap[0]


# solution 3: quick select (faster here due to static array)
# O(n) time and O(1) space
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect()
"""
