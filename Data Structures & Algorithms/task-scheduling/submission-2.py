# heap + count hash map
# O(n) time, O(1) space as heap size is at most 26
class SolutionV1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (-min_cycle, rem_count, task) in max heap
        # min_cycle is number of cycles needed for task to be eligible for execution
        heap = [(0, count, task) for task, count in Counter(tasks).items()]
        heapq.heapify_max(heap)

        # highest count tasks in lower layer (min_cycle) is highest priority
        cycles = 0
        while heap:
            min_cycle, rem_count, task = heapq.heappop_max(heap)
            cycles = max(cycles, -1 * min_cycle) + 1    # adds idle time if needed
            rem_count -= 1
            min_cycle -= n + 1                          # handle cooldown
            if rem_count > 0:
                heapq.heappush_max(heap, (min_cycle, rem_count, task))
        return cycles


# count hash map + math
# O(n) time, O(1) space as heap size is at most 26
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        cycles = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), cycles)