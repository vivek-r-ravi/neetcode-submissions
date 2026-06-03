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
# solution 1: brute force - sort based on distance
# O(nlogn) on time and O(n) on space
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x:x[0]*x[0]+x[1]*x[1])
        return points[:k]
'''

# solution 2: quick select based on quick sort partition step
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest=self.quickSelect(points,k)
        return closest
        
    def distSq(self, pt: List[int]) -> int:
        return pt[0]*pt[0]+pt[1]*pt[1]
    
    def quickSelect(self, arr: list[int], k:int) -> list[int]:
        if k==len(arr):
            return arr
        e=len(arr)-1
        pivot=arr[e]
        left=0
        for i in range(e):
            if self.distSq(arr[i])<self.distSq(pivot):
                arr[left],arr[i]=arr[i],arr[left]
                left+=1
        arr[e],arr[left]=arr[left],arr[e]
        if k==left:
            return arr[:left]
        elif k<left:
            return self.quickSelect(arr[:left],k)
        else:
            return arr[:left] + self.quickSelect(arr[left:],k-left)