# naive solution: use another list to look up (O(n2)) or use a sorted list (O(nlogn))

# solution: use sets to track seen elements
# O(n) time and space
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev=set()
        for num in nums:
            if num in prev:
                return True
            prev.add(num)
        return False