# solution 1: brute force - sort based on distance
# O(nlogn) on time and O(n) on space
class SolutionV1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]*x[0]+x[1]*x[1])
        return points[:k]

# solution 2: quick select based on quick sort partition step and recursion
# O(n) on time and O(logn to n) on space due to recursion stack
import random
class SolutionV2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points):
            return points
        
        def partition(left: int,right: int) -> int:
            rand_idx = random.randint(left, right)
            points[rand_idx], points[right] = points[right], points[rand_idx]
            pivot=right
            pivotDist=self.distSq(points[pivot])
            pivot_idx=left
            for i in range(left,right):
                if self.distSq(points[i])<pivotDist:
                    points[pivot_idx],points[i]=points[i],points[pivot_idx]
                    pivot_idx+=1
            points[pivot],points[pivot_idx]=points[pivot_idx],points[pivot]
            return pivot_idx
            
        def select(left: int, right: int) -> List[List[int]]:
            if left>=right:
                return points[:k]
            pivot_idx=partition(left,right)
            if k==pivot_idx:
                return points[:k]
            if k<pivot_idx:
                return select(left,pivot_idx-1)
            return select(pivot_idx+1,right)
        
        return select(0,len(points)-1)
        
    def distSq(self, pt: List[int]) -> int:
        return pt[0]*pt[0]+pt[1]*pt[1]

# solution 3: quick select based on quick sort partition step and iteration
# iteration is most effficient for quick select as only side is chosen
# O(n) on time and O(1) on space
import random
class Solution:
#class SolutionV3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def partition(left: int,right: int) -> int:
            rand_idx = random.randint(left, right)
            points[rand_idx], points[right] = points[right], points[rand_idx]
            pivot=right
            pivotDist=self.distSq(points[pivot])
            pivot_idx=left
            for i in range(left,right):
                if self.distSq(points[i])<pivotDist:
                    points[pivot_idx],points[i]=points[i],points[pivot_idx]
                    pivot_idx+=1
            points[pivot],points[pivot_idx]=points[pivot_idx],points[pivot]
            return pivot_idx
            
        left,right = 0,len(points)-1
        pivot_idx=len(points)

        while k!=pivot_idx:
            pivot_idx=partition(left,right)
            if k<pivot_idx:
                right=pivot_idx-1
            else:
                left=pivot_idx+1
        
        return points[:k]
        
    def distSq(self, pt: List[int]) -> int:
        return pt[0]*pt[0]+pt[1]*pt[1]
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for pt in points:
            pt.append(pt[0]*pt[0]+pt[1]*pt[1])
        closest=self.quickSelect(points,k,0,len(points)-1)
        for pt in closest:
            pt.pop()
        return closest
        
    def quickSelect(self, arr: list[int], k:int, s:int, e:int) -> list[int]:
        if s >= e:
            return arr[:k]
        pivot=arr[e]
        left=s
        for i in range(s,e):
            if arr[i][2]<pivot[2]:
                tmp=arr[left]
                arr[left]=arr[i]
                arr[i]=tmp
                left+=1
        arr[e]=arr[left]
        arr[left]=pivot
        if left==k or left==k-1:
            return arr[:k]
        elif left<k-1:
            return self.quickSelect(arr,k,left+1,e)
        else:
            return self.quickSelect(arr,k,s,left-1)
'''