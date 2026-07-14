# standard lazy Prim's
# use indices instead of points
# O(n2logn) time O(n2) space
class SolutionV1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        visited[0] = True
        min_heap = []
        for i in range(1, n):
            heapq.heappush(min_heap, (self.dist(points[i], points[0]), i))

        out = 0
        visited_count = 1
        while visited_count < n:
            c, idx = heapq.heappop(min_heap)
            if visited[idx]:
                continue
            visited[idx] = True
            visited_count += 1
            out += c
            for i in range(n):
                if not visited[i]:
                    heapq.heappush(min_heap, (self.dist(points[idx], points[i]), i))

        return out

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


# optimal Prim's (track only best distance)
# O(n2) time O(n) space
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minDist = [float("inf")] * n
        minDist[0] = 0

        out = 0
        visited_count = 0
        while visited_count < n:
            # Find the unvisited node with the smallest connection cost
            cur = -1
            curDist = float("inf")
            for i in range(n):
                if not visited[i] and minDist[i] < curDist:
                    curDist = minDist[i]
                    cur = i

            if cur == -1:
                break

            visited[cur] = True
            visited_count += 1
            out += curDist

            # Update distances to all unvisited nodes
            x1, y1 = points[cur]
            for nei in range(n):
                if not visited[nei]:
                    x2, y2 = points[nei]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < minDist[nei]:
                        minDist[nei] = dist

        return out


# Kruskal's but not most efficient as complete graph
# use indicies instead of points
# O(n2logn) time O(n2) space
class SolutionV3:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x, y):
            p, q = find(x), find(y)
            if p == q:
                return False
            if rank[q] < rank[p]:
                par[q] = p
            elif rank[p] < rank[q]:
                par[p] = q
            else:
                par[p] = q
                rank[q] += 1
            return True

        out = 0
        connected = 0
        i = 0
        edges = [(self.dist(points[i], points[j]), i, j) for i in range(n) for j in range(i + 1, n)]
        edges.sort()
        while connected < n - 1 and i < len(edges):
            c, st, pt = edges[i]
            i += 1
            if not union(st, pt):
                continue
            out += c
            connected += 1

        return out

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
