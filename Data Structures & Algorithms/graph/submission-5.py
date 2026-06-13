# Adjacency List is represented as a hashmap
# keys are vertices, values are a set (instead of list due to O(1) remove)
# O(1) time and O(V+E) space for addEdge and removeEdge
# O(V+E) time and space for hasPath BFS. BFS preferred as it finds shortest path.
from collections import deque


class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        if dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    # BFS Solution O(V+E) time and space
    def hasPathBFS(self, src: int, dst: int) -> bool:
        q = deque([src])
        visit = set([src])
        while q:
            vertex = q.popleft()
            if vertex == dst:
                return True
            for neighbor in self.adjList[vertex]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    q.append(neighbor)
        return False

    # DFS Solution O(V+E) time and space
    def hasPath(self, src: int, dst: int) -> bool:
        visit=set()
        def dfs(src, dst):
            if src == dst:
                return True
            visit.add(src)
            for neighbor in self.adjList[src]:
                if neighbor not in visit:
                    if dfs(neighbor,dst):
                        return True
            return False
        return dfs(src,dst)