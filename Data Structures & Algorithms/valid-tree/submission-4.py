# valid tree: no cycles, 1 connected component


# DFS
# O(V+E) time and space
class SolutionV1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = {}
        for v1, v2 in edges:
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        # cycle detection using DFS with parent parameter
        visited = set()
        def dfs(v, par):
            visited.add(v)
            for nei in adj_list.get(v, []):
                if nei == par:
                    continue
                if nei in visited:
                    return True
                if dfs(nei, v):
                    return True
            return False

        return not dfs(0, -1) and len(visited) == n


# union find
# O(V+E) time O(V) space
class SolutionV2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        par = [i for i in range(n)]
        rank = [0] * n
        n_components = n

        def find(v):
            if par[v] != v:
                par[v] = find(par[v])
            return par[v]

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                par[p1] = p2
            elif rank[p2] < rank[p1]:
                par[p2] = p1
            else:
                par[p2] = p1
                rank[p1] += 1
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return False
            else:
                n_components -= 1
        return n_components == 1


# BFS
# O(V+E) time and space
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = {}
        for v1, v2 in edges:
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        # cycle detection using BFS with parent
        visited = set([0])
        q = deque([(0,-1)])
        while q:
            v, par = q.popleft()
            for nei in adj_list.get(v, []):
                if nei == par:
                    continue
                if nei in visited:
                    return False
                q.append((nei, v))
                visited.add(nei)

        return len(visited) == n
