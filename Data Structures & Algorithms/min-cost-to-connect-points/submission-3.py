# Prim's
# O(ElogV) time O(E) space
class SolutionV1:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set([tuple(points[0])])
        out = 0
        min_heap = []
        for point in points:
            if point != points[0]:
                heapq.heappush(min_heap, (self.dist(point, points[0]), tuple(point)))

        while len(visited) < n:
            c, pt = heapq.heappop(min_heap)
            if pt in visited:
                continue
            visited.add(pt)
            out += c
            for point in points:
                if tuple(point) != pt and tuple(point) not in visited:
                    heapq.heappush(min_heap, (self.dist(point, pt), tuple(point)))

        return out

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


# Kruskal's but not most efficient as complete graph
# use indicies instead of points
# O(n2logn) time O(n2) space
class Solution:
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
