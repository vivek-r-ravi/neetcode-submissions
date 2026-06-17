# brute force with nested loops
# O(n2) time O(1) memory
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out=-float('inf')
        for i in range(len(nums)):
            sub_sum=nums[i]
            out=max(out,sub_sum)
            for j in range(i+1,len(nums)):
                sub_sum+=nums[j]
                out=max(out,sub_sum)
        return out