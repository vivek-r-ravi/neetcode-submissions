class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set([tuple(points[0])])
        out = 0
        min_heap = []
        for point in points:
            if point != points[0]:
                heapq.heappush(
                    min_heap, (self.dist(point, points[0]), tuple(points[0]), tuple(point))
                )

        while len(visited) < n:
            c, st, pt = heapq.heappop(min_heap)
            if pt in visited:
                continue
            visited.add(pt)
            out += c
            for point in points:
                if point != pt and tuple(point) not in visited:
                    heapq.heappush(min_heap, (self.dist(point, pt), tuple(pt), tuple(point)))

        return out

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
