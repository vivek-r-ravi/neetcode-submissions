"""
Implement Dijkstra's shortest path algorithm.

Given a weighted, directed graph, and a starting vertex, return the shortest distance 
from the starting vertex to every vertex in the graph.

Input:

* n - the number of vertices in the graph, where (2 <= n <= 100). 
Each vertex is labeled from 0 to n - 1.
* edges - a list of tuples, each representing a directed edge in the form (u, v, w), 
where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).
*src - the source vertex from which to start the algorithm, where (0 <= src < n).

Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.
"""


# O(ElogV) time and O(V+E) space
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # array of edges to adjList
        adjList = {i: [] for i in range(n)}
        for st, end, w in edges:
            adjList[st].append((end, w))

        # compute shortest paths
        heap = []
        heapq.heappush(heap, (0, src))
        dist = {}
        while heap:
            w_curr, curr = heapq.heappop(heap)
            if curr in dist:
                continue
            dist[curr] = w_curr
            for neighbor, w in adjList[curr]:
                if neighbor not in dist:
                    heapq.heappush(heap, (w + w_curr, neighbor))

        # fill in missing vertices
        for i in range(n):
            if i not in dist:
                dist[i] = -1

        return dist
