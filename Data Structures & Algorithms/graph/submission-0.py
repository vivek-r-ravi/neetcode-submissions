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

    # BFS Solution
    def hasPath(self, src: int, dst: int) -> bool:
        q=deque([src])
        while q:
            vertex=q.popleft()
            for neighbor in self.adjList[vertex]:
                if neighbor==dst:
                    return True
                q.append(neighbor)
        return False
