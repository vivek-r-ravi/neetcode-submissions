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
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points):
            return points
        def select(left: int,right: int) -> int:
            pivot=right
            pivotDist=self.distSq(points[pivot])
            pivot_idx=left
            for i in range(left,right):
                if self.distSq(points[i])<pivotDist:
                    points[pivot_idx],points[i]=points[i],points[pivot_idx]
                    pivot_idx+=1
            points[pivot],points[pivot_idx]=points[pivot_idx],points[pivot]
            if k==pivot_idx or k==pivot_idx+1:
                return points[:k]
            elif k<pivot_idx:
                return select(left,pivot_idx-1)
            else:
                return select(pivot_idx+1,right)
        return select(0,len(points)-1)
        
    def distSq(self, pt: List[int]) -> int:
        return pt[0]*pt[0]+pt[1]*pt[1]