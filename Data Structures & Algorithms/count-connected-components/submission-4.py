# DFS
# O(V+E) time and space
class SolutionV1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for v1, v2 in edges:
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()
        def dfs(v):
            visited.add(v)
            if v not in adj_list:
                return
            for nei in adj_list[v]:
                if nei not in visited:
                    dfs(nei)
            
        out = 0
        for v in range(n):
            if v not in visited:
                dfs(v)
                out += 1
        return out


# BFS
# O(V+E) time and space
class SolutionV2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for v1, v2 in edges:
            if v1 not in adj_list:
                adj_list[v1] = []
            if v2 not in adj_list:
                adj_list[v2] = []
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()
        def bfs(v):
            visited.add(v)
            q = deque([v])
            while q:
                vertex = q.popleft()
                if vertex not in adj_list:
                    continue
                for nei in adj_list[vertex]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
        out = 0
        for v in range(n):
            if v not in visited:
                bfs(v)
                out += 1
        return out


# union find
# O(V+E) time O(V) space
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            if union(v1, v2):
                n_components -= 1
        return n_components
