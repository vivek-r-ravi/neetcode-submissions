# solution 1: hashset to find duplicate (O(n) time and space)
# solution 2: two pointers to modify nums in place to remove duplicates (O(n) time and O(1) space)


# canonical solution: model nums as cyclic linked list and find cycle head
# O(n) time and O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
