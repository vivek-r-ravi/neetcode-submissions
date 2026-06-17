"""
naive solution: use nested loop or another list to look up (O(n2))
alternate solution: use a sorted list (O(nlogn))
"""


# canonical solution 1: use sets to track seen elements
# O(n) time and space
class SolutionV1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()
        for num in nums:
            if num in prev:
                return True
            prev.add(num)
        return False


# canonical solution 2: convert to set and compare length
# O(n) time and space
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
