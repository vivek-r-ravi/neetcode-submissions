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


# Kruskal's
# O(ElogV) time O(E) space
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        par = {tuple(pt): tuple(pt) for pt in points}
        rank = {tuple(pt): 0 for pt in points}

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
        edges = [
            (self.dist(pt1, pt2), tuple(pt1), tuple(pt2))
            for pt1 in points
            for pt2 in points
            if pt2 != pt1
        ]
        edges.sort()
        while connected < n and i < len(edges):
            c, st, pt = edges[i]
            i += 1
            if not union(st, pt):
                continue
            out += c
            connected += 1

        return out

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
