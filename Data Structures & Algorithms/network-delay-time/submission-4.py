# solution: Dijkstra's
# O(ElogV) time and O(V+E) space
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for st, end, t in times:
            adj[st].append((end, t))

        heap = [(0, k)]
        min_t = {}
        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in min_t:
                continue
            min_t[n1] = t1
            for n2, t2 in adj[n1]:
                if n2 not in min_t:
                    heapq.heappush(heap, (t2 + t1, n2))

        if len(min_t) < n:
            return -1

        return max(min_t.values())


# Bellman Ford (not canonical)
# O(V*E) time and O(V) space
class SolutionV2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        max_dist = max(dist.values())
        return max_dist if max_dist < float("inf") else -1
