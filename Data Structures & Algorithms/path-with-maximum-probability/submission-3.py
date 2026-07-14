# Dijkstra's with a max heap
# O(ElogV) time O(V+E) space
class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append((succProb[i], edges[i][1]))
            adj[edges[i][1]].append((succProb[i], edges[i][0]))

        max_heap = [(1, start_node)]
        visited = set([start_node])
        max_prob = 0
        while max_heap:
            p, node = heapq.heappop_max(max_heap)
            if node == end_node:
                return p
            visited.add(node)
            for prob, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush_max(max_heap, (p * prob, nei))

        return max_prob
