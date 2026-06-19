# brute force
# O(n2) time O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        length=float('inf')
        for L in range(n):
            sub_sum=0
            for R in range(L,n):
                sub_sum+=nums[R]
                if sub_sum>=target:
                    length=min(length,R-L+1)
                    break
        return length if length!=float('inf') else 0

# sliding window
# O(n) time O(1) space
class SolutionV1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        L_min, R_min=0, n
        L=0
        sub_sum=0
        for R in range(n):
            sub_sum+=nums[R]
            if sub_sum>=target:
                if R-L<R_min-L_min:
                    L_min,R_min=L,R
                sub_sum-=nums[L]
                L+=1
                
            
        return R_min-L_min+1 if R_min!=n else 0

