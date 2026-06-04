# solution 1: use bucket sort
# O(n) on time and O(3) on space
from collections import Counter
class SolutionV1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count = Counter(nums)
        for n in sorted(count.keys()):
            for j in range(count[n]):
                nums[i]=n
                i+=1

# solution 2: Dutch National Flag solution using 3 pointers
# O(n) on time and O(1) on space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            else:
                i+=1
            
