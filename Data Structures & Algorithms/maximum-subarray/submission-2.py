# brute force with nested loops
# O(n2) time O(1) memory
class SolutionV1:
    def maxSubArray(self, nums: List[int]) -> int:
        out=nums[0]
        for i in range(len(nums)):
            sub_sum=nums[i]
            out=max(out,sub_sum)
            for j in range(i+1,len(nums)):
                sub_sum+=nums[j]
                out=max(out,sub_sum)
        return out

# Kadane's algorithm
# O(n) time O(1) memory
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out=nums[0]
        sub_sum=0
        for n in nums:
            sub_sum=max(sub_sum,0)+n    # extend subarray from start until it becomes -ve
            out=max(out,sub_sum)
        return out