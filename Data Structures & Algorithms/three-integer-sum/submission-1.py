# brute force
# O(n3) time and O(m) space
from itertools import combinations
class SolutionV1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=set()
        for i,j,k in combinations(nums,3):
            if i+j+k==0:
                out.add(tuple(sorted((i,j,k))))
        return [list(x) for x in out]


# two pointers
# O(n2) time and O(1) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=set()
        for m in range(len(nums)-2):
            target=-1*nums[m]
            l=m+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    out.add((nums[m],nums[l],nums[r]))
                    l+=1
                    r-=1
        return [list(x) for x in out]

