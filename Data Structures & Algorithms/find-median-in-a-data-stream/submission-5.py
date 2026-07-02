# naive solution would be to init empty array, append on addNum and sort then find median
# for naive solution, O(1) time for init and addNum, O(nlogn) for median


# solution: two heap pattern; min heap for large elements and max heap for small elements
# O(n) space
# O(1) time for init and median, O(logn) for addNum
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        n1 = len(self.max_heap)
        n2 = len(self.min_heap)
        if n2 - n1 > 1:
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))
        elif n2 - n1 < -1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))

    def findMedian(self) -> float:
        n1 = len(self.max_heap)
        n2 = len(self.min_heap)
        if n1 == n2:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        if n1 > n2:
            return self.max_heap[0]
        else:
            return self.min_heap[0]


# follow up# 1: What if all integer numbers from the stream are in the range [0, 100]?
# use a count array of size 100. O(1) for add and O(100) for median by traversing the array


# follow up# 1: What if 99% integer numbers from the stream are in the range [0, 100]?
# use a count array of size 100, two numbers (count_less_0, count_more_100)
# O(1) for add and O(100) for median by traversing the array