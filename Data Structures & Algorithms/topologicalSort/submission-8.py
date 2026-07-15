"""
Implement topological sort.

Topological sort is an algorithm for linearly ordering the vertices of a directed acyclic graph 
such that for every directed edge (u,v), vertex u comes before v in the ordering.

Given a directed graph, perform a topological sort on its vertices and return the order as a 
list of vertex labels. There may be multiple valid topological sorts for a given graph, 
so you may return any valid ordering.

If the graph contains a cycle, you should return an empty list to indicate 
that a topological sort is not possible.

Input:

n - the number of vertices in the graph. Each vertex is labeled from 0 to n - 1.
edges - a list of pairs, each representing a directed edge in the form (u, v), 
where u is the source vertex and v is the destination vertex.
"""


# approach 1: DFS O(V+E) time and space
class SolutionDFS:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(n)}
        for src, dst in edges:
            adjList[src].append(dst)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * n
        topSort = []

        # cycle exists when a "visiting" node is encountered again
        # return True when no cycle, False when cycle exists
        def dfs(src: int) -> bool:
            if state[src] == 2:  # already visited
                return True
            if state[src] == 1:  # already visiting
                return False
            state[src] += 1  # visiting
            for neighbor in adjList[src]:
                if not dfs(neighbor):
                    return False
            state[src] += 1  # visited
            topSort.append(src)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()

        return topSort


# approach 2: BFS (Kahn's algorithm) O(V+E) time and space
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(n)}
        indegree = [0] * n
        for src, dst in edges:
            adjList[src].append(dst)
            indegree[dst] += 1

        topSort = []
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            curr = q.popleft()
            topSort.append(curr)
            for neighbor in adjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return topSort if len(topSort) == n else []
