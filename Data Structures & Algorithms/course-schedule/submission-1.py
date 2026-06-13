class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list={i:set() for i in range(numCourses)}
        indegree=[0]*numCourses
        for src,dst in prerequisites:
            adj_list[dst].add(src)
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