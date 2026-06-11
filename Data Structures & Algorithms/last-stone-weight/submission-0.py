import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        if len(stones)==2:
            return abs(stones[0]-stones[1])
        heapq.heapify_max(stones)
        while len(stones)>1:
            x=heapq.heappop_max(stones)
            y=heapq.heappop_max(stones)
            if x!=y:
                heapq.heappush_max(stones,x-y)
        return stones[0] if stones else 0