# approach 1: DFS O(V+E) time and space
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList={i:[] for i in range(n)}
        for src,dst in edges:
            adjList[src].append(dst)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state=[0]*n
        topSort=[]
        
        def dfs(src: int) -> bool:
            if state[src]==2:   # already visited
                return True
            if state[src]==1:   # already visiting
                return False
            state[src]+=1       # visiting
            for neighbor in adjList[src]:
                if not dfs(neighbor):
                    return False
            state[src]+=1       # visited
            topSort.append(src)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()

        return topSort

# approach 2: BFS (Kahn's algorithm) O(V+E) time and space
class SolutionBFS:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList={i:[] for i in range(n)}
        indegree=[0]*n
        for src,dst in edges:
            adjList[src].append(dst)
            indegree[dst] += 1

        topSort=[]
        q=deque([i for i in range(n) if indegree[i]==0])
        while q:
            curr=q.popleft()
            topSort.append(curr)
            for neighbor in adjList[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        return topSort if len(topSort)==n else []
