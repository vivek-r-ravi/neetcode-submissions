class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=2
        tmp=nums[0]
        for r in range(2,len(nums)):
            if(nums[r]!=nums[r-1]) or (nums[r]!=tmp):
                tmp=nums[r-1]
                nums[l]=nums[r]
                l+=1
            else:
                tmp=nums[r-1]
        return l if len(nums)>1 else 1