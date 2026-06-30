# sorting solution is O(nlogn) time

# canonical solution: convert to hash set
# O(n) time and space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        out = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                sub_out = 1
                while num + sub_out in nums_set:
                    sub_out += 1
                out = max(out, sub_out)
        return out
