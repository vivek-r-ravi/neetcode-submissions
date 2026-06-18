# brute force with nested loops
# O(n2) time O(1) memory
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        out = nums[0]
        for i in range(n):
            sub_sum = 0
            for j in range(i,n+i):
                sub_sum += nums[j%n]
                out = max(out, sub_sum)
        return out

'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        out=nums[0]
        for L in range(n):
            R=L
            sub_sum=0
            while abs(R-L)<n:
                if sub_sum<0:
                    L=R
                    sub_sum=0
                sub_sum+=nums[R%n]
                if sub_sum>out:
                    out=sub_sum
                R+=1
        return out
'''