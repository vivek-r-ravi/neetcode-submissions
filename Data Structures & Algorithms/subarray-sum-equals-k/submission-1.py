# create prefix sum array and use 2 sum hashmap logic in that to find number of subarrays
# further space compression by checking total in each step instead of creating prefix array
# O(n) time and space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_dict = {k: 1}
        total = 0
        out = 0
        for i in range(n):
            total += nums[i]
            if total in sum_dict:
                out += sum_dict[total]
            sum_dict[total + k] = sum_dict.get(total + k, 0) + 1
        return out
