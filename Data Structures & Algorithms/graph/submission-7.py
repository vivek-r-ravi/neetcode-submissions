"""
Design a directed Graph class.

Your Graph class should support the following operations:

* Graph() will initialize an empty directed graph.
* void addEdge(int src, int dst) will add an edge from src to dst if it does not already exist. 
If either src or dst do not exist, add them to the graph.
* bool removeEdge(int src, int dst) will remove the edge from src to dst if it exists. 
Return whether the edge was removed. Either src or dst may not exist in the graph.
* bool hasPath(int src, int dst) will return whether there is a path from src to dst. 
Assume both src and dst exist in the graph.

Constraints:

Each vertex value will be a unique integer.
Multiple edges from one vertex to another are not allowed.
A vertex will not have an edge to itself, but the graph may contain a cycle.
The graph is not necessarily connected (there may be disconnected components).
"""


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
    def hasPath(self, src: int, dst: int) -> bool:
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
    def hasPathDFS(self, src: int, dst: int) -> bool:
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