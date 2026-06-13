class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # array of edges to adjList
        adjList={i:[] for i in range(n)}
        for st,end,w in edges:
            adjList[st].append((end,w))

        # compute shortest paths
        heap=[]
        heapq.heappush(heap,(0,src))
        dist={}
        while heap:
            w_curr,curr=heapq.heappop(heap)
            if curr in dist:
                continue
            dist[curr]=w_curr
            for neighbor,w in adjList[curr]:
                if neighbor not in dist:
                    heapq.heappush(heap,(w+w_curr,neighbor))

        # fill in missing vertices
        for i in range(n):
            if i not in dist:
                dist[i] = -1
        
        return dist