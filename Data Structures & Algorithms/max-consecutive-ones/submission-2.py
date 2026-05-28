class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # solution 1: brute force simulation O(n)
        '''
        n = len(nums)
        i = 0
        best = 0
        while i<n:
           curr = 0
           for j in range(i,n):
                if nums[j]==1:
                    curr+=1
                else:
                    break
           best = max(curr,best)
           i=j+1
        return best
        '''

        # solution 2: efficient solution using prefix array O(n)
        curr = 0
        best = 0
        for num in nums:
            if num == 1:
                curr += 1
                best = max(best, curr)
            else:
                curr = 0
        return best