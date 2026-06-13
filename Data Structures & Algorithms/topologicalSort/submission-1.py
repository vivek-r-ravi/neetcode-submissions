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

# approach 2: BFS (Kahn's algorithm)
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList={i:[] for i in range(n)}
        indegrees={i:0 for i in range(n)}
        for src,dst in edges:
            adjList[src].append(dst)
            indegrees[dst]+=1

        topSort=[]
        visited=set()
        q=deque([v for v in indegrees if indegrees[v]==0])
        while q:
            for _ in range(len(q)): 
                curr=q.popleft()
                topSort.append(curr)
                visited.add(curr)
                indegrees.pop(curr)
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        indegrees[neighbor]-=1
            q=deque([v for v in indegrees if indegrees[v]==0])

        return topSort if len(topSort)==n else []
