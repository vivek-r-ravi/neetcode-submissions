class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=1                             # write pointer
        for R in range(1,len(nums)):    # read pointer
            if nums[R]!=nums[L-1]:
                nums[L]=nums[R]
                L+=1
        return L