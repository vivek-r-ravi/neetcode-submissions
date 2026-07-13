# canonical solution: cycle detection using union find
# O(V+E) time and O(V) space
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]  # 0 index is dummy
        rank = [0] * (n + 1)  # 0 index is dummy

        def find(v):
            if v != par[v]:
                par[v] = find(par[v])
            return par[v]

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
