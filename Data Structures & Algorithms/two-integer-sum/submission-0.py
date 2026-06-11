class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combo=dict()
        for i in range(len(nums)):
            if nums[i] in combo:
                return [combo[nums[i]],i]
            combo[target-nums[i]]=i