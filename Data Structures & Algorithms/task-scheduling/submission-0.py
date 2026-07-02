# count hash map + heap
#
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (min_cycle, count, task) in max heap
        heap = [(0, count, task) for task, count in Counter(tasks).items()]
        heapq.heapify_max(heap)

        # highest count tasks is highest priority
        out = 0
        while heap:
            min_cycle, count, task = heapq.heappop_max(heap)
            count -= 1
            out = max(out, -1 * min_cycle) + 1
            min_cycle -= n + 1
            if count > 0:
                heapq.heappush_max(heap, (min_cycle, count, task))
        return out
