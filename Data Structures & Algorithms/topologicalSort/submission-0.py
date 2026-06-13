class Solution:
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

