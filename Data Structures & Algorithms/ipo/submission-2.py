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


# brute force
# O(n) time O(1) space
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = [(c,-1*p) for c,p in zip(capital,profits)]
        heapq.heapify(capital_heap)
        profit_heap = []
        completed = 0
        out = w
        while completed < k and (capital_heap or profit_heap):
            while capital_heap and out>=capital_heap[0][0]:
                heapq.heappush_max(profit_heap,-1*heapq.heappop(capital_heap)[1])
            if profit_heap:
                out+=heapq.heappop_max(profit_heap)
            else:
                break
            completed+=1
        return out