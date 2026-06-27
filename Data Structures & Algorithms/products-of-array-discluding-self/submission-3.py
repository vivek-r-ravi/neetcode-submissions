# prefix and suffix arrays
# O(n) time and O(n) space
class SolutionV1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        suffix = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[-(i + 1)] = suffix[-i] * nums[-i]
        for i in range(n):
            nums[i] = prefix[i] * suffix[i + 1]
        return nums


# prefix and suffix arrays (space compression)
# O(n) time and O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prod = 1
        for i in range(n):
            out[i] *= prod
            prod *= nums[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            out[i] *= prod
            prod *= nums[i]
        return out
