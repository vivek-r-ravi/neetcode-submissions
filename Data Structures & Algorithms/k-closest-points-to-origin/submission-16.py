import random


# solution 1: brute force - sort based on distance
# O(nlogn) on time and O(1) on space
class SolutionV1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:k]


# solution 2: max heap
# O(nlogk) on time and O(k) on space
class SolutionV2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            if len(heap) < k:
                heapq.heappush_max(heap, [self.distSq(point), point[0], point[1]])
            else:
                heapq.heappushpop_max(heap, [self.distSq(point), point[0], point[1]])
        return [[point[1], point[2]] for point in heap]

    def distSq(self, pt: List[int]) -> int:
        return pt[0] * pt[0] + pt[1] * pt[1]


# solution 3: quick select based on quick sort partition step and recursion
# O(n) on time and O(logn to n) on space due to recursion stack
class SolutionV3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points

        def partition(left: int, right: int) -> int:
            rand_idx = random.randint(left, right)
            points[rand_idx], points[right] = points[right], points[rand_idx]
            pivot = right
            pivotDist = self.distSq(points[pivot])
            pivot_idx = left
            for i in range(left, right):
                if self.distSq(points[i]) < pivotDist:
                    points[pivot_idx], points[i] = points[i], points[pivot_idx]
                    pivot_idx += 1
            points[pivot], points[pivot_idx] = points[pivot_idx], points[pivot]
            return pivot_idx

        def select(left: int, right: int) -> List[List[int]]:
            if left >= right:
                return points[:k]
            pivot_idx = partition(left, right)
            if k == pivot_idx:
                return points[:k]
            if k < pivot_idx:
                return select(left, pivot_idx - 1)
            return select(pivot_idx + 1, right)

        return select(0, len(points) - 1)

    def distSq(self, pt: List[int]) -> int:
        return pt[0] * pt[0] + pt[1] * pt[1]


# solution 4: quick select based on quick sort partition step and iteration
# iteration is most effficient for quick select as only side is chosen
# O(n) on time and O(1) on space
class SolutionV4:
# class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def partition(left: int, right: int) -> int:
            rand_idx = random.randint(left, right)
            points[rand_idx], points[right] = points[right], points[rand_idx]
            pivot = right
            pivotDist = self.distSq(points[pivot])
            pivot_idx = left
            for i in range(left, right):
                if self.distSq(points[i]) < pivotDist:
                    points[pivot_idx], points[i] = points[i], points[pivot_idx]
                    pivot_idx += 1
            points[pivot], points[pivot_idx] = points[pivot_idx], points[pivot]
            return pivot_idx

        left, right = 0, len(points) - 1
        while left <= right:
            pivot_idx = partition(left, right)
            if k < pivot_idx:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

        return points[:k]

    def distSq(self, pt: List[int]) -> int:
        return pt[0] * pt[0] + pt[1] * pt[1]


# alternate quick select: repeated computation of distance can be avoided by storing computed distances
# O(n) time and O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for pt in points:
            pt.append(pt[0] * pt[0] + pt[1] * pt[1])
        closest = self.quickSelect(points, k, 0, len(points) - 1)
        for pt in closest:
            pt.pop()
        return closest

    def quickSelect(
        self, points: List[List[int]], k: int, left: int, right: int
    ) -> List[List[int]]:

        def partition(left: int, right: int) -> int:
            rand_idx = random.randint(left, right)
            points[rand_idx], points[right] = points[right], points[rand_idx]
            pivot = right
            pivotDist = points[pivot][2]
            pivot_idx = left
            for i in range(left, right):
                if points[i][2] < pivotDist:
                    points[pivot_idx], points[i] = points[i], points[pivot_idx]
                    pivot_idx += 1
            points[pivot], points[pivot_idx] = points[pivot_idx], points[pivot]
            return pivot_idx

        left, right = 0, len(points) - 1
        pivot_idx = len(points)

        while k != pivot_idx:
            pivot_idx = partition(left, right)
            if k < pivot_idx:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

        return points[:k]
