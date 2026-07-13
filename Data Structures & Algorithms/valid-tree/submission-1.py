class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        rank = [0]*n
        n_components = n

        def find(v):
            if par[v] != v:
                par[v] = find(par[v])
            return par[v]

        def union(v1,v2):
            nonlocal n_components
            p1, p2 = find(v1), find(v2)
            if p1==p2:
                return False
            if rank[p1]<rank[p2]:
                par[p1] = p2
            elif rank[p2]>rank[p1]:
                par[p2] = p1
            else:
                par[p2] = p1
                rank[p1] += 1
            n_components -= 1
            return True

        for v1, v2 in edges:
            if not union(v1,v2):
                return False
        return True if n_components == 1 else False