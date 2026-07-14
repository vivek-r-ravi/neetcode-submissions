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
