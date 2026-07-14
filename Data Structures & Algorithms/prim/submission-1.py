# O(ElogV) time O(E) space
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        min_heap = []
        visited = set([0])
        mst = []
        out = 0
        for nei, wt in adj[0]:
            heapq.heappush(min_heap, (wt, 0, nei))

        while min_heap:  # other conditions are len(visited)<n or len(MST)<n-1
            wt, v1, v2 = heapq.heappop(min_heap)
            if v2 in visited:
                continue
            mst.append([v1, v2])
            out += wt
            visited.add(v2)
            for nei, wt in adj[v2]:
                if nei not in visited:
                    heapq.heappush(min_heap, (wt, v2, nei))

        return out if len(visited) == n else -1
