class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # do not create another array, so use the same array
        
        # solution 1: brute force pythonic way
        # even though new array not created, internally additional memory consumed
        '''
        nums[:] = [i for i in nums if i!=val]
        k = len(nums)
        '''
        
        # solution 2: efficient two pointers 
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k