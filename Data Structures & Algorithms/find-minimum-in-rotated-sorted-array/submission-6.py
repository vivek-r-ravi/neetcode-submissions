# binary search in rotated sorted array
# O(logn) time O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        out = nums[l]
        while l <= r:
            if nums[l] <= nums[r]:
                out = min(out, nums[l])
                break
            m = (l + r) // 2
            out = min(out, nums[m])
            if nums[l] <= nums[m]:  # check if left half sorted
                l = m + 1
            else:                   # if right half sorted
                r = m - 1
        return out
