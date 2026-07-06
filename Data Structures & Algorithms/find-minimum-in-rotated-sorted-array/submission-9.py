# binary search in rotated sorted array
# O(logn) time O(1) space
class SolutionV1:
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


# canonical solution: find pivot point using lower bound binary search
# O(logn) time O(1) space
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:   # check if right half sorted
                r = m
            else:                   # if left half sorted
                l = m + 1
        return nums[l]
