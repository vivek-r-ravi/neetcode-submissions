class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        best = 0
        for num in nums:
            if num == 1:
                curr += 1
                best = max(best, curr)
            else:
                curr = 0
        return best