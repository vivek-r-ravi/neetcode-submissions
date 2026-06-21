class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        suffix=[0]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+nums[i-1]
            suffix[-(i+1)]=suffix[-i]+nums[-i]
        for i in range(n):
            if prefix[i]==suffix[i+1]:
                return i
        return -1
