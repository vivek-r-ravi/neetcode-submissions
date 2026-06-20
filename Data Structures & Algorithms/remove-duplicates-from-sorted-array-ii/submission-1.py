class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=2
        for r in range(2,len(nums)):
            if(nums[r]!=nums[r-1]) or (nums[r]!=nums[l-2]):
                nums[l]=nums[r]
                l+=1
        return l if len(nums)>1 else 1