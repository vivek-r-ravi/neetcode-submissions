class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # do not create another array, so use the same array
        nums[:] = [i for i in nums if i!=val]
        k = len(nums)
        return k