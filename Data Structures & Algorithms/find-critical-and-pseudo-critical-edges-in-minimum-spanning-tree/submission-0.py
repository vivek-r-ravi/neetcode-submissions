class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # for each edge:
        # 1. check for crit by building without edge and compare with mst_wt
        # 2. check for pseudo by forcing building with edge and compare with mst_wt
        # helper function to get mst weight with options to skip edge or force edge
        def get_mst_weight(n, edges, force_edge=None, skip_edge_idx=-1):

            par = list(range(n))
            rank = [0] * n

            def find(x):
                if par[x] != x:
                    par[x] = find(par[x])
                return par[x]

            def union(x, y):
                p1, p2 = find(x), find(y)
                if p1 == p2:
                    return False
                if rank[p2] < rank[p1]:
                    par[p2] = p1
                elif rank[p1] < rank[p2]:
                    par[p1] = p2
                else:
                    par[p1] = p2
                    rank[p2] += 1
                return True

            weight = 0
            edges_count = 0

            # try by forcing building with an edge first
            if force_edge:
                union(force_edge[0], force_edge[1])
                weight += force_edge[2]
                edges_count += 1

            # try building without an edge
            for v1, v2, w, i in edges:
                if i != skip_edge_idx and union(v1, v2):
                    weight += w
                    edges_count += 1

            return weight if edges_count == n - 1 else float("inf")

        # get mst weight
        for i, edge in enumerate(edges):
            edge.append(i)
        sorted_edges = sorted(edges, key=lambda x: x[2])
        mst_weight = get_mst_weight(n, sorted_edges)

        # check crit and pseudo
        crit = []
        pseudo = []
        for n1, n2, e_weight, i in edges:
            if get_mst_weight(n, sorted_edges, skip_edge_idx=i) > mst_weight:
                crit.append(i)
            elif get_mst_weight(n, sorted_edges, force_edge=[n1, n2, e_weight]) == mst_weight:
                pseudo.append(i)

        return [crit, pseudo]
