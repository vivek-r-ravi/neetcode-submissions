# brute force
# O(n*k) time O(1) space
class SolutionV1:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        completed = 0
        rem = len(profits)
        out = w
        while completed < k and rem > 0:
            max_p = (0, rem)
            for i in range(rem):
                if out >= capital[i] and profits[i] > max_p[0]:
                    max_p = (profits[i], i)
            if max_p[1] < rem:
                profits[max_p[1]], profits[-1] = profits[-1], profits[max_p[1]]
                capital[max_p[1]], capital[-1] = capital[-1], capital[max_p[1]]
                profits.pop()
                capital.pop()
                completed += 1
                rem -= 1
                out += max_p[0]
            else:
                break
        return out


# two heap
# O(nlogn + klogn) time O(n) space
class SolutionV2:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(capital_heap)
        profit_heap = []
        out = w
        for _ in range(k):
            while capital_heap and out >= capital_heap[0][0]:
                heapq.heappush_max(profit_heap, heapq.heappop(capital_heap)[1])
            if profit_heap:
                out += heapq.heappop_max(profit_heap)
            else:
                break
        return out


# canonical solution: sort + priority list using max heap
# O(nlogn + klogn) time O(n) space
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = [(c, p) for c, p in zip(capital, profits)]
        capital_heap.sort()
        profit_heap = []
        idx = 0
        out = w
        for _ in range(k):
            while idx < len(capital_heap) and out >= capital_heap[idx][0]:
                heapq.heappush_max(profit_heap, capital_heap[idx][1])
                idx += 1
            if profit_heap:
                out += heapq.heappop_max(profit_heap)
            else:
                break
        return out
