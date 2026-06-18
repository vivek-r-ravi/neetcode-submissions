# brute force
# O(n2) time O(1) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        for L in range(n):
            for R in range(L+1,min(n,L+k+1)):
                if nums[L]==nums[R]:
                    return True
        return False