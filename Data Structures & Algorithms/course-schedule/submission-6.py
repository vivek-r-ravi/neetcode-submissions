# solution 1: Cycle detection using DFS (based on topological sort)
# O(V+E) time and space
class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list={i:set() for i in range(numCourses)}
        for src,dst in prerequisites:
            adj_list[src].add(dst)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state=[0]*numCourses
        def dfs(src: int) -> bool:
            if state[src]==2:   # already visited
                return True
            if state[src]==1:   # already visiting
                return False
            state[src]+=1       # visiting
            for neighbor in adj_list[src]:
                if not dfs(neighbor):
                    return False
            state[src]+=1       # visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# solution 2: Topological Sort using BFS (Kahn's Algorithm)
# O(V+E) time and space
class Solution:
#class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for src,dst in prerequisites:
            adj_list[dst].append(src)
            indegree[src]+=1
        
        q = deque([course for course in range(numCourses) if indegree[course]==0])
        top_sort=[]
        while q:
            curr=q.popleft()
            top_sort.append(curr)
            for next in adj_list[curr]:
                indegree[next]-=1
                if indegree[next]==0:
                    q.append(next)

        return numCourses==len(top_sort) 