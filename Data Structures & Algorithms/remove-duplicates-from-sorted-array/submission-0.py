class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L=0
        R=1
        while R<len(nums):
            if nums[L]!=nums[R]:
                L+=1
                R+=1
            else:
                nums.pop(R)
        return R