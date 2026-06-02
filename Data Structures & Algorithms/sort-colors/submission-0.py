from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count = Counter(nums)
        for n in sorted(count.keys()):
            for j in range(count[n]):
                nums[i]=n
                i+=1