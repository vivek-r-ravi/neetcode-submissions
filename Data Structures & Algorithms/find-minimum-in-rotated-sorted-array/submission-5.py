class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        out = nums[l]
        while l<=r:
            if nums[l]<=nums[r]:
                out = min(out,nums[l])
                break
            m = (l+r)//2
            if nums[l]<=nums[m]:
                out = min(out,nums[l])
                l = m+1
            else:
                out = min(out,nums[m])
                r = m-1
        return out