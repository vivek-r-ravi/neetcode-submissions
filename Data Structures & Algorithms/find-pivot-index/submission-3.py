# prefix sum array
# O(n) time and O(n) space
class SolutionV1:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
        for i in range(n):
            if prefix[i]==prefix[n]-prefix[i+1]:
                return i
        return -1

# prefix sum (space compression)
# O(n) time and O(1) space
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        left=0
        for i in range(0,n):
            right=total-left-nums[i]
            if left==right:
                return i
            left+=nums[i]
        return -1
