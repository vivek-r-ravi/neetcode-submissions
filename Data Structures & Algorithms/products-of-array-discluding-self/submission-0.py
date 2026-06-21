# prefix and suffix arrays
# O(n) time and O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*(n+1)
        suffix=[1]*(n+1)
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]*nums[i-1]
            suffix[-(i+1)]=suffix[-i]*nums[-i]
        for i in range(n):
            nums[i]=prefix[i]*suffix[i+1]
        return nums