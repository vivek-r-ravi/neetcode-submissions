# DFS memoization with hash set
# O(V*(V+E) + Q) time, O(V² + E) space
class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        adj_list = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            adj_list[dst].append(src)   # reverse

        preq_map = {}

        def dfs(v):
            if v in preq_map:
                return preq_map[v]      # memoization

            out = set()
            for nei in adj_list[v]:
                out.add(nei)
                out.update(dfs(nei))
            preq_map[v] = out
            return out

        for i in range(numCourses):
            dfs(i)

        return [l in preq_map[r] for l, r in queries]
