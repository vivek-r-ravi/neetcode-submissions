class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cost = [float('inf')]*n
        cost[src] = 0
        for _ in range(k+1):
            cost_copy = cost[:]
            for u, v, w in flights:
                if cost[u] != float('inf') and cost[u] + w < cost_copy[v]:
                    cost_copy[v] = cost[u] + w
            cost = cost_copy
        return cost[dst] if cost[dst]!=float('inf') else -1
