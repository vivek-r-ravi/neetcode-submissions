import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        self.heap=nums
        self.k=k

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        else:
            heapq.heappushpop(self.heap,val)
        return self.heap[0]
        
