class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        L_min, R_min=0, n
        for L in range(n):
            sub_sum=0
            for R in range(L,n):
                sub_sum+=nums[R]
                if sub_sum>=target:
                    if R-L<R_min-L_min:
                        L_min,R_min=L,R 
                    break
        return R_min-L_min+1 if R_min!=n else 0