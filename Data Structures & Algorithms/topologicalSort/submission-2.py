# approach 1: DFS O(V+E) time and space
class SolutionDFS:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList={i:[] for i in range(n)}
        for src,dst in edges:
            adjList[src].append(dst)

        visited=set()
        path=set()
        topSort=[]
        
        def dfs(src: int) -> bool:
            if src in visited:
                return True
            if src in path:
                return False
            path.add(src)
            for neighbor in adjList[src]:
                if not dfs(neighbor):
                    return False
            path.remove(src)
            visited.add(src)
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
        adjList={i:[] for i in range(n)}
        indegree=[0]*n
        for src,dst in edges:
            adjList[src].append(dst)
            indegree[dst] += 1

        topSort=[]
        q=deque([i for i in range(n) if indegree[i]==0])
        while q:
            for _ in range(len(q)): 
                curr=q.popleft()
                topSort.append(curr)
                for neighbor in adjList[curr]:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        q.append(neighbor)

        return topSort if len(topSort)==n else []
