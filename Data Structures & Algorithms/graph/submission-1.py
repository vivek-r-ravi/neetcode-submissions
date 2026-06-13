# Adjacency List is represented as a hashmap
# keys are vertices, values are a set (instead of list due to O(1) remove)
# O(1) time and O(V+E) space for addEdge and removeEdge
# O(V+E) time and space for hasPath BFS. BFS preferred as it finds shortest path.
class Graph:
    
    def __init__(self):
        self.adjList={}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src]=set()
        if dst not in self.adjList:
            self.adjList[dst]=set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList:
            self.adjList[src]=set()
        if dst not in self.adjList:
            self.adjList[dst]=set()
        if dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    # BFS Solution O(V+E) time and space
    def hasPath(self, src: int, dst: int) -> bool:
        q=deque([src])
        while q:
            vertex=q.popleft()
            if vertex==dst:
                return True
            for neighbor in self.adjList[vertex]:
                q.append(neighbor)
        return False
