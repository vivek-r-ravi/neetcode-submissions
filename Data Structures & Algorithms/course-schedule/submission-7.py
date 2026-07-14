# solution 1: Cycle detection using DFS (based on topological sort)
# O(V+E) time and space
class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i: set() for i in range(numCourses)}
        for src, dst in prerequisites:
            adj_list[src].add(dst)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        # cycle exists when a "visiting" node is encountered again
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
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# solution 2: Topological Sort using BFS (Kahn's Algorithm)
# O(V+E) time and space
# class SolutionBFS:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dst in prerequisites:
            adj_list[dst].append(src)
            indegree[src] += 1

        q = deque([course for course in range(numCourses) if indegree[course] == 0])
        completed = 0
        while q:
            curr = q.popleft()
            completed += 1
            for nei in adj_list[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return numCourses == completed
