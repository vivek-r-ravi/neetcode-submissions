# brute force
# O(n*k) time O(1) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for L in range(n):
            for R in range(L + 1, min(n, L + k + 1)):
                if nums[L] == nums[R]:
                    return True
        return False


# hashmap
# O(n) time O(n) space
class SolutionV2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i

        return False


# sliding window and set
# O(n) time O(k) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        L = 0
        window = set()
        for R in range(n):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
