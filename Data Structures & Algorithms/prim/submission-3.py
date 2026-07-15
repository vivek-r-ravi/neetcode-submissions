"""
Implement Prim's minimum spanning tree algorithm.

A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, 
undirected graph while minimizing the total edge weight and avoiding cycles. 
It connects all nodes with exactly V-1 edges, where V is the set of vertices, 
and has the lowest possible sum of edge weights.

Prim's algorithm is a greedy algorithm that builds the MST of a graph starting from an 
arbitrary vertex. At each step, the algorithm adds the lightest edge connecting a vertex 
in the MST to a vertex outside the MST, effectively "growing" the MST one edge at a time.

Objective:

Given a weighted, undirected graph, find the minimum spanning tree (MST) using Prim's algorithm
 and return its total weight. If the graph is not connected, the total weight of the minimum 
 spanning tree should be -1.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing an undirected edge in the form (u, v, w), 
where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).
"""

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
