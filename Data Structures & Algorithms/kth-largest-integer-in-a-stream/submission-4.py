"""
A naive brute force solution would maintain a sorted array nums on init (O(nlogn) time).
For every self.add, insert the val into sorted nums (O(n) time) and return (n-k)th element.
O(n) space
Note: In a data stream, time complexity of self.add is much more important than init.
"""


# solution: maintain min heap of size k. smallest element in heap is kth largest in stream
# O(k) space
# time: O(logk) for add and O(n + (n-k)logn) for init
# if n>>k, creating empty heap and then doing an self.add for every element in num is more optimal for init (O(nlogk))
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
