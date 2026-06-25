# brute force: check every pair
# O(n3) time and O(m) space
class SolutionV1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        out.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(x) for x in out]

# alternate solution: hashmap (similar to Two Sum I)
# O(n2) time and O(n) space

# two pointers with duplicate handling and early stop
# O(n2) time and O(1) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for m in range(len(nums)):
            if nums[m] > 0:  # stop if only positive numbers
                break
            if m > 0 and nums[m] == nums[m - 1]:  # check duplicates
                continue
            target = -1 * nums[m]
            l = m + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    out.append([nums[m], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:  # check duplicates
                        l += 1
        return out