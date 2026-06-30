class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        out=0
        for num in nums:
            if num-1 not in nums_set:
                k=num+1
                sub_out=1
                while k in nums_set:
                    sub_out+=1
                    k+=1
                out=max(out,sub_out)
        return out