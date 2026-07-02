# solution: max heap
# O(n + nlogn) time and O(n) space
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, x - y)
        return stones[0] if stones else 0
