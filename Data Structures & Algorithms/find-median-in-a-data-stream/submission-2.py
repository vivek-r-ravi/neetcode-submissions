import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]

    def addNum(self, num: int) -> None:
        if not self.max_heap or num<=self.max_heap[0]:
            heapq.heappush_max(self.max_heap,num)
        else:
        #elif not self.min_heap or num>self.min_heap[0]:
            heapq.heappush(self.min_heap,num)

        n1=len(self.max_heap)
        n2=len(self.min_heap)
        if n2-n1>1:
            heapq.heappush_max(self.max_heap,heapq.heappop(self.min_heap))
        elif n2-n1<-1:
            heapq.heappush(self.min_heap,heapq.heappop_max(self.max_heap))

    def findMedian(self) -> float:
        n1=len(self.max_heap)
        n2=len(self.min_heap)
        if (n1+n2)%2==0:
            return (self.max_heap[0]+self.min_heap[0])/2
        if n1>n2:
            return self.max_heap[0]
        else:
            return self.min_heap[0]

        