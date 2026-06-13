class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list={i:set() for i in range(numCourses)}
        for src,dst in prerequisites:
            adj_list[src].add(dst)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state=[0]*numCourses
        topSort=[]
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
            topSort.append(src)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return topSort