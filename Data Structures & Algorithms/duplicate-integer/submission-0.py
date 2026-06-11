class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev=set()
        for num in nums:
            if num in prev:
                return True
            prev.add(num)
        return False