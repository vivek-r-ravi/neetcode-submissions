"""
Implement Kruskal's minimum spanning tree algorithm.

A Minimum Spanning Tree (MST) is a tree that spans all the vertices in a given weighted, undirected 
graph while minimizing the total edge weight and avoiding cycles. It connects all nodes with exactly 
V-1 edges, where V is the set of vertices, and has the lowest possible sum of edge weights.

Kruskal's algorithm is a greedy algorithm that finds the MST of graph. It sorts all the edges from 
least weight to greatest, and iteratively adds edges to the MST, ensuring that each new edge doesn't form a cycle.

Objective:

Given a weighted, undirected graph, find the minimum spanning tree (MST) using Kruskal's algorithm 
and return its total weight. If the graph is not connected, the total weight of the minimum spanning tree should be -1.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing an undirected edge in the form (u, v, w), 
where u and v are vertices connected by the edge, and w is the weight of the edge, where (1 <= w <= 10).
Note: If the graph is not connected, you should return -1.
"""


# O(ElogV) time O(E) space
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # initialize union find
        par = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> bool:
            p, q = find(x), find(y)
            if p == q:
                return False
            if rank[q] < rank[p]:
                par[q] = p
            elif rank[p] < rank[q]:
                par[p] = q
            else:
                par[p] = q
                rank[q] += 1
            return True

        # sort edges
        edges.sort(key=lambda x: x[2])

        # union unconnected edges
        mst = []
        out = 0
        i = 0
        while len(mst) < n - 1 and i < len(edges):
            u, v, w = edges[i]
            i += 1
            if not union(u, v):
                continue
            out += w
            mst.append([u, v])

        return out if len(mst) == n - 1 else -1
