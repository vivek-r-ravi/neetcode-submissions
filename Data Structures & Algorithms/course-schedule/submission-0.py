class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # convert array of edges to hash map
        adj_list_prev={}
        adj_list_next={}
        for i in range(numCourses):
            adj_list_prev[i]=set()
            adj_list_next[i]=set()
        for src,dst in prerequisites:
            adj_list_prev[src].add(dst)
            adj_list_next[dst].add(src)
        
        # courses without prerequisite
        q = deque([course for course in adj_list_prev if not adj_list_prev[course]])
        if not q:
            return False
        
        # multi-surface BFS
        completed=set()
        while q:
            curr=q.popleft()
            completed.add(curr)
            for next in adj_list_next[curr]:
                if adj_list_prev[next]<=completed:
                    q.append(next)

        return numCourses==len(completed) 