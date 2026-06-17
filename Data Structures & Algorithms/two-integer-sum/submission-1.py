"""
naive solution: find every sum pair using nested loop O(n2)
alternate solution: sort and use two pointers O(nlogn)
"""


# canonical solution: hashmap to store difference
# O(n) time and space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combo = dict()
        for i in range(len(nums)):
            if nums[i] in combo:
                return [combo[nums[i]], i]
            combo[target - nums[i]] = i
