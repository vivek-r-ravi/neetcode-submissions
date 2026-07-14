# solution 1: Topological sort using DFS
# O(V+E) time and space
class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: set() for i in range(numCourses)}
        for src, dst in prerequisites:
            adj_list[src].add(dst)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        topSort = []

        def dfs(src: int) -> bool:
            if state[src] == 2:  # already visited
                return True
            if state[src] == 1:  # already visiting
                return False
            state[src] += 1  # visiting
            for neighbor in adj_list[src]:
                if not dfs(neighbor):
                    return False
            state[src] += 1  # visited
            topSort.append(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort  # adj_list already reversed so no need to reverse this


# solution 2: Topological Sort using BFS (Kahn's Algorithm)
# O(V+E) time and space
# class SolutionBFS:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adj_list[dst].append(src)
            indegree[src] += 1

        q = deque([course for course in range(numCourses) if indegree[course] == 0])
        top_sort = []
        while q:
            curr = q.popleft()
            top_sort.append(curr)
            for next in adj_list[curr]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        return top_sort if numCourses == len(top_sort) else []
